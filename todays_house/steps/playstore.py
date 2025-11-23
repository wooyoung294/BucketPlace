import allure
from appium.webdriver.common.appiumby import AppiumBy
from pytest_bdd import parsers, when

from todays_house.util.appium_expect import AppiumExpect as AE
from todays_house.util.wait_for_element import wait_for_element


@when('TC_001 Playstore [검색] 버튼 클릭')
@allure.step('TC_001 Playstore [검색] 버튼 클릭')
def click_search_btn_in_playstore(app_driver):
    search_btn = wait_for_element(app_driver, 'UIAUTOMATOR', 'new UiSelector().text("검색")')
    search_btn.click()
    search_input_placeholder = wait_for_element(app_driver, 'UIAUTOMATOR', 'new UiSelector().text("앱 및 게임 검색")')
    AE(app_driver, search_input_placeholder).to_be_visible()
    search_input_placeholder.click()


@when('TC_002 Playstore "오늘의 집" 검색')
@allure.step('TC_002 Playstore "오늘의 집" 검색')
def search_todays_house(app_driver):
    search_input_placeholder = wait_for_element(app_driver, 'UIAUTOMATOR', 'new UiSelector().text("앱 및 게임 검색")')
    search_input_placeholder.click()

    search_input = wait_for_element(app_driver, 'XPATH', '//android.widget.TextView[@text="앱 및 게임 검색"]/..')
    search_input.send_keys('오늘의 집')

    app_driver.press_keycode(66)

    todays_house_item = wait_for_element(
        app_driver, 'ACCESSIBILITY_ID', '오늘의집 - 라이프스타일 슈퍼앱\nBUCKETPLACE\n'
    )
    AE(app_driver, todays_house_item).to_be_visible()


@when('TC_003 Playstore 검색 결과 목록에서 [오늘의 집] 클릭')
@allure.step('TC_003 Playstore 검색 결과 목록에서 [오늘의 집] 클릭')
def click_todays_house_item(app_driver):
    todays_house_item = wait_for_element(
        app_driver, 'ACCESSIBILITY_ID', '오늘의집 - 라이프스타일 슈퍼앱\nBUCKETPLACE\n'
    )
    todays_house_item.click()

    app_info = wait_for_element(app_driver, 'UIAUTOMATOR', 'new UiSelector().text("어서오세요, 새로운 오늘의집")')
    AE(app_driver, app_info).to_be_visible()


@when(parsers.parse('TC_004 Playstore [오늘의 집] 앱 버전 "{version_text}" 확인'))
@allure.step('TC_004 Playstore [오늘의 집] 앱 버전 "{version_text}" 확인')
def checked_app_version(app_driver, todays_house_values, version_text):
    app_info_btn = wait_for_element(app_driver, 'ACCESSIBILITY_ID', '앱 정보 자세히 알아보기')
    app_info_btn.click()

    app_driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("버전"))',
    )

    version_value = app_driver.find_element(
        AppiumBy.XPATH, '//android.widget.TextView[@text="버전"]/following-sibling::android.widget.TextView[1]'
    )

    todays_house_values['android_version'] = version_value.text

    assert version_value.text == version_text

    back_btn = wait_for_element(app_driver, 'ACCESSIBILITY_ID', '위로 탐색')
    back_btn.click()


@when('TC_005 Playstore [오늘의 집] 앱 설치')
def install_todays_house(app_driver, todays_house_values):
    install_btn = wait_for_element(app_driver, 'ACCESSIBILITY_ID', '설치')
    install_btn.click()

    delete_btn = wait_for_element(app_driver, 'ACCESSIBILITY_ID', '제거', time=300)
    AE(app_driver, delete_btn).to_be_visible()

    open_btn = wait_for_element(app_driver, 'ACCESSIBILITY_ID', '열기')
    AE(app_driver, open_btn).to_be_visible()


@when('TC_006 Playstore 오늘의 집 앱 [열기] 버튼 클릭')
def click_open_btn_for_todays_house_app(app_driver, todays_house_values):
    open_btn = wait_for_element(app_driver, 'ACCESSIBILITY_ID', '열기')
    open_btn.click()

    buket_place_logo = wait_for_element(app_driver, 'ID', 'net.bucketplace:id/logo')
    AE(app_driver, buket_place_logo).to_be_visible()
