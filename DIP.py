import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
from scipy.stats import entropy

img_size = 300
image1 = np.array(Image.open('Chelu.jpg').resize((img_size, img_size)))
# print(image1)
print(image1.shape)
image2 = image1.copy()
i = 0

# print(image2)
while i < 300:
    j = 0
    while j < 300:
        k = 0
        while k < 3:
            if 20 > image2[i][j][k] > 0:  # For light images
                image2[i][j][k] = 10
            if 250 > image2[i][j][k] > 220:  # For dark Images
                image2[i][j][k] = 255
            k += 1
        j += 1
    i += 1
# image2[299][299][2]=0
# print("Hahahahahhahah")
# print(image2)
plt.show()
# image2=255-image2 #For Inverse image
Image.fromarray(image2).save('haha.jpg')

print("The Original Entropy", entropy(image1))
print("The New Entropy", entropy(image2))
print("Mean of Original Image", image1.mean())  # Mean od first
print("Mean of New Image before Writing", image2.mean())  # Mean of 2nd
cv2.imwrite('helo.jpg', image2)
print("Mean of New Image", image2.mean())
print("Original Standard Deviation", image1.std())  # Standard Deviation of Original
print("New Standard Deviation", image2.std())  # Standard Deviation of New one
print("RMS of Original", np.sqrt(np.mean(image1 ** 2)))  # Root Mean Square
print("RMS of New one", np.sqrt(np.mean(image2 ** 2)))  # RMS of new Image
#####################################
# PSNR ki kahani

img1 = cv2.imread('cheluchange.jpg')
img2 = cv2.imread('haha.jpg')
img3 = cv2.imread('helo.jpg')
ps_nr = cv2.PSNR(img1, img2)
ha_har = cv2.PSNR(img1, img3)
print("PSNR of Simple One", ps_nr)
print("PSNR of CV one ", ha_har)

# Histogram
image_hist = cv2.imread('cheluchange.jpg')
plt.hist(image_hist.ravel(), 256, [0, 256])
plt.show()
# equ = cv2.equalizeHist(image_hist)
# res = np.hstack(image_hist, equ)
# cv2.imwrite('ress.jpg', equ)

############
image_hist2 = cv2.imread('haha.jpg')
plt.hist(image_hist2.ravel(), 256, [0, 256])
plt.show()

# Image.fromarray(image2).save('cheluchange.jpg')