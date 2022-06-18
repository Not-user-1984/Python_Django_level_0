from selenium import webdriver
driver = webdriver.Firefox (executable_path='/Users/diplug/Python _Projetc/Selenium_Python/firefoxdriver/geckodriver')

driver.get('http://localhost:8000')
assert 'Django' in driver.title

