import time
import base64
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import urllib.request
import http.client
import re

import json
import os.path

DELAY = 2

RU_MONTH_VALUES = {
    'янв': 1,
    'фев': 2,
    'мар': 3,
    'апр': 4,
    'мая': 5,
    'июн': 6,
    'июл': 7,
    'авг': 8,
    'сен': 9,
    'окт': 10,
    'ноя': 11,
    'дек': 12,
}

URL = "https://vk.com/topic-25349116_38313695"
options = Options()
options.add_argument("user-data-dir=C:\\Users\\Alex\\AppData\\Local\\Google\\Chrome\\User Data\\Profileotto")
driver = webdriver.Chrome(executable_path=r'C:\\Users\\Alex\\PycharmProjects\\new\\chromedriver.exe', options=options)
driver.get(URL)

time.sleep(DELAY)

resfile = open("otto.csv", 'w', encoding='utf-8', errors='ignore')

num = driver.find_element_by_class_name("pg_pages").find_elements_by_class_name("pg_lnk")[-1].get_attribute("href").split("=")[1]

pubs = {}

try:
    for i in range(int(num) // 20):
        driver.get(URL + "?offset=" +  str(i * 20))
        time.sleep(DELAY)
        posts = driver.find_element_by_class_name("wall_module").find_elements_by_class_name("bp_post")

        for p in posts:
            author = p.find_element_by_class_name("bp_author")
            a_name, a_href = author.text, author.get_attribute("href")
            dattime = p.find_element_by_class_name("bp_date").text.split(" в ")
            text = p.find_element_by_class_name("bp_text").get_attribute('innerHTML').replace("\n","")
            clear_text =  p.find_element_by_class_name("bp_text").text.replace("\n","")
            try:
                media = p.find_element_by_class_name("post_media").get_attribute('innerHTML').text.replace("\n","")
            except:
                media = ""

            pubs[i] = [a_name, a_href, dattime, text, media]
            print(";".join([a_name, a_href, dattime[0], dattime[1], clear_text, text, media]))
            resfile.write("\t".join([a_name, a_href, dattime[0], dattime[1], clear_text, text, media]) + "\n")

except Exception as e:
    driver.close()
    print(e)



'''
#second method - scrolling to get all comments

SCROLL_PAUSE_TIME = 2

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

'''


