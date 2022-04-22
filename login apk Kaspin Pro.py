from appium import webdriver
##from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

desired_caps = {}

desired_caps ["platformName"] = "Android"
desired_caps ["deviceName"] = "emulator-5554"
desired_caps ["appPackage"] = "org.owline.kasirpintarpro"
desired_caps ["appActivity"] = "org.owline.kasirpintarpro.SplashScreen"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(1)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/tv_login").click()
time.sleep(1)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_email").click()
time.sleep(1)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_email").send_keys("alifkaspin7@yopmail.com")
time.sleep(1)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_password").click()
time.sleep(1)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_password").send_keys("alif2310")
time.sleep(1)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/btn_login").click()
time.sleep(1)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/btn_ok").click()
