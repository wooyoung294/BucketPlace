from typing import Literal, Optional

from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

APP_LOCATORS = {
    'ID': AppiumBy.ID,
    'XPATH': AppiumBy.XPATH,
    'ACCESSIBILITY_ID': AppiumBy.ACCESSIBILITY_ID,
    'CLASS_NAME': AppiumBy.CLASS_NAME,
    'UIAUTOMATOR': AppiumBy.ANDROID_UIAUTOMATOR,
}
LocatorKey = Literal['ID', 'XPATH', 'ACCESSIBILITY_ID', 'CLASS_NAME', 'UIAUTOMATOR']


def wait_for_element(
    driver: WebDriver,
    by: LocatorKey,
    search_value: str,
    search_type: Literal['present', 'visible'] = 'visible',
    time: int = 10,
) -> Optional[WebElement]:
    if search_type == 'present':
        condition = EC.presence_of_element_located((APP_LOCATORS[by], search_value))
        poll = 1
    elif search_type == 'visible':
        condition = EC.visibility_of_element_located((APP_LOCATORS[by], search_value))
        poll = 1
    else:
        raise ValueError("search_type은 'present' 나 'visible' 만 사용할 수 있습니다.")

    try:
        return WebDriverWait(
            driver,
            time,
            poll_frequency=poll,
            ignored_exceptions=(StaleElementReferenceException, NoSuchElementException),
        ).until(condition)
    except TimeoutException as e:
        raise AssertionError(f'요소를 찾지 못함: {by}={search_value}') from e
