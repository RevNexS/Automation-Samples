import datetime
import time
from tkinter import messagebox
import tkinter
import re

class Operations:
    # cuts the string as per given data length
    def cutString(data,datalen)->str:
        data = str(data)
        if len(data)<datalen:
            return data
        return data[0:datalen-3] + "..."    
    # converts DD-MM-YYYY or DD/MM/YYYY format to YYYY-MM-DD
    def convertDDMMYYYYtoYYYYMMDD(data)->str:
        if(data==""):
            return ""
        data = str(data).replace("/","-")
        data = data.split("-")
        day = data[0] if len(data[0]) == 2 else "0"+data[0]
        month = data[1] if len(data[1]) == 2 else "0"+data[1]
        year = data[2]
        return str(f"{year}-{month}-{day}")

    # converts YYYY-MM-DD or YYYY/MM/DD format to DD-MM-YYYY
    def convertYYYYMMDDtoDDMMYYYY(data)->str:
        if(data==""):
            return ""
        data = str(data).replace("/","-")
        data = data.split("-")
        day = data[2] if len(data[2]) == 2 else "0"+data[0]
        month = data[1] if len(data[1]) == 2 else "0"+data[1]
        year = data[0]
        return str(f"{day}-{month}-{year}")

    #holds the system for given period of time in seconds
    def holdProcess(timeInSec):
        time.sleep(timeInSec)
    
    # get The Current Date in DD-MM-YYYY format bydefault
    def getCurrentDate(format = "dmy"):
        if(format == "dmy"):
            return datetime.datetime.today().strftime("%d-%m-%Y")
        return datetime.datetime.today().strftime("%Y-%m-%d")

    # get The Current Date in YYYY-MM-DD format bydefault
    def getCurrentDateTime(format ="ymd"):
        if(format == "ymd"):
            return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    #convert  YYYY-MM-DD string format to  YYYY-MM-DD date formate
    def convertStringToDate(strDate):
        strDate = str(strDate).replace("/","-")
        return datetime.datetime.strptime(strDate,"%Y-%m-%d")

    def getCurrentDateTimeForFileName():
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

    #pass true to isExit 
    def alertMessage(message="",isExit=False):
        messagebox.showinfo("Please Contact System Admin\n",message)
        if(isExit):
            exit(0)

    def removeHtmlTags(text):
        text = str(text).strip()
        if(text==""):
            return ""
        text = text.replace("<br>","||br||").replace("<br/>","||br||").replace("<BR>","||br||").replace("<BR/>","||br||")
        return re.sub(re.compile('<.*?>'), '', text).replace("||br||","<br/>")

    def removeSpecialCharacters(text):
        text = str(text).strip()
        if(text==""):
            return ""
        text = text.replace("â€™", "-").replace("â€“", "-").replace("â€", "-").replace("â€“", "-")
        text = text.replace("¢", "c")
        text = text.replace("£", "£")
        text = text.replace("¤", "")
        text = text.replace("¥", "")
        text = text.replace("¦", "")
        text = text.replace("§", "§")
        text = text.replace("¨", "")
        text = text.replace("©", "(c)")
        text = text.replace("ª", "")
        text = text.replace("«", "<")
        text = text.replace("¬", "-")
        text = text.replace("­", "-")
        text = text.replace("®", "(r)")
        text = text.replace("¯", "-")
        text = text.replace("°", "")
        text = text.replace("±", "+/-")
        text = text.replace("²", "2")
        text = text.replace("´", "'")
        text = text.replace("µ", "y")
        text = text.replace("¶", "P")
        text = text.replace("·", ".")
        text = text.replace("¸", "")
        text = text.replace("¹", "1")
        text = text.replace("º", "")
        text = text.replace("»", ">")
        text = text.replace("¼", "1/4")
        text = text.replace("½", "1/2")
        text = text.replace("¾", "3/4")
        text = text.replace("¿", "?")
        text = text.replace("À", "A")
        text = text.replace("Á", "A")
        text = text.replace("Â", "A")
        text = text.replace("Ã", "A")
        text = text.replace("Ä", "Ae")
        text = text.replace("Å", "A")
        text = text.replace("Æ", "Ae")
        text = text.replace("Ç", "C")
        text = text.replace("È", "E")
        text = text.replace("É", "E")
        text = text.replace("Ê", "E")
        text = text.replace("Ë", "E")
        text = text.replace("Ì", "I")
        text = text.replace("Í", "I")
        text = text.replace("Î", "I")
        text = text.replace("Ï", "I")
        text = text.replace("Ð", "D")
        text = text.replace("Ñ", "N")
        text = text.replace("Ò", "O")
        text = text.replace("Ó", "O")
        text = text.replace("Ô", "O")
        text = text.replace("Õ", "O")
        text = text.replace("Ö", "Oe")
        text = text.replace("×", "x")
        text = text.replace("Ø", "0")
        text = text.replace("Ù", "U")
        text = text.replace("Ú", "U")
        text = text.replace("Û", "U")
        text = text.replace("Ü", "Ue")
        text = text.replace("Ý", "Y")
        text = text.replace("Þ", "p")
        text = text.replace("ß", "ss")
        text = text.replace("à", "a")
        text = text.replace("á", "a")
        text = text.replace("â", "a")
        text = text.replace("ã", "a")
        text = text.replace("ä", "ae")
        text = text.replace("å", "a")
        text = text.replace("á", "a")
        text = text.replace("ó", "o")
        text = text.replace("æ", "ae")
        text = text.replace("ç", "c")
        text = text.replace("è", "e")
        text = text.replace("é", "e")
        text = text.replace("ê", "e")
        text = text.replace("ë", "e")
        text = text.replace("ì", "i")
        text = text.replace("í", "i")
        text = text.replace("î", "i")
        text = text.replace("ï", "i")
        text = text.replace("ð", "a")
        text = text.replace("ñ", "n")
        text = text.replace("ò", "o")
        text = text.replace("ó", "o")
        text = text.replace("ô", "o")
        text = text.replace("õ", "o")
        text = text.replace("ö", "oe")
        text = text.replace("ó", "o")
        text = text.replace("÷", "/")
        text = text.replace("ø", "0")
        text = text.replace("ù", "u")
        text = text.replace("ú", "u")
        text = text.replace("û", "u")
        text = text.replace("ü", "ue")
        text = text.replace("ý", "y")
        text = text.replace("þ", "p")
        text = text.replace("ÿ", "y")
        text = text.replace("–", " ")
        text = text.replace("“", "\"")
        text = text.replace("”", "\"")
        text = text.replace("’", "\'")
        text = text.replace("’", "")
        text = text.replace("&ndash;", "–")
        text = text.replace("&mdash;", "—")
        text = text.replace("&iexcl;", "¡")
        text = text.replace("&iquest;", "¿")
        text = text.replace("&quot;", "\"")
        text = text.replace("&ldquo;", "“")
        text = text.replace("&rdquo;", "”")
        text = text.replace("&lsquo;", "‘")
        text = text.replace("&rsquo;", "’")
        text = text.replace("&laquo;", "«")
        text = text.replace("&raquo;", "»")
        text = text.replace("&nbsp;", "  ")
        text = text.replace("&amp;", "&")
        text = text.replace("&cent;", "¢")
        text = text.replace("&copy;", "©")
        text = text.replace("&divide;", "÷")
        text = text.replace("&gt;", ">")
        text = text.replace("&lt;", "<")
        text = text.replace("&micro;", "µ")
        text = text.replace("&middot;", "·")
        text = text.replace("&para;", "¶")
        text = text.replace("&plusmn;", "±")
        text = text.replace("&euro;", "€")
        text = text.replace("&pound;", "£")
        text = text.replace("&reg;", "®")
        text = text.replace("&sect;", "§")
        text = text.replace("&trade;", "™")
        text = text.replace("&yen;", "¥")
        text = text.replace("&deg;", "°")
        text = text.replace("&aacute;", "á")
        text = text.replace("&Aacute;", "Á")
        text = text.replace("&agrave;", "à")
        text = text.replace("&Agrave;", "À")
        text = text.replace("&acirc;", "â")
        text = text.replace("&Acirc;", "Â")
        text = text.replace("&aring;", "å")
        text = text.replace("&Aring;", "Å")
        text = text.replace("&atilde;", "ã")
        text = text.replace("&Atilde;", "Ã")
        text = text.replace("&auml;", "ä")
        text = text.replace("&Auml;", "Ä")
        text = text.replace("&aelig;", "æ")
        text = text.replace("&AElig;", "Æ")
        text = text.replace("&ccedil;", "ç")
        text = text.replace("&Ccedil;", "Ç")
        text = text.replace("&eacute;", "é")
        text = text.replace("&Eacute;", "É")
        text = text.replace("&egrave;", "è")
        text = text.replace("&Egrave;", "È")
        text = text.replace("&ecirc;", "ê")
        text = text.replace("&Ecirc;", "Ê")
        text = text.replace("&euml;", "ë")
        text = text.replace("&Euml;", "Ë")
        text = text.replace("&iacute;", "í")
        text = text.replace("&Iacute;", "Í")
        text = text.replace("&igrave;", "ì")
        text = text.replace("&Igrave;", "Ì")
        text = text.replace("&icirc;", "î")
        text = text.replace("&Icirc;", "Î")
        text = text.replace("&iuml;", "ï")
        text = text.replace("&Iuml;", "Ï")
        text = text.replace("&ntilde;", "ñ")
        text = text.replace("&Ntilde;", "Ñ")
        text = text.replace("&oacute;", "ó")
        text = text.replace("&Oacute;", "Ó")
        text = text.replace("&ograve;", "ò")
        text = text.replace("&Ograve;", "Ò")
        text = text.replace("&ocirc;", "ô")
        text = text.replace("&Ocirc;", "Ô")
        text = text.replace("&oslash;", "ø")
        text = text.replace("&Oslash;", "Ø")
        text = text.replace("&otilde;", "õ")
        text = text.replace("&Otilde;", "Õ")
        text = text.replace("&ouml;", "ö")
        text = text.replace("&Ouml;", "Ö")
        text = text.replace("&szlig;", "ß")
        text = text.replace("&uacute;", "ú")
        text = text.replace("&Uacute;", "Ú")
        text = text.replace("&ugrave;", "ù")
        text = text.replace("&Ugrave;", "Ù")
        text = text.replace("&ucirc;", "û")
        text = text.replace("&Ucirc;", "Û")
        text = text.replace("&uuml;", "ü")
        text = text.replace("&Uuml;", "Ü")
        text = text.replace("&yuml;", "ÿ")
        text = text.replace("¡", ";")
        text = text.replace("Ã­", "i")
        text = text.replace("Ã³", "o")
        text = text.replace("Ãº", "u")
        text = text.replace("â€™", "-")
        text = text.replace("â€“", "-")
        text = text.replace("â€", "-")
        text = text.replace("â€“", "-")
        text = text.replace("¢", "c")
        text = text.replace("£", "£")
        text = text.replace("¤", "")
        text = text.replace("¥", "")
        text = text.replace("¦", "")
        text = text.replace("§", "§")
        text = text.replace("¨", "")
        text = text.replace("©", "(c)")
        text = text.replace("ª", "")
        text = text.replace("«", "<")
        text = text.replace("¬", "-")
        text = text.replace("­", "-")
        text = text.replace("®", "(r)")
        text = text.replace("¯", "-")
        text = text.replace("°", "")
        text = text.replace("±", "+/-")
        text = text.replace("²", "2")
        text = text.replace("³", "3")
        text = text.replace("´", "'")
        text = text.replace("µ", "y")
        text = text.replace("¶", "P")
        text = text.replace("·", ".")
        text = text.replace("¸", "")
        text = text.replace("¹", "1")
        text = text.replace("º", "")
        text = text.replace("»", ">")
        text = text.replace("¼", "1/4")
        text = text.replace("½", "1/2")
        text = text.replace("¾", "3/4")
        text = text.replace("¿", "?")
        text = text.replace("À", "A")
        text = text.replace("Á", "A")
        text = text.replace("Â", "A")
        text = text.replace("Ã", "A")
        text = text.replace("Ä", "Ae")
        text = text.replace("Å", "A")
        text = text.replace("Æ", "Ae")
        text = text.replace("Ç", "C")
        text = text.replace("È", "E")
        text = text.replace("É", "E")
        text = text.replace("Ê", "E")
        text = text.replace("Ë", "E")
        text = text.replace("Ì", "I")
        text = text.replace("Í", "I")
        text = text.replace("Î", "I")
        text = text.replace("Ï", "I")
        text = text.replace("Ð", "D")
        text = text.replace("Ñ", "N")
        text = text.replace("Ò", "O")
        text = text.replace("Ó", "O")
        text = text.replace("Ô", "O")
        text = text.replace("Õ", "O")
        text = text.replace("Ö", "Oe")
        text = text.replace("×", "x")
        text = text.replace("Ø", "0")
        text = text.replace("Ù", "U")
        text = text.replace("Ú", "U")
        text = text.replace("Û", "U")
        text = text.replace("Ü", "Ue")
        text = text.replace("Ý", "Y")
        text = text.replace("Þ", "p")
        text = text.replace("ß", "ss")
        text = text.replace("à", "a")
        text = text.replace("á", "a")
        text = text.replace("â", "a")
        text = text.replace("ã", "a")
        text = text.replace("ä", "ae")
        text = text.replace("å", "a")
        text = text.replace("æ", "ae")
        text = text.replace("ç", "c")
        text = text.replace("è", "e")
        text = text.replace("é", "e")
        text = text.replace("ê", "e")
        text = text.replace("ë", "e")
        text = text.replace("ì", "i")
        text = text.replace("í", "i")
        text = text.replace("î", "i")
        text = text.replace("ï", "i")
        text = text.replace("ð", "a")
        text = text.replace("ñ", "n")
        text = text.replace("ò", "o")
        text = text.replace("ó", "o")
        text = text.replace("ô", "o")
        text = text.replace("õ", "o")
        text = text.replace("ö", "oe")
        text = text.replace("ó", "o")
        text = text.replace("÷", "/")
        text = text.replace("ø", "0")
        text = text.replace("ù", "u")
        text = text.replace("ú", "u")
        text = text.replace("û", "u")
        text = text.replace("ü", "ue")
        text = text.replace("ý", "y")
        text = text.replace("þ", "p")
        text = text.replace("ÿ", "y")
        text = text.replace("–", " ")
        text = text.replace("“", "\"")
        text = text.replace("”", "\"")
        text = text.replace("’", "\'")
        text = text.replace("’", "")
        text = text.replace("􀃍", "")
        text = text.replace("📍", "")
        return text
        
            