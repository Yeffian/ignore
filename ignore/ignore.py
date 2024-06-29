import sys
import requests


def get_available_languages():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Safari()
    driver.get("https://github.com/github/gitignore")

    # wait for the DOM to load
    time.sleep(5)

    lang_list = driver.find_element(by=By.XPATH, value='//*[@id="repo-content-pjax-container"]/div/div/div[2]/div['
                                                       '1]/react-partial/div/div/div[3]/div[1]/table/tbody')
    trs = lang_list.find_elements(By.TAG_NAME, 'tr')
    i = 0
    for tr in trs:
        if i in [0, 1, 2, 3, 140]:
            pass
        else:
            print(tr.text.split('.')[0])
        i += 1


search = 'https://raw.githubusercontent.com/github/gitignore/main/'
params = sys.argv[1:]


def generate_ignore(languages):
    contents = ''
    for lang in languages:
        contents += '\n' + requests.get(search + lang + '.gitignore').text

    with open('./.gitignore', 'w') as file:
        file.write(contents)
