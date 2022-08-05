########################################################################################################
## This script looks for Apple and Androud updates and exports them to a table in separate html files  #
## @author networksecurityvodoo                                                                        #
## @version v1.0.0 (05-08-2022)                                                                        #
########################################################################################################

## dependencies                                    ##
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/library/urllib.parse.html

import re
from urllib.parse import urljoin


## Current Updates from Apple  ##

import requests
from bs4 import BeautifulSoup


vgm_url = 'https://support.apple.com/en-gb/HT201222'
html_text = requests.get(vgm_url).text
content = BeautifulSoup(html_text, 'html.parser')


# Extract title of page
page_title = content.title.text

# Extract body of page
page_body = content.body

# Extract head of page
page_head = content.head

# print the result
#print(page_head) #, page_head)


filtered_body = page_body.find("div", {"id": "tableWraper"})

# BeautifulSoup to Text 
#res = page_body.get_text()
#print (res)

#Write to file
#text_file = open("sample.txt", "w", encoding='utf-8')
#n = text_file.write(res)
#text_file.close()


with open("output1.html", "w", encoding='utf-8') as file:
    file.write(str(filtered_body))


### ----------------------------------- ##



##### Android Patches #####

android_url = 'https://source.android.com/security/bulletin'
html_text2 = requests.get(android_url).text
android_content = BeautifulSoup(html_text2, 'html.parser')
android_page_body = android_content.body
#filtered_body_android = android_page_body.find_all("div", {"class": "devsite-table-wrapper"})
#mydivs = soup.find_all("div", {"class": "stylelistrow"})



table = android_page_body.find(lambda tag: tag.name=='table') 


# Replace relative Paths in Links <"href"> with absolute paths
absolutize2 = lambda m: ' href="' + urljoin(android_url, m.group(1)) + '"'
table_convert_link = re.sub(r' href="([^"]+)"', absolutize2, (str(table)))

print (table_convert_link)

with open("output2.html", "w", encoding='utf-8') as file:
    file.write(table_convert_link)


