import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCase(unittest.TestCase):

    def test(self):
        #Setting up chromedriver
        chromedriver = "chromedriver"
        driver = webdriver.Chrome(chromedriver)
        
        # Used a temporary pwd command in config.yml to get the path in the docker container. This is where both index.html and styles.css were curled too. 
        path = "file:///home/circleci/project/index.html"
        
        driver.get(path)
        
        driver.find_element_by_xpath("//button[text() = 'Click me!']").click()
        
        #Assertion to validate our javascript function was successful to change the text.
        element = driver.find_element_by_id("js-example").text
        assert element == 'JavaScript has changed this text!'
        
        driver.close()

if __name__ == "__main__":
    unittest.main()

