# How to find API key for discourse page
_Slug: _

---
**Post ID:** 636354  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/how-to-find-api-key-for-discourse-page/178166/1  

I want to access the API key of dicourse page for tds project 1. kindly suggest some ways to access it.

---
**Post ID:** 636375  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/how-to-find-api-key-for-discourse-page/178166/2  

You need to access it somewhat like:


`COOKIES = {
    "_t": " YOUR_COOKIE"
}

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
}

session = requests.Session()
session.headers.update(HEADERS)
session.cookies.update(COOKIES)`
to get your _t, go to inspect->application->cookies->_t cookie there


copy paste whatever i wrote and chatgpt it, it will elaborate for you, if required ![That's a simple, smiling yellow emoticon or emoji.
](https://emoji.discourse-cdn.com/google/slight_smile.png?v=14)

---
**Post ID:** 637330  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/how-to-find-api-key-for-discourse-page/178166/3  

Where can I get a reference or some material that may Guide me to complete the project

