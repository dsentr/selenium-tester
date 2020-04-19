# Python Selenium Tester


This script uses the selenium library to create real browser sessions, and make requests to a webpage. It can be used as a template to make requests to a webpage, and test for specific results. 
One use would be to test a web application and bot detection of a websites authentication endpoints. Since Selenium uses a real browser with real headers and cookies, it is harder to detect as a bot, compared to sending straight requests.


## Getting started

- clone this repository
- Edit the page element IDs and any other information you expect in the page response in the main function. 
- Start a new virtual environment named venv in this folder `python3 -m venv venv`
- Activate the new virtual environment `source venv/bin/activate`
- Install the required python packaged from requirements.txt `pip install -r requirements.txt` This was created using `pip3 freeze > requirements.txt`
- Script usage: `./main.py --repeat 3` as an example to run the test against the webpage 3 times.
