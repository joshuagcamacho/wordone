from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)