import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import assert_that, close_to


class TestWebDriverWait:
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        # desired_caps["deviceName"] = "emulator-5554"
        desired_caps["deviceName"] = "dcd7fa16"
        # desired_caps["platformVersion"] = "10.0"
        desired_caps["appPackage"] = "com.tencent.wework"
        desired_caps["appActivity"] = ".launch.LaunchSplashActivity"
        desired_caps["noReset"] = "true"
        desired_caps['skipServerInstallation'] = "true"
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        pass

    def test_search(self):
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("alibaba")
