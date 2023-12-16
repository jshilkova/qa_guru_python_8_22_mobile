import allure_commons
import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
from selene import browser, support
import allure
import project
from qa_guru_python_8_21_mobile import utils


@pytest.fixture(scope='function', autouse=False)
def ios_mobile_management():
    options = XCUITestOptions().load_capabilities({
        'platformName': 'ios',
        'platformVersion': project.config.ios_version,
        'deviceName': project.config.ios_device_name,

        # Set URL of the application under test
        'app': project.config.ios_app,

        'bstack:options': {
            'projectName': project.config.project_name,
            'buildName': project.config.ios_build_name,
            'sessionName': project.config.ios_session_name,

            'userName': project.config.bs_user_name,
            'accessKey': project.config.bs_password
        }
    })

    browser_setup(options)

    yield

    add_allure_attachments_and_quit()


@pytest.fixture(scope='function', autouse=False)
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({
        'platformVersion': project.config.android_version,
        'deviceName': project.config.android_device_name,

        # Set URL of the application under test
        'app': project.config.android_app,

        'bstack:options': {
            'projectName': project.config.project_name,
            'buildName': project.config.android_build_name,
            'sessionName': project.config.android_session_name,

            'userName': project.config.bs_user_name,
            'accessKey': project.config.bs_password
        }
    })

    browser_setup(options)

    yield

    add_allure_attachments_and_quit()


def browser_setup(options):
    browser.config.timeout = project.config.timeout
    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(
            project.config.driver_remote_url,
            options=options
        )
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )


def add_allure_attachments_and_quit():
    utils.allure.attach_screenshot()
    utils.allure.attach_screen_xml_dump()
    session_id = browser.driver.session_id
    with allure.step('Tear down app session'):
        browser.quit()
    utils.allure.attach_bstack_video(session_id)
