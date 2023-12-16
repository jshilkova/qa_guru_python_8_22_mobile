import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@pytest.mark.ios
@pytest.mark.all
def test_search(ios_mobile_management):
    with step('Select Web View tab'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Web View')).click()

    with step('Verify the get demo is clickable'):
        browser.element((AppiumBy.ID, 'Get a demo')).should(be.clickable)


