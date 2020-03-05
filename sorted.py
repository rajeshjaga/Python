a=[1,3,2,4]
b=['a','b','c','d']
merge=zip(a,b)
res=sorted(merge)
for i in res:
    print(i[1])