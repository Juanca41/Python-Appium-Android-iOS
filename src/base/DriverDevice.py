from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys

class DriverDevice:

    def __init__(self, device):
        self.device = device

    def createDriverSession(self):

        base_url = "http://127.0.0.1:4723/wd/hub"

        if self.device == "android":

            android_native_caps = {} 
            android_native_caps['platformName'] = 'android' 
            android_native_caps['platformVersion'] = '12'
            android_native_caps['automationName'] = 'UiAutomator2'
            android_native_caps['deviceName'] = 'Samsung Galaxy S21'
            android_native_caps['app'] = ('/Users/jcgularte/Desktop/BetterVet/Automation-Mobile-App/src/apps/parking-test.apk')
            android_native_caps['appPackage'] = 'com.spplus.parking.develop' 
            android_native_caps['appActivity'] = 'com.spplus.parking.presentation.splash.SplashActivity' 

            driver = webdriver.Remote(base_url, android_native_caps)
            print("Check Whether device is locked or not :",driver.is_locked())
            print("Current Activity",driver.current_package)
            print("Current Activity",driver.current_activity)
            print("Current context",driver.current_context)
            print("Current orientation",driver.orientation)

        if self.device == "ios":

            ios_native_caps = {} 
            ios_native_caps['platformName'] = 'IOS' 
            ios_native_caps['platformVersion'] = '15.5'
            ios_native_caps['automationName'] = 'XCUITest'
            ios_native_caps['deviceName'] = 'iPhone 13 Pro Max'
            ios_native_caps['autoAcceptAlerts'] = 'true'
            ios_native_caps['app'] = '/Users/jcgularte/Desktop/Cursos/Repositories/Java-Appium-Android-iOS/src/main/resources/BetterVet.app'
            ios_native_caps['useNewWDA'] = 'true'

            driver = webdriver.Remote(base_url, ios_native_caps)
            driver.implicitly_wait(6)

        if self.device == "ios-hybrid":

            ios_hybrid_caps = {} 
            ios_hybrid_caps['platformName'] = 'ios' 
            ios_hybrid_caps['platformVersion'] = '15.5'
            ios_hybrid_caps['automationName'] = 'XCUITest'
            ios_hybrid_caps['deviceName'] = 'iPhone 13 Pro Max'
            # ios_hybrid_caps['app'] = ('/Users/jcgularte/Downloads/BetterVet-QA.apk') 
            ios_hybrid_caps['autoWebview'] = 'true' 
            ios_hybrid_caps['browserName'] = 'safari'

            driver = webdriver.Remote(base_url, ios_hybrid_caps)
            driver.get("https://uat.parking.com")

        if self.device == "android-hybrid":

            android_hybrid_caps = {} 
            android_hybrid_caps['platformName'] = 'Android'
            android_hybrid_caps['automationName'] = 'UiAutomator2'
            android_hybrid_caps['deviceName'] = 'Samsung Galaxy S21'
            android_hybrid_caps['browserName'] = 'Chrome'

            driver = webdriver.Remote(base_url, android_hybrid_caps)
            driver.get("https://uat.parking.com")

            print("Check Whether device is locked or not :",driver.is_locked())
            print("Current Activity",driver.current_package)
            print("Current Activity",driver.current_activity)
            print("Current context",driver.current_context)
            print("Current orientation",driver.orientation)

        else:
            print("No device found for the option you have chosen. Please choose an option between 'ios', 'android', 'ios-hybrid' or 'android-hybrid'.")

        return driver
