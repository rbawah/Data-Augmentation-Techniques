import cv2
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.pyplot import imshow

img_path = 'VGG-FACE-KERAS/misc/cat_getty.jpg'
img = cv2.imread(img_path)

h, w = img.shape[0], img.shape[1]

y, x = h / 5, w / 5

Mat = np.float32([[1, 0, x], [0, 1, y]])
Mat1 = np.float32([[1, 0, -x], [0, 1, -y]])

img_trans = cv2.warpAffine(img, Mat, (w, h))
img_trans1 = cv2.warpAffine(img, Mat1, (w, h))

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
plt.title('translated')
ax1.imshow(img_trans)

ax2 = fig.add_subplot(1, 2, 2)
plt.title('translated')
ax2.imshow(img_trans1)

cv2.imwrite('img_trans.jpg', img_trans)
cv2.imwrite('img_trans1.jpg', img_trans1)