
UNGM Tender Data Mining

This is a script that fetches all tenders for given days from UNGM. And Stores it in DB and output.csv.
Intension of this script is to show Data Mining process. The same methodologies can be used for Other ETL process.

Dir Structure:
Scripts : contains Webscrapper 
Html : contains HTML output. This can be used to show same on website to customer. And output.csv

How to run:
There are run.ps1 file. You can run this using powershell.
It will create venv.
Installs all required library.
And Run the script for you.

Inputs: (script will ask for)
1. No of Days you want to fetch data of.
2. No of Records you want to fetch.

Output: (Both files are generated on first run. Though there is copy incase you are checking from github.)
1. CSV file with Latest tender records. Available at ./output.csv and ./Output/output.csv
2. Database table tblTenders with tenders records. 

After running please dont forget to check output.csv . 
If you also wanna check DB you can do so using SQLite Viewer Extension of VS Code.
https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer


If you face any issue. Feel free to reach at choudharysahil0447@gmail.com
Best Regards : Sahil Choudhary.


Disclaimer:
Do not use this code in production.
Do not share this code. This code is for inteview purpose only.
