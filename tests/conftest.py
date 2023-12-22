import allure_commons
import pytest
from qa_guru_python_8_22_mobile import utils
from appium import webdriver
from dotenv import load_dotenv
from selene import browser, support
import allure


def pytest_addoption(parser):
    parser.addoption(
        '--context',
        default='bstack'
    )


def pytest_configure(config):
    context = config.getoption('--context')
    load_dotenv(dotenv_path=utils.file_path.abs_path_from_project(f'.env.{context}'))


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    context = request.config.getoption('--context')
    from config import config
    options = config.to_driver_options(context)
    browser.config.timeout = config.timeout

    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_url,
            options=options
        )

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    utils.allure_attach.screenshot()
    utils.allure_attach.screen_xml_dump()
    session_id = browser.driver.session_id

    with allure.step('Tear down app sessioncwith id' + session_id):
        browser.quit()

    if context == 'bstack':
        utils.allure_attach.bstack_video(session_id)
