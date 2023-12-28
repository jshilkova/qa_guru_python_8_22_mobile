import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@pytest.mark.android
@pytest.mark.all
def test_search(mobile_management):
    with step('Skip onboarding'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@pytest.mark.android
@pytest.mark.all
def test_open_article(mobile_management):
    with step('Skip onboarding'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Search article'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Python')
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
                    ).element_by(have.text('Pythonidae')).click()

    with step('Verify article title'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Pythonidae'))


@pytest.mark.android
@pytest.mark.all
def test_onboarding_path(mobile_management):
    with step('Verify language selection screen opened'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('over 300 languages'))
    with step('Verify add language control presents'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/addLanguageButton')).should(be.clickable)

    with step('Continue to the second screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    with (step('Verify feed customizing screen opened')):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('New ways to explore'))

    with step('Continue to the third screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    with step('Verify reading lists screen opened'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Reading lists with sync'))

    with step('Continue to the fourth screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    with step('Verify send data screen opened'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Send anonymous data'))

    with step('Click accept button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()
    with step('Verify search input is on the screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')
                        ).should(be.present)
