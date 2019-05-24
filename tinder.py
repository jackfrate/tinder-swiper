from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time


class TinderBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument(
            r"--user-data-dir=C:\Users\jackf\AppData\Local\Google\Chrome\User Data")
        mobile_emulation = {"deviceMetrics": {
            "width": 360, "height": 640, "pixelRatio": 3.0}}
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(
            chrome_options=options)
        # executable_path='chromedriver.exe'

    def respect_women(self):

        self.driver.get("https://tinder.com")
        time.sleep(5)
        # just loop till the card is gone
        try:
            swipes = 0
            # this is a css selector that lets us find a recCard class, even if the shit after it gets changed (which it very well could)
            actions = ActionChains(self.driver)
            # self.driver.find_element_by_class_name('[attribute^="recCard"]')
            while True:
                print('swiped person: ', swipes)
                # press the right arrow
                time.sleep(0.01)
                actions.send_keys(Keys.ARROW_RIGHT).perform()
                swipes += 1
            print("out of swipes \n printed ", swipes, " swipes")
        except:
            print('shits broken fam')


if __name__ == "__main__":
    swipey_boi = TinderBot()
    swipey_boi.respect_women()
