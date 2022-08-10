#https://www.youtube.com/watch?v=nCuPv3tf2Hg
from flask import Flask, render_template, request,jsonify
# from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from pprint import pprint
import pymongo

searchiteminput=input("Enter the search item : ")

listofalllinks=[]
for pageno in range(1,2):

    html_text=requests.get(f'https://www.flipkart.com/search?q={searchiteminput}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={pageno}').text
    soup=bs(html_text, "html.parser")


    everything= soup.find_all('div', class_ ='_1AtVbE col-12-12')


    baseurl="https://www.flipkart.com"
    for i in everything:
        for link in i.find_all('a',href=True):
            listofalllinks.append(baseurl + link['href'])

#testlink='https://www.flipkart.com/samsung-galaxy-f41-fusion-blue-128-gb/p/itm4769d0667cdf9?pid=MOBFV5PWG5MGD4CF&lid=LSTMOBFV5PWG5MGD4CFZ8YQJZ&marketplace=FLIPKART&q=samsung&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=7b24d29c-b75b-4fe9-8c72-592140e0daed.MOBFV5PWG5MGD4CF.SEARCH&ppt=sp&ppn=sp&ssid=vpqmebh1a80000001629486636886&qH=fe546279a62683de'
list2={}
for j in listofalllinks:

    r = requests.get(j).text
    soup1 = bs(r, "lxml")
    try:
        name = soup1.find("span", class_='B_NuCI').text
        review=soup1.find("div", class_="t-ZTKy").text
    except:
        name="No name"
        review="No review found"

    list2={"name: ": name,
           "Review": review
    }

    print(list2)







