from pytest_bdd import scenario

from todays_house.steps.login_page import *
from todays_house.steps.main_page import *
from todays_house.steps.my_page import *
from todays_house.steps.playstore import *


@allure.title('최초 페이스북으로 가입한 이메일로 카카오로 로그인')
@scenario('../scenarios/login.feature', '최초 페이스북으로 가입한 이메일로 카카오로 로그인')
def test_kakao_login():
    pass


@allure.title('최초 페이스북으로 가입한 이메일로 페이스북으로 로그인')
@scenario('../scenarios/login.feature', '최초 페이스북으로 가입한 이메일로 페이스북으로 로그인')
def test_facebook_login():
    pass


@allure.title('최초 페이스북으로 가입한 이메일로 네이버로 로그인')
@scenario('../scenarios/login.feature', '최초 페이스북으로 가입한 이메일로 네이버로 로그인')
def test_naver_login():
    pass
