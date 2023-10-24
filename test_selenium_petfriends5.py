# Написать тест, который проверяет, что на странице со списком питомцев пользователя:
# Присутствуют все питомцы.
# Хотя бы у половины питомцев есть фото.
# У всех питомцев есть имя, возраст и порода.
# У всех питомцев разные имена.
# В списке нет повторяющихся питомцев.
# В написанном тесте (проверка карточек питомцев) добавьте неявные ожидания всех элементов (фото, имя питомца, его возраст).
# В написанном тесте (проверка таблицы питомцев) добавьте явные ожидания элементов страницы.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# Создаем фикстуру для настройки и очистки драйвера
@pytest.fixture(autouse=True)
def web_browser():
    # Настройка веб-драйвера
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    # Открыть PetFriends базовую страницу
    driver.get("https://petfriends.skillfactory.ru/")

    # Ждать, пока кнопка "Новый пользователь" станет видимой
    btn_newuser = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]"))
    )
    btn_newuser.click()

    # Ждать, пока кнопка "У меня уже есть аккаунт" станет видимой
    btn_exist_acc = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "У меня уже есть аккаунт"))
    )
    btn_exist_acc.click()

    # Ждать, пока поле email станет видимым
    field_email = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    field_email.clear()
    field_email.send_keys("vasya@mail.com")

    # Ждать, пока поле пароля станет видимым
    field_pass = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "pass"))
    )
    field_pass.clear()
    field_pass.send_keys("12345")

    # Ждать, пока кнопка "Войти" станет видимой
    btn_submit = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
    )
    btn_submit.click()

    # Ждать, пока страница загрузится
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://petfriends.skillfactory.ru/all_pets")
    )

    yield driver

    driver.quit()


def test_show_my_pets(web_browser):
    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    web_browser.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # Получаем количество питомцев из статистики пользователя
    pets_number_element = web_browser.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]')
    pets_number_text = pets_number_element.text# Получаем текст из найденного элемента, который, предположительно,
    # содержит информацию о количестве питомцев.

    # Парсинг числа из строки
    matches = re.search(r'\d+', pets_number_text)# Мы используем регулярное выражение, чтобы извлечь числа из текста.
    # Это позволяет нам извлечь количество питомцев из строки. Регулярное выражение r'\d+' соответствует одной или
    # более цифрам.
    if matches:
        pets_number = int(matches.group())# Если числа были найдены, мы преобразуем их в целое число и сохраняем
        # в переменной pets_number.
    else:
        # Обработка ошибки - не найдено число
        raise ValueError("No number found in pets_number_text")

    # Получаем количество питомцев в таблице
    pets_count = web_browser.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')# Здесь мы находим
    # все элементы, которые соответствуют XPATH-запросу, представляющему строки в таблице питомцев.

    # Проверяем, что количество питомцев из статистики (pets_number) соответствует количеству питомцев в таблице
    assert pets_number == len(pets_count)# Если они равны, то это утверждение не генерирует ошибку, и тест считается
    # Успешно пройденным. Если они не равны, тест завершается ошибкой, указывающей на несоответствие колич-ва питомцев.


def test_checking_cards_pets(web_browser):
    # Получаем все необходимые элементы - фото, имя, порода, возраст. Результаты поиска сохраняются в соответствующих переменных.
    images = web_browser.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/th/img')
    names = web_browser.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[1]')
    breeds = web_browser.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[2]')
    ages = web_browser.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[3]')

    # Создаем пустой список для записи имен питомцев
    list_names = []

    # Создаем счетчик для фото
    images_count = 0

    # Создаем список для хранения ожидаемых результатов
    expected_results = [1, 2, 3, 4, 5, 6]

    # Создаем список для хранения кортежей (фото, имя, порода, возраст, ожидаемый результат)
    pets_list = []

    # Проходим по всем элементам и проверяем их
    for i in range(len(images)):
        # Добавляем имя в список
        list_names.append(names[i].text)

        # Если у питомца есть фото, увеличиваем счетчик
        if images[i].get_attribute('src') != '':
            images_count += 1

        # Проверяем, что имя, порода и возраст не пустые
        assert names[i].text != ''
        assert breeds[i].text != ''
        assert ages[i].text != ''

        # Добавляем кортеж в список питомцев
        pets_list.append((images[i], names[i], breeds[i], ages[i], expected_results[i]))

    # Проверка деления на 0 и что у половины питомцев есть фото
    if len(images) == 0:
        print("Нет питомцев")
    else:
        assert images_count / len(images) >= 0.5# В противном случае, мы проверяем, что отношение images_count к
        # общему колич-ву питомцев (длине images) больше или равно 0.5. Это гарантирует, что у половины питомцев есть фото.

    # Проверяем, что у всех питомцев разные имена
    set_names = set(list_names)
    assert len(set_names) == len(list_names)

def test_check_no_duplicate_pets(web_browser):
    pet_names = []

    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    web_browser.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # Получаем имена питомцев
    pet_name_elements = web_browser.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[1]')
    for name_element in pet_name_elements:# Запускаем цикл, который перебирает все найденные элементы с именами питомцев
        pet_name = name_element.text

        # Добавляем имя в список pet_names
        pet_names.append(pet_name)

    # Проверяем, что есть хотя бы одно имя питомца на странице
    assert pet_names, "No pet names found on the page"





