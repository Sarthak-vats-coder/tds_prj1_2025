# Urgent Attn Needed: Project 2 Discrepency for GA2_q3 and GA1_q18
_Slug: _

---
**Post ID:** 621668  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-needed-project-2-discrepency-for-ga2-q3-and-ga1-q18/173113/1  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


I have discrepency in two questions.


[](#p-621668-h-1-ga2_q3-1)1. GA2_q3
In GA2_q3 my answer is correct. The github page link is [https://23f1001231.github.io/testsite/](https://23f1001231.github.io/testsite/) and github repo link is [GitHub - 23f1001231/testsite](https://github.com/23f1001231/testsite).


The error in the log is that `<!--email_off-->` tag is missing.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/3/8377bbe918707bf3c306dc456301b60748cb3ee0.png)image965×160 7.52 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/3/8377bbe918707bf3c306dc456301b60748cb3ee0.png)


But  the `<!--email_off-->` tag is present as you can see below


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/2/82128d8e10a7c90eac338770680339e467b4ff37_2_690x154.png)image915×205 14.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/2/82128d8e10a7c90eac338770680339e467b4ff37.png)


Not only that, this solution has also passed in the Graded Assignment 2.


Proof:


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/0/0081bc0b8fe1a584be6ad3dc2982e7db95a136ec_2_690x278.png)image1805×728 99.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/0/0081bc0b8fe1a584be6ad3dc2982e7db95a136ec.png)


I think the evaluation script failed because `<!--email_off-->` was inside a tag and the regex in script could not determined it.


[](#p-621668-h-2-ga1_q18-2)2. GA1_q18
In GA1_q18 my answer is correct. The escaping character in the answer string of the response json which contains the SQL query  is causing the Syntax error in evaluation script’s end as it has not handled those escaping characters properly while running the SQL query .


The SQL query is correct and passed the Graded Assignment 1 which can be seen below.


Proof:


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/c/9c618fd3f8cd0f9fbc4992316d653a6b3828b745_2_690x376.png)image1686×920 68.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/c/9c618fd3f8cd0f9fbc4992316d653a6b3828b745.png)


Error in the evaluation log due to improper handling of escape characters in the answer string of the response json which contains the SQL query is causing the Syntax error which can be seen below:


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/e/9ec078accbbdffcb012d67d7f7284455dc219f66_2_690x76.png)image1438×159 8.23 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/e/9ec078accbbdffcb012d67d7f7284455dc219f66.png)


These discrepancies have been reported to the discrepancy form also [http://64.227.131.20:4200/](http://64.227.131.20:4200/)


Please do the needful and the update the marks for the above correct answers. These discrepancies will badly affect by my course grade overall.

