import os
import base64

input_path = r'input'
input_files = os.listdir(input_path)

for file_name in input_files:
    imageData = open('input\\' + file_name, 'r').read()
    decodedData = base64.b64decode(imageData)
    imgFile = open('output\\' + file_name.removesuffix('.txt') + '.png', 'wb')
    imgFile.write(decodedData)
    imgFile.close()