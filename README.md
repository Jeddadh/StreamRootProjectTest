# Report : Streamroot Test
The repo contains:
-	data_analysis.py : by executing this file you obtain different tables used in this document
-	data_visualisation : by executing this file you obtain different data vizualisation used in this document
-    report.pdf : this readme file in pdf format

## I.	Tech choices & Installation requirements :



### Tech choices :

To analyse and process the given data, I choose to use the Python library Pandas for many reasons:

-	The pandas library is open-source
-	It has a large set of statistical functions and methods.
-	It is combined with python:
o	Gives us the possibility to visualize the data using matplotlib
o	Python has other advanced libraries to do mathematical and statistical calculus like numpy and scipy.
-	I am used to work with Python.

### Installation Requirements:

     Install Python3
     Install pandas (you can use pip3 install panda in the command line)
     Install matplotlib (if it is not already installed with python3)


## II.	Method & data analysis

NB: the first line is a comment. Pandas interprets the first line as a header (by default). I left the “#” so in this document and in the code, I use “#stream” instead of “stream”

1)	Import the data and transform it to a pandas dataframe
`stream_data = pd.DataFrame(pd.read_csv("data (1).csv"))`
2)	Have a brief look at the data using :

`stream_data.head()`

which gives us a look at the first 5 rows of the data.
<img width="718" alt="capture d ecran 2017-06-08 a 16 40 36" src="https://user-images.githubusercontent.com/24195205/26934319-550f7bfe-4c69-11e7-9e58-cb884f06c9ec.png">

3)	Have a global look at the data using the function describe
`stream_data.describe()`
<img width="713" alt="capture d ecran 2017-06-08 a 16 42 16" src="https://user-images.githubusercontent.com/24195205/26934390-8419c76a-4c69-11e7-9b1e-8388c0b93b73.png">

- we notice that the column “cdn” has not the same number of components as the other columns, there is one missing data (534953 vs 534954) .To deal with this we delete all the rows that have missing data. We use the function : `stream_data.dropna(axis=0, how='any')`
- we can see the number of values that takes every variable. 
9 for #stream, 5 for isp, 4 for browser and 2 for connected
- We can notice also that:
  - The 3rd video is the most viewed
  - Arange is the most used isp
  - EarthWolf is the most used browser
4)	Add 3 columns:

  - data_downloaded = p2p + cdn represents the global data downloaded for every video content
 
  - p2p_percentage = p2p/ data_downloaded : represents the percentage of the video downloaded using p2p (because video size is different from one video to an other)
 
  - cdn_percentage = cdn/data_downloaded : represents the percentage of the video downloaded using cdn.
These 3 columns allow us to compare well and have a clearer view to the data.

5.	Analysis using every variable:
#### a. #stream:  
<img width="469" alt="capture d ecran 2017-06-08 a 16 46 58" src="https://user-images.githubusercontent.com/24195205/26934611-22c8d720-4c6a-11e7-9cad-34e7826a04c2.png">


<img width="436" alt="capture d ecran 2017-06-08 a 16 58 22" src="https://user-images.githubusercontent.com/24195205/26935240-b9650cfc-4c6b-11e7-8237-d7809a934970.png">

<img width="346" alt="capture d ecran 2017-06-08 a 16 57 15" src="https://user-images.githubusercontent.com/24195205/26935171-90fecff0-4c6b-11e7-9910-54a472e272dc.png">

- We notice that the The video 3 and 4 have the lower percentage of data downloaded using p2p. even if the video 3 is the most viewed (may be the users are not connected in the same time or are not geographically near to others)

#### b. Connected :
<img width="550" alt="capture d ecran 2017-06-08 a 17 01 04" src="https://user-images.githubusercontent.com/24195205/26935382-175804ae-4c6c-11e7-903a-3b45b942c706.png">

- 	We notice that if the user is not connected to the backend, the data cannot be downloaded using p2p.

#### c.	Browser :
<img width="604" alt="capture d ecran 2017-06-08 a 17 02 43" src="https://user-images.githubusercontent.com/24195205/26935465-543ac942-4c6c-11e7-9097-bde04cad097e.png">
<img width="456" alt="capture d ecran 2017-06-08 a 17 05 06" src="https://user-images.githubusercontent.com/24195205/26935595-a7293134-4c6c-11e7-98ca-156e344d7977.png">
- The mean of p2p_percentage for Vectrice browser is very low compared to the tree other browsers even if the number of people who are connected to the backend is higher using this browser.
<img width="562" alt="capture d ecran 2017-06-08 a 17 06 00" src="https://user-images.githubusercontent.com/24195205/26935639-c6612336-4c6c-11e7-9d18-0c23f49ae906.png">
- Fortunately, vectrice represents only 3,92% of used browsers :
<img width="405" alt="capture d ecran 2017-06-08 a 17 07 13" src="https://user-images.githubusercontent.com/24195205/26935697-f2c7952c-4c6c-11e7-85ad-fcae11a9bc5a.png">


#### d.	Isp:
<img width="471" alt="capture d ecran 2017-06-08 a 17 13 14" src="https://user-images.githubusercontent.com/24195205/26936030-cc755674-4c6d-11e7-875b-b1f1c812fd9b.png">
<img width="620" alt="capture d ecran 2017-06-08 a 17 14 36" src="https://user-images.githubusercontent.com/24195205/26936111-fa5554fe-4c6d-11e7-8094-48047acf4ed5.png">

- The mean of p2p_percentage for Datch Telecom and olga isp is low compared to the tree other isps.

<img width="671" alt="capture d ecran 2017-06-08 a 17 15 53" src="https://user-images.githubusercontent.com/24195205/26936172-29ace820-4c6e-11e7-805c-81168ab2366a.png">

- Using this table we can see also that it seems that there is no relation between the browser and the isp (the percentage for Vertice is always lower independently of the isp /  the percentage for Datch Telecam and Olga is always lower independently of the browser )


## III.	Data-driven Recommendations

By analyzing the given data, I recommend the next :

-	Try to find why the p2p_percentage of the 3rd video is not very high even if it is the most viewed.
-	Explore the technology used in vectrice browser to find out what hinders the downloading using p2p, and try to adapt your technology to that of vectrice to cover as many users as possible. 
-	we notice that p2p technology may not be supported by Datch Telecom, for that it serves its clients directly using cdn network. Thus, we can suppose that the clients of this isp are not satisfied due to the problems of cdn network( low debit , interruption of service...) which justify the low use of this isp. Maybe, you can propose your service to this isp to increase the number of its users.
