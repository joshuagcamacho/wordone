from driver import driver
from selenium.webdriver.common.by import By

def check_status(state: str) -> bool:
    """
    Return True if element is correct; false otherwise.
    """
    
    return state == "correct"


def click_letter(letter: str, driver) -> None:
    """
    Clicks the desired letter
    """
    
    key = "//button[@data-key='{}']".format(letter)
    selected = driver.find_element(By.XPATH, key)
    selected.click()


def click_enter(driver) -> None:
    """
    Clicks the enter button
    """
    enter = driver.find_element(By.XPATH, "//button[@data-key='↵']")
    enter.click()


def check_letter(letter: str, absent_list: list[str], correct_list: list[str]):
    
    key = "//button[@data-key='{}']".format(letter)
    selected = driver.find_element(By.XPATH, key)
    
    # something here not working
    # getting 'None' for state
    state = selected.get_attribute('data-state')
    status = check_status(state)
    
    print(state)
    print(status)
    
    if status and letter not in correct_list:
        correct_list.append(letter)
    elif not status and letter not in absent_list:
        absent_list.append(letter)


def input_word(word: str, driver) -> None:
    """
    Inputs a word
    
    Precondition: len(word) == 5
    """
    
    for c in word:
        click_letter(c, driver)
    
    click_enter(driver)
    
def check_used_letters(driver) -> list[object]:
    used_letters = driver.find_elements(By.XPATH, "//button[@data-state='absent']")
    main = []
    for letters in used_letters:
        [letter, status] = letters.accessible_name.split()
        state = check_status(status)
        print(state)
        main.append(letter)        
    return main