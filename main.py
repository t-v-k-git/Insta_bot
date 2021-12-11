# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException
#C:\Program Files (x86)\Google\ChromeApplication\chrome.exe

path = r"C:\Users\KARTHIKEYA\Downloads\chromedriver.exe"#path for your chromedriver
SIMILAR_ACCOUNT = 'telugu_love_beats143'
USERNAME ='telugu_songs_8d'
PASSWORD ='8dfocks@iiitn'


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(6)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(3)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(6)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(3)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)
        # modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[%s]')
        # m=self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]')
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
         #/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"

            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",
                                       modal)

            time.sleep(3)

            #/html/body/div[5]/div/div/div[2]/ul/div/li[2]/div/div[3]/button
            #find_elements_by_css_selector("li button")
            #button.sqdOP L3NKy y3zKF
            # #react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button
    def follow(self):
        all_buttons=self.driver.find_elements_by_css_selector("li button")
        #o=body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(1) > div > div.Pkbci > button
        for button in all_buttons:
            print(button)
            try:
                button.click()
                time.sleep(3)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()
#/html/body/div[6]/div/div/div/div[3]/button[2]

bot = InstaFollower(path)
bot.login()
bot.find_followers()
bot.follow()
