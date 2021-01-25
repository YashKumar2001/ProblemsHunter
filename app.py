from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from termcolor import colored
import stdiomask

PATH='/Users/yashkumar/Documents/chromedriver/drivers/chromedriver/mac64/87.0.4280.88/chromedriver'

#---------------------------------for finding user solved problems ------------------------------------#

# To search and store problems solved by users
def search_solved():
    for user in users:
        driver.get('https://codeforces.com/submissions/{0}'.format(user))
        driver.find_element_by_xpath('//*[@id="verdictName"]/option[2]').click()
        driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[4]/form/div[2]/input[1]').click()
        idx=driver.find_elements_by_class_name('page-index')
        sz=1
        if(len(idx)>0):
            sz=int(idx[-1].text)+1
        for page in range(1,sz):
            driver.get('https://codeforces.com/submissions/{0}/page/{1}'.format(user,page))
            problems=driver.find_elements_by_xpath('//*[@data-problemid]')
            for cur in problems:
                val=cur.find_element_by_tag_name('a')
                link=val.get_attribute('href').split('/')
                id=link[4]+link[6]
                solved.add(id)

#------------------------------------Part for finding unsolved problems by users-------------#

# Search for problems with difficulty diff
def search(diff):
    driver.get("https://codeforces.com/problemset?tags={0}-{0}".format(diff))
    idx=driver.find_elements_by_class_name("page-index")
    sz=1
    if(len(idx)>0):
        sz=int(idx[-1].text)+1
    for page in range(1,sz):
        driver.get("https://codeforces.com/problemset/page/{1}?tags={0}-{0}&order=BY_SOLVED_DESC".format(diff,page))
        problems=driver.find_elements_by_class_name("id")
        for problem in problems:
            if problem.text not in solved:
                return problem.text

#-------------------------------------Main---------------------------------------------------------------#

chrome_options = webdriver.ChromeOptions()
# comment line below to see chrome
# chrome_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Set for solved problems by users
solved =set()
# user list
users = input("Enter the usernames:").split(' ')
# List of prolem ratings
lis=input("Enter the problem ratings:").split(' ')
lis.sort()

search_solved()
prob={}
for diff in lis:
    prob[diff]=search(diff)
print()
for key,val in prob.items():
    print(key,end=' : ')
    print("https://codeforces.com/contest/{0}/problem/{1}".format(val[:-1],val[-1]))
print()
driver.quit()
