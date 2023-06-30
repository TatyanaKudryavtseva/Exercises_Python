# файл api.py — это будет наш интерфейс взаимодействия с приложением
import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# class PetFriends:
#     """апи библиотека к веб приложению Pet Friends"""
#     def __init__(self):
#         self.base_url = "https://petfriends.skillfactory.ru/"
#     def get_api_key(self, email:str, password:str)->json:# Реализация метода получения аутентификационного ключа.
#         # email и password передаются в заголовке, поэтому нам нужно составить заголовок, которому мы будем передавать
#         # наши параметры. Делаем ниже.
#
#         headers = {
#             "email": email,
#             "password": password
#         }
#         res = requests.get(self.base_url+'api/key', headers=headers)# Запрос будет возвращать результат, сохраним его в переменную res
#         status = res.status_code
#         # Результат приходит в формате json, но иногода он может не читаться, тогда извлекаем text
#         result = ""
#         try:
#             result = res.json()
#         except json.decoder.JSONDecodeError:
#             result = res.text
#         return status, result
#         # мы реализовали метод get, далее напишем для него тест. Тесты всегда хранятся в папке tests
#

class PetFriends:
    """API библиотека к веб приложению Pet Friends"""

    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email: str, passwd: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключем пользователя, найденного по указанным email и паролем"""

        headers = {
            'email': email,
            'password': passwd,
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str = "") -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком наденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет на сервер запрос на удаление питомца по-указанному ID и возвращает
        статус запроса и результат в формате JSON с текстом уведомления об успешном удалении.
        На сегодняшний день тут есть баг - в result приходит пустая строка, но status при этом = 200"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: str) -> json:
        """Метод отправляет запрос на сервер об обновлении данных питомуа по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлёнными данными питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }

        res = requests.put(self.base_url + f'api/pets/{pet_id}', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def create_pet_simple(self, auth_key: json, name: str, anymal_type: str, age: str) -> json:
        """Метод отправляет на сервер данные о добавляемом питомце без фото и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""
        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': anymal_type
        }
        res = requests.post(self.base_url + '/api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result




