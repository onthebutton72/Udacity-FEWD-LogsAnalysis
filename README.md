# Udacity FSWD Project: Logs Analysis

This is the first project for the Udacity Front End Web Developer Nanodegree.  This project involves creating a reporting tool that prints out reports (in plain text) based on the data in the database.  This reporting tool is a Python program using the psycopg2 module to connect to the database.
## Table of Contents

* [Contents](#contents)
* [Instructions](#instructions)
* [Views](#views)
* [Creator](#creators)

## Contents

*  There are three files in this project.  
    - main.py
    - output.txt
    - newsdata.sql

## Instructions

* Clone or download the repository: https://github.com/onthebutton72/fswd-logs-analysis.git
* Change directory to the cloned/downloaded folder
* Download and extract the newsdata.sql file from Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* It is recommended the user use a virtual machine to ensure they are using the same environment that this project was developed on, running on your computer.  You can download [Vagrant](https://www.vagrantup.com/) and [Virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install and manage your virtual machine.  Use vagrant up to bring the virtual machine online and vagrant ssh to login
* Load the database using 
```psql - d news```
* Create the Views from below
* Exit psql with ```CTRL + d```
* Execute command ```python main.py``` (you will need to have Python version 2.7 installed)


## Views

```sql
CREATE VIEW errors AS 

SELECT date(time), count(status)  

AS error 

FROM log 

WHERE status = '404 NOT FOUND' 

GROUP BY date(time) 

ORDER BY date(time)  

DESC;


CREATE VIEW totals AS 

SELECT date(time), count(status)  

AS total 

FROM log 

GROUP BY date(time) 

ORDER BY date(time)  

DESC;
```

## Creators

* Jamie Martinez

