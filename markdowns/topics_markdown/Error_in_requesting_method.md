# Error in requesting method
_Slug: _

---
**Post ID:** 620807  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/error-in-requesting-method/172916/1  

from the  .json file


`{
        "api": "https://gdsproz2.vercel.app/api",
        "test_code": "GA2_q3",
        "status": "ERROR",
        "error": "Expecting value: line 1 column 1 (char 0)"
    },
    {
        "api": "https://gdsproz2.vercel.app/api",
        "test_code": "GA3_q2",
        "status": "ERROR",
        "error": "'int' object is not subscriptable"
    },`
how come, i am able to get the correct status code and answer then why all these ?


`guddu_mishra_z@LAPTOP-JARF4H9A:~$ curl -X POST "https://gdsproz2.vercel.app/api"   -H "Content-Type: application/x-www-form-urlencoded"   -d "questiWhat is the JSON body we should send to https://api.openai.com/v1/chat/completions for this? (No need to run it or to use an API key. Just write the body of the request below.)".)"
"\n    var textarea = document.getElementById(\"q-generate-addresses-with-llms\");  \ntextarea.removeAttribute(\"disabled\");  \ntextarea.classList.remove(\"d-none\");\n\n\n\n\n// Retrieve the textarea by its ID  \nvar textarea = document.getElementById(\"q-generate-addresses-with-llms\");  \n\n// Define the JSON content  \nvar jsonData = {  \n  \"model\": \"gpt-4o-mini\",  \n  \"messages\": [  \n    { \"role\": \"system\", \"content\": \"Respond in JSON\" },  \n    { \"role\": \"user\", \"content\": \"Generate 10 random addresses in the US\" }  \n  ],  \n  \"response_format\": {  \n    \"type\": \"json_schema\",  \n    \"json_schema\": {  \n      \"name\": \"address_response\",  \n      \"strict\": true,  \n      \"schema\": {  \n        \"type\": \"object\",  \n        \"properties\": {  \n          \"addresses\": {  \n            \"type\": \"array\",  \n            \"items\": {  \n              \"type\": \"object\",  \n              \"properties\": {  \n                \"county\": { \"type\": \"string\" },  \n                \"country\": { \"type\": \"string\" },  \n                \"state\": { \"type\": \"string\" }  \n              },  \n              \"required\": [\"county\", \"country\", \"state\"],  \n              \"additionalProperties\": false  \n            }  \n          }  \n        },  \n        \"required\": [\"addresses\"],  \n        \"additionalProperties\": false  \n      }  \n    }  \n  }  \n};  \n\n// Insert the JSON string into the textarea  \ntextarea.value = JSON.stringify(jsonData, null, 2); // Pretty-print with indentation\n\n"`
`guddu_mishra_z@LAPTOP-JARF4H9A:~$ curl -X POST "https://gdsproz2.vercel.app/api"   -H "Content-Type: application/x-www-form-urlencoded"   -d "questiWhat is the ton/x-www-form-urlencoded"   -d "question=What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/"
"https://gkmfrombs.github.io/dolfacts/"guddu_mishra_z@LAPTOP-JARF4H9A:~$`
[@carlton](/u/carlton) sir  [@Jivraj](/u/jivraj) sir i am getting zero marks please look in to this, may be i get some marks for atleast these two questions??

---
**Post ID:** 621179  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/error-in-requesting-method/172916/3  

Please take some action on it sir [@carlton](/u/carlton) .

---
**Post ID:** 621350  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/error-in-requesting-method/172916/4  

I think they are sending `GET` request instead of `POST` request.


I have already posted this in the below thread. See





![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001231/48/67068_2.png)
[Project 2 - TDS Solver - Discussion Thread](https://discourse.onlinedegree.iitm.ac.in/t/project-2-tds-solver-discussion-thread/169029/698) [Tools in Data Science](/c/courses/tds-kb/34)


[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini) 
Why am my I getting GET request to my api endpoint? It must be IITM’s http request because I have not shared it with anyone. 
 [[image]](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/9/e9a461b563e8ed65b91515d22c9999413e33b6f5.png) 
It clearly written in the project 2 in TDS portal that api  must  accept  POST request, not GET. 
 [[image]](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c1a8cba5ed8456711a70a4e5e5618fda747683fb.png) 
It is requested to kindly look into this matter and please clarify.
  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini) Pls clarify and resolve this matter.

---
**Post ID:** 621942  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/error-in-requesting-method/172916/5  

We don’t send any GET request our script only sends POST requests. These requests have come from 10 different ips, must be a bot.

---
**Post ID:** 621949  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/error-in-requesting-method/172916/6  

what about mine sir it was send to me through the mail??

