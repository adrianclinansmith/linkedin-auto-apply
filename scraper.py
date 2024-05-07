# https://medium.com/@vdaate/how-to-build-linkedin-scraper-using-python-and-selenium-9378ea326fe8
import config

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
 
if __name__ == "__main__":
	driver = webdriver.Chrome()
	# sign in
	driver.get("https://ca.linkedin.com/")
	login_field = driver.find_element(By.ID, "session_key")
	login_field.send_keys(config.email)
	time.sleep(3)
	password_field = driver.find_element(By.ID, "session_password")
	password_field.send_keys(config.qt)
	time.sleep(6)
	sign_in_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']")
	sign_in_button.click()
	time.sleep(12)
	# go to jobs
	jobs_button = driver.find_element(By.XPATH, "//span[normalize-space()='Jobs']")
	jobs_button.click()
	time.sleep(15)
	show_all_button = driver.find_element(By.XPATH, "//span[normalize-space()='Show all']")
	show_all_button.click()
	time.sleep(14)
	# setup search filters
	