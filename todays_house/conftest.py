import base64

import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest


@pytest.fixture
def app_driver(worker_id):
    devices_config = [
        {'udid': 'emulator-5554', 'systemPort': 8200},
        {'udid': 'emulator-5556', 'systemPort': 8201},
        {'udid': 'emulator-5558', 'systemPort': 8202},
    ]
    if worker_id == 'master':
        device_info = devices_config[0]
    else:
        worker_index = int(worker_id.lstrip('gw'))
        device_info = devices_config[worker_index % len(devices_config)]

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
        'udid': device_info['udid'],
        'systemPort': device_info['systemPort'],
    }

    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(app_capabilities))

    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def recorded_app_driver(request, app_driver):
    app_driver.start_recording_screen()
    try:
        yield app_driver
    finally:
        app_driver.remove_app('net.bucketplace')
        video_data = base64.b64decode(app_driver.stop_recording_screen())

        allure.attach(video_data, name=f'{request.node.name}', attachment_type=allure.attachment_type.WEBM)


@pytest.fixture
def todays_house_values():
    return {}
