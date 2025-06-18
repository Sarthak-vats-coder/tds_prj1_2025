# Tds-official-Project1-discrepencies
_Slug: _

---
**Post ID:** 612319  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/1  

Please post any discrepancies related to project1.


[@carlton](/u/carlton)


[](#p-612319-who-were-evaluated-how-did-we-decide-what-to-evaluate-1)Who were evaluated? How did we decide what to evaluate?
All the image ids we evaluated were what you submitted to us. This is the list of docker repos that was given to us by [@s.anand](/u/s.anand) as the official list that met all the pre-requisites of Project 1. Therefore we will only evaluate those on this list who are eligible for evaluation with the repos you gave us.


For clarity. Your docker repo gets a unique id every time it is changed. We will ONLY evaluate the image id which was present at the time of the docker repo being pulled. This acts as a time stamped frozen version of your repo. No other image id will be evaluated.


[](#p-612319-how-to-fix-bugs-in-our-scripts-2)How to fix bugs in our scripts
Create Pull requests to [Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1) .


[](#p-612319-docker-image-architecture-issue-report-3)Docker Image Architecture Issue Report
If your Docker image was run on the wrong architecture, please fill out this form:


[Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)


[](#p-612319-bug-fixes-4)Bug fixes
If you find bugs in our evaluation scripts, you might benefit from more marks because of the bug fix. So it is in your interest to look through our scripts and logs and identify bugs or anomalies. You might just go from 0 to heros.


Kind regards,


TDS Team

---
**Post ID:** 612320  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/2  



---
**Post ID:** 612327  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/3  

What is the highest mark anyone has scored? Is it 22/20


[@Carlton](/u/carlton)?

---
**Post ID:** 612331  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/4  

How come me and my group used same code but some got 10 some 11 some 12?

---
**Post ID:** 612332  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/5  

[@carlton](/u/carlton) Please make clear what the average marks are, what highest marks are, and how the project will be evaulated.


We are very close to the end semester exam, and we are still not clear on assignment and project marks. It is a bit frustrating to plan in such circumstances.

---
**Post ID:** 612333  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/6  

You have to see the logs for that. We have shared the logs. Everyone was graded by the exact same code, so there is no partiality. Your code did not produce consistent results.

---
**Post ID:** 612334  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/7  

I have noticed that my image was run on a `x86_64` architecture ( I can see my email in the logs shared ) whereas I built this docker image on my mac which is `ARM`. This is why I can see that my docker image never ran properly and threw the `exec format error`.


This was never mentioned on which architecture machine, our images will be evaluated. I request that my evaluation be done again on the right machine.

---
**Post ID:** 612335  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/8  

My evaluation log file is missing, although I followed all the steps to generate the docker image correctly, it’s showing the server didn’t start for 5 minutes but when I uploaded it, it was working fine. Please help me out sir, I worked hard on the project. I’ll get a zero, but I made the submissions correctly. Some other student also got the “server didn’t start in 5 minutes” but he has an evaluation log file. Please kindly help me out. My roll no. is 22f2001389

---
**Post ID:** 612336  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/9  

We will check and rerun on arm if we ran it on the wrong emulation.

---
**Post ID:** 612338  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/11  

Any suggestions for my case sir ? I’m really tensed.

---
**Post ID:** 612339  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/12  

![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002933/48/118648_2.png) 22f3002933:

I have noticed that my image was run on a `x86_64` architecture ( I can see my email in the logs shared ) whereas I built this docker image on my mac which is `ARM`. This is why I can see that my docker image never ran properly and threw the `exec format error`.


This was never mentioned on which architecture machine, our images will be evaluated. I request that my evaluation be done again on the right machine.




[@carlton](/u/carlton)  same issue, My image was also run on a `x86_64` architecture. I too built on my mac which is `ARM` (M1 Processor). I too can see that my docker image never ran properly and threw the `exec format error`  and  Evaluation log file is MISSING.


Actually my image was run on x86_64 architecture as it was present in that log file and because of the wrong architecture it never started.


I also request that my evaluation be done again on the right machine.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d_2_690x77.png)Screenshot 2025-03-29 at 12.51.59 AM1613×182 19.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d.png)


Even just now I tried running the exact image:


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2_2_690x95.png)Screenshot 2025-03-29 at 12.53.35 AM1220×169 25.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2.png)


It is running fine on my macbook air m1 (ARM)


[@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)

---
**Post ID:** 612341  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/13  

![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f2001389/48/12849_2.png) 22f2001389:

uploaded




Facing the same issue sir, kindly look into it. I had made sure all the files including the docker file were working perfectly fine. Please help me out.


Roll no. 23f1002056

---
**Post ID:** 612342  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/14  

My evaluation log file is missing in report provided. It says tasksA was not found. but I have submitted tasksA in my project file. Also it says server didnt start for 5 mins but for me image was working fine. please kindly help me out. I have made submissions correctly. I request for re evaluation of my project. my roll no is 22f1000703

---
**Post ID:** 612343  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/15  

Respected,


I haven’t received any mail yet regarding the TDS Project 1 marks.


Please look into it.


Regards,


Soham

---
**Post ID:** 612344  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/16  

My evaluation log file is missing.


The 2 other log files i’m given doesnt have my email inside it listed.


the Image id which is given in the MAIL is not present in my docker desktop, my project’s docker image is listed in docker desktop, which doesnot matches the image id given in the MAIL,


What was evaluated? How it was evaluated?


This is the id of the docker image that was evaluated: 0ade87d1bf07


My terminal shows 2 images as last, with respective image ids. I am not sure which one is the real, so please check with both the ids.


tds-project-1              latest    c854274f078d   5 weeks ago    1.38GB


ayush6871/fastapi-agent    latest    27e8375b0ab1   6 weeks ago    1.66GB


I am requesting to look into this case. I think there has been some mistake somewhere.


21f3001194

---
**Post ID:** 612346  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/17  

I have also built the image on Mac and facing the same issue


`exec format error`


It is running fine on my Macbook Pro M1


[@carlton](/u/carlton) [@Saransh_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)

---
**Post ID:** 612347  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/18  

Sir I have noticed a technical glitch for the docker issue, wherein I mistakenly uploaded the wrong docker image link so kindly please kindly re evaluate it.

---
**Post ID:** 612349  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/19  

Sir I haven’t received any mail regarding this Project1 marks. [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---
**Post ID:** 612350  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/20  

[@carlton](/u/carlton) Sir , my Docker image is built on Macbook M1 which as you know uses ARM64 architecture . But evaluated with x86_64 which caused the exec format error due to cross platform compatibility issues . I am kindly requesting you to re-evaluate the project once again .

---
**Post ID:** 612351  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/21  

This is the id of the docker image that was evaluated: d0f14a872042  , but i had never provided this docker image then how it get evaluated, also none of the docker image created by me has this id.


Please, look over it.


Regards,


Harsh Jaiswal


23f1001995

---
**Post ID:** 612352  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/22  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


I wanted to kindly request if you could review the bonus additional tasks, as they were not reflected in the evaluation, despite being mentioned in the instructions. Apart from that I understand and accept my score overall, especially since I had hardcoded the folder paths in my prompt for some questions, which I believe led to those failures.



Bonus: Additional tasks. We may pass additional tasks beyond the list above. If your code handles them correctly, you get 1 bonus mark per task.


Regards,

---
**Post ID:** 612356  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/24  

Would you mind reviewing the evaluation.log screenshot I have attached? I believe I may deserve marks for Task B6. [@carlton](/u/carlton), could you kindly take a look?


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_690x276.png)image1460×585 24.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345.png)

---
**Post ID:** 612357  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/25  

I am also facing the same Please help my roll no is 21f3001750

---
**Post ID:** 612358  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/26  

can you please take a look at this screenshot?


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/b/fb3792e2a76ea8dd4cead0146f0366ceabc3dbb3_2_690x304.png)image1451×640 64.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/b/fb3792e2a76ea8dd4cead0146f0366ceabc3dbb3.png)


The task was done but the LLM made a mistake. I think this type of mistake was outside our control. [@carlton](/u/carlton)

---
**Post ID:** 612359  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/27  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Please correct me if I’m wrong, but I noticed that for tasks B7, B8, and B10, the evaluation log does not include any `POST` or `GET` request traces, unlike the other tasks which have clearly recorded request flows, generated code, and outputs. In these three cases, the log shows only the failure message without any indication that the script was executed or that the output file was read.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_690x256.png)image2003×745 95 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846.png)

---
**Post ID:** 612360  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/28  

Same issue with my. I have built my docker image in mac air m1 but i found that my image was run on a x86_64 architecture (I can see this in the logs shared for x86_server_start.log)

---
**Post ID:** 612362  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/29  

[@carlton](/u/carlton) sir i have same issue.


I have built my docker image in mac air m1 but i found that my image was run on a x86_64 architecture.

---
**Post ID:** 612363  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/30  

Sir even my evaluation log file is missing and I really don’t know what to do because during submission 8/10 of my A tasks were working. Please look into it sir. This is really going to affect my grade and I remember how hard I tried just to get my A tasks running. Please sir


Role nom 23f2000599


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/c/bc7199b82a901c91f7d040bb2328b9b116b55eac_2_225x500.jpeg)10004720831080×2400 255 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/c/bc7199b82a901c91f7d040bb2328b9b116b55eac.jpeg)

---
**Post ID:** 612365  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/31  

Hi [@jivraj](/u/jivraj),


The contents of Expected and Result matches, but still test case’s failed.


Is there formatting check for answer , Isn’t prettier to be done ?


I see that your expected answer isn’t formatted using prettier , am i wrong ?


eg:


![That's a yellow triangle with a black exclamation mark inside.  It's a common warning or alert symbol.
](https://emoji.discourse-cdn.com/google/warning.png?v=14) EXPECTED:


[{‘first_name’: ‘Kevin’, ‘last_name’: ‘Allen’, ‘email’: ‘tonya41@example.com’}, {‘first_name’: ‘Kimberly’, ‘last_name’: ‘Allison’, ‘email’: ‘vmendoza@example.com’}, {‘first_name’: ‘Kathleen’, ‘last_name’: ‘Baldwin’, ‘email’: ‘amclean@example.com’}, {‘first_name’: ‘Jason’, ‘last_name’: ‘Banks’, ‘email’: ‘sharptara@example.org’}, {‘first_name’: ‘Tami’, ‘last_name’: ‘Bass’, ‘email’: ‘kristy61@example.com’}, {‘first_name’: ‘Brenda’, …


![That's a yellow triangle with a black exclamation mark inside.  It's a common warning or alert symbol.
](https://emoji.discourse-cdn.com/google/warning.png?v=14) RESULT:


[


{


“first_name”: “Kevin”,


“last_name”: “Allen”,


“email”: “[tonya41@example.com](mailto:tonya41@example.com)”


},


{


“first_name”: “Kimberly”,


“last_name”: “Allison”,


“email”: “[vmendoza@example.com](mailto:vmendoza@example.com)”


},


{


“first_name”: “Kathleen”,


“last_name”: “Baldwin”,


“email”: “[amclean@example.com](mailto:amclean@example.com)”


},


{


“first_name”: “Jason”,


“last_name”: “Banks”,


“email”: “[sharptara@example.org](mailto:sharptara@example.org)”


},


{


“first_name”: “Tami”,


“last_name”: “Bass”,


“email”: “[kristy61@example.com](mailto:kristy61@example.com)”


},


{


“first_name”: “Brenda”,


“last_name”: “Bradford”,


“email”: “[amandakeith@example.com](mailto:amandakeith@example.com)”


},…

---
**Post ID:** 612371  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/32  



---
**Post ID:** 612372  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/33  

Hi @all


We will identify why arm images created a problem and were run using x86 platform.


We will also rerun evaluations for all the x86 and arm images one more time, before pushing to the dashboard.





![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f3003302/48/67422_2.png) 23f3003302:

Hi [@jivraj](/u/jivraj),




[@23f3003302](/u/23f3003302) output from your server’s response is correct, we will update our evaluation script.





![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2004912/48/108710_2.png) 23f2004912:

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_690x276.png)image1460×585 24.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345.png)




[@23f2004912](/u/23f2004912) We will discuss internally if we can do something about it, but I can’t assure if you will get marks for it, since output from your server is a bit different.





![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001611/48/67277_2.png) 23f1001611:

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_690x256.png)image2003×745 95 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846.png)


image2003×745 95 KB




[@23f1001611](/u/23f1001611) we will look into it





![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/harshjaiswal/48/69560_2.png) HarshJaiswal:

This is the id of the docker image that was evaluated: d0f14a872042 , but i had never provided this docker image then how it get evaluated, also none of the docker image created by me has this id.




[@HarshJaiswal](/u/harshjaiswal) I looked for your response for project1 docker image, and found out that we used correct image id. Here is repo information  `harshjaiswal1/tds_project_final      latest    d0f14a872042   5 weeks ago    214MB`


[@AYUSH_SINGH](/u/ayush_singh)





![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/ayush_singh/48/14039_2.png) AYUSH_SINGH:

ayush6871/fastapi-agent latest 27e8375b0ab1 6 weeks ago 1.66GB




This was submitted to us through google form, for project1.





![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/ayush_singh/48/14039_2.png) AYUSH_SINGH:

The 2 other log files i’m given doesnt have my email inside it listed.




We are aware about it results for 12 students are not generated, we will look into it, and see what caused those 12 images not to run.


[@22f1000703](/u/22f1000703)





![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f1000703/48/125463_2.png) 22f1000703:

My evaluation log file is missing in report provided. It says tasksA was not found. but I have submitted tasksA in my project file. Also it says server didnt start for 5 mins but for me image was working fine. please kindly help me out. I have made submissions correctly.




It would have run at your end but it was supposed to run at anywhere, after dockerising it didn’t run, reason is taskA module was not found.

---
**Post ID:** 612379  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/34  

Same issue for me sir. When I evaluated my file using evaluate.py my 9 cases out of the 10 in Task A was passed but the email I received shows that my evaluation log file is missing. I don’t understand why does it show like that. Please do check and help me out sir.


Reg no. 24f1002633

---
**Post ID:** 612382  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/35  

I suspect there is something wrong with how the evaluation has been done. Although A1 task succeeded, all of my A tasks failed.

---
**Post ID:** 612387  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/36  

I have checked my log file in all of the cases where a file is required it says file not found or directory not found error in the code, how can I check /data folder was provided to the program?


[@carlton](/u/carlton)

---
**Post ID:** 612391  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/37  

[@Jivraj](/u/jivraj) , [@carlton](/u/carlton)


It was a good project, and I have obtained the log files. Upon reviewing the log files, I realized that they are unable to read the files. I checked my project on GitHub and discovered that I forgot to uncomment the line that defines the path using the `os` library. As a result, all file evaluations returned errors such as “can’t read the file.”


I understand that this oversight was my mistake. However, is there any way to reevaluate the code by simply uncommenting that line? I believe the rest of the code is properly written, but due to this single comment, all the files remained unchecked or resulted in errors.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad651e6c7b4c4df44a6b4c7ed935673b7576a076_2_690x388.png)Screenshot (177)1920×1080 206 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/d/ad651e6c7b4c4df44a6b4c7ed935673b7576a076.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/7/078748473287587894e2c880e392cb511618d1f2_2_690x388.png)Screenshot (179)1920×1080 199 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/7/078748473287587894e2c880e392cb511618d1f2.png)

---
**Post ID:** 612392  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/38  

Same here. I also dis not recieve any mail sir.

---
**Post ID:** 612407  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/40  

I noticed that my Docker image was run on an x86_64 architecture (as indicated by my email in the shared logs), whereas I originally built it on my Mac (ARM architecture). Due to this mismatch, the image failed to run properly and resulted in an exec format error.


Since there was no prior mention of the architecture on which our images would be evaluated, I request that my evaluation be conducted again on the appropriate machine. Please help as after doing it correctly getting 0 marks because of such an error feels wrong

---
**Post ID:** 612408  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/41  

[@23f2001975](/u/23f2001975) we had to rely on docker telling us whether an image was arm or x86. So thats why we just did what docker software told us. If it classified an image as arm then we ran it on arm. If it did not then we ran it on x86. Thats why we need students to look through the logs and identify issues so that we can make sure you get the correct evaluation.


If students notify us their image is actually arm based, then we will run it on arm. So dont worry, just inform us of any discrepancy as well as bugs. Our evaluation might not be perfect, there may be bugs. If students can precisely create bug reports then we can take that into consideration when evaluating students as well. The benefit being you might get extra marks because of the bug fix.


We have a script that looks at this discourse post each day and tells us who requires a fresh evaluation. So we will check your image on arm.


Kind regards

---
**Post ID:** 612410  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/42  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/ea516be0e1c56eed1350af31ea0a2546b58528a6.png)image633×197 4.25 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/ea516be0e1c56eed1350af31ea0a2546b58528a6.png)


This is a screenshot of my docker log file. This works if you pass the actual value of the airproxy token at the command line while pulling the docker image. Please do look into this as I’ve put a lot of effort into this.


Thank you


Regards,


23f3002677

---
**Post ID:** 612411  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/43  

@cartlon Same issue.


My image was also run on a `x86_64` architecture. I too built on my mac which is `ARM` (M1 Processor). I too can see that my docker image never ran properly and threw the `exec format error` and Evaluation log file is MISSING.


Can you please rerun the image on ARM based

---
**Post ID:** 612412  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/44  

You have a misspelling in your environment variable, thats why it failed. We do pass the token to your docker exactly as specified in Project 1 page.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/9/59feb291f76643832a4b1b0f68037c2dee61deb1.png)image633×197 5.21 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/9/59feb291f76643832a4b1b0f68037c2dee61deb1.png)


Kind regards

---
**Post ID:** 612413  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/45  

You have to identify the exact bug for your claim to be considered. Thats why we have provided you with the scripts and the logs. You might get lots of marks. Its in your interest to identify the bug.


Kind regards

---
**Post ID:** 612416  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/46  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) what do I do sir am seriously clueless and heartbroken rn pls help atleast for A tasks we should get it

---
**Post ID:** 612417  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/47  

We demoed in the live session the complete process of how to dockerise your project so that it can be run anywhere. Running on your local machine is not a sufficient criteria for passing the evaluation. It is absolutely vital for students to understand deployment. This is a critical skill for anyone who is serious about working in this field.


Also just check if yours is an arm based image or x86. Sometimes that makes a difference. For us there is no way to know other than docker software telling us. As it turns out several students had an arm based image but docker did not tell us that. So we will re run those.


If yours has been run on the wrong emulation then we will re run.


Kind regards

---
**Post ID:** 612418  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/48  

[@carlton](/u/carlton)


I encountered an HTTP 500 error with the following detail:


`{
"detail": "'choices'"
}`
This issue appears across all tasks, even though they were running fine before submission. I suspect there might be a problem with APIPROXY_TOKEN. Could you please look into this?


Additionally, my solution is very similar to the one shared by the System Commands team in their email.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/6/168fb0afeb8b965e92d70295ca00374c5179d6d9.png)Screenshot 2025-03-29 1033271511×749 29 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/6/168fb0afeb8b965e92d70295ca00374c5179d6d9.png)

---
**Post ID:** 612419  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/49  

We have given you the evaluation scripts. Identify where exactly you believe the bug is.


Just guesses is not going to get you extra marks. You have to give us something specific.


Kind regards

---
**Post ID:** 612424  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/50  

[@Jivraj](/u/jivraj) sir please kindly look into it. Please re-evaluate my image, everything was working fine it is an issue with the docker image. Please re-evaluate it sir and please guide me as what to do

---
**Post ID:** 612427  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/51  

I encountered the same issue with `evaluate.py`. However, since you previously advised against coding strictly with `evaluate.py`, I didn’t pursue it further. Now, I’m concerned—how is this a mistake?


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/448bed1174becff2ecb28c56f9d75eb37e2d3689.png)Screenshot (56)1492×362 22.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/448bed1174becff2ecb28c56f9d75eb37e2d3689.png)

---
**Post ID:** 612434  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/52  

Please provide more time for this. Right now, we are also busy with the second project. There are other courses as well.

---
**Post ID:** 612440  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/53  

yaa same issue i am also facing ,


and this LLM thing is very new for us , and we tried our best to complete. , but because of local machine issue , or anything , people end up getting 0 marks , or 4-5 marks , ..


As a lot of students are getting 0 , so please give some bonus , or some marking for there efforts ,


TDS dont have quiz , ,and getting 0 in project will decrease our CGPA too .


please think for it sir [@carlton](/u/carlton)

---
**Post ID:** 612441  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/54  

This is the id of the docker image that was evaluated: 468630ef32b8


I believe this is not my docker ID that was submitted, my docker ID is “bd2d0e570ec6”:


proof:


REPOSITORY                           TAG          DIGEST                                                                    IMAGE ID       CREATED        SIZE


rohit23f1001156/project1_tds         v3           sha256:bd2d0e570ec6b9a4a2b1565602a7c6abd118c4df06ca39e9dd78b0c06cab7542   bd2d0e570ec6   5 weeks ago    816MB


Please, look over it.


Also, in my docker log file, it is showing the error as:


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94b76c5b49a749a2750e840d06fef2715c0b0b69_2_690x462.png)Screenshot 2025-03-29 at 11.10.03 AM2360×1582 503 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/94b76c5b49a749a2750e840d06fef2715c0b0b69.png)


what is the reason for this?


It was running properly before, please help.


Regards,


Rohit


23f1001156


[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---
**Post ID:** 612444  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/55  

[@ROHIT_B_LAKSHMANAN](/u/rohit_b_lakshmanan)


This is exactly what you submitted. We will ONLY consider this as valid.


2/16/2025 9:30:05	23f1001156@ds.study.iitm.ac.in	[GitHub - Rohit23f1001156/project1_tds](https://github.com/Rohit23f1001156/project1_tds)	rohit23f1001156/project1_tds

---
**Post ID:** 612454  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/56  

Yes, I agree.


So, did my docker ID change when I submitted?


I am sorry sir, but I did not make any changes after submitting the project, so I guess my Docker ID should remain the same as before, if I am not mistaken. I kindly request you to check just once more please, as I really don’t know where I have went wrong.


Jivraj Sir had checked liked this for another student, so I just wanted to confirm the same for me.


" I looked for your response for project1 docker image, and found out that we used correct image id. Here is repo information `harshjaiswal1/tds_project_final      latest    d0f14a872042   5 weeks ago    214MB`"


Also sir, could you please tell me why the error as shown in my previous message is being shown? and if there is no chance of it getting correct.


thanks

---
**Post ID:** 612462  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/57  

Hi [@carlton](/u/carlton) !


I am reaching out with deep frustration and concern regarding the evaluation of my project. I have worked tirelessly on this for almost two weeks, dedicating day and night to ensure that the tasks were executed correctly. During my own testing, I was able to get at least 7 out of 10 A tasks working as expected. However, after the evaluation, I was informed that none of the tasks were executed properly, which was quite shocking!


Given the effort and time I have put in, I kindly request you to review my project once more. I am more than willing to demonstrate the functionality in real time to clarify any issues or misunderstandings. Please let me know if there is a possibility to discuss this further, as I genuinely believe my work deserves another review.

---
**Post ID:** 612463  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/58  

[@carlton](/u/carlton),


Jivraj said, “We will discuss internally if we can do something about it.” I understand this well. The output from my server is slightly different, but it still achieves over 95% accuracy. Please do consider it.

---
**Post ID:** 612464  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/59  

Hi [@Pritul_raut](/u/pritul_raut)


No, we won’t reevaluating it.

---
**Post ID:** 612479  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/60  

Hi [@22f2001389](/u/22f2001389)


`File "/app/app.py", line 4, in <module>
    from tasksA import *
ModuleNotFoundError: No module named 'tasksA'`
The error occurs because Python cannot find the `tasksA` module. This is due to the file not existing, not being in the correct directory.


Kind regards

---
**Post ID:** 612484  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/61  

![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/rohit_b_lakshmanan/48/67205_2.png) ROHIT_B_LAKSHMANAN:

This is the id of the docker image that was evaluated: 468630ef32b8




We evaluated you on correct file


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/7/d73b7915b1fb24bc215068e0695616f82f122f96.png)image1757×250 24.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/7/d73b7915b1fb24bc215068e0695616f82f122f96.png)





![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/rohit_b_lakshmanan/48/67205_2.png) ROHIT_B_LAKSHMANAN:

what is the reason for this?


It was running properly before, please help.




Try running docker container after pulling, check if evaluate.py is able to do it’s job.


If you feel there is some issues from our side, we have provided with scirpts we used. You can create a pull request to [Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1)

---
**Post ID:** 612488  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/62  

I’m facing “exec /usr/local/bin/uvicorn: exec format error” ,  My roll number is 21f3003062@ds.study.iitm.ac.in , My roll is in x86 list/log , not in ARM list/log. I have written and tested my code on ARM computer. I request to please check my code manually. [@Jivraj](/u/jivraj) [@carlton](/u/carlton) .

---
**Post ID:** 612493  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/63  

I cannot understand why the project marks are marked zero for me ? i have used the same code as usual but the results are not same ?

---
**Post ID:** 612494  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/64  

No no sir, I can send you an SS of my code, it’s very much there sir, the tasksA file, i really don’t know why this happened.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/2/227c1d29047c3e45a7c98d98421e983e014f666f_2_281x500.jpeg)image2160×3840 1.92 MB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/2/227c1d29047c3e45a7c98d98421e983e014f666f.jpeg)

---
**Post ID:** 612499  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/65  

Same issue with me also

---
**Post ID:** 612500  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/66  

Yeah, it’s there on your local machine, but you didn’t copy it to docker container.


Below is content of your docker file which doesn’t copy tasksA.py file it only copies app.py. You could have figured this out by just running docker container on your local machine earlier, it would have shown you that error.


`FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app

# Copy application files
COPY app.py /app

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]`

---
**Post ID:** 612503  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/67  

[@carlton](/u/carlton) good afternoon sir,


I completed my project 1 and submitted it as instructed. But the result show that evaluate file missing. I did everything right but don’t know how this as the result come. I also had evaluation file in my project too. Please go through things again as this is very unfair for those who took 2 weeks to do this project. My roll no. is 22f3001664. I hope I will get marks, of not full then should be 10/20.


Thank you sir

---
**Post ID:** 612506  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/68  

What to do now sir ? Is there no way to fix this now ? I can change the docker file and overwrite the docker image if you allow me to do so.

---
**Post ID:** 612512  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/69  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/0/10a8acf6ce192b7da1304573e931a156dd91e89f.jpeg)image474×474 41.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/0/10a8acf6ce192b7da1304573e931a156dd91e89f.jpeg)

---
**Post ID:** 612517  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/70  

Figure out the problem in our script and do a pull request to it, we will fix it if it’s a valid bug.





![Image could not be processed](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png) Jivraj:

Create Pull requests to [Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1) .

---
**Post ID:** 612520  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/71  

We looked at your script and there are errors in it. It doesn’t follow what we mentioned in live sessions.


Line number 81 of your app.py


`subprocess.run(["uv", "run", script_name, "--root", "./data"] + args, check=True)`


which creates a data directory inside app directory but evaluate.py expects data directory to be in root directory.

---
**Post ID:** 612522  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/72  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)


I’m writing here to express my concerns regarding the evaluation of my TDS Project-1. Also, kindly pardon me for the long message.


I have received a MISSING statement in my evaluation log file in the project 1 score mail that was released yesterday.


These are the detailed point wise concerns :




I at the earlier stages, found the Tools in Data Science course relatively challenging as it’s just my second term in Diploma and I have only completed BDM and MLF Course till now. Hence, I decided to drop the course in February, however when I could still view the course on the portal, and raised concerns, the assistance provided to me was very grim and low, and after numerous follow-ups, I was finally informed 2½ weeks after dropping my course, that my drop application was received in draft and they would not proceed with it, and I had to continue my course.




By this time, I had already missed 2 graded assignment deadlines and the project 1 submission was due in the coming 2 days. Not losing my spirit and with whatever I could learn and implement I completed the TDS project 1. However, I accidentally attached the wrong docker image link, and I also raised the issue, but didn’t receive a reply.




I understand that it was a fault on my part, but evaluating a student as 0, even though all their functions are right, and they give the required answers, is also wrong since we are expected to provide correct answers, and learn to build the docker image, however, there can be occurrences where a student might make a small mistake like uploading the wrong link, and they must be given a small chance to reprimand them.




I also didn’t receive the mail from the TDS Team which they issued for students whose docker image or GitHub link was erroneous, and hence I realised after the deadline that I had uploaded the wrong docker image link.




I have rechecked all my function, and they are all correct, giving a 0 to a student, who worked hard within the limited available time(given the student had dropped the course but the course team didn’t process it) is very unfair.


Kindly provide me a way to either re-upload my project-1 Docker image link, or ask them to provide me marks on the basis of the functions and codes written, whichever is feasible, atleast to encourage the efforts and time put into the project with little knowledge.


I hope you would look into my plight, and take necessary measures.


Thanks and Regards

---
**Post ID:** 612523  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/73  

I haven’t received any mails regarding the tds project 1 please look into my concern


[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---
**Post ID:** 612538  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/74  

Sir please consider a re-evaluation for me, please :’)

---
**Post ID:** 612543  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/75  

Please consider my situation a peer whos results were exactly same as mine has received 9, then how could I get 1 . 23f1002630 this is my role number please reconsider


[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 612544  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/76  

Few Students including me have not received any mails regarding TDS Project 1. We don’t even know what went wrong or why we didn’t received. Initially I thought that it can be due to some sending error and i will receive little late but even after 14hrs we have not received anything from the team. How are we supposed to check log and see our mistakes when we didn’t even received marks and logs. I request to check into it and provide us our marks and logs.


Thank You.


[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---
**Post ID:** 612573  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/77  

I had built the project well on my Mac OS machine. I am very disappointed with the scores. How do i make amends for revaluation as I feel the code ran well for all tasks on my machine. Please give written steps for revaluation.

---
**Post ID:** 612574  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/78  

Its saying that my evaluation log file is missing, i submitted everything properly. It also says no module named TasksA is found while i got 9/10 marks in the tasksA evaluation script. Kindly look into this, i worked really harrd for this project, [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 612576  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/79  

[@22f3000935](/u/22f3000935) [Page Not Found | Docker Hub](https://hub.docker.com/r/pscoeds24/dataworks-agent)


you submitted this docker url through form response for project1, this repo doesn’t exists on docker.

---
**Post ID:** 612577  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/80  

[@Jivraj](/u/jivraj) sir please tell me whats the issue am very confused and worried

---
**Post ID:** 612578  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/81  

We are aware about such mistakes and we are looking into it. We will reevaluate those images.

---
**Post ID:** 612579  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/82  

If evaluation file is missing for anyone, we will reevaluate it once more and send same through email.


Can you fill form for architecture detection.

---
**Post ID:** 612581  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/84  

Also please , kindly share evaluation log file after execution

---
**Post ID:** 612582  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/85  

I did upload all the necessary files but it stil says tasksA is missing, and i am getting zero marks. Kindly help out [@carlton](/u/carlton) [@Jivraj](/u/jivraj)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/eff7ce6ffba0a1ad0a375cd1f2ea39eb613d333d_2_690x335.png)Screenshot 2025-03-29 1414481387×674 42.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/f/eff7ce6ffba0a1ad0a375cd1f2ea39eb613d333d.png)

---
**Post ID:** 612583  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/86  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/9/294b6ca3b2e386ec06fa6a9e356f2e2004eba2fc.png)image469×233 8.48 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/9/294b6ca3b2e386ec06fa6a9e356f2e2004eba2fc.png)


linux/amd64


which form should i fill sir?

---
**Post ID:** 612586  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/87  

![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/aditya_naidu/48/12438_2.png) Aditya_Naidu:

21f3003062@ds.study.iitm.ac.in , My roll is in x86 list/log , not in ARM list/log. I have written and tested my code on ARM computer. I request to please check my code manually. [@Jivraj](/u/jivraj) [@carlton](/u/carlton) .




please fill the form for collecting architecture, so that we can rerun evals earlier we relied on docker api to tell us which architecture is being used, but it didn’t classify them correctly.

---
**Post ID:** 612588  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/88  

Hi [@23f2000599](/u/23f2000599) check this out





![Image could not be processed](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png) Jivraj:

Docker Image Architecture Issue Report
If your Docker image was run on the wrong architecture, please fill out this form:


[Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)

---
**Post ID:** 612590  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/89  

mine is linux/amd64 sir it doesnt come under arm or x86 i think

---
**Post ID:** 612591  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/90  

Hi [@23f2002400](/u/23f2002400)


Check your Dockerfile if it copies tasksA.py file to docker container.


If it does where does it copy, these are possible mistakes. You were expected to test docker images.

---
**Post ID:** 612592  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/91  

Hi [@23f2000599](/u/23f2000599)


amd64 is x86

---
**Post ID:** 612594  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/92  

Ok sir, will fill the form, thank you

---
**Post ID:** 612596  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/93  

One issue file is my app is listening on port 8000. But evaluations being done on 8219 port. so how it will succeed. Please guide what to do.

---
**Post ID:** 612599  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/94  

That’s external port mapping, we mapped your docker’s port 8000 to external 8219 port, so it won’t create issues.


Just look at docker_orchestration.py file for logic behind it, basically it was for evaluating multiple images parallely.

---
**Post ID:** 612612  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/96  

There is a mistake in the url I guess check this out I have a fully functional image which was pushed 1 month ago


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/256b97d98b6ef5ae6fab6edb3882f92c73f210da_2_690x382.png)image1103×611 55.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/5/256b97d98b6ef5ae6fab6edb3882f92c73f210da.png)


Please check this out


url::[https://hub.docker.com/repository/docker/pscodes24/dataworks-agent/general](https://hub.docker.com/repository/docker/pscodes24/dataworks-agent/general)

---
**Post ID:** 612621  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/97  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/0/7070e3c250af7985b5ca777719e26fb065ee2bb9.png)image1340×431 9.45 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/0/7070e3c250af7985b5ca777719e26fb065ee2bb9.png)


This is the correct answer, eval script is not considering newlines properly. [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---
**Post ID:** 612641  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/98  

same with me ![That's a yellow emoticon/emoji with a small smile and a single blue tear rolling down its cheek.  It depicts a bittersweet or slightly sad feeling.
](https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=14) i dont understand how i got 0.

---
**Post ID:** 612646  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/100  

This is the id of the docker image that was evaluated: 2a8ffa96b140 , but i had never provided this docker image instead my image id is 735a5a477fb2 then how it get evaluated, also none of the docker image created by me has this id. My docker image was created on linux/amd64.


Please, look over it [@carlton](/u/carlton) , [@Jivraj](/u/jivraj) .


Regards,


Atharva Antapurkar


23f1002558

---
**Post ID:** 612648  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/101  

Sir, my evaluation log file is missing, even though I followed all the steps to generate the Docker image correctly. The system indicates that the server didn’t start within 5 minutes, but when I uploaded it, everything was working fine. I put in a lot of effort into this project, and I’m worried I might receive a zero despite making the submission correctly. Kindly help me resolve this issue. My roll number is 22F3004068.


Additionally, my Docker image ID was d2f27c03b878, but the ID mentioned in the email was dfac8596cd4c. Please provide clarity on this discrepancy.


I have also attached my Docker [log file](https://drive.google.com/file/d/1exrdQOCjbrCFux2hC4OQH_BfgiijCzD1/view?usp=drivesdk) for reference


Docker [image](https://hub.docker.com/repository/docker/docaravind21/tds-project-1/tags)

---
**Post ID:** 612655  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/102  

I realized that I made a mistake in my project by forgetting to uncomment a single line of code: os.path.join(os.getcwd(), “path_given”). I feel really bad about this oversight, especially after working so hard on the project and formatting everything carefully. It was an honest mistake, and I take full responsibility for it.


I sincerely request you to consider re-evaluating my work, as I believe it reflects the effort and dedication I put into it. I truly regret this error and will be more careful in the Project 2


[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 612663  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/103  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/b/8b35872a380e8ff279af497184852fd80401b602.png)Screenshot (423)1486×895 43.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/b/8b35872a380e8ff279af497184852fd80401b602.png)


Sir so the  user_email isn’t passed while pulling the docker image?


Thank you.

---
**Post ID:** 612664  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/104  

Hi Team,


I have resolved the issues and pushed a new Docker image.


New Docker Image ID: `913320f92eb3`


Tag: `latest`


OS/ARCH: `linux/amd64`


Please evaluate my updated submission.


Thanks!

---
**Post ID:** 612666  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/105  

Hello,


My log file shows a “file not found” or “directory not found” error. Could you confirm whether `datagen.py` was executed inside the Docker container or on the host OS? If it ran on the host, I don’t see any mounting process for the `/data` folder into the container. Could you please clarify this?


[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 612674  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/106  

is it like this: FileNotFoundError: [Errno 2] No such file or directory: ‘system_input.txt’ ?


I am getting this error.

---
**Post ID:** 612680  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/107  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir, I have fixed my docker image issue that was causing the error. Please re-pull my docker image so that I can get score. Please consider me for re-evaluation. All the codes were correct, only issue was a glitch in the docker image.

---
**Post ID:** 612700  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/108  

Hello Sir, I am facing the same issue. Please look into it. Before submission, I ran my Docker file with the evaluation script to ensure it was working, and it worked fine. Kindly help me out. My roll number is 23F3004321.

---
**Post ID:** 612702  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/109  

Yes, something like that, My log file shows when script tries to access file it says file not found or directory not found.

---
**Post ID:** 612735  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/110  

Sir, I checked my evaluation log, and the error occurred because the AI proxy token limit was exceeded. I ran the evaluation script to verify, and I scored 12/20.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/3/73d3123eb9274a1374ee2ee10f20e9a269c283f8.png)image1456×765 41.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/3/73d3123eb9274a1374ee2ee10f20e9a269c283f8.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/941a71108a292d453f81c1bd42681cdc91acb222.png)image1094×256 9.59 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/941a71108a292d453f81c1bd42681cdc91acb222.png)

---
**Post ID:** 612756  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/111  

Sir, my project scored 1/20, with only B1 passed. However, when I ran the evaluation script, I got 6/10 in A tasks. Is there any way this can be checked, as the project works on deployed.


Kind Regards and thanks

---
**Post ID:** 612760  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/112  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Sir,


This is the id of the docker image that was evaluated: 82aeb74ca739  ,


but i had never provided this docker image instead my image id is de8235663462


then how it get evaluated, also none of the docker image created by me has this id. My docker image was created on linux/amd64.


Please, look over it [@carlton](/u/carlton) , [@Jivraj](/u/jivraj) .


Regards,


S Sharmile


23f3001688

---
**Post ID:** 612772  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/113  

Sir the evaluated docker file ID was mentioned as  5b28fd5b25a7 in the mail sent by you but my docker file ID is 4d8c0cc34e35. I think my docker file is not evaluated properly. Kindly do check this and help me out. My reg no 24f1002633.

---
**Post ID:** 612775  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/114  

[@carlton](/u/carlton)


My docker logs shows that `OSError: Cannot find resource` error occurred when the data generation script tried to access font files in generation for a8.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/f/dfc4c289dcc2ddda315bd9f97a9ff21c166792af.png)image1485×807 37.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/f/dfc4c289dcc2ddda315bd9f97a9ff21c166792af.png)


The datagen.py script looked for Arial font in the try block and when it encountered error it went to the except block to use DejaVuSans, the Pillow default, except it encountered the same error there, which was not handled. Thus, datagen.py stopped abruptly without creating files for A9 and A10 as well. So effectively, my A9 and A10 did not get evaluated properly as it did not have the required files due to error during data generation for A8. Can you please re-evaluate by enclosing each of the data generation function calls in their own try-except blocks?


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/681a3a02c951eaf7014d116d45b9ac35b8fdd2de.png)image302×252 3.45 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/681a3a02c951eaf7014d116d45b9ac35b8fdd2de.png)


I think it would be better to enclose each of these function calls in their own try-except blocks. This screenshot is taken from the datagen.py file sent in yesterday’s results mail.


So, will it be possible to re-evaluate my task A1, A8, A9 and A10? At least A9 and A10 did not even get the files to work on as they weren’t even created due to insufficient error handling in datagen.py .


Also, can you help me to identify the cause of even the Pillow default font not being available? I don’t understand how a font not being available could be caused by my code.


Thank you

---
**Post ID:** 612784  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/115  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03b1e9282075d90736c4e6d9c652495660500acd.png)image1505×276 16.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03b1e9282075d90736c4e6d9c652495660500acd.png)


this is a 429 from sanand which is an error from your side. The evaluation already so delayed now has such issues because of which I am getting 1/20. [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 612818  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/116  

does that mean our script is not evaluated?

---
**Post ID:** 612840  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/117  

Hi [@Vihaanv07](/u/vihaanv07)


This was a good spot, we will rerun all the images where string `Agent Errro: 429 Client Error....` is present.


Thanks and kind regards

---
**Post ID:** 612842  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/118  

Hi [@Jayeshbansal](/u/jayeshbansal)


There were 12 emails for which we didn’t rerun, we will be fair with grading you and will take care of it.

---
**Post ID:** 612854  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/119  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/99027ea63de1e32da4a8e843b59386029099553d.png)Screenshot 2025-03-29 at 7.53.20 PM1440×900 13.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/99027ea63de1e32da4a8e843b59386029099553d.png)


My docker image id is different than the one I submitted


“This is the id of the docker image that was evaluated: 10f11a0e0cd6”


[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) plz check this

---
**Post ID:** 612875  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/120  

Hi [@23F300327](/u/23f300327)


This is what you submitted to us in the gform.


23f3003027@ds.study.iitm.ac.in	mishkat02/automation-agent:latest


We will only evaluate this image.


Kind regards

---
**Post ID:** 612877  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/121  

[@carlton](/u/carlton) then why is the image id different?


in the docker hub as well as my local terminal the image id is 07b16dc68225

---
**Post ID:** 612890  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/122  

When we build it after pulling it, it will get a unique identifier that makes sure we will only ever evaluate exactly that version. We pull it from your submission in the form.


In other words, if any changes occur to the docker repo, our id will no longer match a newer version of the file. This way we can make sure we are evaluating the right version every time. Your id does not have to match ours.


But we can detect changes made to the docker repo through our image id. I hope that is clear.


We will do some extra sanity checks before the 1/4/2025 just incase there are any issues. But thanks for asking the question.


Kind regards

---
**Post ID:** 612935  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/123  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


My logs show,  ‘exec format error’ and it is due to architecture issue,  image was built on mac.


I have updated the google form regarding the architecture. Please rerun my image. Thanks

---
**Post ID:** 612956  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/125  

![Image could not be processed](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png) Jivraj:

Docker Image Architecture Issue Report
If your Docker image was run on the wrong architecture, please fill out this form:


[Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)




Just fill the google form, we are rerunning such images.

---
**Post ID:** 613139  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/126  

Greetings, Sir,


I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between `pandas` and `numpy` caused the container to fail. To my surprise, the same versions (`pandas==2.0.3` and `numpy==1.24.3`) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.


To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.


I’ve pushed the updated image to Docker Hub (`santoshsharma003/tds-project-one-1:latest`). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.


Thank you for your assistance!

---
**Post ID:** 613141  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/127  

Hi [@carlton](/u/carlton), I checked my Docker log file now and realised I missed to push a couple of files to the image. Is there anything I could do now? I have all the required files in my Git repo though. Please help.

---
**Post ID:** 613213  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/128  

Sir in my logs it is showing that there’s cv2 module missing i mightve missed adding that in the requirements. Is there anything you could do to help me please?

---
**Post ID:** 613359  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/129  

I am also facing the same issue. I tried evaluating the scripts with the evaluation file also. Please rerun and let me know. My Roll No is 21F1002866.

---
**Post ID:** 613369  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/130  

Hi,


For Tasks A8, A9 & A10, I am not seeing any errors in my Docker execution logs. I am assuming the evaluation script failed to fetch the output file to verify the output for some reason. Can you please try rerunning these three tasks again? These tasks are working fine for me.


For Task B1. “Data outside /data is never accessed or exfiltrated, even if the task description asks for it.” - So when the evaluation asked to write something to /tmp/hello.txt it has correctly thrown an error saying access denied. I think this should be marked as correct. As the task description itself says so, the return is passed as 200 OK


`ERROR:main:Error executing write_file: Access denied: /tmp/hello.txt
INFO:     172.17.0.1:60918 - "POST /run?task=Write+%27Hello+World%27+to+%60%2Ftmp%2Fhello.txt%60 HTTP/1.1" 200 OK`
Similarly for task B2.


`INFO:main:Checking file path: /data/format.md
ERROR:main:Error executing file_folder_deletion: Deletion not allowed: /data/format.md
INFO:     172.17.0.1:59446 - "POST /run?task=Delete+%2Fdata%2Fformat.md HTTP/1.1" 200 OK`
For Task B4, if branch is not given we are assuming it as ‘main’ branch. Is it not correct? We would have at least expected the branch passed in the request.


For Task B8, I could not see the task description sent in the request in evaluation log file. Can you please check if the task request was passed properly?


Because I see only “=4 B8 failed: not all arguments converted during string formatting” for Task B8

---
**Post ID:** 613592  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/131  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)


Thanks for your encouragement.. tried debugging the issue of image not starting up in the orchestrator script.. I found that the issue was happening because of the http and https proxies being set in docker build


`ARG http_proxy=http://www-proxy-adcq7.us.<xxx>.com:80
 ARG https_proxy=http://www-proxy-adcq7.us.<xxx>.com:80

ENV http_proxy=${http_proxy}
 ENV https_proxy=${https_proxy}`
This was required  as my office environment was behind the proxy and it was required for uv to download the dependencies on startup..


So this had caused the image to run in my office environment and not in orchestrator environment.. now removed the same and tested in a different vm altogether and noticed that the container  started up without issues..


Checkin url: [Update Dockerfile removed hard coded proxies · rsjay1976/TDS-Project1-Jan25@a71e3a8 · GitHub](https://github.com/rsjay1976/TDS-Project1-Jan25/commit/a71e3a84b284d7621f2a769308340454ebd58583)


Have pushed the latet image (rsjay1976/tds-project1-jan25:latests) to docker hub as well..  didnt make any source changes or any other changes in the image.. Would be great if this is considered and image be considered for reevaluation… Appreciate your help

---
**Post ID:** 613688  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/132  

I am also with the same situation sir. Please help with this issue. I have submitted everything correctly and it was working fine. Thanks

---
**Post ID:** 613767  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/133  

Hello Sir,


Greetings,


I have not recieved amy mail regarding my Project 1 Marks, can you please look into it.


Thank you/

---
**Post ID:** 613768  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/134  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) please sir could you help me with this issue previously when i ran on my system it was working perfectly fine

---
**Post ID:** 613804  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/135  

Hello sir


I noticed that the log mentioned:


“python: can’t open file ‘/app/app/main.py’: [Errno 2] No such file or directory.”


However, my main file was named run.py, which might have caused the issue. Since the code was present, I was given a 0. Would it be possible to run it again or consider partial marks for the submission?


Thank you for your time and consideration. I appreciate your help!

---
**Post ID:** 613831  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/136  

Even my file saying the same. I got the ‘No module named tasksA’ error whereas at the time of submission it was working perfectly fine. Please kindly look into this issues sir.


Thank you.

---
**Post ID:** 613847  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/137  

no taskA.py even though i ran the evalution getting 12 score still no evalution.log


help the students please give them second chance

---
**Post ID:** 613862  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/138  

on a side note, to validate and test our docker/podman images on a platform outside of our dev environment we can use [https://labs.play-with-docker.com/](https://labs.play-with-docker.com/).. this is a free platform to download run and test docker images …

---
**Post ID:** 613878  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/139  

Hi [@carlton](/u/carlton) [@Jivraj](/u/jivraj)


I might have found a bug in my code, I have hardcoded my file directory into my code but I didn’t change it later. I have created a safe_open function that will throw a HTTP_403_FORBIDDEN error when tried to access files outside that directory. Because of this all the tasks failed. There also might be environment and configuration issues in my Dockerfile. When I tested locally, it worked fine but because of this small mistake I am now only getting 1/20. Is it possible to change/modify my code?


Thanks for considering, any help would be appreciated. Worked very hard for this

---
**Post ID:** 613952  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/140  

The docker id of the image that was evaluated (as specified the mail 1ae3f64427f0) is not correct, the correct id is 51168f246618.


Name of Docker image -


garriimaa/llm_automation:latest


Please evaluate with the above image name.


GitHub repository for reference - [GitHub - Garima1603/llm_automation](https://github.com/Garima1603/llm_automation)

---
**Post ID:** 614001  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/141  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir I fixed my issue with docker during the given window for discrepancy and requested a re-pulling of the image but still got a mail of score 0. Please sir, I request you to do a re-evaluation, the docker issue is fixed long back by me. It’s an earnest request sir.

---
**Post ID:** 614002  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/142  

Dear sir,  [@carlton](/u/carlton) [@Jivraj](/u/jivraj)


I got result as fail for the project 1 and the reasons listed are as in the screenshot. But as you can see in the second screenshot, i still have that repository which is public, have license file and docker file in it, created 2 months back. I actually don’t know how this issues come in, please resolve this.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/c/2c922cdf1470207949392f3402b7cea1989e2397_2_690x294.jpeg)1885×378 56.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/c/2c922cdf1470207949392f3402b7cea1989e2397.jpeg)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/8/c8edbd63c9ebf7c97ccc221d7c91fa9ee4c8554c_2_690x439.jpeg)2908×579 59.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/8/c8edbd63c9ebf7c97ccc221d7c91fa9ee4c8554c.jpeg)

---
**Post ID:** 614004  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/143  

[@carlton](/u/carlton)


I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:


“Is Dockerfile present in root of GitHub repo?”


Despite this, my dockerfile is present in the root directory of my repository.


Github repo link: [GitHub - karthiksirimilla/tds_project1_final](https://github.com/karthiksirimilla/tds_project1_final)


My evaluation.log , contains the score 6/20


Roll no : 23f1002398


Mailid: 23f1002398@ds.study.iitm.ac.in


My evaluation.log


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/b/db1247df1beef8d4878a7ab13e5ad4eb7e626868_2_246x500.jpeg)IMG_64181290×2619 566 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/b/db1247df1beef8d4878a7ab13e5ad4eb7e626868.jpeg)

---
**Post ID:** 614005  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/144  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_230x500.png)IMG_64171290×2796 305 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56.png)

---
**Post ID:** 614007  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/145  

[@carlton](/u/carlton)  Sir, the image id written in my notification email is wrong. The correct image is this: [https://hub.docker.com/repository/docker/24f1002064/project1/general](https://hub.docker.com/repository/docker/24f1002064/project1/general)


can you please double check this? You can also verify that I have made no changes to it since the due date.

---
**Post ID:** 614011  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/146  

[@carlton](/u/carlton)


I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:


“Is Dockerfile present in root of GitHub repo?”


Despite this, my dockerfile is present in the root directory of my repository.


Github repo link:  [GitHub - karthiksirimilla/tds_project1_final](https://github.com/karthiksirimilla/tds_project1_final)


My evaluation.log , contains the score 6/20


Roll no : 23f1002398


Mailid: 23f1002398@ds.study.iitm.ac.in


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_230x500.png)IMG_64171290×2796 305 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56.png)

---
**Post ID:** 614009  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/147  

Your dockerfile is misspelt.

---
**Post ID:** 614014  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/148  

Thanks for your quick response sir. I just wanted to clarify that my dockerfile was recognized by Docker, and my image was successfully built, so it seems that Docker itself didn’t have an issue with the filename.


However, I understand that the evaluation script might be case-sensitive and specifically looking for “Dockerfile” with an uppercase “D”. If that’s the issue, should I rename and push the file again to the repo sir.


Please let me know if that’s the right fix or if I need to do anything else sir.

---
**Post ID:** 614015  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/149  

The image id varies depending on the system it was built on. When we build it on our Xeon cloud compute it will get a different image id from yours (unless you have a Xeon system). What is common is the dcoker hub image name and tag we used. We used the one you submitted on your form.


But the image id serves the same purpose. If you alter the dockerhub image, our image will no longer match the one from dockerhub. the image id sha will change. So do not worry about whether your sha matches our sha. It just acts as a way for us to make sure that we are consistently looking at the same image.


Kind regards

---
**Post ID:** 614017  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/150  

I recently received an email stating that my Docker image is not publicly available, resulting in a failed prerequisite check for the TDS Project 1. However, I have ensured that my Docker image is publicly accessible. Please help.


[@carlton](/u/carlton)


My Docker image ID is "99d08f2002fa ", and it is set to public. I kindly request you to review this issue, as I have worked very hard on this project and would appreciate the opportunity for a fair evaluation.

---
**Post ID:** 614019  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/151  

can you share the sha?

---
**Post ID:** 614021  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/152  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


There might be some glitches in the system. Could you kindly verify the process again?


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/0/80c8cd52c9f19a6d4047702b56fa98cbcf59b266_2_223x500.jpeg)10004306021080×2412 160 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/0/80c8cd52c9f19a6d4047702b56fa98cbcf59b266.jpeg)


I’ve already received my score in the evaluation log. Additionally, the Docker Hub run logs show no errors, and both the GitHub repo and Docker image are publicly accessible. All the content has been verified and meets the prerequisites.


Let me know if any further action is needed from my end.

---
**Post ID:** 614043  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/153  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) please kindly re-pull my docker image and re-evaluate my project sir. I fixed the issue long back. Please reply kindly. My roll no is : 22f2001389. I have been trying to get to you for long now. Please kindly help me out. Please reply.

---
**Post ID:** 614051  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/155  

[@carlton](/u/carlton)


I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:


“Is Dockerfile present in root of GitHub repo?”


Despite this, my dockerfile is present in the root directory of my repository.


Github repo link: [GitHub - Vansh-22f300/project_tds](https://github.com/Vansh-22f300/project_tds.git)


My evaluation.log , contains the score .


Roll no : 22f3001851


Mail id:22f3001851@ds.study.iitm.ac.in


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/4/d4df01a394ced7de96bc204dd764e71d18c62389_2_225x500.jpeg)Screenshot_2025-04-01-09-11-54-385_com.android.chrome1080×2400 171 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/4/d4df01a394ced7de96bc204dd764e71d18c62389.jpeg)

---
**Post ID:** 614053  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/156  

dockerfile is spelling mistake it should be Dockerfile same thing happened to me .

---
**Post ID:** 614058  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/157  

[@carlton](/u/carlton)


Pls look into this evaluation.py contains two result


Can u confirm that u guys will use 10/20 one ?


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/0/c0842e4115f2f72cc643b6b066c8c503b592c608_2_230x500.jpeg)Screenshot_2025-04-01-08-51-03-781_com.google.android.apps.docs1080×2340 253 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/0/c0842e4115f2f72cc643b6b066c8c503b592c608.jpeg)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f7ff60d992c45e083570f274407f2914b3f3f4c3_2_230x500.jpeg)Screenshot_2025-04-01-08-51-01-349_com.google.android.apps.docs1080×2340 219 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/7/f7ff60d992c45e083570f274407f2914b3f3f4c3.jpeg)

---
**Post ID:** 614062  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/158  

HELLO SIR , DOCKET IMAGE PRESENT IN DOCKER HUB  AND IT IS PUBLIC THEN WHY IT IS FAIL


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/749d670a5762fa641b21182e8967d86071f7b99e.png)image619×241 5.07 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/749d670a5762fa641b21182e8967d86071f7b99e.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/e/de8f280fe809b7770d0e86b62b74b614ed50e17a_2_690x451.png)image919×602 28.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/e/de8f280fe809b7770d0e86b62b74b614ed50e17a.png)


![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/efd0ca8b5a79aca303f8ae07d632c1a62c07bb1f_2_690x37.png)


[@carlton](/u/carlton)

---
**Post ID:** 614086  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/159  

same issue i am also facing ,


[@carlton](/u/carlton)

---
**Post ID:** 614089  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/161  

Respected Sir,


I have received a FAIL status for the prerequisite check:


“Is Docker image present in Docker Hub AND is public.”


However, as shown in my Docker Hub repository, my Docker images are publicly accessible.


I have attached a screenshot for the reference.


Thank you for your time and support.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c33d5a5cb98598131cd2f106e811773a37d4e830_2_690x110.png)Screenshot From 2025-04-01 11-17-441866×300 32.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/3/c33d5a5cb98598131cd2f106e811773a37d4e830.png)

---
**Post ID:** 614123  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/162  

Dear team,


The evaluation shows that the Github repo was not found, however the repository has published and public.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/a/5a304d3e8e047dc18282918c2571491ac331bd11.png)2025-04-01_13:10:20564×317 12.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/a/5a304d3e8e047dc18282918c2571491ac331bd11.png)


Github URL [GitHub - 22f3003029/llm_agent](https://github.com/22f3003029/llm_agent)


Roll Number: 22f3003029


Request your assistance on the issue.


Thank you

---
**Post ID:** 614128  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/163  

Respected Team,


I received an email stating I failed to fulfil prerequisite and scored 0 because of it.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/c/2c79db055fab11beede425b974311028f0d93e1b.png)Screenshot 2025-04-01 132313651×276 6.99 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/c/2c79db055fab11beede425b974311028f0d93e1b.png)


I checked my Docker Hub and there it is showing “Public”


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7bb1e9a2434b55bd730c069340ad3c290255089c_2_690x57.png)Screenshot 2025-04-01 1319441479×124 7.78 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7bb1e9a2434b55bd730c069340ad3c290255089c.png)


Can Anyone explain what I did wrong ?

---
**Post ID:** 614144  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/164  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/25537a49251705580ea50e7a1891ee99cda55e65_2_396x500.png)image593×747 61 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/5/25537a49251705580ea50e7a1891ee99cda55e65.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/1/317e57a3184948d62a96fd0206a53043bb0d2bac_2_690x335.png)image1525×741 52.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/1/317e57a3184948d62a96fd0206a53043bb0d2bac.png)


Sir, I have the image in the docker and it is upload last month and it is public. So why have I received a message saying that the image is not available in the hub. Can you confirm and reevaluate the error.


[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini) [@s.anand](/u/s.anand)

---
**Post ID:** 614149  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/165  

Hi [@Jayeshbansal](/u/jayeshbansal) ,


The docker repo name that you submitted through submission form was different than what your screenshot shows. `/jayeshbansal/add9a05689d3` docker repo doesn’t exists or might not be public, that’s why it failed for you.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e740a0a63b41602934accaa8c9ebceea5202b19_2_690x83.png)image1826×222 23 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/e/6e740a0a63b41602934accaa8c9ebceea5202b19.png)

---
**Post ID:** 614153  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/166  

The log file provided to me too contains File not found error for task A. However, running the code on the evaluate.py files gave me results. Could you please look into the datagen part?


[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Thanks

---
**Post ID:** 614156  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/168  

It is the request to the team,to consider this since it is a problem of just a case letter otherwise the whole hardwork of doing the project will be wasted.


Thank you

---
**Post ID:** 614160  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/169  

Dear instructors, I received the mail today regarding project 1 TDS scores and I have been marked fail because the MIT license is not present. But as can be seen in the screenshot below the MIT license file is present in my GitHub repository. Pls look into this matter.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf6f3e0168b08a862b7613b75dc9dbf83e914086_2_690x406.png)Screenshot 2025-04-01 at 2.45.57 PM1776×1046 91.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/f/cf6f3e0168b08a862b7613b75dc9dbf83e914086.png)

---
**Post ID:** 614164  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/170  

It depends where you tested it running, if it’s running inside a docker container and you feel there is problem with our script then you can debug our code and create a pull request on repo.

---
**Post ID:** 614165  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/171  

Hi [@24ds2000125](/u/24ds2000125)


You didn’t meet the standard naming convention for mit license naming.  Name should be LICENSE(all caps) or LICENSE.md.


check this out.


[Adding a license to a repository - GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)

---
**Post ID:** 614167  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/172  

Hi [@22f3001851](/u/22f3001851)


Standard naming convention for Dockerfile name was not followed we won’t be able to evaluate it.

---
**Post ID:** 614171  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/173  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/9/19ee62dc5d7a4dc1f92c30889a34483fe266978d.png)image412×167 4.49 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/9/19ee62dc5d7a4dc1f92c30889a34483fe266978d.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png)](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png)



My email is 22f3001642@ds.study.iitm.ac.in


[@Jivraj](/u/jivraj)  Could you please check what’s wrong?

---
**Post ID:** 614172  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/174  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh_Saini](/u/saransh_saini) any updates for the people like me whose image was run on the wrong architecture - mine was ARM ( was evaluated or ×86 ). I filled the form that was later sent for selecting the architecture.


I haven’t received any mail since then. But found many mails are sent to others in while.

---
**Post ID:** 614183  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/175  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1baedfbbb7140eb2f3bc80273f8dcfa799bb85e3_2_690x486.png)Screenshot 2025-04-01 at 3.17.14 PM2054×1448 294 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/b/1baedfbbb7140eb2f3bc80273f8dcfa799bb85e3.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/4/e4a17e2340281059ba12ec777f0a33a1c662f3ea_2_690x172.png)Screenshot 2025-04-01 at 3.19.32 PM1894×474 49.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/4/e4a17e2340281059ba12ec777f0a33a1c662f3ea.png)


Sir , I received the mail today regarding project 1 TDS scores and I have been marked fail because my repo is not public , and no docker file , no licence . but they all are present in my repo , and it is public too , , i am attaching the screenshot , you can see that too ,


My email is 23f1000598@ds.study.iitm.ac.in


Could you please check what’s wrong?


[@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini) [@carlton](/u/carlton)

---
**Post ID:** 614185  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/176  

The task B6 was


[https://quotes.toscrape.com/](https://quotes.toscrape.com/) has quotes from famous people.


The .author class has the quote author’s name.


Extract and save all authors from the first page, in order, to /data/b6.json as an array of strings.


E.g. `["Douglas Adams", "J.K. Rowling", ...]`


The output in your file is not an array of double quoted strings.


Instead it is an array of an json object with the keyword author and values as an array of authors.


These are two different things. Almost there but not quite.


Kind regards

---
**Post ID:** 614190  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/177  

Hi Course Team,


I have also received an email today saying that my Project1 failed. But few days back I received an email with evaluation log saying I got 8/20. Which one is true?


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/5/459244734bb379e3b318b5cc687ad47358f764bc_2_314x500.jpeg)10001125081080×1716 242 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/5/459244734bb379e3b318b5cc687ad47358f764bc.jpeg)

---
**Post ID:** 614193  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/178  

Can someone from TA team reply to this?

---
**Post ID:** 614252  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/179  

can somebody tell me how the dockerfile not running in 5 mins is my fault? i had the same requirements.txt as many other people and their file ran in given time while mine did not. what was the need for this, sorry for my harsh words but i’m frustrated, stupid rule?

---
**Post ID:** 614261  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/180  

For your case there was problem with our script that, we have correct, and your submission have dockerfile, license and repo exisits as well, it will be evaluated.

---
**Post ID:** 614266  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/181  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/f/1fedb48b369376de753a03a5286bc7e16a317dbd.png)image522×190 5.51 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/f/1fedb48b369376de753a03a5286bc7e16a317dbd.png)


my dockerfile is available in github, Please look into the issue


Thank you

---
**Post ID:** 614269  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/182  

[@Jivraj](/u/jivraj)


I also have same issue, can you check this…


[Repo link](https://github.com/21f3001076/TDS_Project_1)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/2/0284e9e1646abcf1a2b8e0720b33dcd4d483e301_2_258x500.jpeg)10004311361079×2087 175 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/2/0284e9e1646abcf1a2b8e0720b33dcd4d483e301.jpeg)

---
**Post ID:** 614276  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/183  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) My P1 submission successfully passed all the basic sanity checks on February 15th and obtained a satisfactory score in the P1 evaluation, which was disclosed on March 29th. However, I received a communication today, April 1, stating that my Docker image is not present or public on DockerHub. I kindly request the TDS course team to investigate this matter at the earliest and provide a resolution for students encountering similar issues.


This situation is particularly disheartening—seeing days of effort and dedication to Project 1 reduced to nothing, especially given the already demanding pace of the course.


I will appreciate your prompt attention to this matter.


Kind regards

---
**Post ID:** 614290  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/184  

I understand the problem. It may be possible that the image id i gave may be different as i had multiple dockerfile and there is a possibility that i gave the wrong image id due to some confusion. Is it possible for reevaluation. I have worked very hard and I don’t want to lose my marks because of some wrong id misconfusion. I request to check my dockerfile once again and provide the marks accordingly

---
**Post ID:** 614294  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/185  

dear [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


Dear Sirs,


I have seen that many others have posted similar issues to mine, and you have responded to some of them. To seek your attention, I am replying to this thread.


Please consider my request as well, as I do not want to lose marks on a project I have worked hard on, while also helping others. I am expecting a timely and positive response from your end.


Thank you.

---
**Post ID:** 614302  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/186  

Dear Sir,


I hope you’re doing well. I haven’t received any email regarding the results of Project 1. Could you please check if my result was sent or if there’s any update on this?


I would really appreciate your confirmation.


Mail id - 23f2000798@ds.study.iitm.ac.in

---
**Post ID:** 614304  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/187  

[@carlton](/u/carlton)


Respected Sir,


I have submitted my project following all the guidelines and fulfilling all the prerequisites. My docker file is available publicly and it is present in the root directory of github repo, still the mail says that the file is missing and my score is zero. Can you please look into this issue


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/3/332ce73b428520a8174e81c0d1a6922c2f1e334a.png)image1145×334 7.28 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/3/332ce73b428520a8174e81c0d1a6922c2f1e334a.png)

---
**Post ID:** 614322  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/188  

Name of your dockerfile doesn’t match the standard’s.


It should be `Dockerfile`(with D caps).

---
**Post ID:** 614323  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/189  

No we are doing another run of evaluations. Results will be sent soon.

---
**Post ID:** 614324  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/190  

dockerfile name should be Dockerfile as this is the standard they are considering .so it was not evaluated you better change that, if they revaluate it will be passed

---
**Post ID:** 614325  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/191  

Your submission have Dockerfile, LICENSE and repo exists as well, we found some problems because of redirects not handled in our script.


Your submission will be evaluated.

---
**Post ID:** 614327  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/192  

We won’t be considering changes after deadline, our script looks for commits before deadline and fetches latest commits before deadline.

---
**Post ID:** 614328  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/193  

That’s not possible, anything after deadline is not appreciated.

---
**Post ID:** 614329  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/194  

We have updated just files names will it be considered??

---
**Post ID:** 614330  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/195  

same issue with me , my repo has both the dockerfile , license and is public. Please look into this . [@carlton](/u/carlton) sir . [@Jivraj](/u/jivraj) [GitHub - veershah1231/tds_proj_1: Tds project](https://github.com/veershah1231/tds_proj_1) and i have made them 2 months ago and is not a new commit.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_299x500.jpeg)10001053861072×1787 256 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3.jpeg)

---
**Post ID:** 614337  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/197  

![That's a red "X" symbol on a black background.  It's a common graphical representation of cancellation, error, or negation.
](https://emoji.discourse-cdn.com/google/cross_mark.png?v=14) Did Not Receive Project 1 Score – Need Clarification


Post Content:



Hello, sir [@carlton](/u/carlton) [@Jivraj](/u/jivraj)


I received the evaluation email for my Project 1 Docker Image submission, but unlike my friend (who got an email with his score), my email did not include my score.


My Docker image ID: 6f446c9b84da


The email I received only contains logs and attachments, but no information about my actual score. in the mail recieved by my friend the score is clearly mentioned,


I would really appreciate it if you could clarify my project score and let me know if it was properly evaluated. If there is any issue, I request a reconsideration of my project evaluation.


Thank you for your help!


Attachments:



but in the email which i recieved i got the below thing , there is no information about the project score


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/8/f86eddb6cefbdcfd3e1b7d54b8310cedaad53edf.png)my email without score1403×811 35.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/8/f86eddb6cefbdcfd3e1b7d54b8310cedaad53edf.png)


sir could you please clarify about my project score ???


waiting for the response

---
**Post ID:** 614338  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/198  

I am also facing the same issue sir please provide proper answer for our query. Please consider to recheck the project once again.


Docker image - 5ff55c499b54


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/e/2e0e98a294f898f58e4d9dc68708cf723207c1ad_2_225x500.jpeg)10001616851080×2400 224 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/e/2e0e98a294f898f58e4d9dc68708cf723207c1ad.jpeg)


[@carlton](/u/carlton) , [@Jivraj](/u/jivraj) , [@Saransh_Saini](/u/saransh_saini)

---
**Post ID:** 614343  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/199  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Got a email stating that prereq failed stating below..


Is Docker image present in dockerhub AND is public: FAIL


but i can see that image is public as shown below image.. am i missing something..


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/ea109fa33e1cd4ca86ced5d663681c124e261b09_2_690x135.png)image902×177 12.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/ea109fa33e1cd4ca86ced5d663681c124e261b09.png)

---
**Post ID:** 614344  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/200  

Given that you noticed an error on our side, you could have informed us about the same. However, you made your changes 22 hours ago, which is not acceptable.


`tags = httpx.get(
                f"https://hub.docker.com/v2/repositories/{username}/{repo}/tags?ordering=last_updated",timeout = 60
            ).json()
            tag, size = next(
                (
                    (tag["name"], tag["full_size"])
                    for tag in tags.get("results", [])
                    if pd.Timestamp(tag["last_updated"]) <= DEADLINE
                ),
                (None, 0),
            )`
This is part of our script that does the validation check for docker repo.

---
**Post ID:** 614349  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/201  

Sir,


The License file is present in the github repository however i received a mail that said that it was absent.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a63b3e5cf7847aad19780199e18d9767880f3de8_2_690x405.png)image1145×673 33.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a63b3e5cf7847aad19780199e18d9767880f3de8.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/4/3401452ad3977fe3c1b1abed1f71a21c212e2b67.png)image633×336 7.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/4/3401452ad3977fe3c1b1abed1f71a21c212e2b67.png)


Sir I thought that the ‘LICENSE’ file had to be renamed to ‘MIT LICENSE’.


Can you please look into it. Thankyou!

---
**Post ID:** 614351  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/202  

[@Jivraj](/u/jivraj)


Can you also clarify my issue?


My submission meets all the prerequisites according to my Git repository and Docker image. Additionally, I can see the results in the evaluation log.


You can check the details in the images below. Screenshot of mail and repository


Roll no. : 21f3001076


[GitHub Repo link](https://github.com/21f3001076/TDS_Project_1)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/e/ee709e09763f171bdd0bbadccb2887556edbfa68_2_690x352.jpeg)10004314101080×551 159 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/e/ee709e09763f171bdd0bbadccb2887556edbfa68.jpeg)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94566b0ed49bb7659aa9c8a0941fa3b41bfb563e_2_690x472.jpeg)10004314131080×740 187 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/94566b0ed49bb7659aa9c8a0941fa3b41bfb563e.jpeg)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/f/6f945a759e9a4e932192211dd679839ae21921fe_2_330x500.jpeg)10004314151079×1630 134 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/f/6f945a759e9a4e932192211dd679839ae21921fe.jpeg)

---
**Post ID:** 614352  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/203  

Standard name of dockerfile is Dockerfile that’s why it didn’t pass Dockerfile check

---
**Post ID:** 614366  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/204  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)


I understand sir Dockerfile name was misspelt sir. Since my Docker image was built and recognized, I didn’t realize this would prevent evaluation.


I worked hard on this project sir, and my Docker image was built successfully. Please consider my submission sir.

---
**Post ID:** 614367  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/205  

I  have been trying to resolve all the errors but just noticed that my docker image id associated with the project is “c9dc7fbcf405” , meanwhile the mail I received mentions that some other image id was evaluated.


Can you please look into this matter and evaluate the correct Image ID.


Roll number: 23F1001012


[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 614374  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/206  

[@Jivraj](/u/jivraj) [@Carlton](/u/carlton) I completely understand that changes to the Docker image after the deadline cannot be accepted.


However, there are specific cases like mine where the Project 1 submission successfully passed the sanity checks on Feb 15 and received a decent score when the evaluation results were released on Mar 29.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/a/9acc2fc47ea84b9e26c1ed21442ba873d0dca20e.png)image1272×395 25.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/a/9acc2fc47ea84b9e26c1ed21442ba873d0dca20e.png)


But here’s the catch:** Since the problem statement for Project 1 and Project 2 is nearly the same, I took the opportunity to improve upon my Project 1 and use it as the foundation for my Project 2 submission, which I did by:*



Implementing a ReAct-based workflow planning & orchestration agent, inspired by the paper [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629).
Implementing various tools for web-serping, web-scraping, read-eval-print-loops interpreters for quick calculations, etc.
Enhancing Shell-use & Python-use by improving upon the existing code interpreter I had implemented for P1. This allowed the agent to dynamically generate and execute code without hardcoding anything.
Adding useful API endpoints, including an `/api/` multipart/form endpoint, alongside the existing `/read` and `/run` endpoints from Project 1, plus a `/clear` endpoint to reset the agent’s conversation memory if the context window gets saturated.
Deploying the entire project on a paid GCP VM Instance with a static IP, utilizing my own OpenAI API key while keeping OpenAI’s API as a fallback in case AIPROXY ever gave up.

All this hard work evolved my project into something far beyond a simple Tool-Calling Agent—it essentially became a ReAct Principles based Computer-Using Agent capable of executing complex, non-linear workflows entirely within a container. And I’m not exaggerating: You could ask it to perform something like hyperparameter tuning for a Random Forest Classifier, offloading the results locally on a JSON file and displaying its contents, and it would do that for you—without ever declining the request. I like to think of it as a terminal version of [OpenAI’s Computer-Using Agent](https://openai.com/index/computer-using-agent/).



Given all the effort, time, and money that went into this, it’s incredibly discouraging to see my project naturally fail a sanity check (Docker image digest mismatch) (because of the aforesaid updates) and not get evaluated as a result. This is not the kind of experience that encourages students to learn, experiment, and innovate.


[](#p-614374-to-clarify-all-the-updates-mentioned-above-took-place-after-march-29-after-project-1-had-already-been-evaluated-and-results-had-been-handed-out-furthermore-we-were-never-informed-that-a-reevaluation-would-take-place-on-april-1-had-i-known-i-would-have-ensured-that-my-original-submission-remained-unchanged-and-considered-creating-a-duplicate-of-my-docker-image-and-implementing-all-the-aforementioned-enhancements-on-it-1)To clarify, all the updates mentioned above took place after March 29, after Project 1 had already been evaluated, and results had been handed out. Furthermore, we were never informed that a reevaluation would take place on April 1. Had I known, I would have ensured that my original submission remained unchanged and considered creating a duplicate of my Docker image and implementing all the aforementioned enhancements on it.
My only request is that if my updated P1 submission cannot be evaluated due to the changes made after March 29 (before the P1 reevaluation on April 1), I would really appreciate it if my original P1 eval score could be reinstated instead of receiving a 0—since it was already evaluated and graded.


Would highly appreciate your prompt support in this regard [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 614391  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/207  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0daeec08afc5b8bf1176ea341a88da5d99a592e8_2_225x500.jpeg)pro 1720×1600 81.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/d/0daeec08afc5b8bf1176ea341a88da5d99a592e8.jpeg)


Actually I got the email as my docker file is not in root git hub repository. But everything thing looks fine and my docker file also runs well.. I want to check my repo again ..sir kindly do my my evaluation again and we have put lot of efforts doing this project 1 . Hope the team evaluated and gives the deserved marks


[@carlton](/u/carlton)


@ TDS TEAM

---
**Post ID:** 614390  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/208  

There is no Dockerfile in the root directory of your GitHub repository. The standard naming convention for a Dockerfile is Dockerfile.

---
**Post ID:** 614402  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/209  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) please let know if any issues in my end on the docker image not present issue.. As explained in earlier thread , the only reason docker image had to be pushed  was the removal my office proxies in the docker image which was making the container not to startup from orchestration environment.. any help is appreciated..

---
**Post ID:** 614453  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/210  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  I updated google form 4 days ago on the architecture, Could you let me know when it will be re-evaluated ? Thanks

---
**Post ID:** 614462  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/211  

Hi [@thinkmachine](/u/thinkmachine) [@22f3002723](/u/22f3002723)


Since you updated docker repo few days ago and docker api doens’t support timestamp based pulling we will pull your GitHub repo before 18 th feb and will build through it and run evaluations.


We also have your docker repo evaluation score, will discuss which one to keep.


This is for anyone who updated their docker repo and there are around 10-20 such cases

---
**Post ID:** 614474  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/212  

Thanks for the understanding [@Jivraj](/u/jivraj)

---
**Post ID:** 614498  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/213  

Hi [@thinkmachine](/u/thinkmachine)


As we said before that changes in Docker image after deadline won’t be accepted. Even an extension of the deadline won’t help in this case, simply because Docker API doesn’t support timestamp based pulling. However we would be pulling your GitHub repositories before 18th Feb build a Docker container and run evaluations on that.

---
**Post ID:** 614499  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/214  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh_Saini](/u/saransh_saini) request your help in clarification for the same, the Github repo has been always present but it is marking it as fail. Thank you

---
**Post ID:** 614504  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/215  

A sigh of relief! Thank you so much for the heads up [@Jivraj](/u/jivraj).


[@Saransh_Saini](/u/saransh_saini) Yup! The Docker issue is perfectly understandable. Even I checked my Hub repo, and I couldn’t seem to find an image having the pre-18th Feb digest. Had I been aware of this issue, and the fact that a re-eval would be carried out, I would’ve tagged the updated image differently. Hopefully, cases like mine will aid in resolving any issues in the future.


Once again, thank you both!

---
**Post ID:** 614596  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/216  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh_Saini](/u/saransh_saini)


I am still uncertain as to why I received a second email regarding my project 1 score, indicating a failure due to unmet pre-requisites. I have inquired multiple times, yet I have not received a response. Meanwhile, several other posts, both before and after mine, have been addressed. Kindly clarify about that mail.


Thankyou

---
**Post ID:** 614604  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/217  

[@carlton](/u/carlton)   Sir pls see my issue

---
**Post ID:** 614613  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/218  

I have the same issue. I also received a second mail stating I had failed due to some missing prerequisites though in the first mail my project evaluation had been carried out.

---
**Post ID:** 614620  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/219  

Hi [@lakshaygarg654](/u/lakshaygarg654)


Dont worry you passed pre-requsites. The script that was used earlier for basic checks used a stricter criteria, the newer one we wrote allowed for a looser check. You have scored very well in your latest run. 12 correct tasks.


We have not responded quickly because we are in the midst of finalising all the scores and doing normalisation etc, i.e operational work for Project 1 and 2.


We hope to have Project 2 scores out by this weekend.


Kind regards

---
**Post ID:** 614623  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/220  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Sir can you also see the case of Dockerfile name. Many students have named it dockerfile , lower case ‘d’ character instead of upper case.


Please sir see through it

---
**Post ID:** 614624  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/221  

Thanks [@carlton](/u/carlton) , for your response.


I was never worried about the result, whether it comes late or early. I know you will release it once everything is processed correctly. My concern was only about getting a response. Anyway, thanks for replying.


Also, today’s session has been canceled. I wanted to ask about the issue with editing responses in the Project 2 form. Is there any update on this?

---
**Post ID:** 614709  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/222  

Hi just wanted to know, there was no mail prior stating to keep the Dockerfile in the root folder of the repo (correct me if im wrong). Therefore i have put everything inside a folder - wont this be considered? Please clarify if possible.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f31f9a238afa57c9c57655de5c717546fa4f9268_2_690x274.png)Screenshot 2025-04-02 at 11.41.14 PM1884×750 69.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/3/f31f9a238afa57c9c57655de5c717546fa4f9268.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/5/85aed36152ce7c20f03accf0e9d01a5fc596109c_2_690x224.png)Screenshot 2025-04-02 at 11.43.17 PM2290×744 55.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/5/85aed36152ce7c20f03accf0e9d01a5fc596109c.png)

---
**Post ID:** 614711  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/223  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/a/da4e9a282399e03a47410d7ddb796d4a01802f5d_2_690x259.png)10000041761187×446 55 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/a/da4e9a282399e03a47410d7ddb796d4a01802f5d.png)


Can anyone explain what errors of this sort mean?

---
**Post ID:** 614725  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/224  

You have to show which task triggered this error. Is it all of them or only one of them. Only then we can diagnose what the problem is.

---
**Post ID:** 614740  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/225  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a204d9c51d90a584e4e56d593b24821129e056e_2_519x500.png)10000041901193×1149 136 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/a/6a204d9c51d90a584e4e56d593b24821129e056e.png)


Here it is with the task, however the error doesn’t seem to be related to the task itself based on the returned message in the JSON. It seems to be something wrong with the OpenAI API key. From the reading I did, it seems that the key was perhaps not set properly during evaluation? Not completely sure but please look into it.

---
**Post ID:** 614754  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/226  

Did all tasks produce the same error?

---
**Post ID:** 614757  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/227  

Yes except B1 somehow.

---
**Post ID:** 614768  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/228  

Hi [@AryanTikam](/u/aryantikam)


I looked at your github repo, You have used python’s `openai` module for doing project1, but AIPROXY_TOKEN is supposed to be used through anand sir’s proxy.

---
**Post ID:** 614769  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/229  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


Can you pls tell me my project 1 marks


My evaluation.py had 2 score


First one 1/20 where every task showed error second one had 10/20…

---
**Post ID:** 614770  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/230  

Dockerfile has to be insider root directory of github repo.

---
**Post ID:** 614787  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/231  

This was mistake from our end we rectified it and reevaluated your submission.


Your submission has a good score.

---
**Post ID:** 614790  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/232  

[swati-iitm/project1_final](https://github.com/swati-iitm/project1_final)


This is your github repo which doesn’t have a Dockerfile. That’s why It didn’t pass Prechecks

---
**Post ID:** 614792  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/233  

We have reevaluated it, we have scores avaliable for your submission.

---
**Post ID:** 614796  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/234  

Sir I understand you will be busy evaluating all the files and reevaluating them as well. I just wanted to know if its a confirm 0 for those who got evaluation log file MISSING and didnt get the other mail that many got in the past 2 days… Just to confirm… cause i think am getting 0 from that [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 614804  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/235  

So can anything be done about it now as it seems to pass more tasks without the proxy requirement? It is fine if not.

---
**Post ID:** 614814  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/236  

Please, can you put a screenshot of where it has been communicated, prior to the deadline.

---
**Post ID:** 614825  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/237  

We have communicated it in the live sessions. It was also communicated via an email when students failed first prerequisite check pass back in February 16th. At that time we gave students a time window to fix it.


We discussed it internally with [@s.anand](/u/s.anand) and he stated that it is standard industry practise to put Dockerfile in the root folder of a github and he expects students to do it regardless of whether we explicitly mentioned it or not on the project 1 page. The reason being, any Docker image being built from a github repo is never going to look for the file sitting inside a directory. All build requirements have to be at root (this is not just for Docker, but also any other type of application build). Since root is where the core files to build an application always reside, again this is standard industry practise.


In our meeting we advocated for a lenient approach to search for Dockerfile inside the github and it was vetoed by [@s.anand](/u/s.anand)


So unless you can give a convincing argument why we should change our evaluation script and re run it for everyone again, (because that is effectively what we would have to do to make it fair to everyone), we will not be able to evaluate your docker image.


Kind regards,


TDS team

---
**Post ID:** 614834  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/238  

[@carlton](/u/carlton) Sir, I would like to respectfully ask if this is some sort of April Fool’s joke, as it appears that the TDS team is still only verifying the presence of files in the git repository and checking the accessibility of the repository. I fully understand the importance of marks and the effort we put into Project 1. That’s why I carefully ensured that all the necessary files and links were correctly uploaded yet I received a 0 Score.


I am not the only one facing this issue; several others have encountered the same problem. I kindly request you to review my submission again.


Additionally, I have faced multiple technical issues in recent times. Initially, I was failed in the L1 viva due to a typing mistake, which was later acknowledged. Similarly, in both OPPE 1 and OPPE 2, many students experienced Google Meet issues. On March 29, during my SC OPPE, I faced camera issues in Google Meet, along with VM lagging. Many students have raised similar concerns with Proctor.


Given this track record of technical problems, I strongly believe this could be another error in evaluation. I sincerely request you to re-evaluate my submission.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c15a5d064b9f2bc82a892ef7da1228f031feb29b_2_690x344.png)Screenshot 2025-04-01 0206181335×667 57.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c15a5d064b9f2bc82a892ef7da1228f031feb29b.png)

---
**Post ID:** 614092  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/239  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_394x500.jpeg)IMG_7078828×1049 164 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899.jpeg)


Same for me sir, i had everything correct still its showing:- Is Docker image present in dockerhub


AND is public: FAIL


I have submitted everything correctly . Please carefully look into this and recheck the project submitted.

---
**Post ID:** 614093  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/240  

Sir,it appears that the TDS team is still only verifying the presence of files in the git repository and checking the accessibility of the repository. I fully understand the importance of marks and the effort we put into Project 1. That’s why I carefully ensured that all the necessary files and links were correctly uploaded yet I received a 0


[@carlton](/u/carlton) Sir please look into this.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_394x500.jpeg)IMG_7078828×1049 164 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899.jpeg)


[@carlton](/u/carlton) Sir, given  this track record of technical problems, I strongly believe this could be another error in evaluation. I sincerely request you to re-evaluate my submission.

---
**Post ID:** 614118  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/241  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c240e636b74a12f59d3c0d50fc904bb7361a481a_2_690x439.png)Screenshot 2025-04-01 at 12.50.38 PM2062×1314 262 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/2/c240e636b74a12f59d3c0d50fc904bb7361a481a.png)


[@carlton](/u/carlton) sir, i would like to ask why marks showing 0 infact i am submitting all my requirements things in that form so plz look into this matter.

---
**Post ID:** 614694  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/242  

[@carlton](/u/carlton) sir, similar thing happened to me as well, I had got the mail that git repo, dockerfile and lisence is not present or accessible while all the prerequisites are completed from my end. Can you please reevaluate my submission.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eab711c7e3854b0163bab1970630905785492718_2_290x500.jpeg)10000515561238×2131 182 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/eab711c7e3854b0163bab1970630905785492718.jpeg)

---
**Post ID:** 614737  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/243  

Hi Prashant,


Your prerequisites have passed and your evaluation is 6 tasks have been completed successfully. The email was auto sent because we were doing some checks with an older, stricter script. The newer script passes your evaluation.


Kind regards

---
**Post ID:** 614838  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/244  

Thanks for the quick reply, i don’t have a convincing argument to counter. Just a suggestion it would have been better if you have explicitly put in the sanity check requirements. Something so obvious to you might not be so for others.


if you are referring to this email even here, it was not explicit. Might have missed it in the gmeet. A mail would have been good.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad091bfbf1e7642fa941a72ce2d527fac1e26dd8_2_690x281.png)Screenshot 2025-04-03 at 12.28.22 PM2236×912 208 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/d/ad091bfbf1e7642fa941a72ce2d527fac1e26dd8.png)

---
**Post ID:** 614839  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/245  

I agree with you. It should have been explicitly mentioned in the project page (even if we have mentioned it in live sessions)

---
**Post ID:** 614842  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/246  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Put some light on this poor soul’s message also ;')

---
**Post ID:** 614862  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/247  

my repo has both the dockerfile with correct name (Dockerfile and in the root folder), license and is public. Please look into this . [@carlton](/u/carlton) sir . [@Jivraj](/u/jivraj) [GitHub - veershah1231/tds_proj_1: Tds project](https://github.com/veershah1231/tds_proj_1) and i have made them 2 months ago and is not a new commit.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_299x500.jpeg)10001053861072×1787 256 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3.jpeg)


why is it saying i got 0? please look into it.

---
**Post ID:** 614863  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/248  

[@carlton](/u/carlton) [@jivraj](/u/jivraj) Sir I received a mail like everyone that my git-hub repository is not public and not MIT licensed. I even filled the g-form correctly while submitting.


But I had fulfilled the above required criteria. Please look into this matter ASAP.


Here is my git repo link : [[GitHub - 23f1001415/llm_aa_tds_project](https://github.com/23f1001415/llm_aa_tds_project)]. ([https://github.com/23f1001415/llm_](https://github.com/23f1001415/llm_)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/2/a2b81c003a14d06f5359d4e97e908dd4d87665f7_2_690x388.png)Screenshot (390)1920×1080 266 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/2/a2b81c003a14d06f5359d4e97e908dd4d87665f7.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/1/915ae521873c3a286c2e898ddc8d33881ff5969e_2_690x388.png)Screenshot (391)1920×1080 208 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/1/915ae521873c3a286c2e898ddc8d33881ff5969e.png)


aa_tds_project).


I have attached screenshots for your reference.


Thank you

---
**Post ID:** 614872  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/249  

[@Jivraj](/u/jivraj) I too had the same issue (image was run on wrong architecture) and filled the gform that was circulated. When should we expect to get our scores?


Thanks


Pradeep Mondal

---
**Post ID:** 614874  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/250  

Hi [@21f2000709](/u/21f2000709)


We have used another approach because of architecture problem, by pulling through latest commit from github before 18th feb. Just checked we have results for you.

---
**Post ID:** 614875  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/251  

Hi [@23f1001415](/u/23f1001415)


This was a problem from our side and we rechecked and now we score against your submission.

---
**Post ID:** 614876  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/252  

Hi [@23f1001524](/u/23f1001524)


This was a problem from our end, we have recitified it your submission was valid.

---
**Post ID:** 614877  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/253  

Your latest score through pulling from github and building image thorugh dockerfile have higher score than these 2.

---
**Post ID:** 614882  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/254  

Hi [@23f2004563](/u/23f2004563)


I checked we have scores against your submission.

---
**Post ID:** 614883  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/255  

There was some problem with our script, later we correct and your submission was valid, I have just checked and confirm you.

---
**Post ID:** 614887  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/256  

Can u pls share marks :') dying with curiosity

---
**Post ID:** 614888  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/257  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d5e2932465ab30873ba0e0d597c29da8049ac05_2_690x92.png)image1841×248 24.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/d/6d5e2932465ab30873ba0e0d597c29da8049ac05.png)


This was your submission and we could not locate a docker repo against it.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/2/12102c6f548ec1535363f91201441acbc019a484_2_690x336.png)image1885×918 92 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/2/12102c6f548ec1535363f91201441acbc019a484.png)

---
**Post ID:** 614890  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/258  

Your submission was valid there was some issues with our script for checking. But after building your image after pulling github repo, it didn’t one `taskA` module was missing.

---
**Post ID:** 614893  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/259  

If you used openai’s python module then you were needed to pass your own api key, hardcode it in code.


API key that we were sending was only valid through proxy server created by professor anand.

---
**Post ID:** 614894  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/260  

mail will be sent by either today or tomorrow.

---
**Post ID:** 614895  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/261  

any idea on this sir?..

---
**Post ID:** 614898  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/262  

No we pulled through github and build image on gcloud vm. Anyone with valid submission didn’t receive mail, your submission was valid.

---
**Post ID:** 614899  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/263  

but my evaluation log file was missing… so that would make it a 0 right..I have accepted my fate that it would be a 0 but just a lil hope ![Image description failed](https://emoji.discourse-cdn.com/google/melting_face.png?v=14)

---
**Post ID:** 614900  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/264  

We reevaluated and found your submission was valid but it was running on a different port, 5000 but it was expected to run on 8000 port.

---
**Post ID:** 614901  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/265  

oh so… is it going to be considered? like will i get some score other than a 0… am sorry for asking so much

---
**Post ID:** 614902  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/266  

No it won’t be considered. It was supposed to be running on 8000 port.

---
**Post ID:** 614903  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/267  

Ok got it. Thank you so much ![Image description failed](https://emoji.discourse-cdn.com/google/cry.png?v=14)

---
**Post ID:** 614905  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/268  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a9cdf3350a4eeebd0363ccf02a341ca2dce1716f_2_690x290.png)image1867×787 43.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/9/a9cdf3350a4eeebd0363ccf02a341ca2dce1716f.png)


Hi sir, my Architecture says amd64, in the google docs I have selected x86, i hope it is correct. Also,  I have used podman to test the pull and its working well. Please let me know if i need to do anything else.


[@carlton](/u/carlton)

---
**Post ID:** 614662  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/269  

We are rebuilding all docker submissions from github commit before 18th of Feb, using your Dockerfile manifest present in the repo.


That way there is no architecture issues.


Its part of our secondary check. And more students have gotten scores in this  check. So dont worry.

---
**Post ID:** 614911  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/270  

I just checked from my side also, wow a very dumb mistake now costing me a 0…should have read the project document more clearly ![Image description failed](https://emoji.discourse-cdn.com/google/cry.png?v=14) So sorry for asking.


Am assuming no lenient correction can be done for that? like during the evaluation …


podman run --rm -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:5000 $IMAGE_NAME

---
**Post ID:** 614918  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/272  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/c/4c563983c5ccd623597938159d4356f9857f2dd8_2_690x466.png)Screenshot 2025-04-03 1603361373×928 80.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/c/4c563983c5ccd623597938159d4356f9857f2dd8.png)


I checked it multiple times before submitting, I got 9/10 in task A.

---
**Post ID:** 614923  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/273  

No. Because someone else might have another minor issue they want to fix. We have to apply the rule uniformly.

---
**Post ID:** 614927  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/274  

Ok… I do have a doubt tho, i actually have app.py and main.py in my github, my main.py is running on 8000 and app.py on 5000 …

---
**Post ID:** 614930  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/275  

but in Dockerfile in your github repo you didn’t run main.py,

---
**Post ID:** 614932  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/276  

In your Dockerfile you didn’t copy taskA.py to the container.

---
**Post ID:** 614934  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/277  

Ouch, ok sir… hopefully project 2 doesnt disappoint ![That's a pixelated emoji of a yellow face crying large, blue tears.  It conveys intense sadness or heartbreak.
](https://emoji.discourse-cdn.com/google/sob.png?v=14)

---
**Post ID:** 614958  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/278  

It is there in the master branch of the repository. Now, will the previous evaluation mail that we got be considered or this one?

---
**Post ID:** 615048  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/279  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


I recently received an email with an evaluation file for Project 1, which included a score. However, in the recent email, I noticed that my score was recorded as zero, despite fulfilling all the prerequisites.


I kindly request a re-evaluation of my project, as I believe this may be an error.

---
**Post ID:** 615061  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/280  

[@Jivraj](/u/jivraj)


My discrepancy is still not fixed. Please take a look at it

---
**Post ID:** 615070  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/281  

[@Jivraj](/u/jivraj)


Hlo, could you please check and let me know how much am I scoring in Project 1 after the latest evaluation?

---
**Post ID:** 615124  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/282  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)


Sir,


In the mail that i got about project 1 report. In the log file it was written as TasksA.py file not found in docker, which was the case i observed with many students.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/968890ec5cffbca81bafeef7181db1173e1a6528_2_690x460.png)Screenshot 2025-04-04 at 10.31.02 AM1358×906 47.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/6/968890ec5cffbca81bafeef7181db1173e1a6528.png)


This is my Github repo:


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/c/0ce93452fedd6a15660a312186ed7f3b3a10a39e_2_690x372.png)Screenshot 2025-04-04 at 10.44.24 AM3324×1794 497 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/c/0ce93452fedd6a15660a312186ed7f3b3a10a39e.png)


I built the image using docker build command in vs code terminal. And pushed it same way to dockerhub using docker push command. How is it possible that the docker container missed the TasksA.py file while building or pushing it?


After getting this mail, I ran the project locally again mutliple times just to check if there was any issues in the code. It was getting 9/10 test cases passed.

---
**Post ID:** 615131  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/283  

This is a common mistake many, many students made. They created a working application but not a working container.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e_2_690x493.png)Screenshot 2025-04-04 at 11.13.32 am2116×1512 323 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e.png)


You only copied `app.py` into your docker image.


How do you expect your application to run without the other files that your repo clearly shows is needed?


Thats why many people are failing this. Hope the image makes this clear.


Kind regards

---
**Post ID:** 615135  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/284  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f56ad9b52eb9d732629f1a36b7353194cf6acd9e_2_230x500.jpeg)10000503481080×2340 154 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f56ad9b52eb9d732629f1a36b7353194cf6acd9e.jpeg)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/031fb8ca7808375905f4725bba8fa6e38751802d_2_230x500.jpeg)10000503491080×2340 190 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/031fb8ca7808375905f4725bba8fa6e38751802d.jpeg)


I am getting license not present at root of github repo but i have the license added could someone please explain why ?

---
**Post ID:** 615138  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/285  

[@thinkmachine](/u/thinkmachine)


Firstly, you have passed evaluation and got a decent score (on a more lenient script that we used for everyone.) The email was sent by a script that used a more stricter evaluation (which understandably caused some stress). So you can breathe a sigh of relief. ![That's a simple, smiling yellow emoticon or emoji.
](https://emoji.discourse-cdn.com/google/slight_smile.png?v=14)


However with regards to your long post…


Let me tell you a true story. I personally know a very experienced senior engineer at a top defense contractor for the US, here is some pearls of wisdom from him.


What you have done is what is called in industry as gold plating. Its a cardinal sin in software engineering. NEVER gold plate. ALWAYS build to spec.


In fact its a good reason to fire an engineer. Why?



Because it does not deliver what was required,
Wastes valuable time and resources
Increases technical debt (this is actually a huge cost over the expected lifetime of the project!)
Complicates testing
Leads to scope creep

His advice to me was simple: NEVER gold plate.


I hope you take this pearl of wisdom in your career. It will help you advance and make you stand out.


For personal hobbies this does not apply. But for a client (including us) if you fail to deliver the minimum spec then we cannot grant you an evaluation (by the way this post is not targetted specifically for you, it just felt like an appropriate place to explain this).


Kindest regards

---
**Post ID:** 615182  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/286  

Hi Sir,


I just realized that I mistakenly submitted the image tag “abhay227/version1” instead of the correct image ID. The correct image ID is 4db729a03f74 , which is part of version1 that is already present and publicly available.


I have worked very hard on this project, and I am concerned that due to this error, my whole effort may be wasted. Unfortunately, I did not receive any notification regarding an invalid submission after I submitted the Project1 form, and I only recently became aware of this mistake. I kindly request you please consider this correct image ID.


Thank you for your understanding and assistance. I look forward to your positive response.


[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_690x93.png)Screenshot 2025-04-02 1322141843×250 18.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1.png)

---
**Post ID:** 615197  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/287  

Hi Abhay,


This was a basic error. Unfortunately for basic errors we are not able to relax the requirements. All students were given a clear directive on what the minimum requirements were in order to be evaluated. Failure to follow those clear instructions prevents us from making any exceptions, because then we just have to dump all those requirements for all students and that would not be fair to those that took the care to be careful about their submissions.


Kind regards

---
**Post ID:** 615384  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/288  

Hi sir, hope you are doing well.


Could you please check and let me know if I have passed the project 1 and if yes then how much am I scoring in Project 1 after the latest evaluation?


[@carlton](/u/carlton)

---
**Post ID:** 615386  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/289  

Thanks for the clarification regarding the evaluation, [@carlton](/u/carlton). It’s a relief to know that my original submission was successfully evaluated. Had I known that the stricter evaluation script would pull the image matching the digest from the time of submission (which had been overwritten by April 1), I would’ve used a separate tag to avoid the issue altogether.


Regarding your point on gold plating — I completely understand and have come to appreciate the importance of building to spec from personal experience, especially in production or client-facing settings where fixed targets, maintainability, and minimal scope creep are key. That said, with TDS projects, my goal was purely exploratory — to explore the boundaries of what’s possible within the scope of the problem statement.


What began as just another (pun intended) tedious assignment slowly evolved into a hobbyist research project on LLM agents. ![Image description failed](https://emoji.discourse-cdn.com/google/grinning_face_with_smiling_eyes.png?v=14)


(…caution: long post ahead ![That's a laughing emoji with a single drop of sweat on its temple.  It conveys nervous laughter or amusement that's slightly uncomfortable or awkward.
](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=14))


I noticed that test cases in Project 1 and 2 were highly specific and often overlapping on Python & Shell use. While it would’ve been easy to hardcode 50+ Python functions to pass these cases (which, frankly, many of us were doing), it is non-scalable at best. I quickly realized that stochastic parrots + hardcoded functions were a recipe for disaster, especially considering the inherent randomness in LLM-generated payloads. No two payloads are exactly alike — even minor differences, like an absolute vs relative file path, or some hidden edge case could cause a hardcoded solution to fail unpredictably. There’s also really no way to predict an edge case caused by an LLM.


Some might suggest using `temperature=0` to get more deterministic LLM behavior — and while true to an extent, it does little to encourage exploration, especially in tasks that require self-correction based on environmental feedback. Prompt engineering too wouldn’t be helpful here as 4o-mini isn’t all that great at 0-shot instruction following, especially when the system prompt is already saturated with 50+ fine-grained instructions. There’s only so much stuff it can pay attention to.


Hardcoded tool agents also aren’t really “agents” in my view— they’re more like passive AI powered regex matchers: merely mapping inputs to functions by inferring from context window. That puts all the burden of answering on the hardcoded functions, leaving the agent itself uninvolved in the solutioning process. If they break, the agent will never try to ‘fix’ them and keep calling them like a broken record.


At the core of it, it’s all about how much flexibility vs rigidity we give to the agent. Fully rigid solutions (e.g. hardcoding) overfit and break easily; fully flexible ones (e.g. pure LLM based) hallucinate or drift off-target. The sweet spot lies somewhere in between — The right solution would naturally balance the lesser of two evils in an ideal ratio.


Since most LLMs already excel at code generation and structured solutioning, the most effective strategy that I figured out for the agent was to,



Reason about the task, understand intent,
Reflect, whether this problem is solvable using available tools without human intervention and design structured workflows, in whatever order appropriate (i.e. design a DAG, where each node can be a python step or a shell step or something else)
Execute those workflows (walk the DAG) observing the feedback at each step and reiterating if needed.
Observe the final result, and repeat if needed.

Interestingly, a similar framework was suggested in [this ICLR 2022 paper](https://arxiv.org/abs/2210.03629). That was all the validation I needed to know I was stepping in the right direction.


To make environment interaction possible, the agent didn’t need dozens of narrow tools — just a small, well-defined set of general-purpose tools:



A REPL executor (for quick calcs)
A Python script runner
A Shell executor

With just these, it could handle most tasks flexibly and naturally — avoiding overengineering while still enabling powerful behaviors. Potentially allowing for full fledged Computer-Use via shell and so much more.


As for the fact that it ended up being capable of things beyond the scope of Project 1 (like training & tuning ML models autonomously, reporting results etc.) — that was emergent behavior, not deliberate gold plating. It was a pleasant surprise even to me. I’ve yet to discover more of such interesting hidden use cases. While some might naturally call it scope creeping (and yes that is true, given that we had a deadline, and a play-pretend client-business relationship with the course team), I saw it as an opportunity for exploration and research. Frankly, I AM personally very keen about researching stuff!


I am actually very thankful to the TDS course team & [@s.anand](/u/s.anand) for devising such a thoughtful project that sparked some interesting ideas that I can tinker with. Food for thought! Really!


As for my next project, I now have a fair idea of what I’ll be experimenting with— modalities.


PS: I’m not claiming it’s perfect or production-ready, or it should score a perfect 22/20, but it aligned well with what I believe was the spirit of these projects: thoughtful use of LLMs in agent design. At this point, I’m less concerned about the marks, I’m actually enjoying the thought joyride. ![Image description failed](https://emoji.discourse-cdn.com/google/grinning_face_with_smiling_eyes.png?v=14)



TL;DR


My approach doesn’t rely on regex or hardcoded mappings. Instead, it passes user input directly to an LLM, which then plans and executes workflows using general tools inside a containerized environment. It also learns from feedback and iterates — much like a human. The fact that it can do more than just the minimum spec is a byproduct of that framework. I’ve only just wired the pieces together.


Kind regards

---
**Post ID:** 615471  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/291  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  Sir please Consider this request!

---
**Post ID:** 615606  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/292  

Hello Sir,


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/5/05553623c126727b31b481bf5da4faedb58f8405_2_225x500.jpeg)Screenshot_2025-04-05-18-51-43-721_com.google.android.gm1080×2400 144 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/5/05553623c126727b31b481bf5da4faedb58f8405.jpeg)


I got this mail regarding my project 1 scores. My github repo is present and public as well as MIT License and Dockerfile  is also present at the root of the repo




[github.com](https://github.com/SrishtySnehi/Project_1_tds)



![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/9/f93c7a8f75b0e5f3c99be032499e49464d57c7a2_2_690x344.png)
[GitHub - SrishtySnehi/Project_1_tds](https://github.com/SrishtySnehi/Project_1_tds)
Contribute to SrishtySnehi/Project_1_tds development by creating an account on GitHub.

---
**Post ID:** 615610  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/293  

Hi [@Srishty_Snehi](/u/srishty_snehi)


Your submission is valid, we but it failed while running server, with this error.


taskA module missing
For regenerating this error:



Pull github repo(latest commit before 18th Feb)
Build image using Dockerfile of fetched repo
Run that image.

---
**Post ID:** 615612  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/294  

We are not considering Dockerfile’s with wrong name(anything other than Dockerfile), and wrong location(anything other than root) in github repo.

---
**Post ID:** 615614  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/295  

Will I still get a zero?

---
**Post ID:** 615651  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/296  

Can we expect the results for project 1 and 2 by tomorrow? [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 615666  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/297  

when can we expect our project 1 result?


[@Jivraj](/u/jivraj)

---
**Post ID:** 615984  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/299  

I got my result!! 2/20 so happy its not a 0 thank you for the bonus [@carlton](/u/carlton) [@Jivraj](/u/jivraj) ![That's a pixelated emoji of a yellow face crying large, blue tears.  It conveys intense sadness or heartbreak.
](https://emoji.discourse-cdn.com/google/sob.png?v=14)


Also really great how yall have given the error logs for everyone individually ![That's an emoji of a yellow face with a hand saluting it.  It often conveys a sense of resignation, defeat, or acknowledgment of a mistake.
](https://emoji.discourse-cdn.com/google/saluting_face.png?v=14)

---
**Post ID:** 615988  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/300  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) in earlier evaluation of P1 in that my B1 is passed but in this final scores email it is showing as 0 for B1 pls help


![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/04980bbcf7941e08ba08f59e10a384708518a9eb.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/3/53a192933345964a58001aea8268e62a2e03e5f0_2_690x87.png)b1passed1109×141 12.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/3/53a192933345964a58001aea8268e62a2e03e5f0.png)

---
**Post ID:** 615991  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/301  

Request for Clarification on Zero Marks Given – Repository Was Public with All Required Files


Dear [@Carlton](/u/carlton) sir


I wanted to kindly request a clarification regarding the evaluation of my project submission. I noticed that I have been awarded zero marks, and I’m a bit confused because I had made sure that everything was in place.



My GitHub repository was public at the time of submission.
I had included the Dockerfile as required.
I also added the MIT License to the project.
For your reference, I am also attaching a snapshot of the repository as it was during the submission time.

Given all these were in place, I would really appreciate it if you could provide a concrete reason for giving zero marks. I’m eager to understand what went wrong so I can avoid it in the future and improve myself. But u saying in email that my repo was not public , not having dockerfile and not having mit licsence .


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/e/8e3c9683970a3d0b4da1305c4b85a634f235f437_2_690x369.png)emailsnapshotfor_discourse1785×957 130 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/e/8e3c9683970a3d0b4da1305c4b85a634f235f437.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a6a5cdd6a3ef7b88e3a82742621e730b10c68dd_2_690x362.png)repo_snapshotforDiscourse1842×968 84.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/a/6a6a5cdd6a3ef7b88e3a82742621e730b10c68dd.png)


please just check my repo  manually  and clarify whether it was public or not . What is going on this degree .

---
**Post ID:** 615993  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/302  

And also i ran the evaluate.py and got the 10/10 during submission , atleast you can give 4-5 by which i can pass this course .

---
**Post ID:** 615995  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/303  

Hi sir


I noticed a discrepancy in my Project 1 results. In the initial results shared on March 29th, I had received 8/20 based on the evaluation logs. However, the final result I received today states that none of the tasks in Task A and B were working, and I was awarded only 1 bonus mark.


During my own testing, I was consistently getting 7/10 correct in Task A, so I’m a bit confused about the change.


Kindly request you to look into this discrepancy sir


Thank you

---
**Post ID:** 615996  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/304  

Dear [@carlton](/u/carlton) Sir,


I was getting 8 marks in your evaluation but today I checked the mail, I was awarded 0 marks. I am not sure what happened. Everything was in place. I would really appreciate if you can provide a reason for zero marks. I rechecked everything and looks good. Awaiting your reply. Thanks.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/999d8f9a8df3be1555d6c16db66daa5d56bbed93.png)image452×132 6.53 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/999d8f9a8df3be1555d6c16db66daa5d56bbed93.png)

---
**Post ID:** 616004  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/305  

same i also got 8 marks but today in mail i got 0 marks

---
**Post ID:** 616008  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/306  

Same issue for me, I was getting 10/20 earlier and now, in mail it shows 1.

---
**Post ID:** 616011  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/307  

Same issue for me, i had got 4/20 before but in the mail, my marks is given as 0. Please help

---
**Post ID:** 616019  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/308  

Respected sir,


I have passed all pre-requisites however my file wasn’t evaluated due to port error (127.0.0.1). Please allow me rectify it as it everything else has passed and is in accordance to the guidelines and I had worked really hard for it not to be evaluated only.

---
**Post ID:** 616020  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/309  

Dear [@carlton](/u/carlton) Sir,


I’ve noticed discrepancies in my Project 1 results. During the tests I ran before submitting, I consistently got about 7/10 in Task A. In the results shared earlier, I was informed that my evaluation log file was missing. Later, a Gform regarding the architecture was sent, which I filled and submitted. Now, the final result I received today, shows that the taskA module is missing and I’ve been given a bonus of 1 mark.


I kindly request you to look into the matter and provide an explanation and solution in this regard.


Thank you.

---
**Post ID:** 616038  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/310  

Respected Sir,


I hope you’re all doing well. I’m writing regarding my Project 1 evaluation, as I’ve encountered a discrepancy that I’d like some help with.


According to the evaluation email I received, my score was 0 for all the tasks with an additional bonus of 1 (totaling a P1 score of 1). However, when I ran the provided evaluation script before my submission, I got 7 in Phase A. Additionally, after reviewing the Docker logs, evaluation logs, and the p1_evaluation_error_logs (from the linked Google Sheets), I couldn’t find any reference to my roll number.


Could someone please help me investigate this issue? I’d really appreciate any guidance from the evaluation team.


Thank you for your time and assistance!

---
**Post ID:** 616039  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/311  

[@carlton](/u/carlton) i am sure i had cleared 8/10 test cases in part A of the project despite rigrous checking and no error was found my be but still i have been alloted 0 in all the cases , this is no small issue as project holds a significant amount of weightage in the end term


I had spent hours finishing my project and this i am sure my marks are not on par with the desired work i did


Look into this matter as it signifies if i will be able yo pass tds in this term or not.

---
**Post ID:** 616040  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/312  

I am facing the exact same issue

---
**Post ID:** 616044  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/314  

Hi Hari,


I just manually checked your repo.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559_2_690x436.jpeg)Screenshot 2025-04-06 at 5.32.06 pm1504×952 62.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559.jpeg)


This is what you submitted:


2/15/2025 21:08:32


21f3002112@ds.study.iitm.ac.in


[https://github.com/harrypandey829/tds_llm_automation-agent](https://github.com/harrypandey829/tds_llm_automation-agent)


hariompandey6388/ll-automation-agent2


Kind regards

---
**Post ID:** 616051  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/315  

[@carlton](/u/carlton)  sir  When I submitted project 1, I was passing part A with 8/10 marks but today it is showing 0 marks on my email, but when I run it just now it is showing 4/10 on my vs code.


Whereas when I download the file from GitHub and run it, it is showing 1/10 now.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/d/9d7495b7d3d112adfac7d592ee6e9024351dc618_2_690x351.png)image1897×965 112 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/d/9d7495b7d3d112adfac7d592ee6e9024351dc618.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3fe91b246d5e0f0bf26245d8b4d0ab0d074827f5_2_666x500.jpeg)WhatsApp Image 2025-04-06 at 17.28.47_927a687b1600×1200 181 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/f/3fe91b246d5e0f0bf26245d8b4d0ab0d074827f5.jpeg)

---
**Post ID:** 616053  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316  

To replicate the test environment:


Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv.


`# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo
import argparse
import os
import zipfile

parser = argparse.ArgumentParser (description="Fetch the latest commit before a given deadline.")
parser.add_argument (
    "--owner",
    type=str,
    required=True,
    help="GitHub username."
)
parser.add_argument (
    "--repo",
    type=str,
    required=True,
    help="GitHub repository name."
)
parser.add_argument (
    "--save",
    type=str,
    default="../github/",
    help="Path to save the zip file. Default='../github/'"
)
parser.add_argument (
    "--extract",
    type=str,
    default="../github/",
    help="Path to extract the zip file. Default='../github/'"
)

args = parser.parse_args ()
owner = args.owner
repo = args.repo
save_path = args.save
extract_path = args.extract

deadline = dt.datetime (2025, 2, 18, tzinfo=zoneinfo.ZoneInfo("Asia/Kolkata"))
deadline_str = deadline.isoformat ()

github_headers = {
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "fetch_git_before",
}

url = f"https://api.github.com/repos/{owner}/{repo}/commits?until={deadline_str}&per_page=1&page=1"

try:
    response = requests.get (url, headers=github_headers, timeout=60)
    response.raise_for_status ()  # Raise an error for bad responses

    # Get the sha
    commits = response.json ()
    if commits:
        latest_sha = commits[0]["sha"]
        print (f"Latest commit before {deadline_str}: {latest_sha}")

        # Get the zip of the commit
        zip_url = f"https://api.github.com/repos/{owner}/{repo}/zipball/{latest_sha}"
        zip_response = requests.get (zip_url, headers=github_headers, timeout=60)
        zip_response.raise_for_status ()
        zip_filename = f"{latest_sha}.zip"

        # Create the directory if it doesn't exist
        os.makedirs (save_path, exist_ok=True)

        with open (save_path + zip_filename, "wb") as f:
            f.write (zip_response.content)
        print (f"Downloaded zip file: {zip_filename}")

        # Create the directory if it doesn't exist
        os.makedirs (extract_path, exist_ok=True)

        # Extract the zip file
        with zipfile.ZipFile (extract_path + zip_filename, "r") as zip_ref:
            zip_ref.extractall (extract_path)
        print (f"Extracted zip file to: {extract_path}")

    else:
        print (f"No commits found before {deadline_str}")

except:
    print(f"Error fetching commits: {response.status_code} - {response.text}")`
Pass the required arguments to the above application and it will find the latest commit before the 18th, fetch it and unzip it to the folder you specified. Please use the appropriate arguments as specified in the application.


`docker build -t <your image name>   .`


Run new docker image using


`docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 <your image name>`


Keep datagen.py and evaluate.py in same folder


`uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000`


This then re-produces the exact environment how your application was  tested.


You have to provide a token from your environment for testing.


These instructions are same for everyone. So check first before posting here.

---
**Post ID:** 616054  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/317  

I am also facing same issue cleared 8/10 test cases in part A of the project despite rigrous checking and no error was found  but still i have been alloted 0 in all the cases

---
**Post ID:** 616058  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/318  

[@Arunvembu](/u/arunvembu) [@22f2000008](/u/22f2000008) [@23f1000879](/u/23f1000879) [@22f3003201](/u/22f3003201) [@23f2000926](/u/23f2000926) [@22f3001702](/u/22f3001702) [@Santoshsharma](/u/santoshsharma) [@kartikay1](/u/kartikay1) [@Kasif](/u/kasif)


Check first by following the instructions show here:




![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)


    To replicate the test environment: 
git clone <your repo url> 
cd <your repo directory> 
docker build -t <your image name> 
Run new docker image using 
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 <your image name> 
Keep datagen.py and evaluate.py in same folder 
uv run evaluate.py --email=<any email> --token_counter 1 --external_port 8000 
This then re-produces the exact environment how your application was  tested. 
You have to provide a token from your environment for testing. 
The…
  

Then post with your queries after testing as mentioned above.


Also check the evaluation logs first to see why it failed. Address that question.


Posting “it ran before submission” is insufficient evidence.


The whole point of deployability is that it runs anywhere at anytime.


That is what is being tested, not that it ran on your machine (unless you replicate the test environment exactly).


Kind regards

---
**Post ID:** 616063  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/319  

But in email u said n , your repo was not public, even not had dockerfile nor mit licence that’s what I mentioned.

---
**Post ID:** 616066  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/320  

Your repo is not public! Thats why we cannot see any other files either. If its not public we cannot see if other files exist. We cannot evaluate an invisible repo.

---
**Post ID:** 616067  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/321  

I got email , your repo was not public even had not a dockerfile nor mit licence, that’ what I mentioned.

---
**Post ID:** 616068  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/322  

My repo is public even before it was. How can I set to public..thisis same n while creating new repo u just select the public and not private that’s it n.

---
**Post ID:** 616069  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/323  

What else I can do . For public.

---
**Post ID:** 616072  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/324  

You misspelt your repo. Did you even check the post i sent with your details?





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/314) [Tools in Data Science](/c/courses/tds-kb/34)


    Hi Hari, 
I just manually checked your repo. 
 [[Screenshot 2025-04-06 at 5.32.06 pm]](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559.jpeg) 
This is what you submitted: 

2/15/2025 21:08:32 
21f3002112@ds.study.iitm.ac.in 
[https://github.com/harrypandey829/tds_llm_automation-agent](https://github.com/harrypandey829/tds_llm_automation-agent) 
hariompandey6388/ll-automation-agent2 
Kind regards

---
**Post ID:** 616075  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/325  

Dear [@Jivraj](/u/jivraj) [@carlton](/u/carlton) Sir,


I run evalution  script that you provide us via mail recently, my code is actively running and able to pass 11 task but I was awarded 1 Marks pls check where is the issue,[My full code was done in linux Environment]  (github codespace)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/2/42c024fb5f0088b9a033625cd6e7338bba0c22f2_2_690x170.png)image1380×341 63.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/2/42c024fb5f0088b9a033625cd6e7338bba0c22f2.png)

---
**Post ID:** 616077  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/326  

You have to replicate this test environment for testing.





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)


    To replicate the test environment: 
git clone <your repo url> 
cd <your repo directory> 
docker build -t <your image name> 
Run new docker image using 
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 <your image name> 
Keep datagen.py and evaluate.py in same folder 
uv run evaluate.py --email=<any email> --token_counter 1 --external_port 8000 
This then re-produces the exact environment how your application was  tested. 
You have to provide a token from your environment for testing. 
The…
  

Please replicate this first. We also run it on a linux server.


Kind regards

---
**Post ID:** 616078  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/327  

I am not talking about this , just see the snapshot that I applied above on that email u said your repo is not public

---
**Post ID:** 616081  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/328  

We are ONLY going to evaluate what you submitted. Its the same rule for everyone. If the repo you provided is not accessible,  you will not be evaluated.

---
**Post ID:** 616083  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/329  

Okay tell me one thing if I got fail in this course then in the next term, I will have not to give roe because it’s rule for every other courses.And see provide the content of tds in Indian guy youtuber because we belong to rural areas and not able to understand the accent of foreigners youtuber . It’s kind your sympathy.

---
**Post ID:** 616101  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/330  

Things i have done for my project to work locally:





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

`git clone <your repo url>`




cloned my repo which looked like this after cloning(ignore those green dots)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/517fe247c71c06f80741f22983662ba012749382.png)image274×118 2.87 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/517fe247c71c06f80741f22983662ba012749382.png)


All the files are  in this folder (I wasn’t aware that we cannot have the subfolder in the root directory,I shouldn’t get penalized for this) and added the datagen and evaluate.py file.





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

Keep datagen.py and evaluate.py in same folder




when i do this( ![That's a light blue square button with a prominent white downward-pointing arrow.  It's a common graphical user interface (GUI) element signifying a download or scroll-down function.
](https://emoji.discourse-cdn.com/google/down_arrow.png?v=14)) i get this error





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

`docker build -t <your image name>`




`PS D:\TDS_Project_1\tds-project-1> docker build -t "tushar2k5/tds-project-1"                                                                 
ERROR: "docker buildx build" requires exactly 1 argument.
See 'docker buildx build --help'.

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Start a build`
Instead,in order to run the docker image successfully  we have to do either of the two things(taken help from chatgpt ![Image description failed](https://emoji.discourse-cdn.com/google/upside_down_face.png?v=14)):


1)


`Use full path (recommended if you're outside the project folder):

docker build -t tushar2k5/tds-project-1 D:\TDS_Project_1\tds-project-1`
OR


2)


`Add a dot (.) at the end to specify the current directory as the build context:

docker build -t tushar2k5/tds-project-1 .`
Both the things work for me(![That's a light blue square button with a white upward-pointing arrow in the center.  It's a common graphical user interface (GUI) element indicating an upward action, such as scrolling up or going to a previous level/menu.
](https://emoji.discourse-cdn.com/google/up_arrow.png?v=14))





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

`docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 <your image name>`




`docker run -e AIPROXY_TOKEN=i.am.still.noob.inTDS -p 8000:8000 tushar2k5/tds-project-1`
Done this(can’t leak my token,already many students stolen it from my project-2🤦‍♂️)





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

`uv run evaluate.py --email=<any email> --token_counter 1 --external_port 8000`




`uv run evaluate.py --email=23f2003751@ds.study.iitm.ac.in --token_counter 1 --external_port 8000`
Done this to evaluate my project


Any finally the main part (DRUM ROLLS ![That's a simple cartoon illustration of a red snare drum with two drumsticks resting on top.
](https://emoji.discourse-cdn.com/google/drum.png?v=14),not this one ![Image description failed](https://emoji.discourse-cdn.com/google/oil_drum.png?v=14) (IUKUK))


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fc6fad6517b25106749f3c9c504cf38cc72bed3c.png)image1462×305 14.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fc6fad6517b25106749f3c9c504cf38cc72bed3c.png)


THATS 6/25


Currently I’m getting a big 0 beacause the github doen’t contain the dockerfile(which it does clearly)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/5/55f769f57bb4a5678a20b414877b8f2dee2d7e5d.png)image686×141 5.46 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/5/55f769f57bb4a5678a20b414877b8f2dee2d7e5d.png)


Hopping to get a response from you guys,


Thanks a lot(wrote this much for first time for any course)


(PS:This course has some special place in my heart ![Image description failed](https://emoji.discourse-cdn.com/google/heart.png?v=14))


[@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---
**Post ID:** 616103  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/331  

We fetched your latest github commit before 18th Feb and build image through that and evaluated.


Your latest github repo before 18 has:


username : `singh-yash129`


Repo : `Large-Language-Model`


commit_sha: `88f7439471151283f1218b46d209030dd7f4e5ae`


Use `https://github.com/<username>/<repo>/archive/<commit_sha>.zip` for downloading repo.


If You feel there is any problem with our evaluation script suggest edits to the scirpt.

---
**Post ID:** 616107  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/332  

![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2003751/48/68010_2.png) 23f2003751:

Currently I’m getting a big 0 beacause the github doen’t contain the dockerfile(which it does clearly




Dockerfile has to be inside root of any github repo, this is standard and we had discussion with Professor Anand about such cases where it’s not part of root directory, he suggested we will consider only Dockerfile being present in root folder of the repo.

---
**Post ID:** 616117  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/333  

![Image could not be processed](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png) Jivraj:

Dockerfile has to be inside root of any github repo, this is standard and we had discussion with Professor Anand about such cases where it’s not part of root directory, he suggested we will consider only Dockerfile being present in root folder of the repo.




Sorry but its not possible to attend every single session and you guys haven’t informed us via email so how its our fault.For cases like this you guys should allow us to move our files to the root directory so it can work…(we just have to move files  in the repo please consider it)[@carlton](/u/carlton) [@Saransh_Saini](/u/saransh_saini) [@s.anand](/u/s.anand)


(i have already made a rookie mistake in my dockerfile otherwise i would have got 9/25 but keeping that aside please let me get 6/25)


![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/1/41dc27831c97af2f02287cec795a281e9672723d.gif) ![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/e/3e588079c65a2f9979f97bb5f1d81e3c1691ab20.gif)

---
**Post ID:** 616125  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/335  

Good evening sir.


My original project evaluation conducted by IITM gave me 7/20, however the new evaluation gave me 0/20.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/c/cc8129304f5afb06949f9302d76a9676ce4dea17_2_361x500.png)image650×898 106 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/c/cc8129304f5afb06949f9302d76a9676ce4dea17.png)


This was from the official evaluation sir, could you kindly look into it.

---
**Post ID:** 616128  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/336  

did everything as mentioned i got 7/25 but in mail i got 2 which is bonus?


i know i didn’t add flask in docker it was my mistake ![Image description failed](https://emoji.discourse-cdn.com/google/frowning.png?v=14) but can we just for once neglect that. pleaseeeeeeeee


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/9/09a6d31fb7df32c7cd6ef945bb25dfce03707a15.png)image787×249 8.87 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/9/09a6d31fb7df32c7cd6ef945bb25dfce03707a15.png)

---
**Post ID:** 616129  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/337  

Please do consider allowing us to change the position of the dockerfile to the root. We are doing nothing but changing its location in the repo. This was not mentioned anywhere in the prerequisites before the submission and it is unfair to not consider all our work for a criteria that was nowhere mentioned in the course page before the submissions. It may be standard practice but a lot of us were unaware. Please do consider this request.

---
**Post ID:** 616130  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/338  

Sir, could you please fetch my latest GitHub commit before 18th Feb and build the image through that one?


I received a mail saying that the Docker image is not accessible, but it is already there. Kindly request you to evaluate my submission.

---
**Post ID:** 616133  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/339  

Hi [@Abhay222](/u/abhay222)


Docker image submitted by you doesn’t exists.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/6/f633d628d646e068273aef8682b5405527cabb65_2_690x342.png)image1902×943 93.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/6/f633d628d646e068273aef8682b5405527cabb65.png)

---
**Post ID:** 616135  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/340  

Hi [@23f1000879](/u/23f1000879)


This basically tells you didn’t validate docker Dockerfile and docker image by building and running them, otherwise you would have corrected the mistake.

---
**Post ID:** 616136  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/341  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_690x93.png)Screenshot 2025-04-02 1322141843×250 18.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1.png)


but it is available under version1.

---
**Post ID:** 616140  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/342  

repo that you submitted through google form was different then this one.


Your Gform response


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8aee4e76f9cd47c8bc2e24137881ea41f00a37f_2_690x100.png)image1660×242 21.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b8aee4e76f9cd47c8bc2e24137881ea41f00a37f.png)

---
**Post ID:** 616141  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/343  

Hi, I work in the IT industry. There is no standard like “docker file has to be only in the root folder.”


If at all you are setting a requirement why was this not mentioned in the project page?


We were asked to build an app which solves the given tasks. You were OK for whatever code/tools/method to use as long as it works, there the “industry standard” didn’t show up ironically!!!


Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.


In the same industry that I work - we build the dockers and give it for prod push.

---
**Post ID:** 616146  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/344  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Dear Sir,


I got log with error as /bin/sh: 1: [/root/.local/bin/uv,: not found.


I debugged that I had a small issue in the dockerfile that was submitted and it is


CMD [“/root/.local/bin/uv”, “run”, “app.py”]  has an invisible Unicode non-breaking space (`U+00A0`) between `"run", "app.py"` instead of a regular space. This causes the shell to misread the command.


I know it’s very late for the submission to reconsider, but this small mistake spoiled my hard earned project which got local score 8/25 which could finally get converted to 12 marks. I made this change and pushed it to docker and github repository. Considering this, I request you to please evaluate my submission if possible, because I don’t want to lose the marks which i tried my level best to score. I already have good score in GA’s and ROE.  Expecting a positive response from your end.

---
**Post ID:** 616150  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/345  

sir, but before submission i run evluate.py and it gave me 8/10 in task A. after submission i also got result mail stating that i got 8/20.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/6/6689843088265aa67624484279c35e788ed5d74c_2_690x341.png)image1895×938 90 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/6/6689843088265aa67624484279c35e788ed5d74c.png)


also this mail result Earlier i got From your side. ![Image description failed](https://emoji.discourse-cdn.com/google/frowning.png?v=14)

---
**Post ID:** 616151  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/346  

Sir, I realized that I mistakenly submitted the image tag `"abhay227/version1"` instead of the correct image ID. The correct image ID is `4db729a03f74`, which is part of version1 and is already present and publicly available.


Unfortunately, I didn’t receive any notification about this issue after submission. Receiving this mail at this stage feels disheartening after all the effort I’ve put into the project.  I kindly request you please consider this correct image ID.

---
**Post ID:** 616154  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/347  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/b/fbbc7606d11dda4948aceedc2d598b7f3f4b96b5.png)Screenshot 2025-04-06 202736662×141 5.41 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/b/fbbc7606d11dda4948aceedc2d598b7f3f4b96b5.png)


Hi, all my pre-requisites have been fulfilled, and the evaluation logs say I have a score of 10/25. But I have gotten a score of 0, saying ‘Task A module missing’. This is a kind request to confirm the scores.

---
**Post ID:** 616155  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/348  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/9/695ad6dd9f35a4590a41863def948b9903941388_2_690x282.png)image1915×783 79.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/695ad6dd9f35a4590a41863def948b9903941388.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/e/ae524c05420e98ff1b2b00c89337a31ec8a34a7e_2_690x236.png)image1912×654 36.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/e/ae524c05420e98ff1b2b00c89337a31ec8a34a7e.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0adbce8db00985ca07a8ad9347c9cb9559139dda_2_690x240.png)image1899×663 32.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0adbce8db00985ca07a8ad9347c9cb9559139dda.png)


I cannot find my docker_logs nor evaluation_logs and nor anything on the forms . The mail I got says that i received 0 in project tasks but clearly my project is not evaluated. Please look into this. during earlier evaluation i got 7 marks but this time it is 0.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/ef7afffc65533ff5136a0ae3532470957d66bb1b_2_690x386.png)image1455×814 38 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/f/ef7afffc65533ff5136a0ae3532470957d66bb1b.png)


My roll number is 23f1001524 .

---
**Post ID:** 616156  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/349  

[@carlton](/u/carlton) and [@Jivraj](/u/jivraj) , for Task A i had tested before and all the test cases passed, but all my A tasks has failed with 0, In the evaluation logs, i could see that all task A tests failed due to datagen.py not available.


Could you rerun the test ?

---
**Post ID:** 616168  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/350  

Respected Sir,


Thank you for your response and for providing the steps to replicate the test environment.


Steps Taken to Replicate the Test Environment


I cloned my repository using:


`bash
git clone <my_repo_url>
cd <my_repo_directory>
I built the Docker image using:

bash
docker build -t.
I ran the Docker container with:

bash
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000

I ensured that datagen.py and evaluate.py were placed in the same folder as instructed.

Finally, I ran the evaluation script using:

bash
uvicorn evaluate.py --email=<any_email> --token_counter 1 --external_port 8000`
Issue with Original Submission


After reviewing the evaluation logs, I identified that the issue with my original submission was caused by binary incompatibility between pandas (version 2.0.3) and NumPy (version 1.24.3). These versions worked perfectly during development on my local machine and were tested multiple times across both Linux and Windows platforms before submission. Even after pulling the submitted Docker image from Docker Hub post-submission, it worked without any issues locally.


However, during your evaluation, this incompatibility caused the container to fail.


I acknowledge this issue, have fixed it in my updated submission, and previously conveyed this in my earlier message.


Action Taken


To address this issue, I made a small adjustment to my requirements.txt file to explicitly fix these versions for compatibility across all environments. This was the only change made to my submission. After rebuilding the container with this updated file, I tested it again thoroughly in your replicated test environment, and it worked as expected:


The application initializes correctly on port 8000 within 5 minutes.


It responds to requests within the required timeframe.


I have pushed this updated image to Docker Hub under the same repository:


Docker Hub URL: santoshsharma003/tds-project-one-1:latest


Request for Re-Evaluation


I kindly request that you pull the latest version of my Docker image from Docker Hub and re-run the evaluation process. I understand that deployability is being tested, and I have taken every necessary step to ensure that my submission now works in any environment, including replicating your test setup exactly.


Previous Message for Reference


For your convenience, here is my earlier message explaining this issue in detail:


"Greetings, Sir,


I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between pandas and numpy caused the container to fail. To my surprise, the same versions (pandas==2.0.3 and numpy==1.24.3) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.


To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.


I’ve pushed the updated image to Docker Hub (santoshsharma003/tds-project-one-1:latest). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.


Thank you for your assistance!"

---
**Post ID:** 616189  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/351  

same for me


my roll number is 23f1003094

---
**Post ID:** 616191  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/352  

Same with me sir [@carlton](/u/carlton)

---
**Post ID:** 616193  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/353  

There are no evaluation logs for you, I am not sure which evaluation log you are referring to. Your docker image fails to run the required task because your Dockerfile is misconfigured. Did you follow the test environment setup mentioned in this post before posting your query?





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)


    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …
  

Because if you did, you will realise why your evaluation failed.


You must replicate the test environment and then if you submission works, you have a legitimate appeal. Otherwise we will not consider it. Please replicate the issue using the test environment as detailed in the post link.


Kind regards

---
**Post ID:** 616195  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354  

You can take it up with [@s.anand](/u/s.anand)


I did not come up with the standard.


And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files.



Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.



Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand if we could make the allowance. He made the decision to enforce this protocol.


Kindest regards.

---
**Post ID:** 616197  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/355  

[@carlton](/u/carlton)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/f/2fa3b5ca794441978a80d9d1c4e4c850eb67304c_2_690x348.png)image1892×955 130 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/f/2fa3b5ca794441978a80d9d1c4e4c850eb67304c.png)


Respected Sir,


see the above image its from the scores we got from mail just before the latest one, in that I had got 7/20 and now new mail shows I got 0?? how is this possible…


the link for evaluation in which i got 7/20 is : [23f2001390@ds.study.iitm.ac.in_evaluation.log - Google Drive](https://drive.google.com/file/d/1cNVy9KSfSITZg_KGLF2_wwLWjzNl8mb5/view)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/f/afbded56c295f1e2ff28878559e430ba3ed8244e_2_690x384.png)image1315×732 45.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/f/afbded56c295f1e2ff28878559e430ba3ed8244e.png)


MOST importantly mail shows :


Your final t score calculation is based on


MIN (20, (task score + bonus))


Github repo submitted: [GitHub - 23f2001390/llmagent](https://github.com/23f2001390/llmagent)


Docker repo submitted: 23f2001390/llmagent


Pre-requisites check: (1 for pass, 0 for fail)


Docker repo exists and is public (should have a timestamp before 18th of Feb): 1


Github repo exists and is public (should have a timestamp before 18th of Feb): 1


Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1


Gihub repo check - Dockerfile exists: 1


Your task score is: 0


Your bonus is: 1


Your P1 score is: 1



So according to the above, I passed the pre-requisites and also in mail u have mentioned that:


We have attached the docker logs and the evaluation logs for everyone who passed the pre-requisites.


but I don’t find my mail id or roll number in the docker_logs.zip or evaluation_logs.zip  that has been given in the mail(latest), if I passed the pre requisites my logs should be there in the zip files included in this latest mail right, my roll number is 23f2001390 and email id is 23f2001390@ds.study.iitm.ac.in


and nor do i find my id in the p1_evaluation_error_logs so please help sir


Thank you


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/1/41513a69b4af93110ad5c7a3717fca9f0fecd63b_2_690x327.png)image1078×511 8.14 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/1/41513a69b4af93110ad5c7a3717fca9f0fecd63b.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/6/d694d88bee053086a294de30c7566ea08dbbf9c0_2_690x336.png)image1083×528 8.42 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/6/d694d88bee053086a294de30c7566ea08dbbf9c0.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c2b0b8d98d14050bb8021568b7a3ac7101c7e4df_2_690x351.png)image1905×970 78.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/2/c2b0b8d98d14050bb8021568b7a3ac7101c7e4df.png)

---
**Post ID:** 616203  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/356  

[@carlton](/u/carlton)


Same for sir. I have made my post similarly, roll number is 23f2001390 and email is 23f2001390@ds.study.iitm.ac.in

---
**Post ID:** 616205  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/357  

[@carlton](/u/carlton)


i  also not found anything in this form  , but i got mail to score=0


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/e/9e2ca0680b13a927d524fe5883919c8447d0f8e3_2_690x305.png)image1893×837 85.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/e/9e2ca0680b13a927d524fe5883919c8447d0f8e3.png) ![That's a yellow emoticon/emoji with a small smile and a single blue tear rolling down its cheek.  It depicts a bittersweet or slightly sad feeling.
](https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=14)

---
**Post ID:** 616206  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/358  

Hi Hari,


Your docker failed to build.


Did you try to replicate the test environment as mentioned in





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)


    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …
  

If you tried you would find that it will not build. Thats why you have no logs.


90 such cases are there where the image could not be built from your repo.


The specific error in your case is:


tried copying requirements.txt which doesn’t exists


Thats why there are no logs.


Kind regards

---
**Post ID:** 616212  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/359  

Hello [@carlton](/u/carlton) Sir, please reply to my query

---
**Post ID:** 616213  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/360  

We cannot allow changes to repos. This is a blanket rule for everyone. No exceptions. Since the only way to get your project to work is to make changes to it, we cannot score you for changes.


Kind regards

---
**Post ID:** 616214  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/361  

Thanks for the response. We can go on endless discussions using “nice words” “professionally” with the number of questions we have. Finally we are at the receiving end as students in this setup.


What’s the take away for everyone? Let’s move on. This isn’t the end.


Positive or Negative - Real world outside will make everyone realise and everyone change their opinions (including me) as the time and environment changes.

---
**Post ID:** 616233  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/362  

What I observed is that most of the repositories appear to be copied from a single source. This original repository contains several issues, such as an incorrectly named Dockerfile and missing instructions to copy all necessary data. Unfortunately, many students seem to have uploaded it blindly without reviewing or fixing these problems.

---
**Post ID:** 616239  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/363  

Hi I have my Dockerfile saved as dockerfile, given 0 for project 1 due to this. This doesn’t seem to be a big issue to grade me 0 for this. Kindly correct the score please.

---
**Post ID:** 616305  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/364  

Most common reason for during running docker image was `taskA module was missing` which is because a lot of students blindly copied from someone with building and running image, if they would have done that they could have corrected it at early stage.

---
**Post ID:** 616311  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/365  

For you check failed because of the naming of Dockerfile(It was named as dockerfile(d in small).

---
**Post ID:** 616312  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/366  

This is error that you got while building docker image using docker file in your github repo tried copying requirements.txt which doesn’t exists


In your Dockerfile you are trying to copy requirements.txt but it doesn’t exists in the directory where Dockerfile is located

---
**Post ID:** 616314  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/367  

![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/mitali_r/48/66886_2.png) MITALI_R:

23f1003094




While running docker image create by your github repo, we got following error `taskA module missing`


For regenerating it follow steps that are mentioned here : [Tds-official-Project1-discrepencies - #316](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---
**Post ID:** 616316  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/368  

For you naming of MIT License was not correct.


This shows naming criteria for adding License.


[Adding a license to a repository - GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)

---
**Post ID:** 616318  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/369  

Sir actually my project doesn’t have requirements.txt, instead it installs automatically


when:


`uv run app.py` is run and for docker image it installs while building and I had submitted the docker image with all libraries required(the dockerfile below, in that it installs while building).


my dockerfile from the repo:


`FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn requests python-dateutil pandas db-sqlite3 scipy pybase64 python-dotenv httpx markdown duckdb faker pillow

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app
# Copy application files
COPY *.py /app/
COPY .env /app/

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]`
here u can see it installs using pip install …


here it’s requiring `.env` file to be present in the project folder because my project when I was uploading to both git and docker had `.env` file for AIPROXY_TOKEN and I uploaded to docker with that `.env` file but as git doesn’t allow upload of `.env` file I couldn’t upload`.env` to git


the project will still work after downloading the repository when we upload AIPROXY_TOKEN as environment variable but to again build the docker image for replicating the test environment, my docker image could not be built because`.env` file doesn’t upload to GIT, so when I downloaded the repository from the above method, it didn’t have the `.env` file so it didn’t build so I had to create the `.env` file now to create the docker image, and for the dockerimage I had submitted, I built it with the `.env` file(it supports both`.env` file and environment variable one)

---
**Post ID:** 616319  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/370  

After filling form you didn’t double check form.





![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/abhay222/48/66780_2.png) Abhay222:

I kindly request you please consider this correct image ID.




We can’t reconsider it.

---
**Post ID:** 616323  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/371  

Yes problem was missing `.env` file, Your repo, was supposed to run in a test environment.

---
**Post ID:** 616325  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/373  

Yes sir, please help me

---
**Post ID:** 616326  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/374  

Sorry We can’t do any help, we won’t be considering for eval.

---
**Post ID:** 616328  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/375  

But sir, It was supposed to run right…

---
**Post ID:** 616329  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/376  

It Should build in any test environment using Dockerfile from your github repo.

---
**Post ID:** 616330  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/377  

[@Jivraj](/u/jivraj) please tell me what was my mistake?

---
**Post ID:** 616332  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/378  

It was named wrongly.


You named it LICENCE but it should be LICENSE or LICENSE.md.

---
**Post ID:** 616338  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/379  

But sir, just because the repository doesn’t have .env file it couldn’t build the dockerimage, the docker image will build in any test environment as u said but it requires the .env to be included which the git didn’t have(it doesn’t allow upload of it ofcourse), don’t rerun the evaluation again but please sir atleast give me those 7/20 marks along with the pre-requisite bonus(1mark) that was mailed earlier to me along with logs…this is my primary degree after 12th, I’m also not asking any extra marks just the marks that i got earlier:


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/6/16d50a2f5466ad8d9ed068b4af93899fe3295a4e_2_690x380.png)image1850×1021 132 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/6/16d50a2f5466ad8d9ed068b4af93899fe3295a4e.png)

---
**Post ID:** 616340  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/380  

Hi [@23f2002600](/u/23f2002600) [@21f1005908](/u/21f1005908)





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354) [Tools in Data Science](/c/courses/tds-kb/34)


    You can take it up with [@s.anand](/u/s.anand) 
I did not come up with the standard. 
And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files. 

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in. 

Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand i…

---
**Post ID:** 616341  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/381  

Runned for you, it A1 Fails.

---
**Post ID:** 616342  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/382  

Your docker image and github repo are not consistent,  your docker image was not built with the latest code before 18th feb that’s present in your github repo.

---
**Post ID:** 616343  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/383  

We can’t consider any changes after deadline.

---
**Post ID:** 616344  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/384  

Your docker image and github repo are not consistent.


While running docker image we got following error: `flask module missing`


For regenerating this error follow steps mentioned in below post.




![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)


    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …

---
**Post ID:** 616345  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/385  

Anything after deadline we can’t consider any changes, it was just a matter of time, you didn’t tests running evaluate.py on docker container that was created, otherwise you would have spotted this mistake and rectified it.

---
**Post ID:** 616346  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/386  

In your github repo, Dockerfile should be named as Dockerfile(D caps).

---
**Post ID:** 616347  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/387  

I don’t know reason behind it, earlier evaluation was done by pulling docker image.


Latest one was done through github repo, if code in github repo is not consistent with docker image it might cause problems.


LLM won’t provide same results every time, for that reason we have give bonus marks.

---
**Post ID:** 616354  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/389  

[@carlton](/u/carlton) [@jivraj](/u/jivraj) sir it is my humble request to do something. We are losing our marks because of small negligence or mistakes like i fogot to commit my requirements.txt in my github repository. Already the course has taken tolls on our mind. Please give partial marks for the correct run of the docker image or please evaluate my latest commit with the requirements.txt. Because of this project I will lose my cgpa and the hardwork that I have done till this term. A small mistake is causing me my full marks and grades. Atleast consider partial marking for the docker image which does the tasks. I have maintained 9+ cgpa in the diploma and I took other subjects which are easy this term like BDM still is really difficult to cope with the subject. Please consider something. atleast give 50% of the marks for each task which my image passes.

---
**Post ID:** 616355  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/390  

Sir but i did test my project via evaluate.py and got the 8/10 in my tasks A. A simple port error has resulted in no evaluation at all after all the hardwork.

---
**Post ID:** 616361  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/391  

Sir, how my git repo is not consistent i used the same repo which i have given you in the form even i did not commit any changes after 18th feb also in my docker file there is just a simple mistake that i forgot to add flask dependency just because of that mistake i am losing my marks. I also used same docker image which i have given you through form. Its my humble request please consider or give some solution. It felt like betrayal because we put effort’s.

---
**Post ID:** 616388  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/392  

Dear Sir,


I understand that this request is coming at a late stage, and I truly apologize for the timing. However, I felt it was important to express how much effort and dedication I have invested in this project and throughout the course. The recent issue has been disheartening for me, especially because the work I submitted was not a blind copy from someone else.


Had it been otherwise, I wouldn’t have had the courage to reach out. I genuinely care about this course and the learning it offers, and I’m proud of the commitment I’ve shown so far.


With utmost respect, I kindly request you to reconsider evaluating my project again, if there’s any possible way to do so. It would mean a lot to me and would really motivate me to keep pushing forward in this subject.

---
**Post ID:** 616396  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/393  

Hi [@23f1001524](/u/23f1001524) [@afsalshah](/u/afsalshah) [@23f1000879](/u/23f1000879) [@23f1002056](/u/23f1002056)


I understand your situation. We discussed all these scenarios in our weekly meets, and it was decided that we cannot make allowances for these because there was ample time to test your deployments and also ample sessions were conducted to address any difficulties you might have faced. A basic minimum standard was expected and we are unable to relax that threshold because then it would make evaluations meaningless.


We are not just evaluating on your agent functions. We require deployability as a minimum target. If you solution was not deployable and functional then we cannot evaluate the functioning of your application. Once again I sympathise with what might seem minor errors. But they are not minor, even though it may only be a line that needs changing or a spelling mistake. They actually cause a critical failure.


A minor mistake is a function not working that does not prevent other things from working.


Critical failures prevents everything else from working and thus most of these what seems like minor failures are missclassified. They are in fact critical failures.


I know its not of much comfort right now, but the learnings from this will be important going forward in your career.


Kindest regards

---
**Post ID:** 616428  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/394  

Hi [@carlton](/u/carlton) ,


I couldn’t find my Docker logs or evaluation logs in the latest result mail, even though I had passed the prerequisites. I also tried reproducing the test environment and scored 9/25 (screenshot attached below).


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fd1e9ebbdaabe4f7e853a25f71f645bd06fd0f01.png)image1124×268 9.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fd1e9ebbdaabe4f7e853a25f71f645bd06fd0f01.png)


Would really appreciate it if you could take a look. Thanks in advance!

---
**Post ID:** 616429  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/395  

Did you follow these instructions when building the test environment? Our logs indicated that this was the problem:


tried copying multiple files for that you need to give directory name and it should end with a /





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)


    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …

---
**Post ID:** 616431  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/396  

[@carlton](/u/carlton)  , I followed all the steps instead of `curl -LO https://github.com/<username>/<repo>/archive/<commit_sha>.zip`


`unzip <path to downloaded zipped repo>` , I used git clone .

---
**Post ID:** 616433  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/397  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Not able to see the my id in 22f3002723 in evaluation logs or docker logs.. just curious if there was  any issues in creating the image out of github ?

---
**Post ID:** 616476  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/398  

Thanks for the fixes (I have updated the code now). It was put together quickly and not tested before we actually posted it.

---
**Post ID:** 616480  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/399  

Happy to help sir ![That's an emoji of a yellow face with a hand saluting it.  It often conveys a sense of resignation, defeat, or acknowledgment of a mistake.
](https://emoji.discourse-cdn.com/google/saluting_face.png?v=14)


(Was expecting some different response from your side,but ig we need to accept our faith ![Image description failed](https://emoji.discourse-cdn.com/google/upside_down_face.png?v=14))


Thank you,


(Kindest regards)


Tushar

---
**Post ID:** 616486  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/400  

We are checking you submission. We will get in touch shortly.

---
**Post ID:** 616511  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/401  

[@carlton](/u/carlton) [@jivraj](/u/jivraj) [@s.anand](/u/s.anand),


I hope you’re doing well. I wanted to humbly request a reconsideration regarding the evaluation of my project submission.


I understand there was an issue with building the Docker image from the repository. However, I had successfully built and pushed the Docker image earlier, and I believe it demonstrates that my solution is deployable. If the final evaluation was solely based on building from the repository, I’m a bit confused about why the Docker image was considered earlier and why we were also asked to upload it to Docker Hub if it wasn’t going to be taken into account later. Also the earlier evaluation score where we got some marks at least and now are hopes are crushed after one night.


I do realize that in the real world, these kinds of errors can be critical, and I truly appreciate that the course is structured to prepare us for such expectations. That said, this course has been quite challenging, and for many students—including myself—it has been a source of considerable stress and demotivation.


I sincerely request that you kindly consider awarding some partial marks for the working Docker image that was built and pushed earlier. It does reflect an understanding of deployable solutions, which I’ve worked hard to demonstrate.


I know you all have our best interests in mind, and I’m grateful for the efforts put into making this a rigorous and enriching course. My only concern is that such harsh penalties—especially for a single oversight—can significantly affect our CGPA and future opportunities. I hope my request can be considered with empathy.


Thank you for your time and understanding.

---
**Post ID:** 616519  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/402  

Issues with your submission has been resolved.


Thanks for raising the issue and checking it at your end.

---
**Post ID:** 616523  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/403  

Sir, I sincerely apologize for the mistake I made in naming the LICENSE file as “LIcense” instead of “LICENSE”. I now understand how important these details are, and it was an unintentional oversight on my part. I had put in a lot of hard work into the project, and it would mean a lot to me if you could kindly consider evaluating it, even though the deadline has passed and results are out. I completely understand if it’s not possible, but I just wanted to request a chance as this project was very important to me and I genuinely learned a lot from it.


[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---
**Post ID:** 616532  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/404  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/440f4cd9014c4875f88e79b411d5dea05fcd83ec.png)image1188×699 38.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/440f4cd9014c4875f88e79b411d5dea05fcd83ec.png)


cloned the repository using


`git clone https://github.com/23f2001390/llmagent.git`
[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/e/0e58db81179e18b5c2b4bd7d75bee3f549d8dac0.png)image1041×721 29.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/e/0e58db81179e18b5c2b4bd7d75bee3f549d8dac0.png)


created the `.env` for the aiproxy token as its needed to build the docker image as per my Dockerfile and `.env` file cannot be uploaded to git we have to create it while building docker image


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/4/7451ed8873f25e16cf269a59e4ba5daeba424dc2_2_378x499.png)evalue752×994 45.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/7451ed8873f25e16cf269a59e4ba5daeba424dc2.png)


added the new `evaluate.py` and `datagen.py` from the mail, trying to replicate the test environment


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/5/05986eb39e4662742a5fb924ef4199e6b95f37ae.png)image730×462 21.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/5/05986eb39e4662742a5fb924ef4199e6b95f37ae.png)


moved the new `datagen.py` and `evaluate.py` into the project folder


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a5f2b89e834352615300dcbbc2b2d74749da8e2e_2_690x378.png)image1805×989 79.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/5/a5f2b89e834352615300dcbbc2b2d74749da8e2e.png)


docker image built successfully using


`docker build -t llm-agent .`
[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/f/5f6ef64ca044db4f86e841615328f2f0015d6df1_2_690x396.png)image1694×974 55.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f6ef64ca044db4f86e841615328f2f0015d6df1.png)


running the evaluate.py using:


`uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000`
[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/b/6be8a8566f8f3f47a1f052f039130fabd6193c5b.png)image1385×971 46.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/b/6be8a8566f8f3f47a1f052f039130fabd6193c5b.png)


got consistent 6/25 after even running the file 6 times [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) Please sir check this, just because my docker image needs .env, I cannot get full 0…I need to maintain my cgpa (by getting 0 in project my grade is going too close to E grade sir and already in D, already my ROE got bad due to technical issues which on the same day around 6pm after finding way to unlock the input of answers for roe I completed the roe again in short amount of time like 10 or 20 minutes and got 10/10 but still it was rejected because it was late, max 3 minutes after 1:45PM was allowed…I’m not asking to any extra marks, just my marks) I’m trying to improve it already I have 4 subjects in a single term, please give me atleast this marks with the bonus 1 mark for prerequisites (total 7)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/e/8ef5cf5156fdaca65d927edf5d6c2463da4f7052.png)image704×248 20 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/e/8ef5cf5156fdaca65d927edf5d6c2463da4f7052.png)


Thank you

---
**Post ID:** 616536  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/405  

Yes,the Same case happend to me also we have put lot of efforts in this project but after seeing that in mail you have no mit licence, I added that license but with name of mit license actually to just name that license file as MIT license but due to this all our hardwork is just an experience but actually we are not awarding any marks in project1 . I request the TDS team to consider this issue.

---
**Post ID:** 616584  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/406  

I have passed the pre requisites, but there is no log file for my email.


At least docker logs should be there, right?


Was it missed by any chance?


[@Jivraj](/u/jivraj) [@carlton](/u/carlton)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/4/e49661e517e668b1f6055ac2db0b01d1a2a5552a.png)image916×160 14.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/4/e49661e517e668b1f6055ac2db0b01d1a2a5552a.png)

---
**Post ID:** 616590  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/407  

Sorry to repeatedly ask [@carlton](/u/carlton) [@Jivraj](/u/jivraj)


couldnt see my id (22f3002723) in any of the logs  evaluation or docker .. was there any issue in building image out of docker file in github

---
**Post ID:** 616600  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/408  

Hi [@22f3002723](/u/22f3002723)


 /bin/sh: 1: uv: not found 
This is error that we got on your evaluation while building docker image through github repo.





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)


    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv. 
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo

owner = "your_username"  # Replace with your actual GitHub …

---
**Post ID:** 616601  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/409  

This was error with your submission.`tried copying file named`app`which is not there in github repo`

---
**Post ID:** 616602  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/410  

Respected Sir , [@carlton](/u/carlton) [@Jivraj](/u/jivraj)


My roll number is 23f3001688


Pls check my repository properly because I have dockerfile in my repo but it is mentioned that it is not present.


Here is my repository link and screenshot for your reference sir and the dockerfile is present sir



[github.com](https://github.com/Sharmilecholan/tds_project1)



![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f4296a48f50a92933eb573695c91faee58b51a1_2_690x344.png)
[GitHub - Sharmilecholan/tds_project1](https://github.com/Sharmilecholan/tds_project1)
Contribute to Sharmilecholan/tds_project1 development by creating an account on GitHub.








I think the mistake would have been because in my repo the file name is “dockerfile” and you have mentioned it as “Dockerfile” . So is it a mistake to put “D” in lowercase.


Kindly look into this sir because of this I got 0 in project 1 even though many of the tasks of my projects passed the evaluation test.


Regards,


S Sharmile


23f3001688


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/014b7a8714c79b6921eb8f8da545286cc6dbedc8_2_690x281.png)image1904×778 83 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/1/014b7a8714c79b6921eb8f8da545286cc6dbedc8.png)

---
**Post ID:** 616622  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/412  

[@carlton](/u/carlton) sir, i want to clarify about this. I had got 9/20 in the previous mail in my evaluation log and now the recent mail say i got 1 mark. I want to ask about this. Please help me


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/b/4bbeee344dad6a24766c6978889ccd69086dcc6d_2_225x500.jpeg)WhatsApp Image 2025-04-07 at 15.37.17_fb28b652720×1600 139 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/b/4bbeee344dad6a24766c6978889ccd69086dcc6d.jpeg)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c342418d20b935d414f96817c92300bcec289598_2_225x500.jpeg)WhatsApp Image 2025-04-07 at 15.39.10_edb0b829720×1600 125 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/3/c342418d20b935d414f96817c92300bcec289598.jpeg)

---
**Post ID:** 616631  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/414  

I don’t know how to check for the errors I made, [@Jivraj](/u/jivraj) sir can you at least show the prerequisite form that I submitted so I can check for myself ?.

---
**Post ID:** 616646  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/415  

[@jivraj](/u/jivraj)


earlier I built the project inside app folder so it was


`COPY app /app`
it should have been


`COPY . /app`
Is there anything that can be done on your end now?


All the code is there.

---
**Post ID:** 616654  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/416  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/0/605890bb7fb48c38efa33362d005654d2dd7e765_2_690x86.png)image1822×229 20.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/0/605890bb7fb48c38efa33362d005654d2dd7e765.png)


Sorry for late reply,These are 2 submissions that you made we are considering the latest one.

---
**Post ID:** 616655  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/417  

No we don’t consider any changes after deadline.

---
**Post ID:** 616657  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/418  

There was a module missing error while lead the docker image to run.


Follow below steps for replicating test environment.


[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---
**Post ID:** 616663  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/419  

For dockerfile you have in repo, It was named differently, correct naming has to be Dockerfile.





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354) [Tools in Data Science](/c/courses/tds-kb/34)


    You can take it up with [@s.anand](/u/s.anand) 
I did not come up with the standard. 
And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files. 

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in. 

Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand i…

---
**Post ID:** 616665  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/420  

[@24ds1000119](/u/24ds1000119) and [@YaswanthVaddi](/u/yaswanthvaddi)


We are not considering mismatch in naming for License.

---
**Post ID:** 616666  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/421  

Dear [@carlton](/u/carlton)


This is Senthur. I have reviewed the logs, and it indicates that the


`/app/app/main.py`     file is missing. However, in my project directory, the


`main.py`   file is located in the   `app/`   folder, and the   `run.py`   file is in the root folder of the project, which is   `LLM_Automation_Agent`  . This structure allows the `run.py` file to run the project without any issues by calling the appropriate functions from `app/main.py`.


To run the project, the command I used is:


`python run.py`
Since `run.py` is placed in the root folder and not in any subfolder, it should properly execute the project without any errors, as it redirects the calls to `app/main.py`.


I believe the evaluation may have been incorrect because the project was not executed in the way it was intended. I kindly request you to re-run the project using the `run.py` script located in the root folder (`llm-automation-agent`).


For your reference, I have attached screenshots from my local machine where the project was tested successfully, along with my GitHub screenshot.


Here is the GitHub link to my project:




[github.com](https://github.com/ksenthurkumaran18052004/llm-automation-agent)



![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/e/ce9394993a2cc41f2a17658d6ed40ff9fff7d6a7_2_690x344.png)
[GitHub - ksenthurkumaran18052004/llm-automation-agent](https://github.com/ksenthurkumaran18052004/llm-automation-agent)
Contribute to ksenthurkumaran18052004/llm-automation-agent development by creating an account on GitHub.








[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/62e7f6525fb97f7d1de84d08cde34b2bf2d5e404_2_255x500.jpeg)image1440×2823 252 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/2/62e7f6525fb97f7d1de84d08cde34b2bf2d5e404.jpeg)


Lookig forward towards your support.


With Regards


K Senthur Kumaran

---
**Post ID:** 616667  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/422  

Same here sir, i only changed LICENSE to MIT LICENSE due to the mail i received.


The LICENSE file was already present in the repo as i submitted my project. The change too was made on the 16th of Feb.


Sir, I would highly appreciate if you consider it as the rest of the pre-requisites are working well.Due to this, the project is also not being evaulated.


Thankyou


[@carlton](/u/carlton)

---
**Post ID:** 616672  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/423  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c1d290bffaf6788ece5d9408b1c52566200a8cc9_2_690x149.png)image1823×395 24.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c1d290bffaf6788ece5d9408b1c52566200a8cc9.png)


Just checked right now. I am getting this error.


Replicate test environment following this post.


[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)0

---
**Post ID:** 616683  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/424  

`🟡 Running task: Format `/data/format.md` with `prettier@3.4.2` in-place

HTTP Request: POST http://localhost:8381/run?task=Format+%60%2Fdata%2Fformat.md%60+with+%60prettier%403.4.2%60+in-place "HTTP/1.1 400 Bad Request"

🔴 HTTP 400 {
  "detail": "[Errno 2] No such file or directory: 'C:\\\\Program Files\\\\nodejs\\\\npx.cmd'"
}

HTTP Request: GET http://localhost:8381/read?path=/data/format.md "HTTP/1.1 200 OK"

🔴 /data/format.md
⚠️ EXPECTED:
# Header

| Start | Mid | End |
| :---- | --- | --: |
| 1     | 2   |   3 |

Paragraph has extra spaces and trailing whitespace.

```py
print("23f3003027@ds.study.iitm.ac.in")`
[](#p-616683-result-header-1)![That's a yellow triangle with a black exclamation mark inside.  It's a common warning or alert symbol.
](https://emoji.discourse-cdn.com/google/warning.png?v=14) RESULT:


Header




Start
Mid
End




1
2
3



Paragraph has extra   spaces and trailing whitespace.


`print("23f3003027@ds.study.iitm.ac.in")`
![That's a red "X" symbol on a black background.  It's a common graphical representation of cancellation, error, or negation.
](https://emoji.discourse-cdn.com/google/cross_mark.png?v=14) A2 FAILED


`I am facing Npx error... can I know what went wrong?
@carlton @Jivraj`

---
**Post ID:** 616681  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/425  

![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f300327/48/91361_2.png) 23F300327:

`I am facing Npx error... can I know what went wrong?`


This `npx` error is originating from your Docker container—it’s not being generated by our script. Try to look for what caused this error.

---
**Post ID:** 616713  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/426  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28ee8a9e3739e37d81cedf39142209af2d7f4090_2_690x311.png)Screenshot 2025-04-07 2135381868×843 125 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/8/28ee8a9e3739e37d81cedf39142209af2d7f4090.png)


Oh I see what happened, the image names are different, I don’t know how, given I pushed the latest at 11:51pm and submitted the form at 11:59pm. Thank You [@Jivraj](/u/jivraj) for showing me.


Question: Now that I know. how can I test the container myself, if I want to do exactly what you guys are doing?

---
**Post ID:** 616718  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/427  

My code uses `npx` to format Markdown files using Prettier, specifically via `subprocess.run(["npx", "prettier@3.4.2", "--write", ...])`, which assumes that `npx` is available in the environment. However, since the Docker container is based on Linux and I didn’t explicitly install Node.js or `npx`, this results in an error during evaluation.


To test the functionality correctly, `npx` must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:


bash:`apt-get update && apt-get install -y nodejs npm`


Once installed, `npx prettier@3.4.2` should work as expected.


For reference, this approach worked perfectly when I tested the same task locally on my Windows 11 system, where `npx` is available by default.

---
**Post ID:** 616726  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/428  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)


Before the project evaluation, I ran the test script and successfully passed all Task A and Task B checks. I also built the Docker image as required.


But, when you gus evaluated , I get the following error:docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: “uvicorn”: executable file not found in $PATH: unknown.


Could you please help me understand why this is happening even though the evaluation script ran fine?


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/c/9cd9e40f5ec0afeee28e1dcc5ad0340d2e5872d2_2_690x308.png)image1591×712 123 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/c/9cd9e40f5ec0afeee28e1dcc5ad0340d2e5872d2.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/c/1cc811ef3cd38bebb7a22e0297e57ce6388e5c58_2_690x341.png)Screenshot 2025-04-07 1924191534×760 38 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/c/1cc811ef3cd38bebb7a22e0297e57ce6388e5c58.png)

---
**Post ID:** 616741  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/429  

Can you tell me what application is this (FastAPI) one ?

---
**Post ID:** 616767  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/430  

idk why i am doing this but this is my last request (for evaluation) with proofs. me and my friend both have same docker file code with missing flask dependency (i will try as much to not reveal his id/name) he got 12/20 even tough i tried same methods given by you and same error popped up flask module not found in his case but you gave him 12/20 marks but for me you gave 0? did i done something wrong? I know in industry level it matters much but right now we are students and for us CGPA matters. i am also uploading his docker file image and mine with 0 commits after 18th feb.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/8/78eaf46821c5af8d1f6844561dc235a1e22f6de7_2_690x377.png)image1670×914 67.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/8/78eaf46821c5af8d1f6844561dc235a1e22f6de7.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/0/300e62ae1bb91e990020843f9db4aab25bd9ac70_2_690x468.png)image1376×935 60.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/0/300e62ae1bb91e990020843f9db4aab25bd9ac70.png)

---
**Post ID:** 616782  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/431  

Dear Sirs,


[@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini) [@carlton](/u/carlton)


As per the Project 1 deliverables, I had submitted my Docker Hub repo, that hosted the Docker image. At the time of submission, the image was running smoothly, was fully accessible, and was successfully handling the API calls as intended.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7b8a704d618edd74036a95649a83054e29932879.png)Screenshot 2025-04-07 233513805×197 9.52 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7b8a704d618edd74036a95649a83054e29932879.png)


Github repo submitted: [GitHub - wasimansari-iitm/Project-AI-Agent](https://github.com/wasimansari-iitm/Project-AI-Agent)


Docker repo submitted: wasimansariiitm/my-ai-agent


The previous evaluation was successfully conducted using my Docker image, which was responding as expected. However, during the subsequent evaluation, the image was rebuilt using my GitHub repo link, and unfortunately, the `app.py` file could not be found. As a result, my evaluation logs are missing from the evaluation logs bundle.


I would like to respectfully bring this to your kind attention that the `app.py` file does exist in the repository, but it is located inside a subfolder:


[https://github.com/wasimansari-iitm/Project-AI-Agent/app/app.py](https://github.com/wasimansari-iitm/Project-AI-Agent/blob/main/app/app.py).


But as per the submission instructions, I provided the GitHub repo link only: [https://github.com/wasimansari-iitm/Project-AI-Agent](https://github.com/wasimansari-iitm/Project-AI-Agent).


Humbly stating, I did not anticipate that the image will be rebuilt from the GitHub repo at a later stage due to some unforeseen circumstances. Had I known this, I would have made sure the project repo was structured appropriately to support that scenario. To be noted, that the earlier evaluation ran smoothly, and the app responded to all queries as expected.


I’m unsure what to expect now or request, but I just wanted to bring this issue to your notice. Even if I manage to get a single answer correct upon a successful evaluation, it would mean a lot to me and contribute meaningfully to my overall score. I would be extremely grateful if you could look into my case and extend your support in this matter.


Thank You and Regards,


24ds3000090

---
**Post ID:** 616788  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/432  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Sir, in my docker logs, the datagen script encounters error during creating the credit card image for A8 during which it fails to find both the fonts used in the try and except blocks, resulting in the datagen script to stop abruptly without creating the files for A8 to A10.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a49f182e22015df35039be85cdd26ad71a07f7a3.png)image1298×857 29.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a49f182e22015df35039be85cdd26ad71a07f7a3.png)


I actually want to know if this could have been avoided by some changes in my code or is it an issue in the datagen.py script, because as the situation currently stands, my app wasn’t even tested properly for tasks A8 to A10 as the datagen.py script failed to create the required files because it could not find a font which as far as I knew was not specified that it must be included in my own code or image somehow.


Edit 1: I just realized that the datagen script looked for the fonts in python 3.13/site-packages/…


But my docker image is using the python:3.12-slim-bookworm. Could that be an issue? There was nothing specified about required python version or required python image to be used in docker in the project 1 requirements.


Edit 2:


Even if the font not being available is somehow my fault, A9 and A10 still should not be penalized for A8 without proper checking.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f99c9908823f381a7756ba6fe89d4827ca2faf4.png)image1027×510 11 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f99c9908823f381a7756ba6fe89d4827ca2faf4.png)


Though an error occured in A8, A9 and A10 still could have worked if each of these function calls were enclosed in their own try-except blocks, ensuring independent checks for each task. But the current datagen.py script fails as error propagates to main, where it is not handled and causes abnormal termination without executing the functions for creating files for A9 and A10 as well.


Thank you.


Regards,


Shivaditya

---
**Post ID:** 616843  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/433  

Hi Haricharan


Your Dockerfile does not build the repo. Its misconfigured.


This is the error when building it:


`=> ERROR [8/8] COPY .env /app/                                                                                                                         0.0s
------
 > [8/8] COPY .env /app/:
------
Dockerfile:20
--------------------
  18 |     # Copy application files
  19 |     COPY *.py /app/
  20 | >>> COPY .env /app/
  21 |     
  22 |     # Explicitly set the correct binary path and use `sh -c`
--------------------
ERROR: failed to solve: failed to compute cache key: failed to calculate checksum of ref 468faeeb-6d46-4aeb-a590-25bae24a84d5::y52oingx9lezoq9kjiwp6v58m: "/.env": not found`
[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573_2_690x276.png)Screenshot 2025-04-08 at 11.12.18 am754×302 41 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573.png)


This is because if you look at your Dockerfile .env does not exist in your repo.


Therefore it does not build.


Your docker is supposed to take the AIPROXY token from our environment not from yours.


This is passed dynamically at runtime of the Docker.


Since it fails to build, we cannot evaluate it.


Kind regards

---
**Post ID:** 616847  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/434  

Your docker failed to build from your Dockerfile


`=> ERROR [4/7] RUN uv --version                                                                                                                        0.1s
------
 > [4/7] RUN uv --version:
0.078 /bin/sh: 1: uv: not found
------
Dockerfile:25
--------------------
  23 |     
  24 |     # Verify uv installation
  25 | >>> RUN uv --version
  26 |     
  27 |     # Set working directory inside the container
--------------------
ERROR: failed to solve: process "/bin/sh -c uv --version" did not complete successfully: exit code: 127`
Since we cannot build your docker from your Docker manifest file we cannot evaluate it.

---
**Post ID:** 616853  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/435  

Your container failed to run after building it.


`docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: exec: "uv": executable file not found in $PATH: unknown`
Thats why we cannot evaluate it.

---
**Post ID:** 616862  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/436  

There is clearly some difference between both the applications. That is up to you to figure out. I can only tell whats wrong with yours. After building it and trying to run it this is the error we get. It fails to run as a result and we cannot evaluate it.


`Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 412, in main
    run(
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 579, in run
    server.run()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 999, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/app/app.py", line 23, in <module>
    from tasksB import *
  File "/app/tasksB.py", line 83, in <module>
    from flask import Flask, request, jsonify
ModuleNotFoundError: No module named 'flask'`

---
**Post ID:** 616864  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/437  

Noted your concerns wrt Edit 1 and Edit 2 (and datagen.py running latest python version): Will raise it with [@s.anand](/u/s.anand) during our Wednesday meeting. Once we have an update, we will inform you of the outcome.


Kind regards

---
**Post ID:** 616924  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/438  

Hi,


Please let me know the reason on why I have not got any bonus marks.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a4b4614f55f231153c89c3de51b0c0ae60d44633.png)image1310×681 14.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a4b4614f55f231153c89c3de51b0c0ae60d44633.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/40c10210a7c33774133ec99e68ad77a840209387_2_690x297.png)image1696×732 59.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/40c10210a7c33774133ec99e68ad77a840209387.png)

---
**Post ID:** 616935  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/439  

We used some internal parameters with weights to auto calculate the bonus. Unless your submission met that threshold of 0.5 after scaling you would not get any bonus. Your score was normalised so instead of 3 you got 4 (3.75 got rounded up). But the metrics used to evaluate the quality of your submission only scored you at 0.007 which is far below the threshold required to get a bonus.

---
**Post ID:** 617017  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/440  

Respected Sir,



Yes Sir, I said the same,  `.env` was not able to be uploaded to repo as .env file was not allowed to be uploaded
when we download the repository it doesn’t have the `.env` file,
for docker image to build we need to add `.env` with `AIPROXY_TOKEN`
after that docker image will build, I had given about this in previous message
As you said Sir that you will use separate `AIPROXY_TOKEN`…you can put that in `.env` file and build the docker image
after that Sir its optional to pass `AIPROXY_TOKEN` again while running the docker Image
just the `.env` file required, even without token in that it will work as project has support for both AIPROXY token in .env file and as environment variable

and when I uploaded to repository the .env file was not allowed to upload so had submitted that way, I actually forgot to add step for running the docker image in the previous message, the steps which I used:


`git clone https://github.com/23f2001390/llmagent.git`
adding `.env` with AIPROXY token and replacing `evaluate.py` and `datagen.py` with new ones according to test environment


`docker build -t llm-agent .`
`docker run -p 8000:8000 llm-agent
or
docker run -e AIPROXY_TOKEN=token -p 8000:8000 llm-agent`
and in another terminal


`uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000`
Thank you


Kind regards

---
**Post ID:** 617039  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/441  

Respected sir


I understand it’s my mistake sir and I apologize for that sir, but please consider this time sir since because of this my entire project score went from 9/20 to 0, which would make me difficult to pass this course and continue my diploma.


Please consider this request sir, sorry sir and this would never be repeated in future. My project evaluation was 9/20 initially sir, but later it came down to 0 because of this issue. Kindly consider sir please.


Regards,


S Sharmile


23f3001688

---
**Post ID:** 617096  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/442  

Thanks for relentless efforts [@carlton](/u/carlton) [@Jivraj](/u/jivraj)


I tested the docker file in docker playground again.. Please find the screenshot of the docker build command and the log output of the docker build.. It went thru without issues..


Was the latest docker file used from git lab? Because as explained on March 30 i had to remove the hardcoded http/https proxies of  my office environment,


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d_2_690x363.png)image (18)1272×671 64.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d.png)


build output


`#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 694B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/python:latest
#2 DONE 0.5s

#3 [internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [1/6] FROM docker.io/library/python:latest@sha256:aaf6d3c4576a462fb335f476bed251511f2f1e61ca8e8e97e9e197bc92a7a1ee
#4 DONE 0.0s

#5 [internal] load build context
#5 transferring context: 33B done
#5 DONE 0.0s

#6 [4/6] RUN uv --version
#6 CACHED

#7 [2/6] RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates &&     apt-get clean && rm -rf /var/lib/apt/lists/*
#7 CACHED

#8 [3/6] RUN curl -sSfL https://astral.sh/uv/install.sh | sh
#8 CACHED

#9 [5/6] COPY execute.py /
#9 CACHED

#10 exporting to image
#10 exporting layers done
#10 writing image sha256:2919fe6ce0097ae2fc33aebaba327dbd6a35d256b6d946c97c310fd992944add done
#10 naming to docker.io/library/tdsproject1:latest done`
[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59_2_690x54.png)image1480×117 9.41 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59.png)

---
**Post ID:** 617127  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/443  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd6b7a633fa356674be001b8861629604fb08ea4_2_690x387.png)image1919×1079 301 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd6b7a633fa356674be001b8861629604fb08ea4.png)





![Image could not be processed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002723/48/110636_2.png) 22f3002723:

Was the latest docker file used from git lab




No, we are not allowing any changes to repo after deadline, this is consistent rule for every student. We pulled your github repo latest commit before 18th feb, I am getting following error.

---
**Post ID:** 617129  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/444  

follow the steps mentioned in post below ![That's a simple, smiling yellow emoticon or emoji.
](https://emoji.discourse-cdn.com/google/slight_smile.png?v=14)


[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---
**Post ID:** 617130  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/445  

![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f300327/48/91361_2.png) 23F300327:

To test the functionality correctly, `npx` must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:




That destroys the purpose of containerization, your container should run anywhere anytime, all the dependencies must be preinstalled.

---
**Post ID:** 617234  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/446  

Thanks [@carlton](/u/carlton) [@Jivraj](/u/jivraj)


As mentioned earlier, the pre Feb 18 dockerFile commited in GIT had  my office proxy url’s set as http_proxy and https_proxy.. It worked in my office envuironment and i tested everything in my office environment but based on the results which came on March last week realised that the proxies were preventing the uv to be installed in other environments.


Post that realised we have cloud based "docker playground’ utility where docker builds can be tested agonistic of any environment.. The good thing with playground is our instances last for only 3 hrs and next day we try we are kind of gauranteed of fresh environment without any caches,


Now after March 30th checkin validated the same in docker playground and ensured that the image got tagged and createdd successfully..


It would be great if the March 30th checkin could be considered, Again appreciate all your help so far.

---
**Post ID:** 617273  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447  

Subject: Request for Verification of Dockerfile and Reevaluation of Marks for Project 1


[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Sir,


Regarding the recent feedback on Project 1 for TDS, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named `dockerfile` (not `Dockerfile`). Please verify the repository again with this in mind.


Additionally, my Docker image architecture is linux/amd64 (64-bit x86). I have also filled out the Architecture Information Collector form as requested.


Pre-requisites check: (1 for pass, 0 for fail)


Docker repo exists and is public (should have a timestamp before 18th of Feb): 1


Github repo exists and is public (should have a timestamp before 18th of Feb): 1


Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1


Gihub repo check - Dockerfile exists: 0


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eaea99d88c244f6d9e7407183e4d96e2e1c35d2f_2_690x368.png)image1914×1021 91.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/eaea99d88c244f6d9e7407183e4d96e2e1c35d2f.png)


Here’s the link to my GitHub repository:



[github.com](https://github.com/23f1001822/Task_agent_api)



![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/8/d83b83eaf69931596b2cddbbfea39884f17e047a_2_690x344.png)
[GitHub - 23f1001822/task_agent_api](https://github.com/23f1001822/Task_agent_api)
Contribute to 23f1001822/task_agent_api development by creating an account on GitHub.








Docker repo submitted: sakshamumate/task_agent_api


I kindly request a reevaluation of my project marks based on these clarifications.


Thank you for your attention to this matter. Please let me know if you need any further information or clarification.


Best regards,


Saksham Umate ,


23f1001822@ds.study.iitm.ac.in

---
**Post ID:** 617292  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/449  

Sir, I had posted the query on A8 and datagen exception. Is this a reply to that?

---
**Post ID:** 617294  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/450  

oh yeah sorry, hit the reply to the wrong button, but yes its to your post.

---
**Post ID:** 617296  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/451  

I’ve got good news for you and 30 other students. Thanks to your diligent debugging effort that we were able to find this bug. For now the fix is that we will not evaluate you on a8 and catch the datagen exception so as to not cause cascading failures.


Thanks and kind regards.


We will let you know the outcome of the evaluations soon.

---
**Post ID:** 617576  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/452  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


any way out for my earlier query ?

---
**Post ID:** 617594  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/453  

[@carlton](/u/carlton)


Thank you for the reply .But it was working when i ran the initial evalaute.py .If you don’t  mind could you tell what may have caused this to happen.

---
**Post ID:** 617664  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/454  

Hi Hilal,


You have to recreate the test environment as shown in this post





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)


    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv. 
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo
import argparse
import os
import zipfile

parser = argparse.…
  

That way you will be able to identify why the error was occuring.


The specific error itself means:


Docker is trying to run the command uv inside your container, but it can’t find the uv executable — it’s not installed or not in the system PATH inside the container.


If you did not run evaluate.py as specified in our live sessions by recreating the test environment and then running evaluate.py then it would not have reflected how your dockerised application would work.


Kind regards

---
**Post ID:** 618023  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/455  

sir for my project 1 i got a mail stating that the docker file isn’t public and that’s why prerequisite failed. but i checked it and it seemed absolutely perfect to me. Please look into this issue as my docker repo is public and absolutely as per the requirement.  [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 618030  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/456  

Hi [@22f3003083](/u/22f3003083)


Following was your submission, which is not a valid dockerrepo.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf43ec80b28a06b6a45f49123430da5b2d20bad6_2_690x94.png)image1829×251 22 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/f/cf43ec80b28a06b6a45f49123430da5b2d20bad6.png)

---
**Post ID:** 618032  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/457  

Now I feel so good getting 0.


0 is best.

---
**Post ID:** 618061  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/458  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


As requested earlier, Could you please reevaluate my submission.  The only change that had to be done post Feb 18 checkin was to remove my office proxies on Mar 30 from the docker file  to make it work in all environments.. It  would be great if this could be accomodated..

---
**Post ID:** 618117  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/459  

Hi Jayaram,


Unfortunately, we are not able to relax restrictions on changes to your repo, regardless of the reason. We have kept this rule uniform for everyone. If we allow this change, then everyone has a legitimate reason to request changes and would make the rule meaningless because then everyone will be able to make corrections to their submission. We do not even allow spelling changes.


Kind regards

---
**Post ID:** 618125  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/460  

Thanks for the response [@carlton](/u/carlton) ..  just a small suggestion, to avoid scenarios like what i faced and also with softwares like docker/podman not being too windows friendly, i think students can find it easier if a dev/mock  linux env is provided for course term duration, instead of   everyone having to figuring out with AWS/Azure and all providers.. Anyway thanks and appreciate all the help

---
**Post ID:** 618204  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/461  

Sir, I have done everything for my project, but I am getting zero. I have uploaded my Docker file, but the email says it is not public. Sir, this is affecting my grades — please help me out. [@Carlton](/u/carlton)

---
**Post ID:** 618203  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/462  

These are your project 1 responses,


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/7/a73f7a58a671b757d3df0929df3e0aa912955e6c_2_690x115.png)image1737×291 23.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/7/a73f7a58a671b757d3df0929df3e0aa912955e6c.png)


We are considering latest submission which have docker repo `maheshsingh01/tdsrepos`


which is not accessible publically.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/7/174c8e4e8ad4c6e537203447df3d370b0efa8782_2_690x350.png)image1866×949 92.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/7/174c8e4e8ad4c6e537203447df3d370b0efa8782.png)

---
**Post ID:** 618225  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/463  

Sir, could you please check it once more? I think the issue has been resolved. [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 618231  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/464  

Since repo was not public during evaluation, we won’t be rechecking, or reevaluating.

---
**Post ID:** 618301  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/465  

[@Jivraj](/u/jivraj) I’ve completed all the required steps, but I’m still getting 0, It was working fine before. Could you please help me identify what might be going wrong?

---
**Post ID:** 618314  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/466  

Hi [@21f3003107](/u/21f3003107)


You need to look it up yourself, We have sent out evaluation log and docker log files, check those out.


Evaluation script and other scripts that we have used are there in github repository over here.


[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/1)


If there is some mistake from our end let us know about it.


To replicate test environment follow steps provided below.


[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---
**Post ID:** 618359  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/467  

[@carlton](/u/carlton) Requested sir


This is to request that in my evaluation a got 0 cause of the use of lowercase d instead of uppercase D but I have already submitted the  docker file in my git hub repo also.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/3/1312efae69b50e418bc708a80bd11f752a9be4a5_2_627x500.jpeg)WhatsApp Image 2025-04-11 at 23.34.06_a49fd1e5912×727 79.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/3/1312efae69b50e418bc708a80bd11f752a9be4a5.jpeg)

---
**Post ID:** 618525  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/468  

[@carlton](/u/carlton)


Thank you i found my mistake in my docker file i wrote  this  CMD [“uv”, “run”, “app.py”]  instead of


CMD [“uvicorn”, “main:app”, “–host”, “0.0.0.0”, “–port”, “8000”].Now i think everything works fine

---
**Post ID:** 618965  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/469  

Sir my repo was public

---
**Post ID:** 618997  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/470  

Sir any news on this? Did my score increase at all? My dashboard still shows the old score.

---
**Post ID:** 619160  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/471  

[@carlton](/u/carlton) sir, my project 1 marks have still not increased even though while during evaluation it shows 4/10 for the task 1. It was said that the docker image prerequisite will be removed and without that the evaluation would be done, but there is still no change in my marks. please look into it once, as my dashboard currently reflects 0 for project 1.

---
**Post ID:** 619360  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/472  

These evals are being handled separately. They have not yet been completed. Kindly bear with us till they are complete.

---
**Post ID:** 619619  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/473  

Same here [@carlton](/u/carlton) in my evaluation logs i have scored 10 while marks being reflected are not the same neither on mail nor on site

---
**Post ID:** 619655  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/474  

I looked at your evaluation logs and it says 1 score instead of 10.

---
**Post ID:** 620018  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/475  

Good evening!


[1000092114|690x198](/uploads/short-url/30ijyIo5UiUUEVvnPZklfYVY2mI.jpeg)


I am writing to you to request you please relook into the evaluation.


The docker image which I share is working at my end.  The size of the image is 6 GB which may take more than 5 minutes to load as I wasn’t aware of the infra level restrictions.


I request you to kindly consider my request and please re-evaluate the assignment as I have contributed a lot of effort into it.


Thanks,


Garima

---
**Post ID:** 620556  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/477  

Sir, so will my score get updated because now it is marked as 0.

---
**Post ID:** 620587  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/478  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Sir,


I am Saksham Umate and my project 1 was to be re-evaluation because of docker file not found in root ,but it was their so you had given me confirmation that it will re-evaluate after end term. I had already shared my docker file systems configuration at docker hub


So, I hope you will look at this and re-evaluate my project as I put lots of efforts to complete it


Tell me if any information is needed about project from my side


Thank you!


Best regards,


Saksham


My docker repo details in previous post:




![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001822/48/66833_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447) [Tools in Data Science](/c/courses/tds-kb/34)


    Subject: Request for Verification of Dockerfile and Reevaluation of Marks for Project 1 
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) 
Sir, 
Regarding the recent feedback on Project 1 for TDS, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named dockerfile (not Dockerfile). Please verify the repository again with this in mind. 
Additionally, my Docker image architecture is linux/amd64 (64-bit x86). I have also filled out the Architecture Information Collector form as requested. 
P…
  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f8ee39bed46e6f2a196634ca56106c56c42003d_2_259x500.jpeg)IMG_20250417_1140021080×2083 469 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/f/3f8ee39bed46e6f2a196634ca56106c56c42003d.jpeg)

---
**Post ID:** 620590  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/479  

Evaluations are done for such cases where Dockerfile(with name of Dockerfile as `Dockerfile`) was present inside other folders than root folder of your github repo.

---
**Post ID:** 620595  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/480  

[@carlton](/u/carlton) sir, any info on outcome of [this bug in P1 datagen.py](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/451) ?

---
**Post ID:** 620608  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/481  

Did Mark’s are updated or being update for this students ?

---
**Post ID:** 620628  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/482  

Hi [@22f3000819](/u/22f3000819)


We had updated datagen.py(try block for task) which affected 30 students, but scores changed only for 4 students, for others it remained the same.

---
**Post ID:** 620630  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/483  

We will be pushing marks today.

---
**Post ID:** 620636  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/484  

I probably wasn’t 1 of the 4, right? Anyways thanks for paying attention to the matter.


Regards,


Shivaditya

---
**Post ID:** 620829  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/485  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


Respected Sir,


I hope you are doing well.


This is with reference to your confirmation mail that my project 1 will be re-evaluated after end term


I would like to sincerely apologize for the oversight in my Project 1 submission. Upon reviewing my GitHub repository, I realized that the file was named `dockerfile` (with a lowercase ‘d’) in the Github root repo instead of the required `Dockerfile` (with an uppercase ‘D’).


While the contents of the file were correct and my project passed several evaluation tests, I understand that the evaluation script could not detect the Dockerfile due to this naming issue. I genuinely did not intend to deviate from the standard, and I now fully understand the importance of following naming conventions precisely.


I humbly request you to kindly consider this as an honest mistake and allow a one-time exception, Please sir. This issue has unfortunately resulted in my project score being reduced to 0, which puts my overall course performance at risk. I assure you that I have learned from this experience and such an error will not occur again in the future.


So, I hope you will look at this and re-evaluate my project as I put lots of efforts to complete it.


Thank you very much for your time and consideration.


Warm regards,


S. Sharmile


Roll No: 23f3001688

---
**Post ID:** 621017  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/486  

Sir, my marks still did not get updated, please help me in that regard.

---
**Post ID:** 621117  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/487  

Hi Everyone,


We have sent the updated marks to Operations. At this time of the term they are very busy with lots of updates, so it will take time for them to push it to the dashboard. As soon as they inform us that the scores have been pushed, we will send out a discrepancy form if you find any issues with your score.


Thanks & Kind regards

---
**Post ID:** 621247  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/488  

Sir, my project 1 marks are still 0 even though I had passsd few cases. Please help me sir as my final score is coming as 69.8 , it will be very valuable for me if it crosses 70, please sir help me with this regard

---
**Post ID:** 621699  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/489  

[@carlton](/u/carlton)


Hi Sir,


I hope you’re doing well. I just wanted to let you know that I put a lot of effort into completing Project1, but I accidentally named the Dockerfile as `dockerfile` (with a lowercase ‘d’).


Could you please consider evaluating it with that name? I’d really appreciate it.


Thank you!


My discourse post for more information:




![Image description failed](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001822/48/66833_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447) [Tools in Data Science](/c/courses/tds-kb/34)


    Subject: Request for Verification of Dockerfile and Reevaluation of Marks for Project 1 
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) 
Sir, 
Regarding the recent feedback on Project 1 for TDS, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named dockerfile (not Dockerfile). Please verify the repository again with this in mind. 
Additionally, my Docker image architecture is linux/amd64 (64-bit x86). I have also filled out the Architecture Information Collector form as requested. 
P…

