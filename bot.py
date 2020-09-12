from selenium import webdriver

import os 
import time
import configparser
import random


class IgBot:
    hashtag_list = ['augmented', 'augmented_reality', 'augmentedreality']
    comment_list = ['This is awesome!', 'Augmented Reality is Future.', 'This is literally cool, check our page as well..','You guys are doing great, keep it up','Future is coming with augmented reality.','This is what we like to see.','Our page is as cool as yours, check it out','Keep it up good work.']

    tag = 0
    followed = 0
    likes = 0
    comments = 0

    tagNumber = random.randint(1,3)
    post_from = random.randint(0,10)
    post_interval = random.randint(1,4)
    like_number = random.randint(20,70)


    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'

        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference('network.proxy.type',1)
        self.profile.set_preference('network.proxy.http','localhost')
        self.profile.set_preference('network.proxy.http_port',3128)
        self.profile.update_preferences()


        self.driver = webdriver.Firefox(firefox_profile=self.profile,executable_path=r'./geckodriver.exe')


        self.login()

        self.auto_start()



    def login(self):
        self.driver.get('https://www.instagram.com/')

        self.driver.implicitly_wait(4)

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()

        time.sleep(random.randint(2,7))



    def nav_user(self,user):
        self.driver.get('{}/{}/'.format(self.base_url,self.username))

    # def follow_user(self, user):
    #     self.nav_user(user)

    #     follow_button = self.driver.find_element_by_xpath()

    #     follow_button.click()


    def auto_start(self):
        i = 0
        self.tag = self.tagNumber
        while i < self.tagNumber:
            search_tag = self.hashtag_list[random.randint(0,len(self.hashtag_list) - 1 )]
            i += 1     

            self.driver.get('{}/explore/tags/{}/'.format(self.base_url,search_tag))

            time.sleep(random.randint(2,7))

            start_row = self.post_from // 3 if self.post_from // 3 != 0 else 1
            start_pic_row = self.post_from % 3 if self.post_from % 3 != 0 else 1

            starter_thumb = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[{}]/div[{}]'.format(start_row,start_pic_row)).click()
                                                             
            while(self.like_number != 0):
                time.sleep(random.randint(1,3))
                button_click = 0

                next_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
                btn = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span') 
                aria_label = btn.find_element_by_tag_name('svg').get_attribute("aria-label")
                text_area = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                submit_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button')
                follow_button = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')

                like_decision =  random.getrandbits(1)
                comment_decision =  random.getrandbits(1)
                follow_decision = random.getrandbits(1)

                if aria_label != 'Unlike' and like_decision:
                    btn.click()
                    self.likes += 1
                    self.like_number -= 1
                    time.sleep(random.randint(2,6))
                    if comment_decision:
                        text_area.click()
                        time.sleep(random.randint(2,4))
                        text_area.send_keys(self.comment_list[random.randint(0, len(self.comment_list) - 1 )])

                        time.sleep(random.randint(2,4))
                        submit_btn.click()
                        self.comments += 1
                    if follow_button.text != 'Following' and follow_decision:
                        follow_button.click()
                        self.followed +=1
                        time.sleep(random.randint(2,4))
                while(button_click < random.randint(1,4)):
                    next_btn.click()
                    button_click += 1
        

        print('Tag {} photos.'.format(self.tag))
        print('Followed {} accounts.'.format(self.followed))
        print('Liked {} photos.'.format(self.likes))
        print('Commented {} photos.'.format(self.comments))



if __name__ == '__main__':


    config_path = './config.ini'

    cparser = configparser.ConfigParser()

    cparser.read(config_path)

    username = cparser['AUTH']['USERNAME']
    password = cparser['AUTH']['PASSWORD']

    ig_bot = IgBot(username,password)
