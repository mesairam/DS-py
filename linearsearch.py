print("Linear Search\n")
n=int(input("enter no.of elements\n"))
l=[]
for i in range(0,n):
	l.append(input("enter a value\n"))
s=int(input("enter a value to search\n"))
for i in range(0,n):
	if(l[i]==s):
		print "element found at index",i
		break
else:
	print("element not found")
