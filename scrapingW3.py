from bs4 import BeautifulSoup as bs4
import json
import requests as req

urlTitle = "glossary"
title = urlTitle.capitalize()
# title = "CMath"
# url = "https://www.w3schools.com/python/module_"+urlTitle+".asp"
url = "https://www.w3schools.com/python/python_ref_glossary.asp"

path = "Module"

html = req.get(url).text

soup = bs4(html, 'html.parser')
td = soup.find_all("td")
arr = []
for t in td:
    strt = str(t)
    if "<a href" in strt:
        strt = strt.replace("<td><a", "")
        start = strt.find(">")
        result = strt[start+1:-9]
        arr.append(result)

with open("keywords.json","r") as f:
    jsonFile = json.loads(f.read())
    # jsonFile[path][title] = arr
    jsonFile[title] = arr
    

with open("keywords.json","w") as f:
    json.dump(jsonFile, f, indent=2)