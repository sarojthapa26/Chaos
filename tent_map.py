from  PIL import Image
import matplotlib.pyplot as plt

im=Image.open('flower.jpg')
pix=im.load()
l,h =im.size
pixels  = {}
for x in range(l):
      for y in range(h):
          pixel=pix[x,y]
          n=50*x+y
          pixels.update({n:pixel})

# use cubic map to generate random number
    #inputs = np.array([])
    #outputs = np.array([])
x=0.01
c_numbers=[]
for a in range (2500):
        if x < 0.5:
            xl = 1.67584 * x
            x=xl
        elif x > 0.5:
            xl = 1.67584 - 1.67584 * x
            x=xl
            print(x)
c_numbers.append((a, xl))
# short random numbers along with key
p=sorted(c_numbers,key=lambda  l:l[1])
print()
#split key list
q=[i[0] for i in p]

a=0
imgg =Image.new('RGB', (50, 50), "black")
points=imgg.load()
for i in range(imgg.size[0]):
    for j in range (imgg.size[1]):
        points[i,j]= pixels [q[a]]
        a+=1
        if a==2550:
            break
imgg.save('flower_tent.jpg')
print('Done')