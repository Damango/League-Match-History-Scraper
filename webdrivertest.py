import csv
import bs4
import time
from urllib.request import urlopen as uReq
from selenium.webdriver.support.ui import WebDriverWait as wait
from bs4 import BeautifulSoup as soup


from selenium import webdriver

url = "https://www.leagueofgraphs.com/summoner/na/Busters"

def get_value():
    driver = webdriver.Chrome()
    driver.get(url)
    
  
    
    
    complete = False
    i = 0
    j = 1
    victoryCount = 0
    defeatCount = 0
    


    
    
    
    while not complete:
        if(j + 1 > 30):
            break
        else:
            driver.find_element_by_class_name('see_more_ajax_button').click()
            time.sleep(1)
            j = j + 1
            gamesList = driver.find_elements_by_class_name('victoryDefeatText')
        
    
    while i < len(gamesList):
        if gamesList[i].text == 'Victory':
            victoryCount = victoryCount + 1
        elif gamesList[i].text == 'Defeat':
            defeatCount = defeatCount + 1
        #print(gamesList[i].text)
        
        i = i + 1
   
    
    
    totalGames = victoryCount + defeatCount
   
    print('Victories: ' + str(victoryCount))
    print('Defeats: ' + str(defeatCount))
    print('Total Games: ' + str(totalGames))
    print('Win Rate: ' + str((victoryCount / totalGames) * 100)  + "%")
    driver.quit()
    return

get_value()