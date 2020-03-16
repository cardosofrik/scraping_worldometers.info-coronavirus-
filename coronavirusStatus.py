import requests
import re

class Coronavirusoutbreak:

        def info(self):
        url = requests.get("https://www.worldometers.info/coronavirus/")
        cases = ['<div class="number-table-main">(.*?)</div>',
                 '<span class="number-table" style="color:red ">(.*?)</span>',
                 '<span class="number-table" style="color:#8080FF">(.*?)</span>',
                '<div class="maincounter-number"> <span>(.*?)</span> </div>',
                 '<span style="color:#aaa">(.*?) </span>']
        for i in cases:
            rex = re.compile(i)
            results = ",".join(rex.findall(str(url.content)))
            print(results)

Coronavirusoutbreak().info()