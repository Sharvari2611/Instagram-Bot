# Instagram-Bot
Instagram bot is basically a project which i developed out of curiosity as i wanted to learn the mechanism behind the working of actual bots. All this happens through browser automation.The bot opens instagram logs in with your login credentials  and start doing things we instructed to do. This automation is done using  selenium which is freeware and open source automation tool. Same mechanism has been used here in my bot and it searches for the various mandala pages as the variable passed in the code was mandala pages. It visits the top 5 posts, likes them and comments on the post. This will help in more interaction with various art accounts.

Browser automation works in following way:

You serve it your credentials.
You set the criteria for who to follow, what comments to leave, and which type of posts to like.
Your bot opens a browser, types in https://instagram.com on the address bar, logs in with your credentials, and starts doing the things you instructed it to do.
Next, you’ll build the initial version of your Instagram bot, which will automatically log in to your profile.

How to Automate a Browser:

For this version of your Instagram bot, you’ll be using Selenium which is freeware and open source automation tool.
First, install Selenium. During installation, make sure you also install the chrome webdriver required.The main purpose of the ChromeDriver is to launch Google Chrome. Without that, it is not possible to execute Selenium test scripts in Google Chrome as well as automate any web application. 
Duplicating code is especially bad  because Selenium code is dependent on UI elements, and UI elements tend to change. When they do change, you want to update your code in one place. That’s where the Page Object Pattern comes in and hence we write the code by using classes. we define a class in which we use seperate function for logging into the account and a different function to make the bot do the respective activities.

We write the following code:

    1. from time import sleep
    2. from selenium import webdriver
    3. class Instabot:
    4.	  def __init__(self):
    5.    	self.login('your username','Your password')
    6.    	self.search_for_mandala('mandalaarts')     
    7.   def login(self,username,password):
    8.          self.driver=webdriver.Chrome(executable_path=r"D:\\chromedriver_win32\\chromedriver.exe")
    9.          self.driver.get("https://www.instagram.com/accounts/emailsignup/")
    10.         sleep(5)
    11.         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[2]/p/a").click()
    12.         sleep(3)
    13.         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
    14.         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
    15.         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]").click()
    16.         sleep(5)
	 
Lines 1 and 2 import sleep and webdriver.

Line 8 initializes the Chrome driver and sets it to browser.

Line 9 types https://www.instagram.com/ on the address bar and hits Enter.

Line 10 waits for five seconds so you can see the result. Otherwise, it would close the browser instantly.

Line 11 finds the element <a> whose text is equal to Log in and then clicks on the login link. It does this using XPath, but there are a few other methods you could use.

line 12 would wait for 3 seconds so that we see the result.

Line 13 and Line 14 will find the elements <a> whose text is equal to " Enter Username" and "Password" by using the Xpath and then the username and password  provided in Line 5 will be send to the respective tags.

Line 15 will click on the login as directed and then u would be logged in to the account.
  
In this way we can automate the browser and log in to our accounts and then write the code for the bot to perform the resective actions.
  
