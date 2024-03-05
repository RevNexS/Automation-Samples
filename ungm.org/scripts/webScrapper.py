from Library.Customs.dbManager import DbManager

from Library.Customs.operations import Operations as ops
from Library.Customs.translator import DataTranslator

import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import re
import time
import sys
from math import ceil

from Library.Customs.DatabaseJson import JsonData

class WebScrapper:
    publishStartDate = ""
    publishEndDate = ""
    dataCount = 0
    expiryDate = ""

    global gtranslate
    gtranslate = DataTranslator.gtranslateData
    global getOrgDetails
    JsonData = JsonData()
    getOrgDetails = JsonData.getOrgDetails
    global isInCountryTable
    isInCountryTable = JsonData.isInCountryTable


    __dataObj = []
    __tempData = []
    __finalDataObj = []

    def __init__(self,publishStartDate,publishEndDate,expiryDate,dataCount):
        self.publishStartDate = publishStartDate
        self.publishEndDate = publishEndDate
        self.expiryDate = expiryDate
        self.dataCount = dataCount
        self.url = f""
        self.totalPages = 0
        self.skipCount = 0
        self.nonTranslatedData = 0
        self.tenderCount = 0
    
    
    def getResponse(self):
        HomePageUrl = 'https://www.ungm.org/Public/Notice'
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            driver.get(HomePageUrl)
            #moveMouse = ActionChains(driver)
            self.publishStartDate = dt.strptime(self.publishStartDate , '%Y-%m-%d')
            self.publishStartDate = dt.strftime(self.publishStartDate,'%d-%b-%Y')

            self.publishEndDate = dt.strptime(self.publishEndDate , '%Y-%m-%d')
            self.publishEndDate = dt.strftime(self.publishEndDate,'%d-%b-%Y')

            # Filling Form
            self.fromDate = driver.find_element(By.CSS_SELECTOR , '#txtNoticePublishedFrom')
            self.fromDate.clear()
            self.fromDate.send_keys(self.publishStartDate)

            self.toDate = driver.find_element(By.CSS_SELECTOR , '#txtNoticePublishedTo')
            self.toDate.clear()
            self.toDate.send_keys(self.publishEndDate)
            
            self.DeadlineFromDate = driver.find_element(By.CSS_SELECTOR , '#txtNoticeDeadlineFrom') 
            self.DeadlineFromDate.clear()
            self.DeadlineFromDate.send_keys(self.publishEndDate)

            searchButton = driver.find_element(By.CSS_SELECTOR , '#lnkSearch')
            driver.execute_script("arguments[0].click();", searchButton)
            time.sleep(2)
            totalPage = driver.find_element(By.CSS_SELECTOR ,   '#noticeSearchTotal').text
            if totalPage == '':
                print(f'\n\n****************\nWebpage Returned No Records.\nHint: Input Higher Number, to look for data in Older Dates\n****************\n\n')
            if int(totalPage)%15 != 0:
                self.totalPages = int(totalPage)/15 + 1
            else:
                self.totalPages = int(totalPage)/15

            driver.quit()

        except Exception as e:
            print(f'\n\nError: While Getting the Website.\n{e}\n')
    
    def printTender(TenderNumber,TenderName, TenderDeadline):
            
            print(f'\n-----------------------------------------------------')
            print(f'Tender Number: {TenderNumber}')
            print(f'Tender Name: {TenderName}')
            print(f'Tender Deadline: {TenderDeadline}')
            print(f'----------------------------------------------------')
    
    def repeatTrans(self, transText):
        '''
            Takes Text to be Translated.
            Returns Translated Text after 3 retries or When Translated Text is diffrent then provided Text.
            Also gives a message if Tranlation attempt is exceeded.
        '''
        count = 1
        TransText = transText
        while TransText == transText:
            TransText = gtranslate(transText)
            if count == 3:
                print('Translation Max Tries Exceeded')
                self.nonTranslatedData += 1
                return TransText
            elif TransText != transText:
                return TransText
            count += 1
    
    def getData(self):
        try:
            
            self.getResponse()
            
            print('*'*30,"http://ungm.org",'*'*30)
            print('-'*45)
            print(f"Source : http://ungm.org")
            print(f'Start Date : {self.publishStartDate}')
            print(f'End Date : {self.publishEndDate}')
            print('-'*45)


            print("\nFetching Data...")
            print(f'Total Numbers of Pages to be Surf {ceil(self.totalPages)}\n')
            

            currentPage = 1
            totalPages = self.totalPages
            while currentPage <= totalPages :
                url = 'https://www.ungm.org/Public/Notice/Search'
                jsondata ={
                "PageIndex": currentPage,
                "PageSize": "15",
                "Title": "",
                "Description": "",
                "Reference": "",
                "PublishedFrom": self.publishStartDate,
                "PublishedTo": self.publishEndDate,
                "DeadlineFrom": self.publishEndDate, #publish end date is today's date.
                "DeadlineTo": "",
                "Countries": [],
                "Agencies": [],
                "UNSPSCs": [],
                "NoticeTypes": [],
                "SortField": "DatePublished",
                "SortAscending": "false",
                "isPicker": "false",
                "IsSustainable": "false",
                "NoticeDisplayType": "null",
                "NoticeSearchTotalLabelId": "noticeSearchTotal",
                "TypeOfCompetitions": []
                }
                
                header = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64)  AppleWebKit/5           (KHTML,likGeckoChrome/90.0.4430.212    Safari/537.36",
                    "accept": "*/*",
                    "content-type":"application/json",
                    "authority":"www.ungm.org"
                }
                
                response = requests.post(url, json=jsondata , headers=header ,verify=False).content
                
                soup = BeautifulSoup(response , 'html.parser')
                
                '''
                f = open('ungm.html', 'w')
                f.write(str(soup))
                
                with open(f'homeDivs.html', 'w' , encoding="utf-8") as f:
                    f.write(str(soup))
                '''
                
                i = 0
                divs = soup.select('.tableRow.dataRow.notice-table')
                for div in divs:
                    tenderNumber = div.find('div', {'data-description':'Reference'}).span.text
                    tenderName = div.select_one('.ungm-title.ungm-title--small').text.strip ()
                    if tenderNumber in tenderName:
                        tenderName = tenderName.replace(tenderNumber, '').strip()
                    tenderLink = div.select_one('div.tableCell.resultTitle > div > a').get ('href')
                    Deadline = div.select_one(f'div:nth-child(3) > span').text.strip().split(' (GMT')[0]
                    Deadline = dt.strptime(Deadline,'%d-%b-%Y %H:%M').strftime('%Y-%m-%d')
                    PublishDate = div.select_one('div:nth-child(4) > span').text.strip()
                    PublishDate = dt.strptime(PublishDate,'%d-%b-%Y').strftime('%Y-%m-%d')
                    UnOrg = div.select_one('div.tableCell.resultAgency > span').text.strip()
                    OrgCountry = div.select_one(f'div:nth-child(8) > span').text.strip()
                    if OrgCountry == '''Multiple destinations (see 'Countries' tab below)''': OrgCountry = 'Multiple destinations'
                    
                    
                    i += 1
                    
                    self.__tempData.append(
                        {
                            'TenderName' : tenderName,
                            'TenderLink' : tenderLink,
                            'Deadline' : Deadline,
                            'PublishDate' : PublishDate,
                            'UnOrg' : UnOrg,
                            'OrgCountry' : OrgCountry,
                            'TenderNumber' : tenderNumber
                        }
                        )
                
                currentPage += 1
                print('Total number of tender fetched:',len(self.__tempData))

            self.__formatData()
        except Exception as e:
            print(f'\n\nError: While Fetching Website . \n {e}\n\n')
            
    def __formatData(self):
        try:

            i = 0
            for tenderRow in self.__tempData :
                
                if i == self.dataCount:
                    break
                
                TenderName = tenderRow['TenderName']
                TenderNameTrans = self.repeatTrans(TenderName)
                
                
                if TenderNameTrans == '':
                    self.nonTranslatedData +=1
                    if self.nonTranslatedData > 10:
                        quitTxt = ""
                        print(f'\n\n########\nError : Translation Might not be Working. Please use Nord VPN.\n########\n\nPress k to Exit code')
                        while str(quitTxt).lower != str("k").lower:
                            quitTxt = str(input("\n\nPlease Input : "))
                            exit(0)
                
                Deadline = tenderRow['Deadline']
                PublishDate = tenderRow['PublishDate']
                UnOrg = tenderRow['UnOrg']
                OrgCountry = tenderRow['OrgCountry']
                TenderNumber = tenderRow['TenderNumber']

                tenderLink = tenderRow['TenderLink']
                tenderPageurl = 'https://www.ungm.org' + tenderLink

                WebScrapper.printTender(TenderNumber, TenderNameTrans,Deadline)
                self.tenderCount += 1
                print(f'Number of Tender Collected : {self.tenderCount}')

                # Fetching Indiviual Pages and getting cpvValue, document link and Pdf links.
                header = {
                    'authority' : 'www.ungm.org',
                    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64AppleWebKit/537.36  (KHTML, likeGeckoChrome/103.0.5060.114Safari/537.36',
                    'x-requested-with' : 'XMLHttpRequest'
                    }
                
                response = requests.get(tenderPageurl,headers=header).content
                
                soup = BeautifulSoup(response, 'html.parser')
                '''
                # Debug Helper
                #print(soup.prettify)
                
                with open(f'tenderPage{i}.html', 'w' , encoding="utf-8") as f:
                    soup = str(soup)
                    f.write(soup)
                print(f'save to file{i}')
                '''
                TenderDiscription = soup.find('div' , string='Description').find_next_sibling('div').text
                TenderDiscription = gtranslate(TenderDiscription)
                TenderDiscription = TenderDiscription.replace('\n','<br/>').strip()
                # cut string short if length more than 5000
                if len(TenderDiscription) > 5000:
                    TenderDiscription = TenderDiscription[:4994] + ' ...'

                cpvList = []
                cpvValues = soup.select('div.unspscNode > span > span:nth-child(1)')
                for cpvValue in cpvValues:
                    if cpvValue.text.isdigit() is False:
                        print('cpv discarded :', cpvValue.text)
                    else:
                        cpvList.append(cpvValue.text)
                
                FinalCpvValue = ','.join(cpvList)
                    
                
                TenderPdfDocList = []
                if soup.select_one('a.lnkShowDocument')  != None:
                    tenderPdfdocs = soup.select('a.lnkShowDocument')
                    for tenderPdfdoc in tenderPdfdocs:
                        tenderPdfdocsAltText = tenderPdfdoc.text.strip()
                        TenderPdfDocList.append(f""" <a href="https://www.ungm.org/{tenderPdfdoc.get('href')}" style="font-size:0.90em"> <em> {tenderPdfdocsAltText} </em> </a>""")
                        FinalTenderPdfDoc = '<Br/>'.join(TenderPdfDocList)
                else:
                    FinalTenderPdfDoc = ''
                
                # financier fetching and data
                orgDetials = getOrgDetails(UnOrg)
                orgName = orgDetials[2]
                finanacierID = orgDetials[1]

                # Country code
                OrgCountry = isInCountryTable(CountryName=OrgCountry)[2]
                
                # getting data out of head part of the contact tab
                contactContentHeadTag = soup.select_one('.ungm-list-item > span.title')
                
                OrgAddress = ''
                if contactContentHeadTag is not None:
                    contactContentHead = contactContentHeadTag.text.strip()
                    # If contactTab head section has more then 8 words. 
                    if len(contactContentHead.split()) >= 8:
                        orgEmailList =  re.findall(r"\S+@\S.\S+", contactContentHead)
                        orgEmail = ''
                        orgEmail = orgEmail.join(orgEmailList)
                        OrgAddress = " Email: " + orgEmail + ' ' + OrgAddress
                    else:
                        OrgAddress = contactContentHeadTag.text.strip()

                # getting data out of body part of the contact tab.
                # org email id, url and contact person
                if soup.find('span', text = ' Email: ' ) is not None:
                    orgEmail =  soup.find('span', text = ' Email: ' ).findNextSibling('span').text.strip()
                    if orgEmail not in OrgAddress:
                        OrgAddress = " Email: " + orgEmail + ' ' + OrgAddress
                
                if soup.find('span', text = ' First name: ' ) is not None:
                    orgPersonName = soup.find('span', text = ' First name: ' ).findNextSibling('span').text.strip()
                    orgPersonSurname = soup.find('span', text = ' Surname: ' ).findNextSibling('span').text.strip()
                    orgContactPerson = orgPersonName + ' ' + orgPersonSurname
                    if orgPersonName and orgPersonSurname not in OrgAddress:
                        OrgAddress = "Name: " + orgContactPerson + ' ' + OrgAddress


                finalTelephoneNo = ''
                if soup.find('span', text = ' Telephone number: ' ) is not None:
                    telephoneNo = soup.find('span' , text= ' Telephone number: ').findNextSibling('span').text.strip()
                    if soup.find('span' , text= ' Telephone country code: ') is not None :
                        telephoneCode = soup.find('span' , text= ' Telephone country code: ').findNextSibling('span').text.strip()
                        finalTelephoneNo =" Tel: " + telephoneCode + ' ' + telephoneNo 
                    else:
                        finalTelephoneNo = " Tel: " + telephoneNo
                    
                    if telephoneNo not in OrgAddress:
                        OrgAddress = " Tel: " + finalTelephoneNo + ' ' + OrgAddress
                        



                if(Deadline != "" and (dt.strptime(Deadline,"%Y-%m-%d") < dt.now()) ):
                        self.skipCount += 1
                        print(f"\nThis Record Is Skipped As Not in Deadline {Deadline} is Expired\n")
                        continue
                
                self.__finalDataObj.append({
                    "file_id": "", 
                    "tender_notice_no" :TenderNumber,
                    "tender_title":TenderNameTrans,
                    "tender_details": TenderDiscription,
                    "org_country":OrgCountry,
                    "org_name": orgName,
                    "org_address": OrgAddress,
                    "org_email": "",
                    "org_url":"",
                    "org_Tel":finalTelephoneNo,
                    "financier": finanacierID,
                    "mfa": "1",
                    "org_contact_person":"",
                    "est_cost":"",
                    "deadline":Deadline,
                    "currency":"",
                    "cpv_value":FinalCpvValue,
                    "source":"UNGM",
                    "domain_name":"https://www.ungm.org/",
                    "tender_doc_link": tenderPageurl ,
                    "file_name":"",
                    "region_id":"Rg00008",
                    "ext1":"",
                    "document_link_attached":FinalTenderPdfDoc
                })
                
                i += 1

        except Exception as e:
            print(f'\n\nError: While Formatting Data. \n {e}\n')
            
            
    def insertRecord(self):
        print("\n\nInserting Record")
        db = DbManager("Masterdb_AMS.db") 
        dbFinal = DbManager("Masterdb_AMSFinal.db")
        duplicateCount = 0
        skipCount = 0
        totalData = len(self.__finalDataObj)
        insertCount = 0
        RecordCount = 1

        for data in self.__finalDataObj :
            if(not(db.checkDuplicateByTenderDocLink(tenderDocLink=data['tender_doc_link'],source='UNGM',deadline=data['deadline']))):
                print(f"{RecordCount}/{totalData} {str(insertCount)} Record Inserted")
                
                fileName = ops.getCurrentDateTimeForFileName()
                data["file_id"] = fileName 
                data["file_name"] = ".\\Output\\Html\\ID005"+fileName+".html" 
                
                db.createDocHtml(data)
                isInsert = db.insert(data)
                isInsertFinal = dbFinal.insert(data)
                if isInsert and isInsertFinal :
                    insertCount += 1
            else:
                print(f"{RecordCount}/{totalData} {str(duplicateCount)} Duplicate")
                RecordCount += 1
                duplicateCount += 1
            ops.holdProcess(0.2)        
        print(f"\nSource : http://ungm.org")
        print("Total Record : ",totalData)
        print("Skiped Count : ",skipCount)
        print("Duplicate Count : ",duplicateCount)
        print("Insert Count : ",insertCount)



