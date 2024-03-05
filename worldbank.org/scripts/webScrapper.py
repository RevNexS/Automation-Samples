# from Library.Customs.
from Library.Customs.translator import DataTranslator
from datetime import datetime as dt
from Library.Customs.dbManager import DbManager
from Library.Customs.operations import Operations as ops
from Library.Customs import country
# from Library.Customs.DatabaseJson import JsonData

from Library.Customs.DatabaseJson import JsonData
import country_converter as coco


import requests
from bs4 import BeautifulSoup

import dateparser as dp
import json
import time
import re


class WebScrapper:

    publishStartDate = ""
    publishEndDate = ""
    dataCount = 0
    expiryDate = ""
    url = ""

    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    

    __dataObj = []
    __finalDataObj = []
    __finalDataObjNonTrans = []


    def __init__(self,publishStartDate,publishEndDate,expiryDate,TotalRecords,dataCount):
        
        self.publishStartDate = publishStartDate
        self.publishEndDate = publishEndDate
        self.expiryDate = expiryDate
        self.TotalRecords = TotalRecords
        self.skipCount = 0
        self.total_pages = 0
        self.nonTranslatedData = 0
        self.isInCountryTable = JsonData.isInCountryTable
        self.CountryNotFoundList = set()
        self.dataCount = dataCount

        self.gtranslate = DataTranslator.gtranslateData

    def printTender(self,TenderNumber,TenderName, TenderDeadline):
        '''
            Show Fetch Data to While runing scripts.
        '''
        print(f'-----------------------------------------------------')
        print(f'Tender Number: {TenderNumber}')
        print(f'Tender Name: {TenderName}')
        print(f'Tender Deadline: {TenderDeadline}')
        print(f'----------------------------------------------------')


    def repeatTrans03(self, Text: str): # 03 cause its the 3rd itteration of code.
        Text = Text.strip()

        if Text == '':
            return Text
        else:
            nonTransText = Text

        TransText = ''
        count = 1
        while nonTransText == TransText or TransText == '':
            TransText = self.gtranslate(nonTransText)
            count += 1 
            if count == 6: return TransText
            if count > 3: print('Waiting for Internet . 180sec') , time.sleep(180) 
            #if count == 4:

        return TransText


    def getResponse1(self, PageNo):
        try:
            
            headers = {
              'accept': 'application/json, text/plain, */*',
              'accept-language': 'en-US,en;q=0.8',
              'origin': 'https://projects.worldbank.org',
              'referer': 'https://projects.worldbank.org/',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
            }

            RecordInOneRequest = 1000
            PageNo = PageNo * 1000 # Hince Page 1 = 0 , Page 2 = 20 , Pg 3 = 40, page 3 = 60
            url = f"https://search.worldbank.org/api/v2/procnotices?format=json&fct=procurement_group_desc_exact,notice_type_exact,procurement_method_code_exact,procurement_method_name_exact,project_ctry_code_exact,project_ctry_name_exact,regionname_exact,rregioncode,project_id,sector_exact,sectorcode_exact&fl=id,bid_description,project_ctry_name,project_name,notice_type,notice_status,notice_lang_name,submission_date,noticedate&srt=submission_date%20desc,id%20asc&apilang=en&rows={RecordInOneRequest}&lang=en&showrecent=true&srce=notices&os={PageNo}"
            response = requests.post(url=url, headers=headers)

            if response.status_code == 200:
                return response
        except Exception as e:
            print(e)
            print('Error status code', response.status_code, response.text)

    def getData(self):
        try:
            print('\n','*'*30,'site : https://projects.worldbank.org','*'*30)
            PageNo = 0 # starts at 0
            TotalRecords = self.TotalRecords
            RecordFetch = PageNo * 1000
            while  RecordFetch < TotalRecords:
                response = self.getResponse1(PageNo)
                JsonFetch = response.json()
                JsonFetch = JsonFetch["procnotices"]
                
                for Record in JsonFetch: 
                    TenderNumber = {Record.get('id') is not None : Record.get('id') }.get(True, "") # Info : if else one liner. refer docs. .get here just check if key is present in list.
                    ProjectID = {Record.get('project_id') is not None : Record.get('project_id') }.get(True, "")
                    PublishDate = {Record.get('noticedate') is not None : Record.get('noticedate') }.get(True, "")
                    TenderTypeFilter = {Record.get('notice_type') is not None : Record.get('notice_type') }.get(True, "")
                    TenderCountry = {Record.get('project_ctry_name') is not None : Record.get('project_ctry_name') }.get(True, "")
                    #TenderTitle = {Record.get('bid_description') is not None : Record.get('bid_description'),
                    #                Record.get('project_name') is not None : Record.get('project_name') }.get(True, "")

                    if Record.get('bid_description') is not None:
                        TenderTitle = Record.get('bid_description')
                    elif  Record.get('project_name') is not None :
                        TenderTitle = Record.get('project_name')
                    else:
                        TenderTitle = ''


                    self.__dataObj.append({
                        "TenderNumber"  :TenderNumber ,
                        "ProjectID" : ProjectID,
                        "PublishDate" : PublishDate,
                        "TenderTypeFilter":TenderTypeFilter, 
                        "TenderCountry": TenderCountry,
                        "TenderTitle": TenderTitle
                    })
                
                RecordFetch += len(JsonFetch)
                PageNo += 1
            self.formatData()
            
        except Exception as e:
            if e == KeyError:
                print(f"Element not found: \nTender Variable not found of dict Key : {e}", e)
            else :
                print(e)
    
    def getTenderDetailPage(self, url):
        try:
            headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.8',
            'origin': 'https://projects.worldbank.org',
            'referer': 'https://projects.worldbank.org/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            }

            response = requests.get(url=url, headers=headers)

            if response.status_code == 200:
                return response
        except Exception as e:
            print(e)
            print('Failed to Fetch Tender Page : \nError and Status Code :\n', response.status_code, response.text)


    def formatData(self):
        try:
            RecordCount = 1
            # loop is causeing issue when there is extra data hence removing extra data.
            del self.__dataObj[self.TotalRecords:]

            for data in self.__dataObj:
                
                if RecordCount == self.dataCount:
                    break

                TenderNumber = data['TenderNumber']
                ProjectID = data['ProjectID']
                PublishDate = data['PublishDate']
                TenderTypeFilter = data['TenderTypeFilter']
                TenderCountry = data['TenderCountry']
                TenderTitle = data['TenderTitle']
                FinalTenderNumber = f'Tender Notice No. {TenderNumber} , Project No. {ProjectID}'
                TenderLink = f'https://projects.worldbank.org/en/projects-operations/procurement-detail/{TenderNumber}' # Note : not an api link

                url = f"https://search.worldbank.org/api/v2/procnotices?format=json&apilang=en&fl=*&id={TenderNumber}&apilang=en"

                response = self.getTenderDetailPage(url=url)
                

                data = response.json()

                find = data['procnotices'][0]
                ten_Deadline = {find.get('submission_deadline_date') is not None : find.get('submission_deadline_date')}.get(True, "")
                ten_Detail = {find.get('notice_text') is not None : find.get('notice_text')}.get(True, "")
                country_code = {find.get('contact_ctry_code') is not None : find.get('contact_ctry_code')}.get(True, "")
                country = {find.get('project_ctry_name') is not None : find.get('project_ctry_name')}.get(True, "")
                org_name = {find.get('contact_organization') is not None : find.get('contact_organization')}.get(True, "")
                org_address = {find.get('contact_address') is not None : find.get('contact_address')}.get(True, "")
                org_city = {find.get('contact_ctry_name') is not None : find.get('contact_ctry_name')}.get(True, "")
                org_email = {find.get('contact_email') is not None : find.get('contact_email')}.get(True, "")
                org_contectNum = {find.get('contact_phone_no') is not None : find.get('contact_phone_no')}.get(True, "")
                
                org_contactPerson = {find.get('contact_name') is not None : find.get('contact_name')}.get(True, "")
                org_contactPerson = f'{org_contactPerson} <br>Contact Number : {org_contectNum}<br>'
                
                org_website = {find.get('contact_web_url') is not None : find.get('contact_web_url')}.get(True, "")


                ten_Detail = ten_Detail.replace('\n', '<diff>')
                DiscriptionSoup = BeautifulSoup(ten_Detail , 'html.parser')
                Discription = ''
                for Tags in DiscriptionSoup:
                    Discription += f'{Tags.text} <diff><diff>'
                
                Discription = Discription.replace('<br>', '<diff>').replace('</br>', '<diff>').replace('<br/>', '<diff>').replace('\n', '<diff>')
                DiscriptionStrippedToFitTrans = ops.cutString(Discription, 4800)
                DiscriptionTrans = self.repeatTrans03(DiscriptionStrippedToFitTrans)
                DiscriptionTrans = DiscriptionTrans.replace('<diff>','<br/>')

                #format deadline
                if ten_Deadline != "":
                    Deadline = dp.parse(ten_Deadline).strftime('%Y-%m-%d')
                else :
                    Deadline = ""

                #Print Tender Info
                self.printTender(TenderNumber=TenderNumber, TenderName=TenderTitle, TenderDeadline=Deadline)
                print(f"Records Fetched : {RecordCount}/{self.TotalRecords}")
                RecordCount += 1
                

                expiryDate = dt.strptime(self.publishEndDate,"%Y-%m-%d")
                startingDate = dt.strptime(self.publishStartDate,"%Y-%m-%d")
                PublishDate = dt.strptime(PublishDate,"%d-%b-%Y")

                if(not(startingDate <= PublishDate <= expiryDate) or PublishDate ==''):
                    self.skipCount += 1
                    print(f"This Record Skipped as Date ({PublishDate}) is out of range of PublishDate requested")
                    continue
                
                if Deadline == None:
                    print('\nThis tender is skipped due to deadline is empty\n')
                    continue
                if(Deadline == "" or (dt.strptime(Deadline,"%Y-%m-%d") < dt.now()) ):
                    self.skipCount += 1
                    print(f"This Record Is Skipped As Deadline is Expired : {Deadline}")
                    continue
                

                repeatTrans = self.repeatTrans03
                TenderTitleTrans = repeatTrans(TenderTitle)
                orgAddressTrans = repeatTrans(org_address)
                orgAddressTrans = f'{orgAddressTrans} <br> Country : {country}'

                DiscriptionTrans = f'Tender is Invited for : {TenderTitleTrans} <br><br> {DiscriptionTrans}'
                orgNameTrans = repeatTrans(org_name)
                

                # Country function
                checkLibrary = coco.convert #Country_converter library
                checkDatabaseTableInLibrary = self.isInCountryTable # DatabaseJson Library

                Website_Country_Code = checkLibrary(names=country, to='ISO2',not_found= " ")

                if Website_Country_Code != " ":
                    DBCountryDetails = checkDatabaseTableInLibrary(Code=Website_Country_Code)
                    FinalCountryCode = DBCountryDetails[2]
                else:
                    FinalCountryCode = ""
                


                self.__finalDataObj.append({
                    "file_id": "",
                    "tender_notice_no" :FinalTenderNumber,
                    "tender_title":TenderTitleTrans,
                    "tender_details":DiscriptionTrans,
                    "org_country": FinalCountryCode,
                    "org_name":orgNameTrans,
                    "org_address":orgAddressTrans,
                    "org_email":org_email,
                    "org_url":org_website,
                    "org_Tel":org_contectNum,
                    "financier": "119",
                    "mfa": "119", 
                    "org_contact_person":org_contactPerson,
                    "est_cost":'',
                    "deadline": Deadline,
                    "currency":'',
                    "cpv_value":'',
                    "source":"worldbank.org",
                    "domain_name":"https://projects.worldbank.org",
                    "tender_doc_link": TenderLink,
                    "file_name":"",
                    "region_id":"Rg00008", 
                    "ext1":"",
                    "document_link_attached":''
                    })
                
                DiscriptionNonTrans = DiscriptionStrippedToFitTrans.replace('<diff>','<br>')
                
                self.__finalDataObjNonTrans.append({
                    "file_id": "",
                    "tender_notice_no" :"",
                    "tender_title":TenderTitle,
                    "tender_details":DiscriptionNonTrans,
                    "org_country": '',
                    "org_name":org_name,
                    "org_address":org_address,
                    "org_email":'',
                    "org_url":'',
                    "org_Tel":'',
                    "financier": "",
                    "mfa": "", 
                    "org_contact_person":'',
                    "est_cost":'',
                    "deadline": '',
                    "currency":'',
                    "cpv_value":'',
                    "source":"",
                    "domain_name":"",
                    "tender_doc_link": '',
                    "file_name":"",
                    "region_id":"", 
                    "ext1":"",
                    "document_link_attached":''
                    })
                
        except Exception as e:
            print(f"Error! While formatting: (getFormat)\n{e}")





    def insertRecord(self):
        print("\n\nInserting Record")
        db = DbManager("Masterdb_AMS.db") 
        dbFinal = DbManager("Masterdb_AMSFinal.db")
        duplicateCount = 0
        skipCount = 0
        totalData = len(self.__finalDataObj)
        insertCount = 0
        RecordCount = 1
        
        for data , dataNonTrans in zip(self.__finalDataObj, self.__finalDataObjNonTrans) :
            if(not(db.checkDuplicateByTenderDocLink(data['tender_doc_link'],data['source'],data['deadline']))): 
                print(f"{RecordCount}/{totalData} {str(insertCount)} Record Inserted")
                
                RecordCount += 1

                fileName = ops.getCurrentDateTimeForFileName()
                data["file_id"] = fileName 
                data["file_name"] = ".\\Output\\Html\\ID019"+fileName+".html" 
                db.createDocHtml(data,nonTranslatedData=dataNonTrans)
                isInsert = db.insert(data)
                isInsertFinal = dbFinal.insert(data)
                if isInsert and isInsertFinal :
                    insertCount += 1
            else:
                print(f"{RecordCount}/{totalData} {str(duplicateCount)} Duplicate")
                RecordCount += 1
                duplicateCount += 1
            ops.holdProcess(0.2)        
        print("\nSource : https://worldbank.org") 
        print("Total Record : ",totalData)
        print("Skiped Count : ",skipCount)
        print("Duplicate Count : ",duplicateCount)
        print("Insert Count : ",insertCount)