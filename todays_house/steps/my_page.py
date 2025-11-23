import os

import allure
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from pytest_bdd import then, when

from todays_house.util.appium_expect import AppiumExpect as AE
from todays_house.util.wait_for_element import wait_for_element

load_dotenv(verbose=True)
USER_NAME = os.getenv('USER_NAME')


@when('TC_014 오감지수 서비스 오픈 바텀시트 닫기')
@allure.step('TC_014 오감지수 서비스 오픈 바텀시트 닫기')
def close_five_senses_bottom_sheet(app_driver):
    app_driver.back()

    my_page_view = wait_for_element(app_driver, 'ID', 'net.bucketplace:id/view_pager')
    AE(app_driver, my_page_view).to_be_visible()

    user_name_label = wait_for_element(app_driver, 'UIAUTOMATOR', 'new UiSelector().text("' + USER_NAME + '")')
    AE(app_driver, user_name_label).to_be_visible()


@when('TC_015 [설정] 버튼 클릭')
@allure.step('TC_015 [설정] 버튼 클릭')
def click_config_btn(app_driver):
    config_btn = wait_for_element(app_driver, 'ACCESSIBILITY_ID', 'Gear icon')
    config_btn.click()

    managed_my_info = wait_for_element(app_driver, 'UIAUTOMATOR', 'new UiSelector().text("내 정보 관리")')
    AE(app_driver, managed_my_info).to_be_visible()


@then('TC_016 앱 마켓과 동일한 버전 노출')
@allure.step('TC_016 앱 마켓과 동일한 버전 노출')
def checked_app_version(app_driver, todays_house_values):
    app_driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("버전 정보"))',
    )
    version_value = app_driver.find_element(
        AppiumBy.XPATH, '//android.widget.TextView[@text="버전 정보"]/following-sibling::android.widget.TextView[1]'
    )

    assert todays_house_values['android_version'] in version_value.text
