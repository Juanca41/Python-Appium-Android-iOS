import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
import src.helpers.CustomLogger as cl

class Test():

    @pytest.mark.AndroidNative
    @pytest.mark.usefixtures("init_driver")
    def test_methodOne(self):
        log = cl.customLogger()
        elementLocator = (AppiumBy.ID, "com.spplus.parking.develop:id/text1")
        elementLocated = WebDriverWait(self.driver,15).until(EC.presence_of_element_located(elementLocator)).text
        # text = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[1]").text
        assert elementLocated == "Easily book daily and monthly parking when you need it."
        log.info("Assertion passed.")

    @pytest.mark.AndroidNative
    @pytest.mark.usefixtures("init_driver")
    def test_methodTwo(self):
        log = cl.customLogger()
        elementLocator = (AppiumBy.ID, "com.spplus.parking.develop:id/text1")
        elementLocated = WebDriverWait(self.driver,15).until(EC.presence_of_element_located(elementLocator)).text
        try:
            assert elementLocated == "Easily book daily and monthly parking when you need it", "TEXTS ARE NOT EQUAL"
        except AssertionError as e:
            self.driver.save_screenshot("output/screenshots/error.png")
            log.error("Assertion error")
            pytest.fail(str(e))
            # m2.critical("Critical Msg")
            # m2.warning("Warn msg")
            # m2.info("Info msg")
            # m2.debug("Debug msg")

# test =Test()
# test.methodOne()
# test.methodTwo()

