from  PIL import Image
import matplotlib.pyplot as plt

im=Image.open('dog_arnold.jpg')
pix=im.load()
l,h =im.size
pixels  = {}
for x in range(l):
      for y in range(h):
          pixel=pix[x,y]
          n=220*x+y
          pixels.update({n:pixel})

# use cubic map to generate random number
x=0.01
c_numbers=[]
for a in range (262144):
        x1= 3.623456789 * x * (1 - x)
        x=x1
        c_numbers.append((a,x1))

# short random numbers along with key
p=sorted(c_numbers,key=lambda  l:l[1])

#split key list
q=[i[0] for i in p]
a=0
imgg =Image.new('RGB', (512, 512), "black")
points=imgg.load()
for i in range(imgg.size[0]):
    for j in range (imgg.size[1]):

        points[i,j]= pixels [q[a]]
        a+=1
        if a==262144:
            break
imgg.save('')
print('Done')