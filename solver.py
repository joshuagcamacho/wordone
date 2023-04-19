from selenium.webdriver.common.by import By
from driver import driver
import functions
import time

driver.get("https://www.nytimes.com/games/wordle/index.html")

# close the 'How to play' prompt
close_button = driver.find_element(By.TAG_NAME, "button")
close_button.click()

functions.input_word('crane', driver)
time.sleep(6)

used_letters = functions.check_used_letters(driver)
print(used_letters)
wrong = []
misplaced = {
    1 : '',
    2 : '',
    3 : '',
    4 : '',
    5 : ''
}
correct = {
    1 : '',
    2 : '',
    3 : '',
    4 : '',
    5 : ''
}
