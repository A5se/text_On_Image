import pytesseract
from PIL import Image
img = Image.open('maxresdefault.jpg')
pytesseract.pytesseract.tesseract_cmd = r'D:\python projects\text on image\ocr\tesseract.exe'
file_name = img.filename
file_name = file_name.split('.')[0]

text = pytesseract.image_to_string(img)
print(text)
with open(f'{file_name}.txt','w',encoding="utf-8") as text_file:
    text_file.write(text)