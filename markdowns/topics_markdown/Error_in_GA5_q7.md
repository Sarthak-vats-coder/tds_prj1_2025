# Error in GA5_q7
_Slug: _

---
**Post ID:** 621758  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/error-in-ga5-q7/173124/1  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@iamprasna](/u/iamprasna)


While reviewing the logs for my project submission, I noticed that test GA5_q7 failed with the following error:


`{
        "test_code": "GA5_q7",
        "status": "FAILED",
        "error": "HTTP 413: <html>\r\n<head><title>413 Request Entity Too Large</title></head>\r\n<body>\r\n<center><h1>413 Request Entity Too Large</h1></center>\r\n<hr><center>nginx/1.24.0 (Ubuntu)</center>\r\n</body>\r\n</html>\r\n"
    }
]`
From my understanding, this error occurs when the uploaded file exceeds the server’s maximum request size, which is typically limited by the client_max_body_size setting in nginx. Since we were not expected to modify server configurations or deployment settings as part of the submission, this seems to be outside the scope of my control.


I kindly request if it would be possible to re-run the test case with a smaller input file for this question. I have tested the logic locally, and it works correctly with various input sizes.


Please let me know if anything further is needed from my side.

---
**Post ID:** 622025  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/error-in-ga5-q7/173124/2  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini) please look into this

---
**Post ID:** 622246  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/error-in-ga5-q7/173124/3  

Hi Mishat,


Unfortunately the requirement was that your endpoint would be able to handle anything that a GA would normally require. Since your endpoint fails to handle that scenario, we cannot re evaluate this endpoint. The same file was sent to others and it succeeded.


Kind regards

