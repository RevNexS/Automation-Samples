
try:
    from Library.Customs.operations import Operations as ops
except:
    from operations import Operations as ops
    
import sqlite3

class DbManager:
    def __init__(self,database):
        self.__database = "./Database/" + database
        self.__connection()

    def __connection(self):
        self.__conn = sqlite3.connect(self.__database)

       
    def create_table(self):
        cursor = self.__conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblTenders(
                id INTEGER,
                file_id TEXT,
                tender_notice_no TEXT,
                short_description TEXT,
                tender_details TEXT,
                org_country TEXT,
                organisation_name TEXT,
                org_address TEXT,
                org_email TEXT,
                org_url TEXT,
                org_Contact_Person TEXT,
                deadline TEXT,
                deadline_2 TEXT,
                est_cost TEXT,
                currency TEXT,
                financier TEXT,
                MFA TEXT,
                ncbicb TEXT,
                cpv_value TEXT,
                source TEXT,
                tender_doc_file TEXT,
                status INTEGER,
                notice_type INTEGER,
                quality_addeddate TEXT,
                file_name TEXT,
                region_id TEXT,
                compulsary_qc INTEGER,
                ext1 TEXT,
                Selection_status INTEGER,
                CPV_status INTEGER,
                quality_status INTEGER,
                added_on TEXT
            )
        ''')
        self.__conn.commit()


    #insert into Database
    def insert(self,dataObj)-> bool:
        data = dataObj
        returnVal = False
        status = 2
        compulsaryQc = 0
        noticeType = 2
        mfa = data.get("mfa",0)
        financier =  data.get("financier",0)
        ncbicb = data.get("ncb_icb","icb")
        cpvValue = data.get("cpv_value","")
        ext1 = data.get("ext1","")
        selectionStatus = qualityStatus = cpvStatus = 1   
        deadLine2 = "1900-01-01 00:00:00.000" # no use just insert     
        regionId = data['region_id']
        quality_addeddate = ops.getCurrentDateTime("dmy")
        addedOnDate = ops.getCurrentDateTime("ymd")
        tenderDetails = f"Tenders Are Invited For {data['tender_title']} <br/><br/>"+str(data['tender_details']).capitalize() if(data['tender_details']!="") else ""
        if(tenderDetails==""):
            tenderDetails = f"Tenders Are Invited For {data['tender_title']} <br/><br/>" if data['tender_title'] else ""
            tenderDetails += f"Organization Name : {str(data['org_name']).upper()} <br/>" if data['org_name'] else ""
            tenderDetails += f"Organization Address : {str(data['org_address'])} <br/>" if data['org_address'] else ""
            tenderDetails += f"Closing Date : {str(data['deadline'])} <br/>" if data['deadline'] else ""

        if(data['org_country']=="" or data['deadline']== "" or data['tender_title']== "" or data['org_name']== ""):
            regionId = "Rg00007"
            compulsaryQc = 1
            status = 1
            noticeType = 0
        self.__connection()
        cursor = self.__conn.cursor() 
        # connecting Database
        sqlQuery = '''insert into tblTenders(
            file_id,tender_notice_no,short_description,tender_details,org_country,organisation_name,org_address,org_email,org_url,
            org_Contact_Person,deadline,deadline_2,est_cost,currency,financier,MFA,ncbicb,cpv_value,source,tender_doc_file,status,
            notice_type,quality_addeddate,file_name,region_id,compulsary_qc,ext1,Selection_status,CPV_status,quality_status,added_on
            )
        values (?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?)'''
        
        # icbncb if it is in india it's value will be ncb or else icb 
        if(data['tender_notice_no']!='' and  len(data['tender_notice_no'])>100):
            data['tender_notice_no'] = ops.cutString(data['tender_notice_no'],100)
        value = []
        value = (
                data['file_id'],
                data['tender_notice_no'],
                ops.cutString(data['tender_title'],200).capitalize(),                
                tenderDetails,
                data['org_country'],
                ops.cutString(str(data['org_name']),300).upper(),
                data['org_address'],
                data['org_email'],
                data['org_url'],
                ops.cutString(data['org_contact_person'],100),
                data['deadline'],
                deadLine2,
                data['est_cost'],
                data['currency'],
                financier,
                mfa,
                ncbicb,
                cpvValue,
                data['source'],
                data['tender_doc_link'],
                status,
                noticeType,
                quality_addeddate,
                data['file_name'],
                regionId,
                compulsaryQc,
                ext1,
                selectionStatus,
                cpvStatus,
                qualityStatus,
                addedOnDate
            )
        try:
            cursor.execute(sqlQuery, value)
        except Exception as err: # pyodbc.DatabaseError
            ops.alertMessage(err,False)
            self.__conn.rollback()
        else:
            self.__conn.commit()
            returnVal = True
        finally:
            cursor.close()
            self.__conn.close()
            return returnVal

    def checkDuplicateByTenderNoticeNo(self,tenderNo,org_country,deadline,source=""):
        tenderNo = str(tenderNo)
        sqlQuery = f"SELECT id FROM tblTenders where tender_notice_no = '{tenderNo}' and org_country = '{str(org_country).upper()}' and deadline = '{deadline}'"
        if(source!=""):
            sqlQuery += f" and source = '{source}'"
        self.__connection()
        cursor = self.__conn.cursor()
        try:
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            if(len(row)>0):
                return True
            return False
        except Exception as err: # pyodbc.DatabaseError
            self.__conn.rollback()
        else:
            self.__conn.commit()
        finally:
            cursor.close()
            self.__conn.close()

    def checkDuplicateByTenderDocLink(self,tenderDocLink,source="",deadline=""):
        sqlQuery = f"SELECT id FROM tblTenders where tender_doc_file = '{tenderDocLink}'"
        if(source!=""):
            sqlQuery += f" and source = '{source}'"
        if(deadline!=""):
            sqlQuery += f" and deadline = '{deadline}'"
        self.__connection()
        cursor = self.__conn.cursor()
        try:
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            if(len(row)>0):
                return True
            return False
        except Exception as err: # pyodbc.DatabaseError
            self.__conn.rollback()
        else:
            self.__conn.commit()
        finally:
            cursor.close()
            self.__conn.close()

    def createDocHtml(self,data,nonTranslatedData = ""):
        docHtml = '''
            <style style="text/css">  	
                .hoverTable{
                    width:100%;
                    border-collapse:collapse; 	
                }	
                .hoverTable td{  
                    padding:7px; 
                    border:#4e95f4 1px solid;	
                }	
                .hoverTable tr{		
                    background: #f4f8fe;	
                }    
                .hoverTable tr:hover {
                    background-color: #ffff99;    
                }
                </style>'''
        tempDocHtml = ""
        if(data['tender_notice_no']!=""):
            tempDocHtml = '''
                <tr>
                    <td>Tender No: </td>
                    <td>''' + data['tender_notice_no'] + '''</td>
                </tr>                
            '''
        if(data['tender_title']!=""):
            tempDocHtml += '''
                <tr>
                    <td>Tender Title: </td>
                    <td>''' + data['tender_title'] + '''</td>
                </tr>                
            '''
        if(data['tender_details']!=""):
            tempDocHtml += '''
                <tr>
                    <td>Tender Details: </td>
                    <td>''' + data['tender_details'] + '''</td>
                </tr>                
            '''
        if(data['deadline']!=""):
            tempDocHtml += '''
                <tr>
                    <td>Closing Date:</td>
                    <td>''' + data['deadline'] + '''</td>
                </tr>                
            '''
        if(data['org_name']!=""):
            tempDocHtml += '''
                <tr>
                    <td>Purchaser: </td>
                    <td>''' + data['org_name'] + '''</td>
                </tr>                
            '''
        if(str(data['org_contact_person']).strip()!=""):
            tempDocHtml += '''
                <tr>
                    <td>Contact Person: </td>
                    <td>''' + data['org_contact_person'] + '''</td>
                </tr>                
            '''

        if(data['org_address']!=""):
            tempDocHtml += '''
                <tr>
                    <td>Purchaser Address:</td>
                    <td>''' + data['org_address'] + '''</td>
                </tr>                
            '''
        if(data['org_email']!=""):
            tempDocHtml += '''
                <tr>
                    <td>Purchaser Email:</td>
                    <td>''' + data['org_email'] + '''</td>
                </tr>                
            '''

        if(data['org_url']!=""):
            tempDocHtml += '''
                <tr>
                    <td>Purchaser URL:</td>
                    <td>''' + data['org_url'] + '''</td>
                </tr>                
            '''

        if(data['tender_doc_link']!=""):
            tempDocHtml += '''
                <tr>
                    <td>Link:</td>
                    <td> <a href="'''+ data['tender_doc_link']+ '''" target="_blank" />View More</a></td>
                </tr>                
            '''
        documentLink = data.get("document_link_attached",None) 
        if(documentLink != None and len(documentLink)>0):
            tempDocHtml +='''
            <tr>
                <td>Attachment:</td>
                <td> ''' + str(data['document_link_attached']) + '''</td>
            </tr>
            '''
        docHtml +=f'''<table class="hoverTable">
            <tbody>            
            {tempDocHtml}
            </tbody>
            </table>
        '''
        if(nonTranslatedData!=""):
            docHtml +='''
                <br><br><font color="red">[Disclaimer: The above text is machine translated. For accurate information kindly refer the original document.]</font><br>
            '''
            tempDocNonTranslatedHtml = ""

            if(data['tender_notice_no']!=""):
                tempDocNonTranslatedHtml = '''
                    <tr>
                        <td>Tender No: </td>
                        <td>''' + data['tender_notice_no'] + '''</td>
                    </tr>                
                '''
            if(nonTranslatedData['tender_title']!=""):
                tempDocNonTranslatedHtml += '''
                <tr>
                    <td>Tender Title:</td>
                    <td>''' + nonTranslatedData['tender_title'] + '''</td>
                </tr>                
                '''
            if(nonTranslatedData['tender_details']!=""):
                tempDocNonTranslatedHtml += '''
                <tr>
                    <td>Tender Details: </td>
                    <td>''' + nonTranslatedData['tender_details'] + '''</td>
                </tr>                
                '''
            if(data['deadline']!=""):
                tempDocNonTranslatedHtml += '''
                    <tr>
                        <td>Closing Date: </td>
                        <td>''' + data['deadline'] + '''</td>
                    </tr>                
                '''

            if(nonTranslatedData['org_name']!=""):
                tempDocNonTranslatedHtml += '''
                <tr>
                    <td>Purchaser:</td>
                    <td>''' + nonTranslatedData['org_name'] + '''</td>
                </tr>              
                '''
            if(nonTranslatedData['org_contact_person']!=""):
                tempDocNonTranslatedHtml += '''
                <tr>
                    <td>Contact Person:</td>
                    <td>''' + nonTranslatedData['org_contact_person'] + '''</td>
                </tr>              
                '''
            if(nonTranslatedData['org_address']!=""):
                tempDocNonTranslatedHtml += '''
                <tr>
                    <td>Purchaser Address:</td>
                    <td>''' + nonTranslatedData['org_address'] + '''</td>
                </tr>            
                '''
            if(data['org_email']!=""):
                tempDocNonTranslatedHtml += '''
                    <tr>
                        <td>Purchaser Email:</td>
                        <td>''' + data['org_email'] + '''</td>
                    </tr>                
                '''
        
            if(data['org_url']!=""):
                tempDocNonTranslatedHtml += '''
                    <tr>
                        <td>Purchaser URL:</td>
                        <td>''' + data['org_url'] + '''</td>
                    </tr>                
                '''         

            docHtml +=f'''
                <table class="hoverTable">
                {tempDocNonTranslatedHtml}
                </table>
            '''

        docHtml = f'''
            <html>
                <head>
                <title>Tenders Document </title> 
                <meta charset ="utf-8">
                <meta name ="viewport" content ="width=device-width, initial-scale=1">
                <link rel ="stylesheet" href ="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
                </head>
                <body>
                <div class="container">
                <h2>Tender Details</h2> 
                <div class ="clearfix">
                    {docHtml}
                </div>
                <br/>
                </div>
                </body>
            </html>
        '''            
        try:
            f = open(data['file_name'], "x",encoding="utf-8")
            f.write(docHtml)
            f.close()
        except Exception as e :
            print(e)
            exit(0)
        
    # #for Testing Connections    
    # def viewAllRows(self):
    #     sqlQuery = "select TOP (100) * from tblTenders"
    #     cursor = self.__conn.cursor()
    #     rows = pandas.read_sql_query(sqlQuery,self.__conn)
    #     self.__conn.commit()
    #     cursor.close()
    #     self.__conn.close()
    #     print(rows)

    
db = DbManager('Masterdb_AMS.db')
db2 = DbManager('Masterdb_AMSFinal.db')
db.create_table()
db2.create_table()