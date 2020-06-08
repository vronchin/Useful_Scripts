import requests
from bs4 import BeautifulSoup
listOfCrashes = []
for year in range(1908, 2020):
    htmlRequest = requests.get("http://planecrashinfo.com/{0}/{0}.htm".format(year))
    soup = BeautifulSoup(htmlRequest.text)
    for i in range(4,len(soup.body.select("tr td")),4):
        listOfCrashes.append({"date": soup.body.select("tr td")[i].get_text(),
        "location" : soup.body.select("tr td")[i+1].get_text(),
        "aircraft" : soup.body.select("tr td")[i+2].get_text(),
        "fatalities" : soup.body.select("tr td")[i+3].get_text()})

print(len(listOfCrashes),listOfCrashes[:5])