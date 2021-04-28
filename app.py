from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from termcolor import colored
import itertools
import threading
import time
import sys
from os import system, name 

PATH=''
done = False
text="Fetching solved problems"
choice=0
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
        sys.stdout.write('\r'+text + c)
        sys.stdout.flush()
        time.sleep(0.1)

#----------------------------------------------Login----------------------------------------------#
def login():
    username=''
    password=''
    if(username==''):
        username=input("Enter your codeforces username:\n")
        password=input("Enter your codeforces password:\n")
    driver.get('https://codeforces.com/enter?')
    driver.find_element_by_xpath('//*[@id="handleOrEmail"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="enterForm"]/table/tbody/tr[4]/td/div[1]/input').click()

#----------------------------------------------registered users----------------------------------------------#
def get_users():
    link=input("Enter the link for mashup:")
    driver.get(link)
    driver.find_element_by_xpath('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table/tbody/tr[2]/td[6]/a[2]').click()
    rows=driver.find_elements_by_xpath('//*[@id="pageContent"]/div[5]/div[6]/table/tbody/tr') 
    for row in range(1,len(rows)):
        td=rows[row].find_elements_by_tag_name('td')[1]
        user=td.find_element_by_tag_name('a').text
        users.append(user) 

#---------------------------------for finding user solved problems ------------------------------------#

# To search and store problems solved by users
def search_solved():
    for user in users:
        driver.get('https://codeforces.com/submissions/{0}'.format(user)) 
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="verdictName"]/option[2]'))).click()
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[{0}]/div[4]/form/div[2]/input[1]'.format(choice+1)))).click()
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

#------------------------------------Problems added in past--------------------------------------------#
#To avoid adding problems that were part of past mashup
def past_problems():
    with open('solved.txt') as f:
        for line in f:
            solved.add(line.rstrip())

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
# comment line below to see chrome working
# chrome_options.headless = True
# To avoid downloading chrome driver every time, download chrome driver for your chrome version and insert the path to that file
# into the path variable located at the top in app.py 
if PATH=='':
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
else:
    driver = webdriver.Chrome(PATH, options=chrome_options)
wait=WebDriverWait(driver, 20)

# user list
users=list()
choice=eval(input("Enter the choice:\nEnter 1 to give username manually\nEnter 2 to fetch users from mashup link\n"))
if(choice==1):
    users=input("enter the usernames:\n").split(' ')
else:
    login()
    time.sleep(6)
    get_users()
more=1
t = threading.Thread(target=animate)
t.start()
solved =set()
past_problems()
# Set for solved problems by users
search_solved()
done=True
# text="Searching problems"
while(more):
    clear()
    # List of prolem ratings
    lis=input("Enter the problem ratings:\n").split(' ')
    lis.sort()

    prob={}
    for diff in lis:
        prob[diff]=search(diff)
    clear()
    print("\nResults:")
    file=open('solved.txt','a')
    for key in lis:
        val=prob[key]
        solved.add(val)
        file.write(val+"\n")
        print(key,end=' : ')
        print("https://codeforces.com/contest/{0}/problem/{1}".format(val[:-1],val[-1]))
    file.close()
    more=int(input("Wanna Search for more problems?Press 1 else press 0\n"))
    
driver.quit()
