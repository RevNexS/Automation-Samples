import cv2
import pytesseract


class ImageOcr :
    def convertImgToStr(self, imgUrl):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img = cv2.imread(imgUrl)
        img = self.getGrayscale(img)
        img = self.thresholding(img)
        img = self.removeNoise(img)
        customConfig = r'--oem 3 --psm 6'
        return pytesseract.image_to_string(img,lang='eng', config=customConfig)

    #get greyscale
    def getGrayscale(self,imgUrl):
        return cv2.cvtColor(imgUrl,cv2.COLOR_BGR2GRAY)        

    #noise removal
    def removeNoise(self,imgUrl):
        return cv2.medianBlur(imgUrl,5)
    
    #thresholding
    def thresholding(self,imgUrl):
        return cv2.threshold(imgUrl,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    