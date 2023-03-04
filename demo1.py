
import pytesseract as ts
version = ts.get_tesseract_version()
print('version:',version)


langs = ts.get_languages()
print('langs:',langs)

# img_fn = 'book.png'
# img_fn = 'D:\chepaijiance\plate.jpg'
img_fn=r'D:\chepaijiance\yolov5-7.0\runs\detect\exp10\crops\license-plate\d648b2ae1abc09f3_jpg.rf.3451503900a53564047347dc902024a22.jpg'
lang = 'chi_sim'
# lang = 'eng'
text = ts.image_to_string(img_fn)
print(text)