import os
import time

import allure
from dotenv import load_dotenv
from pytest_bdd import when

from todays_house.util.appium_expect import AppiumExpect as AE
from todays_house.util.wait_for_element import wait_for_element

load_dotenv(verbose=True)
USER_ID = os.getenv('USER_ID')
USER_PW = os.getenv('USER_PW')


@when('TC_007 [카카오톡으로 계속하기] 버튼 클릭')
@allure.step('TC_007 [카카오톡으로 계속하기] 버튼 클릭')
def click_kakao_login_btn(app_driver):
    kakao_login_btn = wait_for_element(app_driver, 'ID', 'net.bucketplace:id/loginText')
    kakao_login_btn.click()

    existing_account_popup = wait_for_element(app_driver, 'ID', 'net.bucketplace:id/titleText')
    AE(app_driver, existing_account_popup).to_have_text("'페이스북 간편가입'으로\n이미 가입한 계정이 있습니다.")

    user_id_label = wait_for_element(app_driver, 'ID', 'net.bucketplace:id/messageText')
    AE(app_driver, user_id_label).to_have_text(USER_ID)


@when('TC_008 [네이버] 아이콘 버튼 클릭')
@allure.step('TC_008 [네이버] 아이콘 버튼 클릭')
def click_naver_icon_btn(app_driver):
    naver_icon_btn = wait_for_element(app_driver, 'ACCESSIBILITY_ID', '네이버로 가입하기')
    naver_icon_btn.click()

    wait_for_element(
        app_driver,
        'XPATH',
        '//*[contains(@text, "네이버 : 로그인")]',
        search_type='present',
        time=15,
    )


@when('TC_009 네이버 오늘의집 전체 약관 동의 후 [동의하기] 버튼 클릭')
@allure.step('TC_009 네이버 오늘의집 전체 약관 동의 후 [동의하기] 버튼 클릭')
def agree_all_trems_and_confirm(app_driver):
    terms_all_agree_check_box = wait_for_element(
        app_driver, 'XPATH', '//android.widget.CheckBox[contains(@text, "전체 동의하기")]', time=30
    )
    time.sleep(1)
    terms_all_agree_check_box.click()

    agree_btn = wait_for_element(app_driver, 'XPATH', '//android.widget.Button[@text="동의하기"]', time=30)
    time.sleep(1)
    agree_btn.click()


@when('TC_010 [기존 계정 로그인] 버튼 클릭')
@allure.step('TC_010 [기존 계정 로그인] 버튼 클릭')
def click_existing_account_login_btn(app_driver):
    existing_account_login_btn = wait_for_element(app_driver, 'ID', 'net.bucketplace:id/positiveText')
    existing_account_login_btn.click()

    black_friday_event_page = wait_for_element(app_driver, 'ID', 'net.bucketplace:id/title')
    AE(app_driver, black_friday_event_page).to_have_text('오늘의집 집요한 BLACK FRIDAY')


@when('TC_011 [페이스북] 아이콘 버튼 클릭')
@allure.step('TC_011 [페이스북] 아이콘 버튼 클릭')
def click_facebook_icon_btn(app_driver):
    facebook_icon_btn = wait_for_element(app_driver, 'ACCESSIBILITY_ID', '페이스북으로 가입하기')
    facebook_icon_btn.click()

    black_friday_event_page = wait_for_element(app_driver, 'ID', 'net.bucketplace:id/title')
    AE(app_driver, black_friday_event_page).to_have_text('오늘의집 집요한 BLACK FRIDAY')
