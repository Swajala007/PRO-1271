#import time
import csv
#from selenium import webdriver
from bs4 import BeautifulSoup
import requests
url = requests.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")
#br = webdriver.Chrome("C:/Users/sanya/OneDrive/DesktopCoding/PRO-127/chromedriver.exe")
#br.get(url)
#time.sleep(10)

def scraping():
    header=["Name","Distance","Mass","Radius","c4","c5","c6","c7"]
    star =[]

    for i in range(0,5):
        data = BeautifulSoup(url.text,"html.parser")
       
        tb = data.find_all("table")
        print(tb)
        tabler = tb[7].find_all("tr")
       # print(tabler) 
    
        tbr = tb.find_all("tr")
        tmd = []
    
        for i in tbr:
            td = i.find_all("td")
            #print(td)
            #tempdata = []
          #  for index,td in enumerate(td):
             #   try:
              #      tempdata.append(td.contents[0])
               # except:
              #      tempdata.append[""] 
            data = [i.text.rstrip() for i in td]
            tmd.append(data)
           # print(tmd)
           

       
        #page.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()    
        
    with open("scrapingdata.csv","w") as f:
        csvdata = csv.writer(f)
        csvdata.writerow(header)
        for i in range(0,len(data)):
            csvdata.writerow(data[i])
scraping()                                

