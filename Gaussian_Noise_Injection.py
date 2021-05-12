import numpy as np
import cv2

img_path = 'VGG-FACE-KERAS/misc/cat_getty.jpg'
img = cv2.imread(img_path)#[...,::-1]#/255.0

#generate the gaussian noise
mean = 0.0   
std = 1.0   
noise = np.random.normal(mean, std, img.shape)

#Normalize the input image
info = np.iinfo(img.dtype)
img = img.astype(np.float64) / info.max

#Inject noise of varying leves: 25%, 50%, 75%
noisy_img_25 = img + 0.25*noise
noisy_img_50 = img + 0.5*noise
noisy_img_75 = img + 0.75*noise

#Clip nosiy image to 0 - 1 and rescale by multiplying by 255
noisy_img_25 = 255*np.clip((noisy_img_25),0,1)
noisy_img_50 = 255*np.clip((noisy_img_50),0,1)
noisy_img_75 = 255*np.clip((noisy_img_75),0,1)


noisy_img_25 = noisy_img_25.astype(np.uint8)
noisy_img_50 = noisy_img_50.astype(np.uint8)
noisy_img_75 = noisy_img_75.astype(np.uint8)

cv2.imwrite('noisy_img_25.jpg', noisy_img_25)
cv2.imwrite('noisy_img_50.jpg', noisy_img_50)
cv2.imwrite('noisy_img_75.jpg', noisy_img_75)