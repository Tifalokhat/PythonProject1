from PIL import Image
im=Image.open('google.jpg')
# print(type(im),im)
r,g,b=im.split()
# print(r)
# print(g)
# print(b)
om=Image.merge(mode='RGB',bands=(r,b,g))
om.save('new_google.jpg')