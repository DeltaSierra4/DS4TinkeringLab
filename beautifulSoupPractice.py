'''
Created on Aug 25, 2017

@author: DeltaSierra4_
'''

'''This is a practice file for learning how to use beautifulsoup'''

#Import and set url
import requests
from bs4 import BeautifulSoup

#Prompt asking for user ID name that you wish to look up.
userName = raw_input("Whose ID are you looking up?")
date1 = raw_input("From what date? Enter in yyyymmdd format.")
date2 = raw_input("to what date? Enter in yyyymmdd format.")

while not date1.isdigit() or not date2.isdigit() or date1 > date2:
    print "You entered an invalid character, or the dates are not in the correct order."
    date1 = raw_input("From what date? Enter in yyyymmdd format.")
    date2 = raw_input("to what date? Enter in yyyymmdd format.")

urlString = "http://arcturus.su/tenhou/ranking/ranking.pl?name="+userName+"&r=24&d1="+date1+"&d2="+date2+"&l=0"

url = requests.get(urlString)
stuff = url.text


#analyze html
soup = BeautifulSoup(stuff, 'html.parser')

#Select the points you want to extract!
name = soup.html.head.title
#title = soup.html.body.h2.encode("utf-8")

#Print your results
print "name: " + name.string

print soup.find("div", {"id": "records"})