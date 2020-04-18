#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse

class UnsupportedBrowserType(Exception):
   """Raised when Browser is not one of Chrome, Firefox, or Edge"""
   def __init__(self, value):
     message = f"{value} is not one of Chrome, Firefox, or Edge"
     super().__init__(message)

class browser:
  options = Options()
  options.add_argument('window-size=1440x900')
  options.add_argument('headless')

  def __init__(self, browsertype="Chrome"):
    self.options = Options()
    self.browsertype = browsertype
    if self.browsertype == "Chrome":
        self.driver = webdriver.Chrome(options=self.options)
    elif self.browsertype == "Firefox":
        self.driver = webdriver.Firefox(options=self.options)
    elif self.browsertype == "Edge":
        self.driver = webdriver.Edge(options=self.options)
    else:
        raise UnsupportedBrowserType(self.browsertype)
        
  @classmethod
  def chrome(cls):
      # constructor method
      return webdriver.Chrome(options=cls.options)

  @classmethod
  def firefox(cls):
      return webdriver.Firefox(options=cls.options) 

  @classmethod
  def Edge(cls):
    return webdriver.Edge(options=cls.options)


def main():
    for i in range(0,args.repeat):
        tester = browser.chrome()
        tester.get('https://www.targetwebsite.com/loginpage')
        #time.sleep(1) # use this to wait one second if waiting on redirect

        tester.find_element_by_id('username').send_keys("johnny.bravo@live.com")
        tester.find_element_by_id('password').send_keys("buddyboy") 
        # Find the submit button after entering credentials
        submitbutton = tester.find_element_by_css_selector("CSS_selector_here)
        submitbutton.click()
        # Start of checking expected web page after submtting password
        pageresponse = tester.find_element_by_xpath("XPATH response here").text
        if pageresponse.find("incorrect") !=-1:
            # if it returns -1, then the substring is not found in the string
            # this conditional means the substring does exist in the string
            print(pageresponse)
        else:
            print("Password is correct, or page response is something new, such as denied by web app firewall/bot detection")
        tester.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Runs a series of web requests using selenium to test web page responses.')

    parser.add_argument('--repeat', metavar='repeat', type=int, nargs=None,
                    help='Input the number of times to repeat webpage request')

    args = parser.parse_args()
    main()