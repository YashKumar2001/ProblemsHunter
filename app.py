from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from termcolor import colored
import stdiomask
import itertools
import threading
import time
import sys
from os import system, name 

PATH='/Users/yashkumar/Documents/chromedriver/chromedriver'
done = False

# clear function to clear terminal screen
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
        
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rSearching problems' + c)
        sys.stdout.flush()
        time.sleep(0.1)

#---------------------------------for finding user solved problems ------------------------------------#

# To search and store problems solved by users
def search_solved():
    for user in users:
        driver.get('https://codeforces.com/submissions/{0}'.format(user))
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="verdictName"]/option[2]'))).click()
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[2]/div[4]/form/div[2]/input[1]'))).click()
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
chrome_options.headless = True
driver = webdriver.Chrome(PATH, options=chrome_options)
wait=WebDriverWait(driver, 20)

# Set for solved problems by users
solved =set()
# user list
users = input("Enter the usernames:\n").split(' ')
# List of prolem ratings
lis=input("Enter the problem ratings:\n").split(' ')
lis.sort()

t = threading.Thread(target=animate)
t.start()
search_solved()
prob={}
for diff in lis:
    prob[diff]=search(diff)
done=True
clear()
print("\nResults:")
for key,val in prob.items():
    print(key,end=' : ')
    print("https://codeforces.com/contest/{0}/problem/{1}".format(val[:-1],val[-1]))
driver.quit()
