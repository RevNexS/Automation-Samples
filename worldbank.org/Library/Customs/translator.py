# from google_trans_new import google_translator
try:
    from Library.google_trans_new.google_trans_new import google_translator
except:
    from ..google_trans_new.google_trans_new import google_translator

class DataTranslator:
    def __init__(self) -> None:
        pass

    def gtranslateData(data)-> str:
        try:
            Gtranslator = google_translator()
            return str(Gtranslator.translate(data,lang_tgt='en'))
        except Exception as ex :
            return ""            

#d =  DataTranslator.gtranslateData("Erikoishematologian")
#print(f"trans : {d}")