import easyocr as ocr  #OCR

reader = ocr.Reader(['en'],model_storage_directory='.')

result = reader.readtext("Toyota_Yaris Cross_Tires_References.jpeg")

for text in result:
    print(text[1])