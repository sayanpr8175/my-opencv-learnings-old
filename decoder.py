import cv2
import numpy as np

image = cv2.imread('encodedimage.png')
image_cpy = image.copy()
keyrange_1 = int(image.shape[0])
keyrange_2 = int(image.shape[1])

XKey = input("Enter decryption key, whatever you received when you encoded the image")

#print(XKey)
#XKey.split("A")
rowKey = int(XKey.split("A")[0].split("X")[1])
colKey_1 = int(XKey.split("A")[1].split("B")[0])
colKey_2 = int(XKey.split("A")[1].split("B")[1])

msg = ''

for col in range(colKey_1, colKey_2+1) :
    msg+=chr(image[rowKey][col][0])

print("Hi, your message - > ", msg)

