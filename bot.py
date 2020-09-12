from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver import ActionChains

import os 
import time
import configparser
import random


class IgBot:
    hashtag_list = ['augmented', 'augmented_reality', 'augmentedreality','ar','augmentedrealityart','augmentedrealityapplicationtesting','technology','virtualreality','virtualshow','business','businessfuture','robotics','robot','robots','industrialdesign','industrialarchitecture','informationtechnology','leadingtechnology']
    comment_list = ['This is awesome! :)', 'Augmented Reality is the Future, check our page too.', 'This is literally cool, check our page as well..','This is great post! Keep it up','Future is coming with augmented reality, just keep in mind :)','This is what we like to see :)','Our page is as cool as yours, check it out','Keep it up good work.', 'Thank you for this great post','This is amazing post :0','This post made our day, thanks a lot','Thanks a lot for the post','We really like your page, keep it up good work','You are sharing amazing post, appreciate it','We like these kind of post :)','Like your page and posts!','Like this post a lot','Your page is amazing, good work!','Love your posts and page as well, good work','Have a great day and keep it up good work','Interesting with technology? just bare with us, like your posts as well','Hope you are doing like in this post, have a great day','Life is great, thank you for this inspirational post','Inspiration does not come easily right? check our page as well','Love what you are doing, well done']

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
                time.sleep(random.randint(2,10))
                button_click = 0

                next_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
                btn = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span') 
                aria_label = btn.find_element_by_tag_name('svg').get_attribute("aria-label")
                # text_area3 = self.driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                # text_area = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                # text_area2 = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form').find_element_by_tag_name('textarea')
                
                submit_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button')
                follow_button = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')

                like_decision =  random.getrandbits(1)
                comment_decision =  random.getrandbits(1)
                follow_decision = random.getrandbits(1)

                if aria_label != 'Unlike' and like_decision:
                    btn.click()
                    self.likes += 1
                    self.like_number -= 1
                    time.sleep(random.randint(2,10))
                    if comment_decision:
                        # text_area3.click()
                        print('comment try')
                        time.sleep(random.randint(2,10))
                        comment_text = self.comment_list[random.randint(0, len(self.comment_list) - 1 )]
                        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()
                        time.sleep(random.randint(2,10))
                        textarea1 = self.driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                        for character in comment_text:
                            actions = ActionChains(self.driver)
                            actions.move_to_element(textarea1)
                            actions.send_keys(character)
                            actions.perform()
                            time.sleep(random.uniform(0.2,0.5))                            
                        # text_area3.send_keys(self.comment_list[random.randint(0, len(self.comment_list) - 1 )])
                        time.sleep(random.randint(2,10))
                        submit_btn.click()
                        self.comments += 1
                    if follow_button.text != 'Following' and follow_decision:
                        time.sleep(random.randint(1,10))
                        follow_button.click()
                        self.followed +=1
                        time.sleep(random.randint(2,10))
                while(button_click < random.randint(1,10)):
                    time.sleep(random.randint(1,6))
                    next_btn.click()
                    button_click += 1

            time.sleep(random.randint(3, 12))

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
