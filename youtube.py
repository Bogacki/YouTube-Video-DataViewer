from selenium import webdriver
from selenium.webdriver.common.by import By
from pytube import YouTube

chrome_driver_path = ".\chromedriver"

class yt:
    def __init__(self):
        self.driver = ""
        self.videos = []
        self.query = ""


    def open_driver(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.set_page_load_timeout(15)


    def search_videos(self, input):
        if self.driver:
            pass
        else:
            self.open_driver()
        self.input = input.replace(" ", "+")
        self.driver.get(f"https://www.youtube.com/results?search_query={self.input}")
        found_confirm = False
        try:
            confirm = self.driver.find_element(By.LINK_TEXT,"ZGADZAM SIĘ")
            if confirm:
                found_confirm = True
                confirm.click()
        except:
            pass
        if found_confirm == False:
            try:
                confirm = self.driver.find_element(By.LINK_TEXT, "I agree")
                if confirm:
                    found_confirm = True
                    confirm.click()
            except:
                pass
        self.videos = self.driver.find_elements(By.CSS_SELECTOR,"#video-title")[0:5]

        return self.videos

    def get_video_data(self,index):
        video = self.videos[index].get_attribute('href')
        video = YouTube(video)
        return video


