a=input()
pos = a.find('.')
if pos == -1:
    print("0")
else:
    print(a[pos+1:pos+2])