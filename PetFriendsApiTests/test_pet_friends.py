# from api import PetFriends
# from settings import valid_email, valid_password
#
# pf = PetFriends()# инициализируем нашу библиотеку и пишем тесты
#
# def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
#     status, result = pf.get_api_key(email, password)# делаем вызов метода из библиотеки и полученные результаты сохраняем
#     # в переменные status и result. Далее сверяем полученный результат с нашим ожиданием
#     assert status == 200# проверяем, что статус в ответе 200
#     assert 'key' in result# проверяем, что в результате нам возвращается ключ, т.е в ответе д.б 'key'


from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ This method allows to get API key which should be used for other API methods. Проверяем что запрос api ключа
     статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    """ This method allows to get the list of pets. Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name='Синди', animal_type='Кошка',
                                     age='3', pet_photo='images/111.jpg'):
    """This method allows to add information about new pet.
    Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_successful_delete_self_pet():
    """This method allows to delete information about pet from database"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Эвкалипт", "коала", "5", "images/222.jpeg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()

def test_successful_update_self_pet_info(name='Синди', animal_type='Кошка', age='3'):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception('There is no my pets')

def test_create_pet_simple(name='Eucalyptus', animal_type='Koala', age='6'):
    """This method allows to add information about new pet. Проверяем, что можно добавить питомца без фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name,animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_no_data(name='', animal_type='', age=''):
    """Проверка с негативным сценарием. Проверяем, что можно добавить питомца с пустыми данными в поле имя, тип животного и возраст"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert  result['name'] == name
def test_get_api_key_for_data_user_empty(email='', password=''):
    """ Проверка с негативным сценарием. Проверяем что запрос api ключа c пустыми значениями логина и пароля возвращает статус 403
    и в результате не содержится слово key """
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
def test_add_pet_invalid_age(name='Kuzma', animal_type='dog', age='2345'):
    '''Проверка с негативным сценарием. Добавление питомца с числом более трех знаков в переменной age.'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert  result['age'] == age
    number = result['age']

def test_get_api_key_invalid_email(email=invalid_email, password=valid_email):
    '''Проверяем запрос с невалидным емейлом и с валидным паролем.
    Проверяем нет ли ключа в ответе'''
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
def test_get_api_key_invalid_password(email=valid_email, password=invalid_password):
    '''Проверяем запрос с невалидным паролем и с валидным емейлом.
    Проверяем нет ли ключа в ответе'''
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
def test_add_pet_number_animal_type(name='Kuzya', animal_type='739757', age='5'):
    '''Проверка с негативным сценарием. Добавление питомца с цифрами вместо букв в поле animal_type.'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200


