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



URL = "https://vk.com/topic-25349116_24612271"
options = Options()
options.add_argument("user-data-dir=C:\\Users\\Alex\\AppData\\Local\\Google\\Chrome\\User Data\\Profileotto")
driver = webdriver.Chrome(executable_path=r'C:\\Users\\Alex\\PycharmProjects\\new\\chromedriver.exe', options=options)
driver.get(URL)

time.sleep(DELAY)

resfile = open("otto_" + str(URL.split("/")[-1]) + ".csv", 'w', encoding='utf-8', errors='ignore')

num = driver.find_element_by_class_name("pg_pages").find_elements_by_class_name("pg_lnk")[-1].get_attribute("href").split("=")[1]

pubs = {}

try:
    for i in range(0,int(num) + 1 ,20):
        driver.get(URL + "?offset=" +  str(i ))
        time.sleep(DELAY)
        posts = driver.find_element_by_class_name("wall_module").find_elements_by_class_name("bp_post")

        for p in posts:
            author = p.find_element_by_class_name("bp_author")
            a_name, a_href = author.text, author.get_attribute("href")
            avatar = p.find_element_by_class_name("bp_img").get_attribute("src")
            dattime = p.find_element_by_class_name("bp_date").text.split(" в ")
            text = p.find_element_by_class_name("bp_text").get_attribute('innerHTML').replace("\n","")
            clear_text =  p.find_element_by_class_name("bp_text").text.replace("\n","")
            try:
                media = p.find_element_by_class_name("post_media").get_attribute('innerHTML').text.replace("\n","")
            except:
                media = ""

            pubs[i] = [a_name, a_href, dattime, text, media]
            print(";".join([a_name, a_href, dattime[0], dattime[1], clear_text, avatar, text, media]))
            resfile.write("\t".join([a_name, a_href, dattime[0], dattime[1], clear_text, avatar, text, media]) + "\n")

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


