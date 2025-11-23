from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AppiumExpect:
    def __init__(self, driver: WebDriver, element: WebElement = None, timeout: int = 5):
        self.driver = driver
        self.element = element
        self.timeout = timeout

    def _wait_until(self, condition, message: str = None) -> bool:
        try:
            WebDriverWait(
                self.driver,
                self.timeout,
                ignored_exceptions=(StaleElementReferenceException,),
            ).until(condition, message)
            return True
        except TimeoutException as e:
            raise AssertionError(message or f'[WAIT FAILED] Timeout after {self.timeout}s') from e

    def to_be_visible(self) -> bool:
        if not self.element:
            raise AssertionError("to_be_visible() requires 'element' to be set in AppiumExpect.")
        return self._wait_until(EC.visibility_of(self.element), '요소를 찾지 못함')

    def not_to_be_enable(self):
        if not self.element:
            raise AssertionError("not_to_be_enable() requires 'element' to be set in AppiumExpect.")
        try:
            self._wait_until(EC.element_to_be_clickable(self.element), '요소가 활성화 상태')
            raise AssertionError('요소가 활성화 상태입니다')
        except TimeoutException:
            # 타임아웃 예외가 발생하면 요소가 비활성화된 상태이므로 정상
            return True

    def to_be_enable(self):
        if not self.element:
            raise AssertionError("to_be_enable() requires 'element' to be set in AppiumExpect.")
        assert self._wait_until(EC.element_to_be_clickable(self.element), '요소를 찾지 못했거나 비활성화 상태')

    def to_have_text(self, text: str) -> bool:
        if not text:
            raise AssertionError("to_have_text() requires 'text' to be set in AppiumExpect.")
        if not self.element:
            raise AssertionError("to_have_text() requires 'element' to be set in AppiumExpect.")

        def _has_text(_driver):
            value = self.element.text or self.element.get_attribute('text') or ''
            return text in value

        return self._wait_until(_has_text, f"요소 텍스트에 '{text}' 가 포함되지 않음")

    def to_be_checked(self) -> bool:
        if not self.element:
            raise AssertionError("to_be_checked() requires 'element' to be set in AppiumExpect.")

        def _is_checked(_driver: WebDriver):
            value = self.element.get_attribute('checked')
            return str(value).lower() == 'true'

        return self._wait_until(_is_checked, '요소가 체크 상태가 아님')
