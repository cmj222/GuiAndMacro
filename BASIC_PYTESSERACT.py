import pytesseract

from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

A = Image.open('이미지.png')
result = pytesseract.image_to_string(A, lang='kor')

##result = "테 스 트 입 니 다 !"

result = result.replace(" ","")
print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
