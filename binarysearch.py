print("Binary Search\n")

n=int(input("enter no.of elements\n"))
l=[]
for i in range(0,n):
	l.append(input("enter a value\n"))
print "before sorting",
print(l)
for i in range(n):  
	for j in range(0, n-i-1):
		if l[j] > l[j+1] :
	                l[j],l[j+1]=l[j+1],l[j]
print "After sorting",
print(l)
s=input("enter a value to search\n")
#declaring min middle and max varibles...
min=0;max=n 
while(min <= max):
	mid=((min+max)/2)
	if(s>l[mid]):
		min=mid+1
	elif(s<l[mid]):
		max=mid-1
	elif(s==l[mid]):
		print "element found at index",
		print(mid)
		break
	else:
		min=max+1
else:
	print("element not found")
		
	
