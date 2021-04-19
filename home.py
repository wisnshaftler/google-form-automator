from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import random

browser = webdriver.Chrome('chromedriver')
(browser.page_source).encode('utf-8')

link = input("enter link ") #get user link
rounds = int(input("how much vote wanted ")) #get how many times needs to run this code
votes = input("if specific vate wanted, then add need answer number \n ex :- first question need answer is 2 and second question need answer is 3 then enter like this \n 2,3 \n if you dont want this press enter without entering numnber ")
votes = votes.split(",") #split votes 

qcount = 0 #declare the question count variable

input("press enter to start")
browser.get(link) #load the webpage

quez = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionBaseRoot")#get all questions to array
qcount = len(browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionBaseRoot"))#count how much questions have to answer

print("found " + str(qcount) + " questions")

onGoin =0 #current going question

if len(votes) ==qcount: #if user choose custom answers run this codes
    qcount = qcount-1 #adjest the numbers to computer 
    while rounds >0:
        try:
            answersCount = len(quez[onGoin].find_elements_by_xpath(".//div[contains(@class, 'exportToggleEl')]"))#get how much answers have
            winner = int(votes[onGoin].strip())-1 #give the winning answer this is the selected one
            selectedOne = quez[onGoin].find_elements_by_xpath(".//div[contains(@class, 'exportToggleEl')]") #select the all answers
            selectedOne[winner].click()#click on the wining answer
            onGoin = onGoin+1 #increasing the question id
            
            if(qcount < onGoin):
                rounds = rounds-1
                browser.find_element_by_class_name("appsMaterialWizButtonEl").click()#find submit button and click it
                onGoin =0
                browser.get(link)#load the form again
                quez = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionBaseRoot")#load all questions
                print("needs to run " + str(rounds) +" rounds")
        except:
            answersCount = len(quez[onGoin].find_elements_by_xpath(".//div[contains(@class, 'quantumWizTogglePapercheckboxEl')]"))
            winner = int(votes[onGoin].strip())-1
            selectedOne = quez[onGoin].find_elements_by_xpath(".//div[contains(@class, 'quantumWizTogglePapercheckboxEl')]")
            selectedOne[winner].click()
            onGoin = onGoin+1
            
            if(qcount < onGoin):
                rounds = rounds-1
                browser.find_element_by_class_name("appsMaterialWizButtonEl").click()
                onGoin = 0
                browser.get(link)
                quez = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionBaseRoot")
                print("needs to run " + str(rounds) +" rounds")
                
    print("Done")
    browser.close()
    input("press enter ")
    exit()

#below codes are like above codes same thing. the difference is the answer is get randomly 
qcount = qcount-1
while rounds >0:
    try:
        answersCount = len(quez[onGoin].find_elements_by_xpath(".//div[contains(@class, 'exportToggleEl')]"))
        winner = random.randint(1, answersCount)-1
        selectedOne = quez[onGoin].find_elements_by_xpath(".//div[contains(@class, 'exportToggleEl')]")
        selectedOne[winner].click()
        onGoin = onGoin+1
        
        if(qcount < onGoin):
            rounds = rounds-1
            browser.find_element_by_class_name("appsMaterialWizButtonEl").click()
            onGoin =0
            browser.get(link)
            quez = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionBaseRoot")
            print("needs to run " + str(rounds) +" rounds")
    except:
        answersCount = len(quez[onGoin].find_elements_by_xpath(".//div[contains(@class, 'quantumWizTogglePapercheckboxEl')]"))
        winner = random.randint(1, answersCount)-1
        selectedOne = quez[onGoin].find_elements_by_xpath(".//div[contains(@class, 'quantumWizTogglePapercheckboxEl')]")
        selectedOne[winner].click()
        onGoin = onGoin+1
        
        if(qcount < onGoin):
            rounds = rounds-1
            browser.find_element_by_class_name("appsMaterialWizButtonEl").click()
            onGoin = 0
            browser.get(link)
            quez = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionBaseRoot")
            print("needs to run " + str(rounds) +" rounds")

print("Done")
browser.close()
input("press enter ")
exit()
