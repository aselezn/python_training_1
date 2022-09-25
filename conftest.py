import pytest
import json
import os.path
from fixture.application import Application

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None: #проверка: загрузка конфигурации, если она еще не загружена и ранее не была прочитана
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),request.config.getoption("--target"))  #получаем директорию, в которой лежит файл
        with open(config_file) as f: #config_file - путь к файлу/ f - объект в этом файле
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")

