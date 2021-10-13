a=int(input("vd"))
p=int(input("vp"))
for b in range(5):
    a=a+a*(p/100)
    a+=a*(p/100)
    print(a)

