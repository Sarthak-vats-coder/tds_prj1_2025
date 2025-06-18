# Graded assignment 6
_Slug: _

---
**Post ID:** 603963  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/1  

Please post any questions related to [Graded Assignment 6 - Data Analysis](https://seek.onlinedegree.iitm.ac.in/courses/ns_25t1_se2002?id=25&type=assignment&tab=courses&unitId=23)


Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.


Deadline 2025-03-15T18:30:00Z

---
**Post ID:** 603964  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/2  



---
**Post ID:** 603966  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/3  

The answer choices for questions 1 and 2 in graded assignment 6 are quite confusing. Both questions are single-select, yet three out of the four options are correct in each case. I’m unsure whether to choose one of the correct options or if the question is actually asking for the incorrect one. Could someone please clarify?


[@carlton](/u/carlton)

---
**Post ID:** 602355  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/4  

[@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


I have similar concern


For Q1, I used the following code:


`print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = kk['price_retention'].corr(kk[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')`
And got the following output:


`Pearson correlation for Karnataka between price retention and column
	Mileage (km/l)            : 0.03
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.04`
Whereas options are below where none of them are correct.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fa9a2e601c94da84cbd25c406235d1009b204c.png)image281×219 9.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fa9a2e601c94da84cbd25c406235d1009b204c.png)


Whereas for Q2 (Punjab and Yamaha) I used the following code:


`print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') & (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = pb['price_retention'].corr(pb[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')`
and got the following answers:


`Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l)            : 0.24
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.08`
The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/51b03d00c3e962e6c4fc7fc64930a23e82500006.png)image278×216 9.19 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/51b03d00c3e962e6c4fc7fc64930a23e82500006.png)

---
**Post ID:** 603367  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/5  

[@24f2006061](/u/24f2006061) We are looking into it. We will update based on our analysis. Thanks for letting us know.


Kind regards

---
**Post ID:** 603970  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/6  

I used a python script to get the solution to quesiton 1 of week 6 graded assignment. It matches three options. Is this a bug or like we then need to analyze using the pearson coefficient to determine which option is the correct one


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630_2_690x131.png)image1383×263 25 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630.png)

---
**Post ID:** 604313  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/7  

Dear Sirs, Can we have some response on these issues related particularly to the questions 1 and 2 of Graded Assignment 6. It looks like multiple options are correct in the given options. Any guidance or hint, on how to arrive at the right answer will be helpful. Thanks and regards. [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)

---
**Post ID:** 604590  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/8  

Yeah…Even I am facing the same issue. Out of the 4 options provided, 3 options are correct in my case both for Q1 & Q2, but both these questions are single-choice questions. Kindly look into it and help us out [@carlton](/u/carlton) !

---
**Post ID:** 605292  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/9  

I guess for both Q1 & Q2, we need to find the option that is having stronger correlation (positive/negative). Please correct me if I am wrong.

---
**Post ID:** 605551  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/10  

Any updates on these? I am too facing the same issue.


[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)

---
**Post ID:** 605753  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/11  

In GA6 for first 2 questions 3 out of 4 options are correct. Even the question is not clearly asking anything. Kindly suggest are we supposed to select the wrong one


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04_2_690x190.png)image2083×575 47.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04.png)

---
**Post ID:** 605798  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/12  

Kindly update us regarding the status of Q1 & Q2 [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 605954  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/13  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh_Saini](/u/saransh_saini)


Dear TDS Team,


There are multiple issues in Graded Assignment 6 that require urgent attention:



Questions 1 and 2, along with their options, are ambiguous.
In Questions 3 and 4, I am unable to obtain an exact answer that matches any of the given options, despite trying multiple approaches, including the Excel regression method and other models in a Google Colab file.
The data for Question 10 is missing. I attempted to run the shapefile in QGIS, but it resulted in an error. Additionally, I searched for the shapefile of New York roads on official websites, but their servers are currently under maintenance.

The assignment deadline is approaching, but these issues remain unresolved. Kindly look into this matter at the earliest and provide a resolution as soon as possible.


Thank you for your support.

---
**Post ID:** 605995  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/14  

Yes, there are no specifics in Q1 to Q4 and are quite ambiguous.


For instance:



forecast the 2027 resale value of the Hero - HF Deluxe in Gujarat, using historical data.



but is this talking about the average resale value as no input features are specified?

---
**Post ID:** 606007  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/15  

Let’s wait for their response.


I submitted nearby option for Q3 and Q4

---
**Post ID:** 606017  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/16  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh_Saini](/u/saransh_saini)


Can you please provide any update ASAP as the deadline for this GA coincides with Quiz 2. With many ambiguities unresolved it’s hard to solve this and study for Quiz 2 (and do offline college work even though that’s not your problem).


Thanks

---
**Post ID:** 606228  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/17  

Hi @all


Question intends you to select most correlated one.


Select option which is absolute highest.

---
**Post ID:** 606558  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/18  

[@Jivraj](/u/jivraj)  - Can you please check answer choices for Q7 for GA6 where no choices are matching with the answer. The answer is coming to around 11.5 kms which is 11500 meters.


Q.A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction : (26.5596,-99.5336) ;Maple Fields Station : (26.4212,-99.4597);South Glen Crossing : (26.5962,-99.5243);Cedar Creek Retreat : (26.56,-99.4519) & Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance

---
**Post ID:** 606603  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/19  

[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b_2_690x197.png)image1318×377 34.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b.png)


what to do if 3 options have same value -0.04 and all are correct?

---
**Post ID:** 606761  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/20  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


My question 7 for GA6 is :


A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance


Whose options provided are :


10418 meters


12287 meters


10965 meters


11149 meters


However, after trying all methods out there my distance comes out to be 6873 meters, I selected 10418 as the answer (closest approximation to 6873 meters)


I assume that the question must have been central command post to summit shores village (whose answer turns out to be 12287 meters)


Kindly look into the question, and let me know about the same (the destination from central command post)

---
**Post ID:** 606802  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/21  

Have you succeeded in running the shape file for Q10? It seems to have some error.


[@lakshaygarg654](/u/lakshaygarg654)

---
**Post ID:** 606808  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/22  

No,


I use google to get MTFCC code for given road segment and  after that mtfcc pdf to classify that road segment.

---
**Post ID:** 606825  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/23  

I  downloaded the complete shape file zip from the [census.gov](http://census.gov) site.


Here is the link: [https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl_2024_36_prisecroads.zip](https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl_2024_36_prisecroads.zip)


It works fine in QGIS.


[@lakshaygarg654](/u/lakshaygarg654)

---
**Post ID:** 606854  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/24  

they have not provide all the files needed to read that shp file in the question .


but your link includes them. thanks…

---
**Post ID:** 606897  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/25  

I tried to access shapefile from official website 4-5 days ago, but server was under maintenance. I will check again Q10 after quiz 2.


Thanks for sharing.

---
**Post ID:** 607050  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/26  

My question 9 for GA6 is :


[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/e/9e4fdb96e0a90caace70968fd4201106dc133169.png)Screenshot 2025-03-15 205444878×668 38.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/e/9e4fdb96e0a90caace70968fd4201106dc133169.png)


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/0/0004348c8331f2b18dd055c7397be51c8c692902_2_690x189.png)Screenshot 2025-03-15 2054561333×366 45.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/0/0004348c8331f2b18dd055c7397be51c8c692902.png)


I solved it in colab but options are getting mismatched there…kindly clarify this issue..

---
**Post ID:** 607057  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/28  

for the above question the options are None of these are matching and answer is around 11.5 kms


3848 meters


6265 meters


4110 meters


5106 meters

---
**Post ID:** 607119  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/29  

For 7th Question in GA6 I got the answer 14265.93 Meters but the option I have in 7th are


6069 meters


7687 meters


6106 meters


7035 meters


[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---
**Post ID:** 607151  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/30  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


for question 4, i have tried `=forecast` and also `=forecast.ets`, both of them are not working. There are two columns for years. One is year of manufacturing, another is year of registration. which one to take.


for question 7, none of the options match. I am selecting the `MOST ACCURATE` among the given options. Hope, it is correct

---
**Post ID:** 607211  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/31  

Can anyone help me out on how to approach and solve the 10th question please!?

---
**Post ID:** 607252  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/32  

Check the distances of other locations from the central location. One student found Question 7 of the GA6 Option Set based on the distances of other points, which do not match the requirements of Question 7.

---
**Post ID:** 607272  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/33  

i have the same issue

---
**Post ID:** 607273  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/34  

yes i have the same issue


and i got the same answer and am give the same options


[@carlton](/u/carlton) sir what to do?

---
**Post ID:** 607277  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/35  

[@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


For 7th Question in GA6 I got the answer 14265.9275 Meters but the option I have in 7th are


6069 meters


7687 meters


6106 meters


7035 meters

---
**Post ID:** 607316  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/36  

Hello Sir,


Can you please check if this is the right answer. As per email received from [@carlton](/u/carlton) sir we should select the absolute maximum value.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/4/b468c32e53fddf462c583b8664f183dd7afe37aa_2_690x277.png)image978×393 23.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/4/b468c32e53fddf462c583b8664f183dd7afe37aa.png)


Example : If we get answers as -0.3 and 0.2 then -0.3 is the right answer as it’s absolut value is maximum.


For the first question the correlation matrix is as follows,


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/5/c524c9f7645716e0fac9d8850df15c4c20af05dc_2_690x397.png)image748×431 17.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/5/c524c9f7645716e0fac9d8850df15c4c20af05dc.png)


So shouldn’t it be -0.13?

---
**Post ID:** 607333  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/37  

Thanks for the colour picture.


If you read the aforementioned email…


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/0/f0a5df3069d591c0175e61d70123d9ffb4ec7e83_2_690x247.png)Screenshot 2025-03-17 at 9.09.55 am1760×632 65.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/0/f0a5df3069d591c0175e61d70123d9ffb4ec7e83.png)


Kind regards (in colour ![Image description failed](https://emoji.discourse-cdn.com/google/wink.png?v=14))

---
**Post ID:** 608219  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/38  

Thank you sir. i have got questions 1 and 2 both marked as 0.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/7/97636ac2d59c3df1caf852a42d90de4642e8ce6f_2_690x329.png)image962×459 29.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/7/97636ac2d59c3df1caf852a42d90de4642e8ce6f.png)


In my case Please note the above two questions are asked to calculate pearson correlation coefficient for KTM brand and for maharashtra and Karnataka states.


I have used excel to calculate the pearson correlation coefficient. Below the values I got for each question. Please verify.


|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for Karnataka||


-0.026685695


|pearson correlation coefficient between average distance travelled and Price retention for kTM for karnataka||


0.003953219


|pearson correlation coefficient between average Engine capacity and Price retention for kTM for karnataka||


-0.010839295


|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for maharashta||


0.029128825


|pearson correlation coefficient between average distance travelled and Price retention for kTM for Maharashtra||


0.013019585


|pearson correlation coefficient between average Engine capacity and Price retention for kTM for Maharashtra||


-0.056866212

---
**Post ID:** 608222  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/39  

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)


Dear sirs,


I have question no 7 got marked as 0. Please check the question below and the haversine distance for the given post comes to around 11.5 kms which is not matccing with any of the options and I have selected the closest answer. please check and let me know.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/f/ff2eccf6d2263eb106345ce8b07d037c0a417845_2_690x390.png)image935×529 40.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ff2eccf6d2263eb106345ce8b07d037c0a417845.png)

---
**Post ID:** 608561  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/40  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)


I did raise the question 2 days before the GA6 Deadline and doing so again after being marked as incorrect


My question 7 was A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance


10418 meters


12287 meters


10965 meters


11149 meters


Whose right answer turned out 6873, however the answer pushed is 12287 meters, which is nowhere near the closest options (it would’ve been correct if the destination was summit shores village which isn’t the case with this question)


Also, my question 4 was :


As an investment analyst monitoring motorcycle resale values, develop a forecasting model to predict future resale prices by brand and segment, considering seasonality and long-term trends. Specifically, forecast the 2027 resale value of the Kawasaki - Ninja 300 in Tamil Nadu, using historical data.


134483


94774


150666


199711


Whose correct option (through different methods and algorithms) was approximately closest to 94774 and again answer pushed is 150666 which again turns out to be incorrect


So is the case with questions 1 and 2 (where answers aren’t pushed according to absolute values, but as conveyed earlier, I believe this shall be resolved)


Kindly look into it


Thanks and Regards

---
**Post ID:** 608883  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/41  

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh_Saini](/u/saransh_saini)


In Q4 , neither which regression model to use is given nor the what random state to use is given. I tried linear regression, random forest regression but it is giving   answer which vary each time I compute, also, the option values are quite close.


[![Image description failed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/d/7dbfae953c7d9e015dbc80328ef657b813ba912d_2_690x250.png)image1227×446 24 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7dbfae953c7d9e015dbc80328ef657b813ba912d.png)

---
**Post ID:** 609762  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/43  

@all


we are looking into problems with question 4, 6 and 10.

---
**Post ID:** 618164  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/44  

Hi,


Have the corrections been done on GA6 marks?

---
**Post ID:** 618197  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/45  

Yes, corrections have been done in Ga6 marks.

---
**Post ID:** 618321  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/46  

Just to confirm, were the answers shown on the portal correct because I’m getting the same score as shown in the portal.

