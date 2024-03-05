from time import time
from scripts.webScrapper import WebScrapper
import datetime
from datetime import datetime, timedelta
from Library.Customs.converter import DB_Converter


print('\n'*3)
print("*"*30)
print("\n\nScrapper Start from Here.")
print("Please Watch out for your input for number of days.")

default_input_var = 2
input_var = input(f"\nEnter the How many previous days of data you want to fetch in interger type : eg(1,2,3,...) : \n> Default [{default_input_var}] : ")
if input_var == '':
    input_var = default_input_var
else:
    input_var = int(input_var)

default_dataCount = 30
dataCount = input(f'\nEnter number of Records to fetch : eg 10 , 20 , 30 , 100, 200 ,...\n> Default [{default_dataCount}] : ') 
if dataCount == '':
    dataCount = default_dataCount
else:
    dataCount = int(dataCount)

executionStartTime = time()

publishStartDate = str((datetime.today()- timedelta(input_var)).strftime('%Y-%m-%d'))
publishEndDate = str((datetime.today()).strftime('%Y-%m-%d'))
expiryDate = datetime.today().strftime("%Y-%m-%d")

webScrapObj = WebScrapper(publishStartDate,publishEndDate,expiryDate,dataCount)
webScrapObj.getData()
webScrapObj.insertRecord()
executionTime = time()-executionStartTime
print(f"Time Taken To Execute {int(executionTime/60)}min {int(executionTime%60)}sec")
quitTxt = ""

dbc = DB_Converter.to_csv()

print('\n\n\nDont Forget to check output. Its in ./output.csv and ./Output/')
print("\nPress Q or q to Quit")
while str(quitTxt).lower != str("q").lower:
    quitTxt = str(input("Please Input : "))
    print("\nThank you for trying UNGM Data Mining Scripts.\nBest Regards. Sahil Choudhary.")
exit(0)

