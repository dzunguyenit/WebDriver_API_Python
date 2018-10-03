from selenium import webdriver
from selenium.webdriver.common.by import By


class AirbnbExercise1():

    def test(self):
        baseUrl = "https://www.airbnb.com/"
        # driver = webdriver.Firefox()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # Elements and design has changed on Airbnb website after the lecture was made
        searchBox = driver.find_element(By.NAME, "query")
        searchBox.send_keys("Hawaii")


nguyen = AirbnbExercise1()
nguyen.test()
