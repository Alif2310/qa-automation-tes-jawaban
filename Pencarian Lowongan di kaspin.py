from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://kasirpintar.co.id/careers")
driver.find_element_by_id("posisi").send_keys("QA Automation Engineer")

driver.find_element_by_id("cari").click()

