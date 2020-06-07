import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('straw.jpg',0)
print(img)

minV = 255 - np.max(img)
maxV = 30

print(minV)
print(maxV)

edges = cv2.Canny(img, minV, maxV, 3, 3, True)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
