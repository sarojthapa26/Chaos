import matplotlib
from PIL import Image
import numpy as np
from pylab import *

a = 1.4
b = 0.3
x0 = 0.1
y0 = 0.3
#x = [x0]
#y = [y0]
#0.3992
read_image=Image.open('dog_henon.jpg','r')
plain_image=list(read_image.getdata())
def henon_map(x,y):
    x1= y + 1.0 - a *x*x
    y1= b * x
    return x1,y1

cipher_image=[]
sum=0
for p in range(48400):
    tup=()
    for r in range(3):
            rgb = plain_image[p][r]
            block =0
            for s in range(8):
                x1, y1 = henon_map(x0,y0)
                if x1 < 0.3992:
                    bit =0
                else:
                    bit =1
                block+=bit*(2**s)
                x0=x1
                y0=y1
            cipher_rgb =rgb^block
            tup+=(cipher_rgb,)
    #print(rgb-(cipher_rgb^block))
    cipher_image.append(tup)

im2 = Image.new(read_image.mode, read_image.size)
im2.putdata(cipher_image)
im2.save('dog_ori.jpg')
print('done!')
#print(cipher_image)