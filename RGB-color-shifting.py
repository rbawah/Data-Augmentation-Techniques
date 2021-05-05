from PIL import Image

img_path = 'VGG-FACE-KERAS/myDataSet/aliko.JPG'
img = Image.open(img_path)

def reduce_red() :
    Matrix = ( 0.5,  0,  0,   0, 
           0,  1,  0,   0, 
           0,  0,  1, 0)
    img1 = img.convert("RGB", Matrix)
    return img1.save('img1.jpg')

def increase_blue() :
    Matrix = ( 1,  0,  0,   0, 
           0,  1,  0,   0, 
           0,  0,  1.5, 0)
    img2 = img.convert("RGB", Matrix) 
    return img2.save('img2.jpg')

def adjust_green_blue() :
    Matrix = ( 1,  0,  0,   0, 
           0,  1.6,  0,   0, 
           0,  0,  1.1, 0)
    img3 = img.convert("RGB", Matrix)
    return img3.save('img3.jpg')

def all_adjustments():
    reduce_red()
    increase_blue()
    adjust_green_blue()
    
#all_adjustments()