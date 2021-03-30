from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


def login():
    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(3)
    username = webdriver.find_element_by_name('username')
    username.send_keys('official_rakshit')
    password = webdriver.find_element_by_name('password')
    password.send_keys('')
    button_login = webdriver.find_elements_by_xpath("//*[contains(text(), 'Log In')]")
    button_login[0].click()
    sleep(5)
    notnow = webdriver.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
    notnow[0].click()
    sleep(3)
    notnow = webdriver.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
    notnow[0].click()
    sleep(3)

def search():
    search_bar = webdriver.find_elements_by_class_name("XTCLo")
    search_bar[0].send_keys("#musiccover")
    sleep(3)
    search_bar[0].send_keys(Keys.RETURN)
    search_bar[0].send_keys(Keys.RETURN)
    sleep(5)

def traverse_items():
    items = webdriver.find_elements_by_class_name("_9AhH0")
    i=0
    items[0].click()
    sleep(3)
    while webdriver.find_elements_by_xpath("//*[contains(text(), 'Next')]") is not None:
        video_element = webdriver.find_elements_by_class_name("_5wCQW")
        if len(video_element)>0:
            comment("Sounds Great")
        next_item = webdriver.find_elements_by_xpath("//*[contains(text(), 'Next')]")
        next_item[0].click()
        sleep(3)

def comment(text):
    comment_input = webdriver.find_elements_by_class_name("Ypffh")
    comment_input[0].click()
    comment_input = webdriver.find_elements_by_class_name("Ypffh")
    comment_input[0].send_keys(text)
    comment_input[0].send_keys(Keys.RETURN)

chromedriver_path = '/Users/rakshitsharma/Documents/Rakshit/Instagram Bot/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=r"/Users/rakshitsharma/Documents/Rakshit/Instagram Bot/chromedriver")
sleep(2)
login()
search()
traverse_items()
