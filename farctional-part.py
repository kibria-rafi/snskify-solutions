a=input()
pos = a.find('.')
if pos == -1:
    print("0")
else:
    print("0."+a[pos+1:])