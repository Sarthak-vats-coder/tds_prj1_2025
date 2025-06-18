# URGENT ATTN REQ: technical discrepancy and inconsistency in the evaluation scripts of graded assignment and project 2
_Slug: _

---
**Post ID:** 621934  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/1  

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


Dear Sir,


The SQL is syntactically correct and in executable format as evidenced by its successful execution and acceptance by the evaluation script of the Graded Assignment.


[![The image shows a coding exercise involving an SQLite database.  The task is to write an SQL query that calculates the total sales of "Gold" tickets, handling variations in capitalization and extra spaces in the `type` column.  A sample table of ticket data and a correctly answered SQL query are provided.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/514ac690e9a0d891497501d503827232690f2745.png)image690×376 15.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/514ac690e9a0d891497501d503827232690f2745.png)


The error appears to stem from the way the Project 2 evaluation script handles escape characters such as newline (`\n`). This inconsistency has resulted in a correct answer being marked as incorrect, despite the fact that the same query was previously accepted by the evaluation script of Graded Assignment without any issue. Such ambiguity in the evaluation process is concerning and leads to confusion and unfair penalization of students.


I respectfully request that you review this matter and ensure that the evaluation criteria are consistent across the evaluation scripts. Denying marks due to technical discrepancies in the evaluation scripts, rather than the correctness of the SQL query itself, is unjust. This issue has severe repercussions: If unresolved, it will unjustly lower my overall course grade despite submitting a correct solution. Such an outcome, resulting from no fault of my own, is deeply concerning and undermines the fairness of the evaluation process. I kindly request that you reconsider my submission and award the marks that are rightfully due.



On 21/04/25 4:42 pm, [22f3002542@ds.study.iitm.ac.in](mailto:22f3002542@ds.study.iitm.ac.in) wrote:




Hi [23f1001231@ds.study.iitm.ac.in](mailto:23f1001231@ds.study.iitm.ac.in),


You reported the following issue for “Project2”, Question 1:


"The escape characters i.e. \n in the answer string which contains SQL query is raising syntax error in your end.The SQL query is correct and has passed in the graded assignment.

---
**Post ID:** 621938  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/2  

Hi Premdeep,


We will update your score to consider `\n` for SQL query.


I had briefly read your post and incorrectly assumed that the script was not handling newline characters (which are invisible whitespaces).


The prescription given by Anand in a live session exclusively conducted by him was clear.


We should be able to copy paste your answer from the JSON response and put it in the GA and it should work. There only some notable exceptions, and this is where formatted text is expected. This question does not require formatted text, but it does require handling of quotes.


Your response has literal a `\` and literal `n` characters. It fails the copy paste test. If it had the invisible actual new line characters encoded then it would be parsed correctly. In your own image that you shared you did not copy paste the return response of your function into your GA.


I also looked at your repo and the mistake you made for this question was you used a multiline string for the SQL query. The result of the `json.dumps` for this question (which does not require or expect formatted text) would end up with \n that we do not parse. We are only parsing for quotes which our script does handle.


As a result, I would like to reiterate, your return fails the copy paste test.


Therefore we will not be able to award you marks for this. There are many students who got this correct. I suggest you to check out some of their repos to see why they were able to get the right answer.


Kind regards


TDS Team

---
**Post ID:** 621947  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/3  

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


Dear Sir,


The required tag,`<!--email_off-->`, is indeed present in my deployed site at [https://23f1001231.github.io/testsite/](https://23f1001231.github.io/testsite/), as can be verified directly. Furthermore, this exact implementation was previously evaluated successfully and accepted as correct by the evaluation script for Graded Assignment 2, demonstrating its validity. Github repo link : [https://23f1001231.github.io/testsite/](https://23f1001231.github.io/testsite/)


[![The image shows a GitHub repository page displaying the contents of an `index.html` file.  The file contains a small amount of HTML code. The page also shows the file's commit history, indicating a recent update. The overall theme is dark.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/2/225974cc9b93a894713b0801f1103dc3f57e4248_2_690x187.png)image1094×298 61.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/2/225974cc9b93a894713b0801f1103dc3f57e4248.png)


[![The image shows a web browser displaying the source code of a webpage. The code includes a simple "Hello World" heading and an email address obfuscated within HTML comment tags.  The browser's title bar shows the URL of the webpage.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/a/4ae67ed3e0f3236c8652000d8ea64545c16fe996_2_690x231.png)image1056×355 37.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/a/4ae67ed3e0f3236c8652000d8ea64545c16fe996.png)


[![The image shows a coding interface with a question asking for a GitHub Pages URL.  A user has correctly entered a URL, which is marked as correct.  Below, instructions are given on how to clear the cache if changes aren't reflected.  A "Check" button is also present.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/d/8df7589d673e3fec6cdb32208c222b2a929dd400_2_690x119.png)image928×161 11.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/d/8df7589d673e3fec6cdb32208c222b2a929dd400.png)


Video proof below shows my solution as correct and valid by the evaluation script of the Graded Assignment.



[![The image shows a Google Colab notebook, displaying code and information about Google Colab.  A video thumbnail titled "Intro to Google Colab" is also visible. The overall theme suggests a tutorial or guide on using Google Colab.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/5/b5166263d9f0b525540bdb94c07a7c021b5dee2f.jpeg)](https://www.youtube.com/watch?v=AIYHzn5yoC8)

The error in Project 2 appears to arise from the evaluation script’s handling of the tag—specifically, its use of a regex that fails to detect `<!--email_off-->` when it follows an `<a>` element. This is a technical flaw in the evaluation process, not an issue with my solution. The inconsistency between the evaluation scripts for the Graded Assignment and Project 2 has resulted in a correct answer being unfairly marked as incorrect. Such ambiguity in automated evaluation is deeply concerning and leads to confusion and unwarranted penalization of students.


Denying marks due to technical discrepancies in the evaluation scripts, rather than the correctness of the submitted solution, is unjust. If this issue remains unresolved, it will negatively and unfairly impact my overall course grade, despite my submission being fully correct and in line with assignment requirements. This outcome, caused by factors outside my control, undermines the integrity and fairness of the evaluation process.


I respectfully request that you review my discrepancy issue in light of these facts and ensure that evaluation criteria are applied consistently. I kindly request you to reconsider my solution and award the marks that are rightfully due.


Thank you for your attention and understanding.


Best Regards,


Premdeep Maiti


![That's a completely black image.  There's nothing visible.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/d/2daeaa8b5f19f0bc209d976c02bd6acb51b00b0a.gif)



On Mon, Apr 21, 2025 at 5:36 PM <[22f3002542@ds.study.iitm.ac.in](mailto:22f3002542@ds.study.iitm.ac.in)> wrote:




Hi [23f1001231@ds.study.iitm.ac.in](mailto:23f1001231@ds.study.iitm.ac.in),


You reported the following issue for “Project2”, Question 3:


"My answer is correct. The error shows “actual”: “ tag not


found”. But there is  in my solution. The github page link


is [https://23f1001231.github.io/testsite/](https://23f1001231.github.io/testsite/)


and the github repo link is [GitHub - 23f1001231/testsite](https://github.com/23f1001231/testsite) This


solution has been accepted as correct answer in the graded assignment 2.


"


Our response:


“The precise tag is missing in your github pages. Just check with one of


the peer who have got this correct.”


Thanks,


TDS Team

---
**Post ID:** 621956  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/4  

[@carlton](/u/carlton) [@s.anand](/u/s.anand) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini) Sir


I wanted to respectfully bring to your attention a concern regarding the evaluation of my Project 2 submission.


My project is functioning properly in my browser, but it doesn’t use `http` or `https` in the URL—it’s accessed directly without a protocol. I believe this might have caused an issue with the evaluation script, rather than an actual error in my submission. I’d like to kindly request that the evaluation script be updated to account for such cases, as the core requirements of the project were fulfilled to the best of my understanding.


With due respect, I’ve invested a lot of time and effort into this project, and it’s disheartening to see that a technicality might affect the evaluation. We’ve studied exception handling in both Java and Python—so I was a bit curious (asking respectfully, of course!) why there wasn’t similar handling in the evaluation logic for edge cases like mine. I completely understand the depth of your knowledge, and I say this with all humility—I’m just trying to understand and express a genuine concern.


I don’t have professional experience in web or app development, but my cousin, who works in tech, told me that even in real-world projects, bugs can appear after deployment. That’s why we have QA and support teams in companies (or so I’ve been told!).


To be honest, I initially thought TDS would be   [easier](https://discourse.onlinedegree.iitm.ac.in/t/difficulty-rating-for-diploma-subjects-2-0-based-on-student-ratings-and-my-experience/85681) compared to Java, PDSA, or SC. Ironically, I’ve cleared all four subjects this term, including both projects—except TDS, where Project 2 has become a bit of a nightmare. Without the Project 2 score, I might end up passing with just an ‘E’ grade, which would hurt my overall CGPA. Worse, I’d have to repeat the course and pay the fee again—which isn’t covered under the CSR fund.


So, with the utmost respect and sincerity, I request you to please consider re-evaluating my submission using the updated endpoint. Not just for me, but there are several students whose hopes are resting on this project’s score. Updating the script shouldn’t affect students who already scored well, but it might help a few others avoid repeating the course unnecessarily.


I’m not asking for bonus marks or any special treatment—just a fair second look. As a law student (LLB), I deeply respect rules and processes. I only ask this in the spirit of fairness and with full respect for your time and effort.


Please consider this message as a humble and respectful request—I’m just exercising my right to politely express a concern.

---
**Post ID:** 621976  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/5  

We have made the update to your score and awarded you 4 marks (out of 20) for your endpoint.


Kind regards

---
**Post ID:** 621979  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/6  

[@carlton](/u/carlton)


So, marks will be awarded for both the questions I mentioned?

---
**Post ID:** 621980  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/7  

[@carlton](/u/carlton)


So, marks will be awarded for both the questions I mentioned?


…

---
**Post ID:** 621999  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/8  

[@carlton](/u/carlton)


??


…_______…

---
**Post ID:** 622098  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/9  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini) [@s.anand](/u/s.anand)


Please response. Efficient communication is very important in this type of course.

---
**Post ID:** 622108  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/10  

You already got an A and more marks will not change the grade. You have received an increase in your P2 score and that is reflected in your t score.

---
**Post ID:** 622109  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/11  

Sir can you please check my post [URGENT wrong score on dashboard - #2](https://discourse.onlinedegree.iitm.ac.in/t/urgent-wrong-score-on-dashboard/173206/2)


i got 70 in my mail for official score and now it shows 54 in my dashboard i have no clue whats going on

---
**Post ID:** 622114  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/12  

[@carlton](/u/carlton) Please reply me on this post [URGENT ATTN REQ: technical discrepancy and inconsistency in the evaluation scripts of graded assignment and project 2 - #4](https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/4)

---
**Post ID:** 622116  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/13  

The course team and operations have consulted on this. We will not be able to make an allowance for this request because the rule was applied uniformly for everyone.


Kind regards

---
**Post ID:** 622118  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/14  

[@jkmadathil](/u/jkmadathil)


Kindly ask developer to look into this.


Thanks


PS. There seems to be portal error that has nothing to do with the course team, Operations has been notified that there is a glitch on their front end that is showing the wrong grades and scores. Please wait for them to fix it.

---
**Post ID:** 622125  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/15  

I just wanted to request a re-evaluation of my project. I got 0 marks, but my deployed project is working fine and meets all the prerequisites mentioned. I had updated the domain using the API and submitted the correct link through the Google Form, but I think it was evaluated using the old domain. Also, one of my friends got 80 without HTTPS, so I’m a bit confused about the criteria. I’m not asking for an S or A grade—just a fair evaluation. I’ve put in a lot of effort and really don’t want to pay the fee again to repeat the course, especially since I already got 0 in P1. I hope you can please take another look.

---
**Post ID:** 622135  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/17  

Can we expect an update by today? [@carlton](/u/carlton)

---
**Post ID:** 622147  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/18  

sir i have mention issue i got but no update on this


[![The image shows two test cases from an API test suite.  Case 1 failed to find a hidden email in HTML, despite the email tag being present. Case 2 failed because the API returned a different result than expected when searching for a Hacker News post about a text editor.  A contact section is also present at the bottom.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c1658c8662c6eff1e4a28cfef341b496f4c4c7b9_2_353x500.jpeg)report (1)_page-00011242×1755 215 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c1658c8662c6eff1e4a28cfef341b496f4c4c7b9.jpeg)


[![The image shows a Hacker News search result, followed by a problem description and solution attempt regarding a JSON parsing task.  The task involves counting the occurrences of a specific key ("XF") within a deeply nested JSON file. An error message indicates an issue with the JSON file's validity.  The image also includes sections detailing the expected outcome and the user's approach to solving the problem.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/0/c08bc16b33fde11d9552d0ca2fe71b1b22d113e2_2_353x500.jpeg)report (1)_page-00021242×1755 179 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/0/c08bc16b33fde11d9552d0ca2fe71b1b22d113e2.jpeg)


[![The image shows a debugging log of a JSON processing task.  The author correctly parsed a nested JSON file to count occurrences of the key "XF," getting a correct count (14602). However, the API returned an error ("Invalid literal for int()"), indicating a problem on the API side, likely in its handling of the file input or data type conversion.  The author concludes their solution was correct for the original question, but might be affected by changes to the question's criteria.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/d/7d0d5a927877a33bb29013175f58685e9d17d897_2_353x500.jpeg)report (1)_page-00031242×1755 185 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7d0d5a927877a33bb29013175f58685e9d17d897.jpeg)

---
**Post ID:** 622162  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/19  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini) [@s.anand](/u/s.anand)


[![This is a student's online course portal showing their progress in a "Tools in Data Science" course at IIT Madras.  The page displays assignment scores, quiz results, project grades, the final exam score, and a final course grade of A (82.00).  A sidebar shows navigation options.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd9de6281660efb1bab7ed87439e74a985714637_2_279x500.png)2025-04-22_18-25555×992 79.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd9de6281660efb1bab7ed87439e74a985714637.png)



[carlton]     ([https://discourse.onlinedegree.iitm.ac.in/u/carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton))Regular


[1d](https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/2)


Hi Premdeep,


We will update your score to consider `\n` for SQL query.


Kind regards


TDS Team




[carlton]     ([https://discourse.onlinedegree.iitm.ac.in/u/carlton](https://discourse.onlinedegree.iitm.ac.in/u/carlton))Regular


[22h](https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/5)


We have made the update to your score and awarded you 4 marks (out of 20) for your endpoint.


Kind regards



According to the official dashboard, there has been no increase reflected in my Project 2 score, which remains at 20 out of 100. This is inconsistent with your claim that my score has already been updated.


I have previously submitted a formal discrepancy form for two questions that were incorrectly evaluated by the Project 2 evaluation script. Furthermore, [@carlton](/u/carlton) has explicitly confirmed that the marks for these questions would be updated. To date, this correction has not been implemented and my score hasn’t updated.


The marks in question are not trivial. If the corrections are made as promised, my overall course percentage will increase by a minimum of 6%. This is a substantial change that directly affects my academic record. The assertion that “more marks will not change the grade” overlooks the broader implications of accurate and fair assessment.


It is a fundamental principle of academic integrity and fairness that students receive the marks they have rightfully earned. Denying the correction of a clear and acknowledged error constitutes an unjust deprivation of my rightful academic standing. Such actions may not align with the principles of due process.


I respectfully request that you to update my Project 2 score to accurately reflect the corrections as confirmed by [@carlton](/u/carlton) , provide a clear clarification of my revised Project 2 score (out of 100) and ensure that my overall course percentage is recalculated accordingly.

---
**Post ID:** 622170  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/20  

Hello Sir,


I kindly request reevaluation for project 2 as its still showing 0 and I don’t see any logs in my endpoint


Also for assignment 1 grades tab( below modules tab) is showing 100 by on dashboard its reflecting 65 . Sir please have a look.

---
**Post ID:** 622178  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/21  

[@carlton](/u/carlton)


Project 2 marks update


Sir I am a degree potential student and i got 35 marks with U grade in TDS. My project 2 marks are not added.


The reason is one of my mistake that i misunderstood that we have to provide browser link for the project 2 instead of api one.


I am aware of two mails from  TDS team side to update the url but my browser link was working perfectly so did not updated it and when results came it said that 405 errror. and i got 0 marks.


I am giving the correct api link here :


[https://tdssolver-7s6meq5el-akbar-alis-projects-e047c36e.vercel.app/api/](https://tdssolver-7s6meq5el-akbar-alis-projects-e047c36e.vercel.app/api/)


Please sir help me about it. I am a degree potential student and  i will have to take TDS only in my next term.


Please help me sir i just need 5 marks. Please reevaluate me Sir.


One more thing is that when i tried to send post request using powershell,


curl was not working so i had to use something else. like …


[](#p-622178-define-the-endpoint-and-the-question-1)Define the endpoint and the question


$uri


= “[https://tdssolver-7s6meq5el-akbar-alis-projects-e047c36e.vercel.app/api/](https://tdssolver-7s6meq5el-akbar-alis-projects-e047c36e.vercel.app/api/)”


$questionText = “What is 17 multiplied by 8?”






Create the content body as form-urlencoded
$body = @{ question = $questionText }






Send the POST request
$response = Invoke-RestMethod -Uri $uri -Method Post -Body $body


-ContentType “application/x-www-form-urlencoded”






Show the result
$response


[![The image shows PowerShell code that queries a Hacker News RSS API to find the latest post about minimalism with at least 38 points.  The code constructs a POST request, sends it, and then extracts and prints the URL of the found post. The resulting URL is displayed at the bottom.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/3/336bbe479ddddaffbcfeb5f6fd15ea2e2ed03a4b.png)image1062×415 22.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/3/336bbe479ddddaffbcfeb5f6fd15ea2e2ed03a4b.png)

---
**Post ID:** 622233  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/23  

Please refer to this post.





![That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow/beige.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[URGENT ATTN REQ: technical discrepancy and inconsistency in the evaluation scripts of graded assignment and project 2](https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/2) [Tools in Data Science](/c/courses/tds-kb/34)


    Hi Premdeep, 
We will update your score to consider \n for SQL query. 
I had briefly read your post and incorrectly assumed that the script was not handling newline characters (which are invisible whitespaces). 
The prescription given by Anand in a live session exclusively conducted by him was clear. 
We should be able to copy paste your answer from the JSON response and put it in the GA and it should work. There only some notable exceptions, and this is where formatted text is expected. This qu…
  

Your logs have been shared with you. But I have pasted it here as a reference.


`[
    {
        "api": "http://172.232.122.21:8000/api/",
        "test_code": "GA1_q18",
        "status": "ERROR",
        "error": "near \"\"SELECT SUM(units * price) AS total_sales\\n        FROM tickets\\n        WHERE TRIM(LOWER(type)) = 'gold';\"\": syntax error"
    },
    {
        "api": "http://172.232.122.21:8000/api/",
        "test_code": "GA4_q6",
        "status": "FAILED",
        "actual": "\"http://www.engineerbetter.com/blog/yubikey-all-the-things/\"",
        "expected": "https://blog.jacobstechtavern.com/p/building-a-2fa-app-that-detects-patterns"
    },
    {
        "api": "http://172.232.122.21:8000/api/",
        "test_code": "GA2_q3",
        "status": "FAILED",
        "actual": "<!--email_off--> tag not found",
        "expected": "<!--email_off-->23f1001231@ds.study.iitm.ac.in<!--/email_off-->"
    },
    {
        "api": "http://172.232.122.21:8000/api/",
        "test_code": "GA3_q2",
        "status": "ERROR",
        "error": "invalid literal for int() with base 10: '{\"model\": \"gpt-4o-mini\", \"messages\": [{\"role\": \"system\", \"content\": \"Respond in JSON\"}, {\"role\": \"user\", \"content\": \"Generate 10 random addresses in the US\"}], \"response_format\": {\"type\": \"json_schem"
    },
    {
        "api": "http://172.232.122.21:8000/api/",
        "test_code": "GA5_q7",
        "status": "PASSED"
    }
]`

It is a fundamental principle of academic integrity and fairness that students receive the marks they have rightfully earned. Denying the correction of a clear and acknowledged error constitutes an unjust deprivation of my rightful academic standing. Such actions may not align with the principles of due process.



We have you scored currently at 12 out of 20.


You asked for a fair evaluation.


You actually should be scored 8 out of 20, reducing your T score from 82 to 78, just out of maintaining the principle of fairly evaluating everyone. This will result in a grade change for you.


If you still want a fair evaluation we are happy to forward your request to operations. [@jkmadathil](/u/jkmadathil)  has been consulted on this and course team together has looked at your grievance and we have made it publicly visible so that it can be judged fairly.


Kind regards

---
**Post ID:** 622237  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/24  

Hi [@23f1002997](/u/23f1002997)


It’s unfortunate that you had to go through this, but since it was your mistake to not update your URL despite repeated notifications, under whatever assumptions, there is nothing we can do. I can understand that a small mistake like this has lead to a setback for a term, and honestly I can relate very strongly with this. But take it as a life lesson and try to score well in the next term.


Best wishes


Saransh Saini

---
**Post ID:** 622292  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/25  

Hi [@Algsoch](/u/algsoch),


Case 1: This might be an error. Send me your github pages endpoint I’ll have a look.


Case 2: Question asked for the recent post where 2FA was mentioned with at least 95 points.


Case 3: Question asked for the number of times key “Y” appears.

---
**Post ID:** 622298  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/26  

Hi [@23f1001231](/u/23f1001231)


Your submission was validated by the course portal, so it testifies its correctness. But I want to clarify our side.


I checked your response. The problem is not that your tag is present in `<a>` tags. Its because your closing email_off tag doesn’t have a slash as mentioned in the question page.


![The image shows a snippet of code, likely from a configuration file or script.  It appears to contain an email address (`22f1001123@ds.study.iitm.ac.in`) obfuscated by  `<!--email_off-->` tags before and after it.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/2/12175ad65255c16916632d78f6798feac06a8910.png)


Moreover this was specifically mentioned in the question we sent you in the API request.


`"Publish a page using GitHub Pages that showcases your work. Ensure that your email address 23f1001231@ds.study.iitm.ac.in is in the page's HTML. GitHub pages are served via CloudFlare which obfuscates emails. So, wrap your email address inside a: <!--email_off-->23f1001231@ds.study.iitm.ac.in<!--/email_off--> What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/"`
So, in short it wasn’t a bug in our script, rather leniency given by the course portal.

---
**Post ID:** 622315  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/27  

[github.com](https://github.com/algsoch/portfolio-1744830932)



![This is a screenshot of a GitHub page showing a portfolio for a user named `algsoch`.  The portfolio's ID is `1744830932`, and it's associated with the email address `24f2006438@ds.study.iitm.ac.in`. The page displays that the portfolio has one contributor, zero issues, zero stars, and zero forks. A small image shows the owner standing in front of a "Birthday" backdrop.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/0/f09d3449e5f92c59aa581d28ff633e44e2941426_2_690x344.png)
[GitHub - algsoch/portfolio-1744830932: Portfolio page for 24f2006438@ds.study.iitm.ac.in](https://github.com/algsoch/portfolio-1744830932)
Portfolio page for 24f2006438@ds.study.iitm.ac.in

---
**Post ID:** 622380  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/28  

[@carlton](/u/carlton) please look into this!!!

---
**Post ID:** 622395  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/29  

Hi Shrishty,


We have shared the logs with you. The HTTP 500 error indicates there was a problem with your backend and was generating an error.


`[
    {
        "api": "https://tdsproject2-production.up.railway.app/api/",
        "test_code": "GA1_q18",
        "status": "FAILED",
        "error": "HTTP 500: {\"detail\":\"cannot access local variable 'httpx' where it is not associated with a value\"}"
    },
    {
        "api": "https://tdsproject2-production.up.railway.app/api/",
        "test_code": "GA4_q6",
        "status": "FAILED",
        "error": "HTTP 500: {\"detail\":\"cannot access local variable 'httpx' where it is not associated with a value\"}"
    },
    {
        "api": "https://tdsproject2-production.up.railway.app/api/",
        "test_code": "GA2_q3",
        "status": "FAILED",
        "error": "HTTP 500: {\"detail\":\"cannot access local variable 'httpx' where it is not associated with a value\"}"
    },
    {
        "api": "https://tdsproject2-production.up.railway.app/api/",
        "test_code": "GA3_q2",
        "status": "FAILED",
        "error": "HTTP 500: {\"detail\":\"cannot access local variable 'httpx' where it is not associated with a value\"}"
    },
    {
        "api": "https://tdsproject2-production.up.railway.app/api/",
        "test_code": "GA5_q7",
        "status": "FAILED",
        "error": "HTTP 500: {\"detail\":\"cannot access local variable 'httpx' where it is not associated with a value\"}"
    }
]`
Kind regards

---
**Post ID:** 623515  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/30  

Sir, I have extracted the files from the GitHub Repository, built my DockerFile withe the DockerImage I have posted. The build is successful and the dockerimage is also running sir. I have attached the screen shot below


[![The image shows a terminal window displaying the output of a Docker build process.  Numerous SHA256 hashes are listed alongside file sizes and build times.  The process successfully builds and runs a Uvicorn application, which is confirmed by the final INFO messages.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f58734cfd90a7011b3effca56b9023d51b773c0.png)Screenshot 2025-04-12 1153421466×702 50.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f58734cfd90a7011b3effca56b9023d51b773c0.png)


Sir, But I couldn’t run the last command you gave,


`uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000`
As I dont have evaluate.py


But, the DockerImage is built and is running without error sir.


Please guide me after this sir


Thank You So much sir


Sir, I already posted before 10 days, I didn’t get any reply. I am posting again

---
**Post ID:** 623516  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/31  

Good Afternoon Sir.


This is regarding project 1 and project 2.


Project-1 Evaluation


Sir, For the project 1, I have written the code, uploaded in GitHub and the dockerfile image is created and uploaded successfully.


Sir, I already contacted regarding Project - 1, you said to check it by replicating the test environment. I did till running the dockerfile but I needed evaluate.py sir, which I didn’t get it. I got only 5 marks sir. Can you please check my code once sir and verify it as I have written the code and the dockerfile is running successfully.


Project-2 Evaluation


Regarding project 2 also, I have uploaded my code in GitHub and deployed my app in Vercel. But, I got 0 sir. Can you check my code once again and verify it? According to the guidance given, I deployed my app through Vercel. The app got deployed but I am getting 404 Error, even after trying any troubleshooting method. Maybe, Vercel is in development stage.


Sir, but I wrote the code and deployed, but I got 0 marks only. Please check it and guide me to get it corrected. Sir, due to the projects I got poor marks on TDS. Please, I request you to re-evaluate and give me correct marks.


In anticipation of quick response


Thank You


Sir, I have filled the E-Mail for discrepancy, but there is no change. Please help me out sir.


Thank You

---
**Post ID:** 623521  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/32  

Project 1 : You tried to copy parent folder(Ref:line number 8 in your [Dockerfile](https://github.com/sudhishssn134/project_1_tds/blob/main/Dockerfile)) but there is no parent folder with respect to github repo’s root folder, so it fails evaluation.


Project 2 : Response we received through google form was [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api) which is local host url not a vercel endpoint.

