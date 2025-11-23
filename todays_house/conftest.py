import base64

import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest


@pytest.fixture
def app_session_driver():
    app_capabilities = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'appPackage': 'com.android.vending',
        'uiautomator2ServerLaunchTimeout': 120000,
        'uiautomator2ServerInstallTimeout': 120000,
        'uiautomator2ServerReadTimeout': 120000,
        'adbExecTimeout': 120000,
        'newCommandTimeout': 10800,
        'skipServerInstallation': False,
    }

    appium_server_url = 'http://localhost:4723'
    app_driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(app_capabilities))

    yield app_driver
    app_driver.quit()


@pytest.fixture(autouse=True)
def app_function_driver(request, app_session_driver):
    app_session_driver.start_recording_screen()
    try:
        yield app_session_driver
    finally:
        app_session_driver.remove_app('net.bucketplace')
        video_data = base64.b64decode(app_session_driver.stop_recording_screen())

        allure.attach(video_data, name=f'{request.node.name}', attachment_type=allure.attachment_type.WEBM)


@pytest.fixture
def todays_house_values():
    return {}
