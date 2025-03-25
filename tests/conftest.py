import pytest
from selenium import webdriver


def pytest_addoption(parser): # Эта функция добавляет пользовательский параметр командной строки --language
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose interface language: en, ru, fr, etc.",
    )

@pytest.fixture(scope="session")
def language(request): # Эта фикстура извлекает значение параметра --language, указанного при запуске.
    return request.config.getoption("--language")


@pytest.fixture(scope="function") # Scope — "function" означает, что новый экземпляр браузера будет открыт перед каждым тестом и закрыт после его завершения.
def browser():
    print("\nstart browser for test..") # Выводит сообщение: "start browser for test..".
    browser = webdriver.Chrome() # Открывает экземпляр Chrome.
    yield browser # После завершения теста выполняет yield и затем
    print("\nquit browser..") #  закрывает браузер, выводя "quit browser.."
    browser.quit()