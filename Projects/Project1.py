import numpy as np
from imageio import imread, imwrite
import cv2
path = r'C:\Users\kriss\desktop\Day.png'
img = imread(path)
arr = img*np.array([0.1,0.2,0.5])
arr2 = (255*arr/arr.max()).astype(np.uint8)

imwrite('Night.png', arr2)
img2 = cv2.imread('Night.png')
gma = 1 #Gamma is directly propoertional to the darkness
gma_img = np.array(255*(img2/255)**gma, dtype='uint8')
cv2.imwrite(r'c:\Users\kriss\desktop\NightX.png', gma_img)
print('Done !!')