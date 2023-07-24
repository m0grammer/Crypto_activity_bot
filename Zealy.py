import requests, lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_project():
    url = 'https://zealy.io/explore/new-web3-communities'
    response = requests.get(url)
    # Проверка, что сайт отвечает
    if response.status_code == 200:
        # Специальный код (суп) для работы с html разметкой
        soup = BeautifulSoup(response.content, 'lxml')
        # Создание списка всех активностей
        cards = list(soup.find_all('h4', class_='heading-3 select-none line-clamp-1'))
        # Удобное отображение их
        projects = []
        for project in cards:
            projects.append(project.text)

        print(projects)
    # Что-то с сайтом или у тебя с компом
    else:
        print("something went wrong")

def get_stat():
    url = "https://zealy.io/explore/new-web3-communities"
    xpath_expression = '//span[@aria-label="Members"]'
    options = Options()
    options.add_argument("--headless")  # Запуск браузера в режиме без графического интерфейса

    # Указываем путь к chromedriver (замените на путь к вашему драйверу)
    driver = webdriver.Chrome(executable_path='/путь_к_вашему_драйверу/chromedriver', options=options)

    driver.get(url)

    # Находим элементы по указанному XPath
    elements = driver.find_elements(By.XPATH, xpath_expression)

    driver.quit()

    print([element.text for element in elements])
get_stat()


    

        


