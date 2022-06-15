from random import randint

a=[0]*20

for i in range(20):

   a[i]=randint(0,100)

   if a[i]==20:

       a[i]=200

print (a)