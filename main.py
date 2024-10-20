fruit=['apple','banana','melone','apple','banana','apple']
fdata={}
for i in fruit:
    fdata[i]=fdata.get(i,0)+1
print(fdata)