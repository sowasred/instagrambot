from selenium import webdriver

import os 
import time
import configparser
from random import randint
class IgBot:
    hashtag_list = ['#augmented', '#augmented_reality', '#augmentedreality']

    prev_user_list = []

    new_followed = []
    tag = 0
    followed = 0
    likes = 0
    comments = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'

        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference('network.proxy.type',1)
        self.profile.set_preference('network.proxy.http','localhost')
        self.profile.set_preference('network.proxy.http_port',3128)
        self.profile.update_preferences()

        self.auto_start()

        self.driver = webdriver.Firefox(firefox_profile=self.profile,executable_path=r'./geckodriver.exe')


        # self.login()


    def login(self):
        self.driver.get('https://www.instagram.com/')

        self.driver.implicitly_wait(4)

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()

        time.sleep(randint(2,7))



    def nav_user(self,user):
        self.driver.get('{}/{}/'.format(self.base_url,self.username))



    def follow_user(self, user):
        self.nav_user(user)

        follow_button = self.driver.find_element_by_xpath()

        follow_button.click()


    def auto_start(self):
        tagNumber = randint(1,3)
        i = 0
        while i < tagNumber:
         print(i)
         i += 1

    





if __name__ == '__main__':


    config_path = './config.ini'

    cparser = configparser.ConfigParser()

    cparser.read(config_path)

    username = cparser['AUTH']['USERNAME']
    password = cparser['AUTH']['PASSWORD']

    ig_bot = IgBot(username,password)
