from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from io import StringIO

driver = webdriver.Chrome('/Users/sivab/Downloads/chromedriver')
years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
url = 'https://www.iplt20.com/points-table/men/'
for i in years:
    url_c = url+i
    driver.get(url_c)
    players = driver.find_elements_by_xpath('//td[@class="ng-binding"]')
    f = open("demofile.txt", "a")
    f.write(i+'\n')
    f.write('Played,Won,Lost,Tied,N/R,Net Run Rate,For,Against,Pts')
    i = 1
    for p in players:
        if(i<9):
            f.write(p.text+',')
            i = i+1
        elif(i==9):
            f.write(p.text+'\n')
            i=1
