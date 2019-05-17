
csvfile=open("ex0_sample.csv",'r')
a=csvfile.read()
arr=a.split()

for a in arr :
    print(a)
