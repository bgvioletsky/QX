'''
Author: bgcode
Date: 2024-08-11 09:04:38
LastEditors: bgcode
LastEditTime: 2024-08-11 09:05:38
Description: 
FilePath: /QX/script/proxy.py
'''
import requests
from lxml import html

url = "https://jc.guanxi.cloudns.be/"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    tree = html.fromstring(response.text)
    a_tag = tree.xpath("//div[@class='header']/a")[0]
    link = a_tag.get("href")

    local_filename = "guanxi"
    with requests.get(link, stream=True, timeout=10) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print(f"File downloaded successfully to {local_filename}")
except Exception as e:
    print(f"An error occurred: {e}")