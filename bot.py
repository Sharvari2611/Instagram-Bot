from time import sleep
from selenium import webdriver
from random import randint
class Instabot:
	links=[]
	comments=['Great post!','Amazing work:)','Your posts are awesome','Awesome!!!','This is so great!']
	def __init__(self):
		self.login('kalaa_kaushalya','sharu@1999')
		self.search_for_mandala('mandalaarts')

	def login(self,username,password):
		self.driver=webdriver.Chrome(executable_path=r"D:\\chromedriver_win32\\chromedriver.exe")
		self.driver.get("https://www.instagram.com/accounts/emailsignup/")
		sleep(5)
		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[2]/p/a").click()
		sleep(3)
		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]").click()
		sleep(5)
		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
		sleep(3)
		self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
		sleep(3)

	def search_for_mandala(self,hashtag):
		search_box=self.driver.find_element_by_xpath("//input[@placeholder='Search']")
		search_box.send_keys('#'+ hashtag)
		sleep(5)
		self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
		sleep(5)

		links=self.driver.find_elements_by_tag_name('a')
		def condition(link):
			return '.com/p/'in link.get_attribute('href')
		valid_links=list(filter(condition,links))
			
		for i in range(5):
			link=valid_links[i].get_attribute('href')
			if link not in self.links:
				self.links.append(link)
		for link in self.links:
			self.driver.get(link)
			sleep(3)
		#like
			self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
			sleep(3)
		#comment
			self.driver.find_element_by_class_name('RxpZH').click()
			sleep(1)
			self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys(self.comments[randint(0,4)])
			sleep(2)
			self.driver.find_element_by_xpath("//button[@type='submit']").click()
			sleep(2)
def main():
	my_bot=Instabot()
if __name__=='__main__':
	main()


