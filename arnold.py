from PIL import Image
im = Image.open('sparrow_cubic.jpg')
width, height = im.size
unit = width/10
blocks = {}
r=0
#print width
for j in range(10):
    for i in range(10):
        area=(unit*i,unit*j, unit*(i+1),unit*(j+1))
        r=j*10+i
        img = im.crop(area)
        blocks.update({r:img})
sn=[]
for k in blocks.keys():
  sn.append(k)
print (sn)

ns = []
#arnold cat map for block shuffling
def arnold_cat(n):
    ns = []
    for num in n:
        p= num%10
        q= int(num/10)
        q = (q+p) % 10
        p = (2*q+3*p) % 10
        ns.append(q*10+p)
    return ns
key=5
n = sn
for i in range(key):
    m=arnold_cat(n)
    n=m
print(n)
#blocks[44].save('trrrry.png')

encr=[]
for p in n:
    encr.append(blocks[p])
#print encr

imgg =Image.new('RGB', (width, height), "white")

apple=imgg
#apple.save("adsfakdsj.png")
#imgg.paste(blocks[44],[20,20],None)
#imgg.save("tryyyy.png")
i=0
for a in range(10):
    for b in range(10):
        loc=[22*b,22*a]
        apple.paste(encr[i],loc,None)
        i+=1
apple.save("sparrow_arnold.jpg")