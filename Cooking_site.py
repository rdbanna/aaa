from bs4 import BeautifulSoup
import requests
import pandas as pd
import math
import re
import panda as pd

def Getcontent(childsoup):
    global Nameof,updme,maing,sec
    #for heading / name
    Nameof= childsoup.find('h1').getText()
    #for method
    met = childsoup.find('ol', class_="recipe-method__list")
    newme = met.find_all('li')
    updme = ""
    for x in range(len(newme)):
        updme = updme + str(x + 1) + " " + newme[x].getText() + "\n"
    #for ingrident
    ing = childsoup.find('div', class_="gel-layout recipe-ingredient-list")
    main = ing.find_all('li')
    maing = ""
    for c in main:
        maing = maing + c.getText() + "\n"
    #for only name of ingrudebt
    Second = childsoup.find_all('a', class_="recipe-ingredients__link")
    sec = ""
    for v in Second:
        sec = sec + v.getText() + "\n"
    return Nameof,sec,updme,maing


def linkgen(seeall,numberofr
    ChildUrls = []
    numofp=numberofr//24
    for x in range(math.ceil(numofp)):
        ChildUrls.append(seeall+"&page="+str(x+1))
    return ChildUrls

#proogrma starts here

Countryurl="https://www.bbc.co.uk/food/cuisines"
rcou=requests.get(Countryurl)
CountrySoup=BeautifulSoup(rcou.content,"html.parser")
CountryLink=CountrySoup.find_all('a',class_="promo promo__cuisine")
CountryLinks=[]
for C in CountryLink:
    CountryLinks.append("https://www.bbc.co.uk"+C.get('href'))

Names = []
Maing = []
Met = []
Cui = []
Sec = []










for P in CountryLinks:
    Mainurl = P
    rmain = requests.get(Mainurl)
    Mainsoup = BeautifulSoup(rmain.content, 'html.parser')
    PageUrl = "https://www.bbc.co.uk"+Mainsoup.find('a',class_="see-all-recipes-link").get('href')

    numbers=Mainsoup.find('div',"see-all-recipes-link__container").getText()
    temp = re.findall(r'\d+', numbers)
    res = list(map(int, temp))
    number=int(res[0])
    childurls = []
    for y in linkgen(PageUrl,number):
        rchild = requests.get(y)
        childpa = BeautifulSoup(rchild.content, 'html.parser')
        division = childpa.find('div', class_="gel-layout gel-layout--equal promo-collection")
        clinks = division.find_all('a')
        for v in clinks:
            childurls.append("https://www.bbc.co.uk" + v.get('href'))

    point = 0
    for y in childurls:
        point = point + 1
        ornchild = requests.get(y)
        childsoup = BeautifulSoup(ornchild.content, 'html.parser')
        cuis = Mainsoup.find('h1').getText()
        Getcontent(childsoup)
        Names.append(Nameof)
        Maing.append(maing)
        Sec.append(sec)
        Met.append(updme)
        Cui.append(cuis)
        print("NOw running"+" "+str(point)+" "+cuis)
        print("vishal")
            for x in range(5):
                print("vishal")

MainData=pd.DataFrame(
    {
        'Recipe name':Names,
        'ingredients':Maing,
         'ingredients name':Sec,
        'method':Met,
        'Cuisine':Cui,

    }
)
MainData.to_csv(input("enter file name"))







