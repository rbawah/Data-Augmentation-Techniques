from PIL import Image

img_path = 'VGG-FACE-KERAS/misc/mnist_dream_14.png'
img = Image.open(img_path)

def rot_45():
    return img.rotate(45).save('img_rot451.png')

def rot_90():
    return img.rotate(90).save('img_rot901.png')

def rot_180():
    return img.rotate(180).save('img_rot1801.png')

rot_45()
rot_180()
rot_90()