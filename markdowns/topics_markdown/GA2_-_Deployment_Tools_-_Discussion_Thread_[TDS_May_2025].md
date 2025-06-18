# GA2 - Deployment Tools - Discussion Thread [TDS May 2025]
_Slug: _

---
**Post ID:** 623682  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/1  

Please post any questions related to [Graded Assignment 2 - Deployment Tools](https://exam.sanand.workers.dev/tds-2025-05-ga2).


Please use markdown code formatting (fenced code blocks beginning with ```) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.


Deadline: 2025-05-26T18:30:00Z

---
**Post ID:** 623817  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/2  



---
**Post ID:** 625115  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/3  

Having a problem in [Technical Assessment](https://exam.sanand.workers.dev/tds-2025-05-ga2#hq-ollama).


"Paste your ngrok forwarding URL here:


[https://abcd1234.ngrok-free.app](https://abcd1234.ngrok-free.app)


SyntaxError: Unexpected token ‘<’, "<!DOCTYPE “… is not valid JSON”


but when I’m doing “curl -i [https://abcd1234.ngrok-free.app/api/tags](https://abcd1234.ngrok-free.app/api/tags)”


the output is “{“models”:}”. So, what’s the actual issue? [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---
**Post ID:** 625130  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/4  

Sir, since free ngrok links show a warning page on the initial request, the same page appears in the GET request for the TDS 2025 May GA2 - Local Ollama Endpoint. Could you please include a `ngrok-skip-browser-warning` header in the evaluation request, or provide a way to bypass this issue?

---
**Post ID:** 625590  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/5  

Q2


Hi [@Jivraj](/u/jivraj) [@carlton](/u/carlton) . When I try submitting the URL from my phone I get a correct answer whereas from my laptop I get this error. Is it an issue of caching in the browser?


[![This is a screenshot of a webpage element, likely part of a tutorial or debugging tool for GitHub Pages.  It shows an error message indicating that an email address is not found in the deployed GitHub Pages website, despite being included in the code.  The user is prompted to check the URL and possibly clear the cache.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0acac009624fdd725ba77e3400ccdd677c1df499_2_690x205.png)Screenshot from 2025-05-12 22-13-401297×387 45.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0acac009624fdd725ba77e3400ccdd677c1df499.png)


[![The image shows a code challenge or tutorial on GitHub Pages.  The user is tasked with publishing a page including an email address, correctly formatted to avoid obfuscation by CloudFlare.  The challenge also involves identifying the correct GitHub Pages URL and understanding how to bust the cache if necessary.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a6cb7c590bdf5bd1f141b766d27b82cd711464ef_2_364x500.jpeg)dab57387-ece3-454c-87c1-e3e6a7f66314933×1280 84.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6cb7c590bdf5bd1f141b766d27b82cd711464ef.jpeg)

---
**Post ID:** 625594  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/6  

Hi [@23f2004759](/u/23f2004759) Can you look under network tab what the response is?


It might be browser that’s causing issue.

---
**Post ID:** 625595  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/7  

Yes I tried using a different browser and it worked just fine. Sorry for the inconvenience [@Jivraj](/u/jivraj) Sir ![That's a simple, smiling yellow emoticon or emoji.
](https://emoji.discourse-cdn.com/google/slight_smile.png?v=14)

---
**Post ID:** 625596  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/8  

![That's a stylized uppercase letter "V".  It appears metallic, possibly gold or bronze, with a textured, almost animal-print-like surface.  The background is a muted green.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/varunagnihotri/48/103035_2.png) VarunAgnihotri:

`ngrok-skip-browser-warning`




done that.


Kind regards.

---
**Post ID:** 625121  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/9  

Sir, since free ngrok links show a warning page on the initial request, the same page appears in the GET request for the TDS 2025 May GA2 - Local Ollama Endpoint. Could you please include a `ngrok-skip-browser-warning` header in the evaluation request, or provide a way to bypass this issue?

---
**Post ID:** 625700  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/11  

So now can we do this ques? Were there some kind of issue on the website? [@Jivraj](/u/jivraj)

---
**Post ID:** 625826  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/12  

Hi,


For the assignment 10. I was able to create the FastAPI application and run queries based on random classes from the dataset and with multiple classes in a single api call, All the responses are as expected, But when I check in the portal no matter what I do the check fails. I tested the queries being sent when I click the check button, I copied the url, test it in my local rest client and got the results which I think are correct. Below is the url and its output (truncated the response).


sample input


`127.0.0.1:8000/api?class=12W&class=10O&class=5B&class=5J`
output


`{
  "students": [
    {
      "studentId": "69",
      "class": "12W"
    },
    {
      "studentId": "320",
      "class": "12W"
    },
    {
      "studentId": "538",
      "class": "10O"
    },
    {
      "studentId": "598",
      "class": "5J"
    },
    {
      "studentId": "637",
      "class": "10O"
    },
    {
      "studentId": "657",
      "class": "5B"
    },
....
  ]
}`
I get the error


`Error: At [0].studentId: Values don't match`
Assuming that the check is done in Ascending order then first element is the smallest and the first element in the csv file.


Please help me in identifying the issue or guide me in the right direction.

---
**Post ID:** 626284  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/13  

Hi,


I still get an error


`TypeError: Failed to fetch`
the same url is working in cli, and in browser too with the warning.

---
**Post ID:** 626556  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/14  

in Q11, i am facing this issue while creating an organization, Your current account, [23f3003724@ds.study.iitm.ac.in], doesn’t have the permissions to perform this task. Log into the Cloud Console using either your Workspace or Cloud Identity super administrator account. You can also copy a link to this Users and Groups task and request that your super administrator complete this step.


kindly help me with this..

---
**Post ID:** 626559  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/15  

in Q6, that one including vercel deployement, i performed the deployement, but the deployement shows deployement not found to me, what could be the possible reason if any of u dealt with a similar issue?

---
**Post ID:** 626835  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/16  

[@Jivraj](/u/jivraj) sir i am facing issues in the vercel question that is the 6th one my deployment is working fine infact i am getting the results as per the question but when i submit the link on the portal it says FAILED TO FETCH.


but when i paste the same  link in my browser with and without parameters i get the desired result

---
**Post ID:** 626956  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/17  

You need to get the oauth credentials from your personal account to setup the OAuth. Then you can use the IITM Account when choosing the account in the actual application run.

---
**Post ID:** 626981  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/18  

okay, well i am done with the issues i was facing, thank you, could u just tell me if we have some sort of limit for requesting in Q12??

---
**Post ID:** 627122  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/20  

in GA-2 yesterday night i solved 6 question and saved all of them last submission shows 6/10 . but today when i started solving remaining question and after saving again it showing 2.75/10 . some question like 9,11 which was based on local showing incorrect now. in yesterday session sir told whatever you do just save it it will persist as solving all 10 Questions in one go is not possible .


sir, pls clearify , do i have to to solve all question in one go, as after doing shut down it all vanishes despite saving .


[![A pale green box displays three recent game saves, showing the date, time, and score for each save.  The most recent save is indicated as the official score.  Each entry has a "Reload" button.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fcdf06a6f424dff38e365f453301905660e9fd5e.png)image743×346 16.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fcdf06a6f424dff38e365f453301905660e9fd5e.png)


[![The image shows a form with instructions to paste the output of `echo $GITHUB_REPOSITORY $GITHUB_TOKEN`.  A user has entered `22f3000982/eshopco-onboarding ghu_iC5reUSM5qKHgNMP13` into the input field, but received an "Error: No codespaces found" message. A "Check" button is also visible.  The image seems to be from a code testing or deployment interface.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/6/26316e3e6242e5047bf2f5d2e9d1cd4b73f02347.png)image592×247 10.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/6/26316e3e6242e5047bf2f5d2e9d1cd4b73f02347.png)

---
**Post ID:** 626954  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/21  

For the GA2, its better to submit all at once as a lot of the answer changes based on the time & duration from last run, as well as you need to make sure that the local servers are running. Token & codesapces timeout after a certain period and you need to redo those.


Easiest way is to do till q8 one by one and anytime you like they are persistent, and for all the rest try to do them at a sitting and don’t close any of the servers (local apis, codespace, ngrok) till all submit

---
**Post ID:** 627211  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/22  

Some submissions require live server, so you have to run that particular code everytime you are solving those questions.

---
**Post ID:** 627338  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/23  

why am i getting Failed to fetch and 403 forbidden in Q12 (ollama)?

---
**Post ID:** 627527  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/24  

Same for me. No matter what I do.

---
**Post ID:** 627675  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/25  

[![The image shows a coding challenge.  The task is to create a FastAPI server that returns student data (student ID and class) in JSON format, either all students or filtered by class using query parameters.  The user has entered an API URL, but it's resulted in a "Failed to fetch" error.  A "Check" button suggests automated verification of the server's response against expected data.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/4/c4527f43f2db7715edfc15d349b014c3967f8625_2_664x500.jpeg)image1079×812 142 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/4/c4527f43f2db7715edfc15d349b014c3967f8625.jpeg)


In question 10, There is an error that Unable to fetch although I have done all the steps correctly.

---
**Post ID:** 627679  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/26  

Sir I’m getting “Failed to fetch” error on q12 ga2. I kept trying to solve but I’m still stuck.

---
**Post ID:** 627714  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/27  

Same issue, It shows data on localhost but not on [https://ee39-113-193-108-241.ngrok-free.app](https://ee39-113-193-108-241.ngrok-free.app)

---
**Post ID:** 627812  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/28  

Hi, you are returing a key in json, you should try returning list directly somewhat like this


`[
    {
      "studentId": "69",
      "class": "12W"
    },
    {
      "studentId": "320",
      "class": "12W"
    },
....
]`

---
**Post ID:** 627901  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/29  

Well I did that and now I get the error.


`Error: At root: Type mismatch - one is array, other is object`
If I follow the example given in the assignment I get the error.


`Error: At [0].studentId: Values don't match`

---
**Post ID:** 627902  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/30  

I tried almost everything even tried serving ollama with nginx and enabling CORS ORIGIN *. Nothing seems to work. I am not sure what am I doing wrong here.



Run Ollama service with modified service file . This is the file located in `/usr/lib/systemd/system/ollama.service`

`[Unit]
Description=Ollama Service
Wants=network-online.target
After=network.target network-online.target

[Service]
ExecStart=/usr/bin/ollama serve
WorkingDirectory=/var/lib/ollama
Environment="HOME=/var/lib/ollama"
Environment="OLLAMA_MODELS=/var/lib/ollama"
Environment="OLLAMA_ORIGINS=*"
Environment="OLLAMA_HOST=0.0.0.0:11434"
Environment="OLLAMA_ALLOW_CREDENTIALS=true"
Environment="OLLAMA_ALLOWED_HEADERS=Content-Type,Authorization"
Environment="OLLAMA_ALLOWED_METHODS=GET,POST,OPTIONS"
User=ollama
Group=ollama
Restart=on-failure
RestartSec=3
RestartPreventExitStatus=1
Type=simple
PrivateTmp=yes
ProtectSystem=full
ProtectHome=yes

[Install]
WantedBy=multi-user.target`

Stop the service and run `ollama serve`

`export OLLAMA_ORIGINS="*"
ollama serve`

Configure nginx and serve all requests to ollama and make sure the all ORIGINS are allowed

In all the cases when I try to access the ngrok url from a different machine or device (mobile) everything works as expected except that first warning that shows by ngrok. For cli or any api client everything works. The moment I try out in with the “check” button in the assignment no matter what I do I get `TypeError: Failed to fetch`.


When I check the network tab i see this error


![The image shows a network request log entry for a "version" resource. The request failed with a "Cross-Origin Resource Sharing (CORS) error: PreflightMissingAllowOriginHeader".  This indicates a problem with the server not properly configuring CORS headers to allow the request from the specified initiator ("exam-tds-2025-05").
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a4255dcdc4b83e1d51164319de92dec63ca078ca.png)


And when I try to disable CORS or no matter what I do I get this error


![That's a screenshot of a terminal or command-line interface showing two API requests.  Both requests received a "No Content" (204) response.  The top one was an OPTIONS request to the `/api/version` endpoint. The time of the request is shown as 23:58:13.393 IST. The bottom request's details are partially obscured.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/3/63222e2733930433e3f211c8deeb5e6e37f65573.png)


I tried several browsers and combinations of disabling CORS but nothing seems to work.

---
**Post ID:** 627937  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/31  

Unable to generate client id and client secret from institute id. However, this issue is not there while using personal email. What to do?


[![The image shows a form for creating a new project.  The user needs to select a parent organization or folder to continue, and there is a search bar to find available folders.  The user has 12 projects remaining in their quota.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/9/19bb8409ffca3168fb8a502374038ce73dd7dcf5_2_690x199.png)Screenshot 2025-05-19 0732271754×507 40.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/9/19bb8409ffca3168fb8a502374038ce73dd7dcf5.png)

---
**Post ID:** 628185  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/32  

Image Compression


I tried many things to compress the given image to 400 bytes.


But not able to achieve it. Have tried using Pillow and other online image compression tools as well. But not able to compress beyond 500 Bytes.

---
**Post ID:** 628213  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/33  

use cwebp directly dont use python. It will compress for sure.

---
**Post ID:** 628215  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/34  

Try using the firefox browser once.

---
**Post ID:** 628304  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/35  

I Did that too. I get the error related to preflight missing origin header.

---
**Post ID:** 628371  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/36  



---
**Post ID:** 628389  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/37  

I also have the same problem. Can anyone please guide??

---
**Post ID:** 628469  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/38  

Some common errors & to fix them for the Q12 (ngrok & Ollama) check this post once [https://discourse.onlinedegree.iitm.ac.in/t/ga-2-q12-failed-to-fetch/175331/2?u=vanshbordia](https://discourse.onlinedegree.iitm.ac.in/t/ga-2-q12-failed-to-fetch/175331/2)

---
**Post ID:** 628551  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/39  

IN GA 2 Q12  “Local Ollama Endpoint”, There is some internal issue from portal.


In Localhost and .ngrok-free.app site also fetch data but on portal it shows “TypeError: Failed to fetch”


And another way to check using curl that also shows right.


here are screenshot that verify:


[![The image shows two browser windows displaying the same JSON response — `{"version": "0.7.0"}` — from two different API endpoints.  One endpoint is on `localhost`, the other uses ngrok (a tunneling service).  Both responses indicate an API version of 0.7.0.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6aee9d95f5efe3af5cff4b95fd1a6e0453651b43_2_690x255.png)Screenshot from 2025-05-20 14-38-541904×704 28.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/a/6aee9d95f5efe3af5cff4b95fd1a6e0453651b43.png)


[![The image shows a terminal window displaying ngrok status information.  It shows an active ngrok session forwarding a localhost port to a public URL, along with details about the session, connection statistics, and recent HTTP requests.  The session is using a free plan.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/f/bf67f9455cc89b260dec7bb0e17eb87451ee7970_2_690x348.png)Screenshot from 2025-05-20 14-39-431920×969 94.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/f/bf67f9455cc89b260dec7bb0e17eb87451ee7970.png)


[![The image shows a terminal window on a dark-themed desktop.  A curl command has been executed to retrieve the version of an ngrok application (version 0.7.0).  The output shows the version number.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/948804a76ebcda0cd5250528ebd33308be3e6495_2_690x380.png)Screenshot from 2025-05-20 14-40-181578×870 34.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/948804a76ebcda0cd5250528ebd33308be3e6495.png)


[![The image shows a web page for a case study on setting up remote diagnostics for an AI chat assistant.  It guides the user through enabling CORS, exposing the application via ngrok, and verifying the setup using a provided URL.  The current attempt to fetch the URL has failed, indicated by an error message.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/8/5885922f056e02de5f6876acb8f9e9b7ee3d60c3_2_690x302.png)Screenshot from 2025-05-20 14-40-511920×843 93.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/8/5885922f056e02de5f6876acb8f9e9b7ee3d60c3.png)

---
**Post ID:** 628568  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/40  

use your personal mail id, not the mail id provided by the institute

---
**Post ID:** 628591  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/41  

Sir,


[![The image shows a form requesting a Vercel URL.  The user entered `https://tds-vercel-v2.vercel.app/api`, which doesn't match the expected format (shown as `https://your-app.vercel.app/api`), resulting in a "Values don't match" error.  A "Check" button is available.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/7/5777f19efa7eac5145e5c128ec70bf7b749bfda8_2_690x292.png)Screenshot 2025-05-20 at 6.34.40 PM1278×542 33.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/7/5777f19efa7eac5145e5c128ec70bf7b749bfda8.png)


GA2 Question 6:  I have successfully deployed the api in vercel [Link](https://tds-vercel-v2.vercel.app/api)  and could get the exact output as desired. But I am getting an error response while checking as  *“Error: At [0]: Values don’t match” *. I tried both as



returning a json

`return JSONResponse(content=body)`
[![The image shows a web browser window displaying a JSON response  `{"marks": [84, 51]}` from an API call to `https://tds-vercel-v2.vercel.app/api?name=K&name=AXkB1`.  The browser's address bar and a few tabs are also visible.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8f8eb71a2e3c138b84f359815dbc8e8c3c1e9417_2_690x209.png)Screenshot 2025-05-20 at 6.49.07 PM1284×390 30.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/f/8f8eb71a2e3c138b84f359815dbc8e8c3c1e9417.png)



also as a string (in order to mimic the exact formatting mentioned in the question with spaces).

[![The image shows a browser window displaying a JSON response  `{ "marks": [84, 51] }` from an API endpoint (`tds-vercel-v2.vercel.app/api?name=K&name=AXkB1`).  The browser's address bar and a few browser tabs (Gmail, Graded Assignment, Grading document, and Dashboard) are also visible.  A "Pretty print" checkbox is also shown, suggesting the JSON is formatted for readability.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/9/59aa87ba1d01416003f5cac502835118bee6ca7f_2_689x260.png)Screenshot 2025-05-20 at 6.34.28 PM1106×418 27.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/9/59aa87ba1d01416003f5cac502835118bee6ca7f.png)


`return Response(content=body, media_type="application/json") ```

Screenshot of my response is also attached. Please let me spot my error. Thanks.`

---
**Post ID:** 628652  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/42  

[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/9/b9e8131873710e27e2a0be0f7097b04ccff4256b_2_372x500.png)Screenshot 2025-05-20 185036536×719 25.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9e8131873710e27e2a0be0f7097b04ccff4256b.png)


While connecting vercel with github it says this as told in the picture.

---
**Post ID:** 628657  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/43  

[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/1/617a6b06686eb6d38d3ec8e28984ec43148cf955_2_690x480.png)image1125×784 21.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/1/617a6b06686eb6d38d3ec8e28984ec43148cf955.png)


The File size is less than 400 byes and i have already done it to lossless still it is not accepting as we can see in the picture as well. I have tried number of times and still it is not being saved

---
**Post ID:** 628659  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/44  

Yes same error happening with me

---
**Post ID:** 628671  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/45  

In Question 2 , when I upload the compressed file it passes the question and I get a score for it . However , when I refresh the  browser that  file is not present there in that question anymore and i don’t get the marks for that after Save.

---
**Post ID:** 628690  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/46  

Without resizing, image size isn’t going below 800 bytes

---
**Post ID:** 628724  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/47  

You need to save the file after you upload, and if you refresh the browser the uploaded file in longer referenced hence you need to reupload it to get the correct score.

---
**Post ID:** 628726  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/48  

After runing this code: ngrok http 11434 --response-header-add “X-Email: 23ds3000034@ds.study.iitm.ac.in” --response-header-add ‘Access-Control-Expose-Headers: *’


On LocalHost data fetched successfully, but on forwarded ngrok URL not able to fetch data.


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/c/ece4cd7dbb84f5ddd6839bb061d26871753e0de9_2_490x500.png)Screenshot from 2025-05-18 15-28-02992×1011 63.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ece4cd7dbb84f5ddd6839bb061d26871753e0de9.png)


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7bd6f59488e666ee4f37d10a1e44e8cdf64427e9_2_690x353.png)Screenshot from 2025-05-18 15-28-321736×890 55 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7bd6f59488e666ee4f37d10a1e44e8cdf64427e9.png)


[![The image shows a dark-themed web browser displaying a "can't reach this page" error message.  The error indicates a DNS resolution failure (DNS_PROBE_FINISHED_NXDOMAIN), suggesting the provided URL is incorrect or the server is unreachable.  A refresh button is available.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/4/d4c9d77f8735acc07ee7a458cc9a43db7d226c3e_2_490x500.png)Screenshot from 2025-05-18 15-28-52992×1011 45.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/4/d4c9d77f8735acc07ee7a458cc9a43db7d226c3e.png)

---
**Post ID:** 628464  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/49  

Errors



504 Gateway Timeout: The ngrok server is not receiving a response from your local Ollama server within the timeout period.


Check that your Ollama server is running and responding correctly. Go to `http://localhost:11434/` to check if its working.


404 Not Found: The requested resource is not found on the server.


Ensure that the URL is correct and the resource exists on your local server.


403 Forbidden: The request is forbidden due to security reasons.


Check that your local server is not blocking the request due to security settings (Generally CORS / Auth Error).


CORS error: Cross-Origin Resource Sharing (CORS) error occurs when the browser prevents a webpage from making requests to a different origin (domain, protocol, or port) than the one the webpage was loaded from.

Few Fixes



`ollama_origins`: Set this to the list of allowed origins. Set the value to *
`ollama_host`: Set this to run on all your network interfaces. Set the value to 0.0.0.0

Linux / Bash -


`export OLLAMA_ORIGINS="*"
export OLLAMA_HOST="0.0.0.0"`
Windows (Command Prompt)


`set OLLAMA_ORIGINS=*
set OLLAMA_HOST=0.0.0.0`
Windows (PowerShell)


`$env:OLLAMA_ORIGINS = "*"
$env:OLLAMA_HOST = "0.0.0.0"`
If it gives DNS probe / other errors try running `ngrok diagnose` and make sure all things are coming as OK in that.


Make sure that your system firewall is correctly setup.

---
**Post ID:** 628543  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/50  

As per your knowledge, you are 50% right in my case, i am using Ubuntu 24.04.2 LTS, and some internal issue with ngrok is now FIXED.



Use a Custom DNS Resolver (Fixes Local DNS Issues):


Edit your `/etc/systemd/resolved.conf`:```


sudo nano /etc/systemd/resolved.conf

`Uncomment and set:`
DNS=8.8.8.8


FallbackDNS=1.1.1.1


`Then restart the resolver:`
sudo systemctl restart systemd-resolved


`THIS FIXED MY ISSUE !!!!`

---
**Post ID:** 628732  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/51  

try cwebp in your terminal directly and try to upload the image using firefox browser.


Using python my image was not able to get compressed below 400bytes but using cwebp helped.

---
**Post ID:** 628788  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/52  

[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/d/8dd7aad39dd2a114b500c36f51f1b1f27d388824.png)image666×299 26.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/d/8dd7aad39dd2a114b500c36f51f1b1f27d388824.png)


Even after compressing the image to lowest quality, the size of output.webp is 870 bytes. I tried different methods including other mentioned terminal tools, online tools, using PIL in Python for compressing the image but none of them is compressing below 800 bytes. Only resizing is working, but we need to keep the dimensions intact.

---
**Post ID:** 628796  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/53  

Hi,


for Q 6 with Vercel, I have resolved the issue. The order in which the marks appear was the issue. The code wasn’t accurate.


wrong code:


`marks = []
    for entry in marks_data:
        if entry.get("name") in names:
            marks.append(entry.get("marks"))`
Correct code is as follows:


`marks = []
    # Build a dictionary for fast lookup
    name_to_marks = {entry["name"]: entry["marks"] for entry in marks_data}

    # Preserve the order of names in query
    marks = [name_to_marks.get(name, None) for name in names]````

---
**Post ID:** 629100  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/55  

Hi @all


There are fix coming for the question 12.

---
**Post ID:** 629245  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/56  

I hope the fix will be implemented soon please see to it that it is implemented before the deadline. FYI I tried changing the DNS and browsers, OSes the problem still exists. I get a 204 (No Content) error where as when I try to access the same url in the same profile on the adjacent tab everything works. I see the version, tags and message “ollama running”.

---
**Post ID:** 629249  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/57  

While doing ngrok + ollama - I am getting error, the reason I suspect is - I am not able to pass headers as given in the command in assignment. It throws - Malformed URL for me when I start ngrok server with headers, so when I tried to run tunnelling directly (without any headers/included all the headers via wildcard *) it throws CORS error I suspect (analysed using network tab)


Please guide what am I doing wrong here?


I have tried editing ngrok.yml too so that I do not have to pass the headers separately, however it does not work as ngrok version I have is 3.22 which does not allow putting these props in yml.

---
**Post ID:** 629381  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/58  

Any information about the q2 boxes Image compression which  is not being compressed less than 400 at any cost. Many of the students are facing the same problem

---
**Post ID:** 629403  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/59  

Dear IITM,


I am writing to submit my assignment for the eShopCo AI Chat Diagnostics task. Below, I provide a detailed explanation of the steps I followed, the results I obtained, and the current status of my Ollama AI chat server exposed via ngrok.


[](#p-629403-steps-completed-1)Steps Completed:

Enabled CORS on Ollama


I set the environment variable `OLLAMA_ORIGINS="*"` to allow cross-origin requests from any domain.


Command used:

bash


Copy code


`export OLLAMA_ORIGINS="*"
ollama serve`
This successfully started the Ollama server locally on `http://localhost:11434`.


2. Exposed Ollama Server via ngrok with Headers


I exposed the local Ollama instance using ngrok, injecting my email in the response headers, and adding necessary CORS headers for frontend integration and diagnostics.


Command used:


bash


Copy code


`ngrok http 11434 \
  --response-header-add "X-Email: 24f1000666@ds.study.iitm.ac.in" \
  --response-header-add "Access-Control-Expose-Headers: *" \
  --response-header-add "Access-Control-Allow-Headers: Authorization,Content-Type,User-Agent,Accept,Ngrok-skip-browser-warning"`
ngrok printed this HTTPS forwarding URL:


`https://43a1-103-11-116-215.ngrok-free.app`


3. Verification via curl commands:



Accessing the root endpoint:

bash


Copy code


`curl http://localhost:11434`
Response: `Ollama is running`



Fetching available models from the Ollama API:

bash


Copy code


`curl http://localhost:11434/v1/models`
Response (JSON):


json


Copy code


`{
  "object": "list",
  "data": [
    {
      "id": "gemma3:1b-it-qat",
      "object": "model",
      "created": 1747847262,
      "owned_by": "library"
    }
  ]
}`

Testing the ngrok endpoint with headers:

bash


Copy code


`curl -I https://43a1-103-11-116-215.ngrok-free.app`
Response headers include:


makefile


Copy code


`Access-Control-Allow-Origin: *
X-Email: 24f1000666@ds.study.iitm.ac.in  (via ngrok response-header)`

Attempted chat endpoint:


Accessing `/v1/chat` on both local and ngrok URLs returned a 404 Not Found error, indicating the Ollama server does not expose a chat API at this path.
Sending a POST request to `/` or `/v1/chat` returned HTTP 405 Method Not Allowed, confirming only GET requests are accepted on this server.


[](#p-629403-summary-and-current-status-2)Summary and Current Status:

CORS is successfully enabled on Ollama with `Access-Control-Allow-Origin: *` header visible on responses.
ngrok exposure works correctly, forwarding requests to my local Ollama instance and injecting the required email header (`X-Email`).
The available API endpoint `/v1/models` returns valid JSON, proving the Ollama server is reachable remotely and responding correctly.
The chat endpoint `/v1/chat` is not available in the current Ollama server setup, so chat messages cannot be sent via HTTP POST as part of this assignment.
The setup satisfies the assignment’s core requirements to enable CORS, expose the server remotely, and verify headers and JSON responses.


[](#p-629403-ngrok-forwarding-url-for-verification-3)ngrok forwarding URL for verification:
cpp


Copy code


`https://43a1-103-11-116-215.ngrok-free.app

you can check the below attachments for proof.

Thank you.

Best regards,
Chauhan Saumyakumar Dilipkumar
IIT Madras`

---
**Post ID:** 629405  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/60  

please help me out for the 12th question it is working fine in my device and any other device but iitm is not accepting the url


here is the forwarding url:


[https://5b22-103-11-116-215.ngrok-free.app](https://5b22-103-11-116-215.ngrok-free.app)

---
**Post ID:** 629520  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/61  

I have attempted the 10th question exactly as required and I am also successfully getting the endpoint.


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/5/45ea0284e7869b3b0a678b454db049497faa5ef5_2_690x387.png)image1366×768 116 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/5/45ea0284e7869b3b0a678b454db049497faa5ef5.png)


But still, the TDS assignment portal is throwing the following error:


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/0/e067993b285a71830a9a70ab366a574efd82e058_2_689x259.png)image1299×489 24.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/0/e067993b285a71830a9a70ab366a574efd82e058.png)


Please let me know of the further steps to resolve this issue.

---
**Post ID:** 629570  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/62  

I was finally able to resolve the issue. Thanks a ton to [@Jivraj](/u/jivraj). The issue was in ngrok command this is the command which worked for me.


`ngrok http 11434 --response-header-add "X-Email: <YOUR_ID>@ds.study.iitm.ac.in" --response-header-add 'Access-Control-Expose-Headers: *' --response-header-add 'Access-Control-Allow-Headers: *'`
Please add your id in the email.

---
**Post ID:** 629619  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/63  

With the GA-2 Question - 10 there are two sub question


(i). [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api) and it has menioned that it should return some thing like this which was clearly mentioned


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84a602ebe5d21eb41c26fad298c11cdf865ee9bc.png)image252×347 1.92 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84a602ebe5d21eb41c26fad298c11cdf865ee9bc.png)


And my output was like


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/2/42b5aea594f020def3836c1031b1d5e143d1fe0d.png)Screenshot 2025-05-22 223820348×497 9.29 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/2/42b5aea594f020def3836c1031b1d5e143d1fe0d.png)


I think this will be correct.


(ii). If the URL has a query parameter `class` , it should return only students in those classes. For example, `/api?class=1A` should return only students in class 1A. `/api?class=1A&class=1B` should return only students in class 1A and 1B. There may be any number of classes specified. Return students in the same order as they appear in the CSV file (not the order of the classes).


I can’t clealy understand what will be expected output is as it mentioned “it should return only students in those classes. For example, `/api?class=1A`” return only student means list of students like this.


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f06d3869bdc542d0718cfff67cc0690761bde7a.png)Screenshot 2025-05-22 223842769×420 10.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f06d3869bdc542d0718cfff67cc0690761bde7a.png)


But still getting error like this


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/0/c09510ce21bc00c16fca06131fc9bd8fbfbd4ffa.png)image1077×210 13.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/0/c09510ce21bc00c16fca06131fc9bd8fbfbd4ffa.png)


Any one have any idea about what (or) how the output will look like for this `http://127.0.0.1:8000/api?class=1A&class=1B` this input. so that I can modify the code.

---
**Post ID:** 629600  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/64  

I’ve tried Question 12 in every way but I am still getting the following error:


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/b/ab312af1daebfd67818f7d80af4eb6826fcb8d75.png)image1283×246 15 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/b/ab312af1daebfd67818f7d80af4eb6826fcb8d75.png)

---
**Post ID:** 629608  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/65  

For this api where you are mentioning the class also, your output should contain both the studentId as well as class like in this below given image.


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/2/42b5aea594f020def3836c1031b1d5e143d1fe0d.png)Screenshot 2025-05-22 223820348×497 9.29 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/2/42b5aea594f020def3836c1031b1d5e143d1fe0d.png)


currently for this api call you are getting only a single array containing the studentId of the mentioned class which is not the correct response format as given in the question.

---
**Post ID:** 629610  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/66  

can you try it out in wsl or linux, we are not good with debugging issues in windows os. Also check below, there are some changes to headers.





![Image could not be processed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/bhuvan/48/121831_2.png) bhuvan:

`ngrok http 11434 --response-header-add "X-Email: <YOUR_ID>@ds.study.iitm.ac.in" --response-header-add 'Access-Control-Expose-Headers: *' --response-header-add 'Access-Control-Allow-Headers: *'`


[@saumya1](/u/saumya1) , [@ShubhamSharma](/u/shubhamsharma) , [@vanshbordia](/u/vanshbordia) , [@23ds3000034](/u/23ds3000034) try above suggestion by bhuvan


Hi [@24f3004935](/u/24f3004935) Q12 is now been fixed, read messages from above regarding solutions to issues with Q12.


If there is still problem with Q12 I would suggest you to go through initial bit of Yesterday’s(22 May) Session where Q12 was discussed.

---
**Post ID:** 629612  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/67  

Under browser dev-tools Check in network tab what exactly is problem.


Common issues:



CORS not being used properly.
Network connectivity error.
Networking rules, if using wsl try to access it through public ip of wsl

---
**Post ID:** 629614  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/68  

Hi [@23f2003651](/u/23f2003651) , [@TANISH_AGGARWAL](/u/tanish_aggarwal)


There is script available with us which compresses image under mentioned size, I check for your image it works and able to compress image under 400 mb which is accepted by portal as well.

---
**Post ID:** 629615  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/69  

Never came across this error, here is what perplexity suggests [https://www.perplexity.ai/search/social-account-is-not-yet-conn-oiYIx4zQSb._Yb1uyikOlA](https://www.perplexity.ai/search/social-account-is-not-yet-conn-oiYIx4zQSb._Yb1uyikOlA)

---
**Post ID:** 629616  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/70  

Hi [@23f2003824](/u/23f2003824)


can you check what you are seeing in the network tab of dev tools in browser.

---
**Post ID:** 629623  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/72  

is it just Q12 is not working in windows?  do i have to use wsl. it is showing 403 error throught the forwarding url

---
**Post ID:** 629624  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/73  

Regarding WSL usage we highly recommend that because we are more comfortable with that, and can help students out. For 403 error, you would need to enable cross origins.


Find documentation below for doing so [Allowing CORS to local Ollama](https://objectgraph.com/blog/ollama-cors/).

---
**Post ID:** 629633  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/74  

CORS is enabled but still the error is 403

---
**Post ID:** 629640  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/75  

good afternoon sir


when i run (venv) PS C:\q11> uvicorn app:app --reload on the terminal, i am getting an error


Error loading ASGI app. Could not import module “app”.


my app.py has all the read, read and write and modify section enabled. could you pls help me on this, thank you.

---
**Post ID:** 629150  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/76  

make sure you have app = FastApi()


also


It is recommended to use wsl.

---
**Post ID:** 629155  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/77  

i have made sure of that too sir, app is FastApi() and i used it on wsl

---
**Post ID:** 629161  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/78  

one more requirement, before running last running command


make sure that you are in the folder where the your written code is there


you can check by command `ls` or `dir`, if this command should show the file in current folder


and can change your directory using `cd`

---
**Post ID:** 629643  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/79  

With the GA-2 Question - 10 there are two sub question


(i). [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api) and it has menioned that it should return some thing like this which was clearly mentioned


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84a602ebe5d21eb41c26fad298c11cdf865ee9bc.png)image252×347 1.92 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84a602ebe5d21eb41c26fad298c11cdf865ee9bc.png)


And my output was like


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/2/42b5aea594f020def3836c1031b1d5e143d1fe0d.png)Screenshot 2025-05-22 223820348×497 9.29 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/2/42b5aea594f020def3836c1031b1d5e143d1fe0d.png)


I think this will be correct.


(ii). If the URL has a query parameter `class` , it should return only students in those classes. For example, `/api?class=1A` should return only students in class 1A. `/api?class=1A&class=1B` should return only students in class 1A and 1B. There may be any number of classes specified. Return students in the same order as they appear in the CSV file (not the order of the classes).


I can’t clealy understand what will be expected output is as it mentioned “it should return only students in those classes. For example, `/api?class=1A`” return only student means list of students like this.


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f06d3869bdc542d0718cfff67cc0690761bde7a.png)Screenshot 2025-05-22 223842769×420 10.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f06d3869bdc542d0718cfff67cc0690761bde7a.png)


But still getting error like this


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/0/c09510ce21bc00c16fca06131fc9bd8fbfbd4ffa.png)image1077×210 13.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/0/c09510ce21bc00c16fca06131fc9bd8fbfbd4ffa.png)


Any one have any idea about what (or) how the output will look like for this `http://127.0.0.1:8000/api?class=1A&class=1B` this input. so that I can modify the code.

---
**Post ID:** 629657  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/80  

try this:


`ngrok http --host-header=localhost 11434 --response-header-add "X-Email: <email>@ds.study.iitm.ac.in" --response-header-add 'Access-Control-Expose-Headers: *' --response-header-add 'Access-Control-Allow-Headers: *'`

---
**Post ID:** 629688  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/81  

[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/1/f121ccfb47464e79071680a4159e5be40694098e_2_690x311.png)image1364×616 29.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/1/f121ccfb47464e79071680a4159e5be40694098e.png)


my vercel url and it works just fine but still it can’t fetch the json value


[https://your-g9upka9i8-akashjana2123s-projects.vercel.app](https://your-g9upka9i8-akashjana2123s-projects.vercel.app)

---
**Post ID:** 629728  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/82  

for the image compression question i used this command


`pngquant --quality=0-0 download.png`
and the resultant image was 316bytes


Error: Could not process image. Is it a browser-supported image? Image pixels do not match the original


i have checked both the dimensions and they were both 500*500


what is the issue i am facing ?

---
**Post ID:** 629807  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/83  

GA-2 Q-2 Compress an Image


In this question, I have an image of 9.6 KB and I need to compress it to less than 400 bytes. I have tried multiple Python codes and tools like squoosh.app, but the image is not compressing to less than 1 KB.


Kindly help.

---
**Post ID:** 629866  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/84  

For the 12th question i did the following set of commands


`export OLLAMA_ORIGINS="*"
export OLLAMA_HOST="0.0.0.0"
ollama serve`
i got like this


`2025/05/23 10:00:28 routes.go:1233: INFO server config env="map[CUDA_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_CONTEXT_LENGTH:4096 OLLAMA_DEBUG:false OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_INTEL_GPU:false OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:/var/snap/ollama/common/models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NEW_ENGINE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:0 OLLAMA_ORIGINS:[*://localhost http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://* vscode-file://*] OLLAMA_SCHED_SPREAD:false ROCR_VISIBLE_DEVICES: http_proxy: https_proxy: no_proxy:]"
time=2025-05-23T10:00:28.721Z level=INFO source=images.go:463 msg="total blobs: 5"
time=2025-05-23T10:00:28.721Z level=INFO source=images.go:470 msg="total unused blobs removed: 0"
time=2025-05-23T10:00:28.721Z level=INFO source=routes.go:1300 msg="Listening on 127.0.0.1:11434 (version 0.6.8)"
time=2025-05-23T10:00:28.722Z level=INFO source=gpu.go:217 msg="looking for compatible GPUs"
time=2025-05-23T10:00:28.738Z level=INFO source=gpu.go:377 msg="no compatible GPUs were discovered"
time=2025-05-23T10:00:28.738Z level=INFO source=types.go:130 msg="inference compute" id=0 library=cpu variant="" compute="" driver=0.0 name="" total="13.6 GiB" available="12.7 GiB"
[GIN] 2025/05/23 - 10:00:38 | 200 |      72.426µs |   49.204.115.73 | GET      "/"
[GIN] 2025/05/23 - 10:00:38 | 404 |      11.263µs |   49.204.115.73 | GET      "/favicon.ico"
[GIN] 2025/05/23 - 10:00:46 | 403 |     396.741µs |   49.204.115.73 | OPTIONS  "/api/version"
[GIN] 2025/05/23 - 10:11:02 | 403 |      69.057µs |   49.204.115.73 | GET      "/"`
the requests are not being processed


and i did the ngrok port forwarding with this command


`ngrok http --host-header=localhost 11434 --response-header-add "X-Email: <email>@ds.study.iitm.ac.in" --response-header-add 'Access-Control-Expose-Headers: *' --response-header-add 'Access-Control-Allow-Headers: *'`
whats the problem here anyone

---
**Post ID:** 629953  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/85  

good afternoon sir, i am facing this error in vercel app question from week 2 when i run vercel --prod in my wsl. my vercel.json is as follows


{


“functions”: {


“api/index.py”: {


“runtime”: “vercel-python@3.12”


}


},


“routes”: [


{


“src”: “/api”,


“dest”: “/api/index.py”


}


]


}


Error: Function Runtimes must have a valid version, for example `now-php@1.0.0`.


could you pls guide. thank you.

---
**Post ID:** 629868  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/86  

Try modifying your vercel.json with this and make sure that your files are in the respective dir


`{
  "builds": [
    { "src": "api/index.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/api", "dest": "api/index.py" }
  ]
}`

---
**Post ID:** 629882  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/87  

thank you very much for the response sir. i got a message you just deployed a new project but upon accessing it, i am getting a 404 not found error.

---
**Post ID:** 629951  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/88  

There must be some problem with the your configuration, in week2 session 1 on youtube Carlton showed how to configure vercel properly, check that out.


Kind Regards


Jivraj

---
**Post ID:** 629960  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/89  

![Image could not be processed](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png)
[GA2 - Deployment Tools - Discussion Thread [TDS May 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/66) [Tools in Data Science](/c/courses/tds-kb/34)


    can you try it out in wsl or linux, we are not good with debugging issues in windows os. Also check below, there are some changes to headers. 

[@saumya1](/u/saumya1) , [@ShubhamSharma](/u/shubhamsharma) , [@vanshbordia](/u/vanshbordia) , [@23ds3000034](/u/23ds3000034) try above suggestion by bhuvan 
Hi [@24f3004935](/u/24f3004935) Q12 is now been fixed, read messages from above regarding solutions to issues with Q12. 
If there is still problem with Q12 I would suggest you to go through initial bit of Yesterday’s(22 May) Session where Q12 was discussed.

---
**Post ID:** 629978  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/90  

[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/1/f121ccfb47464e79071680a4159e5be40694098e_2_690x311.png)image1364×616 29.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/1/f121ccfb47464e79071680a4159e5be40694098e.png)


my url ([https://your-g9upka9i8-akashjana2123s-projects.vercel.app](https://your-g9upka9i8-akashjana2123s-projects.vercel.app)) works perfectly and works according to the question in GA2 Q6 but still it throws this error

---
**Post ID:** 629754  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/91  

when trying to access the link it throws access error, maybe that could be a cause for the test cases not able to validate them.


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/3/b3038d86a17674e9a416368bb36509d034baa995_2_690x417.png)image1007×609 12.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/3/b3038d86a17674e9a416368bb36509d034baa995.png)


to make it public



Go to your Vercel Dashboard.
Select your project.
Go to Settings > General.
Find the Privacy setting.
Change the project from Private to Public.
Save the changes.

---
**Post ID:** 629988  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/92  

The Error you are facing is because there wouldn’t be any initial “/” endpoint, you can paste the /api endpoint and check for the response


`https://your-app.vercel.app/api`
for getting particular class, you can use


`https://your-app.vercel.app/api?name=X&name=Y`

---
**Post ID:** 630007  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/93  

i am working on wsl on my windows machine


these are the following steps i have performed


`export OLLAMA_ORIGINS="*"
export OLLAMA_HOST="0.0.0.0"
ollama serve`
then i have used ngrok with the following command


`ngrok http --host-header=localhost 11434 \
  --response-header-add "X-Email: 22fe3002579@ds.study.iitm.ac.in" \
  --response-header-add "Access-Control-Expose-Headers: *" \
  --response-header-add "Access-Control-Allow-Headers: *"`
now i have tested with the following output


`curl http://localhost:11434
Ollama is running`
[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/5/c5ddb5dac41f9eea867b5c2f031d3e9b3b726e4d.png)image798×195 6.54 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/5/c5ddb5dac41f9eea867b5c2f031d3e9b3b726e4d.png)


`curl http://localhost:11434/v1/models
{"object":"list","data":[{"id":"gemma3:1b","object":"model","created":1747990322,"owned_by":"library"}]}`
[https://63bd-49-204-115-73.ngrok-free.app](https://63bd-49-204-115-73.ngrok-free.app)


TypeError: Failed to fetch


still getting the same error [@Jivraj](/u/jivraj)

---
**Post ID:** 630056  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/94  

Hi There !


Can you please share the step by step guide along with the github repository for this question because I am also facing the same issue.

---
**Post ID:** 630057  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/95  

Hi There! can you please share the solution since I facing the similar issue.

---
**Post ID:** 630061  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/96  

[](#p-630061-image-compression-1)Image Compression
No matter what I try, it just isn’t getting compressed below 400 bytes. I was able to bring it down to 511 bytes, but no more


[](#p-630061-question-2)Question
Download the image below and compress it losslessly to an image that is less than 400 bytes.


![Image could not be processed](data:image/png;base64,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19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMCgn7W19MJECBAgECJgKCXMHsJAQIECBA4KyDoZ309nQABAgQIlAgIegmzlxAgQIAAgbMC/wbW8UnoMk1g6wAAAABJRU5ErkJggg==)


[](#p-630061-what-i-tried-3)What I Tried

I removed the alpha channel
Then compressed the png

[](#p-630061-please-help-or-analyze-if-the-given-question-is-even-solvable-4)Please help or analyze if the given question is even solvable

---
**Post ID:** 630089  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/98  

If AnyOne is facing issue in Q12 with mac , do one thing just load a previous version of ollama from their git release page , to run ollama do


“export OLLAMA_HOST=0.0.0.0


ollama serve”


and to run ngork do


`ngrok http 11434 --response-header-add "X-Email: <YOUR_ID>@ds.study.iitm.ac.in" --response-header-add 'Access-Control-Expose-Headers: *' --response-header-add 'Access-Control-Allow-Headers: *'`
That’s it Should run now , Not sure about windows but i guess it should run there too .

---
**Post ID:** 630090  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/99  

![Image could not be processed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/mathurapriya/48/14288_2.png) Mathurapriya:

`marks = []
    # Build a dictionary for fast lookup
    name_to_marks = {entry["name"]: entry["marks"] for entry in marks_data}

    # Preserve the order of names in query
    marks = [name_to_marks.get(name, None) for name in names]````


Thanks A Ton [@Mathurapriya](/u/mathurapriya)

---
**Post ID:** 630099  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/100  

Hi Sir,


for Q12, I can open the url from other accounts also (`Ollama is running` is showing). But still getting an error as “failed to fetch”.   [@Jivraj](/u/jivraj)


My observations:



I checked in the network tab of the `Assignment page`, it shows CORS error but I have included `Access-Control-Allow-Origin: "*"`
I checked in the ngrok logs, it shows as part of the assignment, it is trying to hit  `/favicon.ico` which is returning 404. (should I add some icon for this? or is this expected?)


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/3/63c002caa7407ed30a668b65d196f5aa849f9fab_2_690x112.png)Screenshot 2025-05-24 at 10.30.44 AM2274×372 105 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/3/63c002caa7407ed30a668b65d196f5aa849f9fab.png)
When I click on the ngrok url, inspite of adding `Ngrok-skip-browser-warning` to the header,  I can’t make the following screen go off. I tried a lot of things here.


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/0/a0adf93f57a31f5fdaabe5ca83fb388a5ca0f481_2_690x416.png)Screenshot 2025-05-24 at 10.32.46 AM2026×1222 246 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/0/a0adf93f57a31f5fdaabe5ca83fb388a5ca0f481.png)

Please help me what is expected/ suggest any workaround for this.


Thank you!

---
**Post ID:** 630104  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/101  

there are many methods you can approach this, i have used Flask API



initialize a git
create a folder api and place the data.json that you have downloaded and create index.py

index.py


`from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('api/data.json') as f:
    students = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = []
    for name in names:
        student = next((s for s in students if s["name"] == name), None)
        marks.append(student["marks"] if student else None)
    return jsonify({"marks": marks})`
outside the api folder create vercel.json and requirements.txt


vercel.json


`{
  "builds": [
    { "src": "api/index.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/api", "dest": "api/index.py" }
  ]
}`
requirements.txt


`Flask
flask-cors`
make sure you push it to your repository


`git add .
git commit -m "vercel deployment"
git push origin main`
sign in to vercel and under create project select the following repository and click deploy


make sure that your vercel configurations are proper.


then you would get the link.

---
**Post ID:** 630106  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/102  

I have tried using this command


`pngquant --quality=0-0 download.png`
and i was able to compress it to 316 bytes.


But when i tried to upload it, i got the error.


`Error: Could not process image. Is it a browser-supported image? Image pixels do not match the original`


The image pixels was same as the original (500*500), so does the other properties


i have tried with chrome and edge and still gives me the same error.


[@Jivraj](/u/jivraj) could you please look into it.

---
**Post ID:** 630141  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/103  

Have You solved all the problems I am facing fetch error for all the api based questions.


Can you please share you github so we can solve together or I can easily ask for halp from you.

---
**Post ID:** 630272  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/104  

[@Jivraj](/u/jivraj) -


After several attempts, I was able to successfully expose my local Ollama server via ngrok and confirmed that it’s returning a valid 200 OK response with all the expected CORS and custom headers. However, while checking the answer for Q12, I’m still getting the error:


`TypeError: Failed to fetch`
This is occurring despite the fact that:



The server responds with HTTP/2 200 OK
All required headers (Access-Control-Allow-Origin, X-Email, etc.) are present
The response body is valid JSON

Here’s a sample response from my server:


`HTTP/2 200
access-control-allow-headers: *
access-control-allow-origin: *
access-control-expose-headers: *
content-type: application/json; charset=utf-8
x-email: 21f1005745@ds.study.iitm.ac.in
...

{"model":"llama2","created_at":"2025-05-24T09:34:20.93916Z","message":{"role":"assistant","content":""},"done_reason":"load","done":true}`
Could this be an issue on the evaluation script’s side — perhaps due to the model’s output being blank or due to how it interprets the headers?


I have tried another browser as well, but that gave me - `TypeError: NetworkError when attempting to fetch resource.`


Let me know if there’s a specific format or header I might still be missing. Happy to retry with updated instructions if needed.

---
**Post ID:** 630276  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/105  

For the Q 12, I have tried using


`ngrok http --host-header=localhost 11434 --response-header-add "X-Email: 23ds2000044@ds.study.iitm.ac.in" --response-header-add 'Access-Control-Expose-Headers: *' --response-header-add 'Access-Control-Allow-Headers: *'` command. But still not working not able to clerly understand what king of response we receive.


This was image from ngrok login pannel


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/941f43d5c79fe277966d6a4b4b295035732340bf_2_690x225.png)Screenshot 2025-05-23 1205191738×569 28.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/941f43d5c79fe277966d6a4b4b295035732340bf.png)


This was from termminal  output with curl command


[![Image could not be processed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/b/db13a569917f856c32be9f240f0e2a2f75667ac0.png)Screenshot 2025-05-23 120415992×389 12.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/b/db13a569917f856c32be9f240f0e2a2f75667ac0.png)


Is there is any other fixes required??


Thankyou!!!

---
**Post ID:** 630179  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/107  

same issue with me


please help us

---
**Post ID:** 630273  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/108  

![That's a solid, uniform block of light blue color.  There is no texture or variation in the image.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/948bcc04e2eee5b6d0e83d2b47259474eef1e7c3.png)
[objectgraph.com](https://objectgraph.com/blog/ollama-cors/?utm_source=perplexity)


![It's a cartoon illustration of an alpaca's head and shoulders, presented in a simplistic, black-outlined style against a white, rounded-square background.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/c/3c66e8a6ff05df93f3157e0f91e7d5720f26b4c4.png)
[Allowing CORS to local Ollama](https://objectgraph.com/blog/ollama-cors/?utm_source=perplexity)
Open AI Ollama Catalyst







Use linux/wsl and enables cors and restart ollama as instructed in this website


and


then redo the q12, you should able to solve.

---
**Post ID:** 630384  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/109  

Thanks for the article, it helped out.


Even though they have mentioned the steps for enabling CROS for ollama, it didnt work at first.


`sudo systemctl edit ollama.service`
changing the ollama.service configuration was not being reflected, so i reinstalled ollama using this tutorial


[![The image is a tutorial graphic titled "How to Uninstall Ollama in Ubuntu and Erase Installed Models".  It features the Ubuntu penguin logo, a picture of an alpaca, and a cartoon alpaca icon. The text is in bold, red and navy blue.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/a/2aed7214af2cb6787ca57316b95a28e6796ed20c.jpeg)](https://www.youtube.com/watch?v=PLU1UpQuKbg)

`sudo systemctl edit ollama.service`
while running this command the system might throw a force edit command which would delete all the contents in the service file, so avoid doing that. if you did that add these in the ollama.service file


`[Service]
Environment="OLLAMA_HOST=http://0.0.0.0:11434"
Environment="OLLAMA_ORIGINS=*"
ExecStart=
ExecStart=/usr/local/bin/ollama serve
User=ollama #replace with your user name (whoami)
Restart=on-failure`
then following the article enables CROS and it worked out.


Thanks

---
**Post ID:** 630575  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/110  

i have a problem in q7. i got the result but it says the “Error: No step matches 23f3004381@ds.study.iitm.ac.in” whereas my answer is correct in [GitHub - bharatsrinivasiitm/q7](https://github.com/bharatsrinivasiitm/q7)


[![The image shows a GitHub Actions workflow configuration.  It's attempting to run a simple "Hello, world!" command, but is failing because it cannot find a matching step.  The error message indicates a mismatch between the configured email address and the steps defined. The user is prompted to enter their repository URL.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/d/8daeb35ccf7c16f419d754f05eabc1a20e1322be.png)Screenshot 2025-05-25 023457837×542 18.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/d/8daeb35ccf7c16f419d754f05eabc1a20e1322be.png)

---
**Post ID:** 630613  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/112  

[![This is a screenshot of a GitHub Actions workflow YAML file.  The workflow, named "Workflow with Email Identifier," is triggered manually or by pushing to the `main` branch.  It defines a job `hello-world` that runs on an Ubuntu machine and performs two steps: printing "Hello, world!" and displaying the current date.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/f/dfd487195ca972ad5e44c9fba1fdb8f78e81a566_2_413x500.png)image687×831 37.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/f/dfd487195ca972ad5e44c9fba1fdb8f78e81a566.png)


You haven’t modified the GPT yml file with your email address, you’re still using the placeholder value

---
**Post ID:** 630637  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/113  

[@Jivraj](/u/jivraj) , [@carlton](/u/carlton) Sir, what to do for the  question about codeepaces, I have already finished solving it , but the codespace automatically shuts down after 30 mins of inactivity , so after the deadline is passed , there is a possibility that my codespace could have shut down and it may not be live ,so the answer could be marked as wrong? Please clarify what to do


Regards,


Prateek P

---
**Post ID:** 630928  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/114  

Don’t worry about that, it should work when you submit assignment.

---
**Post ID:** 630975  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/115  

Hi , my code is also working on browser


`https://tds-23f3002416-puneet-bajajs-projects-cf63608e.vercel.app/api`


But i am getting


`TypeError: Failed to fetch`


can you help me, how did you get it working

---
**Post ID:** 631141  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/116  

A related question: For the FastAPI server (question 10), I get one mark for putting in the URL when the server is up and running. However, if I stop the server and move on to answering other questions, and then try submitting again, I lose that 1 mark.


Do I have to have the server running for this question every time I submit? Shouldn’t I be given the 1 mark after getting it right the first time?

---
**Post ID:** 631169  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/117  

![That's a close-up, slightly blurry, headshot of a man with short, light brown hair.  He appears to be middle-aged, and the lighting casts shadows on his face. He's wearing what looks like a dark-colored shirt or jacket.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/s.anand/48/15264_2.png) s.anand:

Deadline: 2025-05-26T18:30:00Z




Hi [@carlton](/u/carlton) [@HritikRoshan_HRM](/u/hritikroshan_hrm)


I’m a little confused. Is the deadline 25th or is it 27th (Tuesday)?

---
**Post ID:** 631228  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/118  

Issue with GA 2 Submissions and Session Errors


Dear [@s.anand](/u/s.anand) and [@carlton](/u/carlton)


I hope you’re doing well.


I wanted to let you know that I have completed all the questions in GA 2. Most of them involve using FastAPI, which I’ve been running locally on `http://127.0.0.1:8000/`. However, I’ve been facing some issues with the platform while submitting the answers.


Specifically, for questions involving Google Authentication and Vercel, the system initially told me the answers were correct, but when I revisited them later, I received errors like “session expired” or similar messages. This happened with Questions 12, 11, 10, and 6. Since these questions often required different local sessions or saving work separately, I ended up losing progress or getting lower marks despite having completed them.


From my side, I’ve solved every question. The issue seems to be related to how the platform handles sessions and saves progress across different parts of the assignment. Could you please advise me on how to proceed or if there’s a way to ensure my work is properly counted?


Thank you for your help!


Best regards,


Kratika Jain

---
**Post ID:** 631281  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/119  

Hi Kratika,


The way to deal with questions that require the server or service to be live while submitting, is to leave those questions till the last and answer all the other questions first. Then turn on those services and submit those remaining questions so that you are able to get the full marks for the GA.


Please remember that your last save will be your official score. So make sure that the last save in the part where you reload is your best score.


God bless,


Carlton D’Silva

---
**Post ID:** 631629  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/120  

Dear [@carlton](/u/carlton) [@HritikRoshan_HRM](/u/hritikroshan_hrm) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)


Yesterday,  solving question no. 11(GA2)  involving Google Authentication  the system initially told me the answer was correct, but when I revisited the assignment today, I received the error  “Google client id  is expired” and when I regenerated the authentication token again and run; it started showing error comparing previous client ID and not taking the new one.


Kindly look into the matter i.e. why server is taking previous google authenticated client id?


Hereby attaching the screnshots


[![The image shows a web page for a Google authentication process.  A long, seemingly encoded token is displayed, along with an error message indicating a mismatch between the audience and client ID.  The page also provides instructions and prompts the user to check their settings.  The bottom shows a "Local LLM Runner: Ollama" section.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28b08c03dcbba98f5bb8def30d064ca5e06b0ba6_2_690x363.png)Screenshot 2025-05-25 2202151915×1008 78 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/8/28b08c03dcbba98f5bb8def30d064ca5e06b0ba6.png)


[![The image shows a web browser displaying a JSON response containing an ID token.  The token is a long, alphanumeric string.  The URL in the browser's address bar indicates that the response is related to an ID token from a localhost server.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/c/bcbd987257943f2199c245ac207d5b30f992e116_2_690x166.png)Screenshot 2025-05-25 2202061919×463 101 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/c/bcbd987257943f2199c245ac207d5b30f992e116.png)

---
**Post ID:** 631681  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/121  

Hi There! Are you able to solve the Q12.

---
**Post ID:** 631957  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/122  

[![This is a screenshot of an online quiz, "TDS 2025 May GA2 - Deployment Tools," showing instructions that encourage exploration and even "hacking" the code to find answers.  The user has already saved their progress multiple times, achieving a score of 9.  A Discourse link is provided for questions.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/e/bef51e1c990be91ea9f067cf3f7af17a341ba81b_2_690x431.png)Screenshot (510)1920×1200 127 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/e/bef51e1c990be91ea9f067cf3f7af17a341ba81b.png)


Please someone help me out I have solved all the problems except 12 (Due: fetch error: enable to fetch link) but my score is being displayed as 0 even though when I saved multiple times whe my score was 9.

---
**Post ID:** 631969  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/123  

Hi, Can someone from the course team confirm if there is any error with the checking script of Question 5? or if I missed something obvious?


Coz this question seems trivial, I fixed the said line of code and got the output as 1304 which isn’t being accepted.



[![The image shows a Jupyter Notebook code cell with Python code that processes an image (lenna.webp).  The code calculates and prints the number of pixels in the image with a lightness value greater than 0.852, using the `colorsys` and `numpy` libraries. The output shows that there are 1384 such pixels.  There's a comment indicating a corrected line of code for image loading.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/d/5d7ba169af0dd165dbaa81607727770239144115_2_345x160.png)image1566×730 99.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/d/5d7ba169af0dd165dbaa81607727770239144115.png)


[![The image shows a Google Colab notebook code snippet designed to calculate the number of pixels in an image with a lightness above 0.852.  The code uses `numpy` and `PIL` libraries and requires the user to upload an image. There's a bug in the code which needs fixing before running it to get the correct answer.  The user has attempted the answer '1304', which is marked incorrect.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/2/72b2035da811ce440d6e806134b7674fcef65d69_2_690x319.png)image2636×1222 262 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/2/72b2035da811ce440d6e806134b7674fcef65d69.png)



Try it out in [Colab Notebook](https://colab.research.google.com/drive/1GIIAaIMjdPxluA6WM5UY46hTNZ-96C2w?usp=sharing) yourself.

---
**Post ID:** 631971  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/124  

Also, since the deadline is now over. This is the command that worked for me to get Ollama working through ngrok finally.


`ngrok http 11434 --host-header=localhost:11434 --response-header-add "X-Email: 23f3003060@ds.study.iitm.ac.in" --response-header-add 'Access-Control-Expose-Headers: *'  --response-header-add 'Access-Control-Allow-Headers:ngrok-skip-browser-warning'`
Sharing it for the sake of others that faced issues ![That's a simple, smiling yellow emoticon or emoji.
](https://emoji.discourse-cdn.com/google/slight_smile.png?v=14)

---
**Post ID:** 632005  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/125  

last saved will taken. so, 9

---
**Post ID:** 632228  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/126  

What will be my final score here? after 12 am I clicked on save button and score went to 9 due to last question server went offline. Please let me know


[![The image shows a computer screen displaying a list of recent game saves.  Three saves are listed, showing the date, time, and score achieved.  The most recent save is indicated as the official score.  A "Logout" button and a "Questions" section are also visible.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/5/652646a3ef1c0006bcc66e14cc024af449ac31de_2_690x388.jpeg)20250526_0035254080×2296 1.63 MB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/5/652646a3ef1c0006bcc66e14cc024af449ac31de.jpeg)

---
**Post ID:** 632021  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/127  

The deadline was 25/5/2025 23:59:59, so whatever was the last score before the deadline will be considered. Since your 9 was after the deadline, any submissions after the deadline is not considered. So in this case it will be 10. We will send out a mail with what we have recorded as your official score, if you find it shows any different then please feel free to get in touch.


Kind regards

---
**Post ID:** 632027  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/128  

Okay thank you so much!

---
**Post ID:** 632231  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/129  

Hi , For GA2 of TDS, I have submitted answers of 10 questions, but I think because i didn’t saved it, My current marks is showing 3.5(As per my last save) on portal([Technical Assessment](https://exam.sanand.workers.dev/tds-2025-05-ga2)), which was 8 when i was clicking on checkall button.


Can I resubmitt it and save it again as the window for submission is passed for GA2 when i am posting this thread?

---
**Post ID:** 632032  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/130  

If you did not save it will not be considered. Its a minimum requirement to be graded. These are the only results we have for you on our server. Since it is best 4/7 assignments you still have 4 more assignments where you can make it up for a better score. I do find it rather interesting that you still submitted a score of 3.75 even after the deadline instead of the score you claimed of 8. Care to explain?


[![The image shows a table with three columns.  The first column contains timestamps from May 24th and 25th, 2025. The second column contains numerical values mostly around 3.75, with one value at 3.5 and one at 2.5. The third column consistently shows the number 10.  It appears to be some kind of log or data record.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/0/0070e90aaf9a90731e29f2dca97af2ef4ecc6e02.png)Screenshot 2025-05-26 at 10.33.41 am842×552 19.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/0/0070e90aaf9a90731e29f2dca97af2ef4ecc6e02.png)


Kind regards

---
**Post ID:** 632237  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/131  

I have submitted both the graded assignments of TDS but for both it shows not submitted…

---
**Post ID:** 632236  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/132  

Just after the instructions in graded assignment portal, there is one thing RECENT SAVE, all your assignment submission’s marks is shown immediately after you submit(SAVE) your assignment.


Your last submission before the deadline will be counted as final score.


Note: Just clicking on check button will not save your result. You will need to click on SAVE button. Then that result will be shown in recent save section at top, just below instructions section.

---
**Post ID:** 632257  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/133  

The marks are not yet updated on the IITM Portal, as mentioned by the TAs they will be pushed after some time (GA1 score mail was sent a few days back and to view the score of that assignment that last save before the deadline is counted).

---
**Post ID:** 632270  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/134  

As I explained , I was just checking the answer, I was not saving, After 12 when i tried to shave questions it was not saving. But when I tried now it has saved and showing score as 8. I am attaching the screenshot for the same. I don’t know if it will be considered or not.


[![This is a screenshot of an online quiz interface.  The quiz has ended, the user achieved a score of 8 out of 10, and the user is allowed to use any resources including hacking the code.  The screenshot also shows recent saved scores and a link to a discussion forum.  The user is logged in with an email address from iitm.ac.in.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8fbc869bf863aa53e2f67179bc55c1474a54b993_2_690x340.png)Final_score_26_05_20251882×930 63.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/f/8fbc869bf863aa53e2f67179bc55c1474a54b993.png)

---
**Post ID:** 635052  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/135  

Thank you the above command worked for me.

