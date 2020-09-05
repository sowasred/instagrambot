from selenium import webdriver

import os 
import time

class IgBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference('network.proxy.type',1)
        self.profile.set_preference('network.proxy.http','localhost')
        self.profile.set_preference('network.proxy.http_port',3128)
        self.profile.update_preferences()


        self.driver = webdriver.Firefox(firefox_profile=self.profile,executable_path=r'./geckodriver.exe')
        self.driver.get('https://www.instagram.com/')


if __name__ == '__main__':
    ig_bot = IgBot('temp_username','temp_password')

    print(ig_bot.username)