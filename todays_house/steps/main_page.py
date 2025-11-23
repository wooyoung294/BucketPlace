import allure
from pytest_bdd import when

from todays_house.util.appium_expect import AppiumExpect as AE
from todays_house.util.wait_for_element import wait_for_element


@when('TC_012 오늘의집 집요한 BLACK FRIDAY 페이지 닫기')
@allure.step('TC_012 오늘의집 집요한 BLACK FRIDAY 페이지 닫기')
def close_black_friday_event_page(app_driver):
    back_btn = wait_for_element(app_driver, 'ID', 'net.bucketplace:id/backIcon', time=20)
    back_btn.click()

    shopping_tap = wait_for_element(app_driver, 'ID', 'net.bucketplace:id/shoppingTab')
    AE(app_driver, shopping_tap).to_be_visible()


@when('TC_013 [마이페이지] 버튼 클릭')
@allure.step('TC_013 [마이페이지] 버튼 클릭')
def click_my_page_btn(app_driver):
    my_page_btn = wait_for_element(app_driver, 'UIAUTOMATOR', 'new UiSelector().text("마이페이지")')
    my_page_btn.click()

    first_visited_creator_guide_img = wait_for_element(
        app_driver, 'ACCESSIBILITY_ID', 'first visited creator guide image'
    )
    AE(app_driver, first_visited_creator_guide_img).to_be_visible()

    confirm_my_score = wait_for_element(app_driver, 'UIAUTOMATOR', 'new UiSelector().text("내 점수 확인하기")')
    AE(app_driver, confirm_my_score).to_be_visible()
