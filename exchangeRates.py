'''
Created on Sep 7, 2017

@author: DeltaSierra4_

This program collects the exchange rate data for various currencies
'''
from bs4 import BeautifulSoup
import urllib2

#urlList = ["https://www.bloomberg.com/quote/USDJPY:CUR", "https://www.bloomberg.com/quote/USDKRW:CUR", "https://www.bloomberg.com/quote/USDGBP:CUR", "https://www.bloomberg.com/quote/CNYKRW:CUR", "https://www.bloomberg.com/quote/EURUSD:CUR"]
urlList = []

currlist = urllib2.urlopen("https://www.easymarkets.com/int/learn-centre/discover-trading/currency-acronyms-and-abbreviations/")
currySoup = BeautifulSoup(currlist, "html.parser")
table = currySoup.find("table")
rows=table.findAll('td')
rowText = [str(item.string) for item in rows]
rowCurrency = rowText[1::2]
for i in range(0,len(rowCurrency)):
    if len(rowCurrency[i]) != 3:
        rowCurrency[i] = rowCurrency[i][0:3]

allAdded = False
while not allAdded:
    fromCurrency = raw_input("From what currency would you like to exchange? Type the three letter abbreviation in uppercase.") 
    toCurrency = raw_input("To what currency would you like to exchange? Type the three letter abbreviation in uppercase.")
    if fromCurrency.upper() not in rowCurrency or toCurrency.upper() not in rowCurrency:
        print "One of your currencies is not recognized. Please input them again."
        continue
    urlAdd = "https://www.bloomberg.com/quote/" + fromCurrency.upper() + toCurrency.upper() + ":CUR"
    urlList.append(urlAdd)
    allDone = raw_input("Would you like to add more? Type Y if you're done, or type N to add more links.")
    while allDone.upper() != "Y" and allDone.upper() != "N" or not allDone.isalpha():
        print "That was an incorrect input"
        allDone = raw_input("Would you like to add more? Type Y if you're done, or type N to add more links.")
    if allDone.upper() == "Y":
        allAdded = True

for item in urlList:
    res = urllib2.urlopen(item)
    soup = BeautifulSoup(res, "html.parser")
    if soup.select_one(".price") == None:
        print "Whoops, looks like Bloomberg doesn't handle that currency!"
        continue
    exRate = soup.select_one(".price").string
    print item[32:38] + ": " + exRate + " " + item[35:38] + " per " + item[32:35]

pause = raw_input("Press the enter key to exit.")