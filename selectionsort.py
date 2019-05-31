print("Selection sort\n")
n=int(input("enter no.of elements\n"))
A=[]
for i in range(0,n):
	A.append(input("enter a value\n"))
print "Before Sorting",
print(A)
for i in range(len(A)): 
	min_idx = i 
	for j in range(i+1, len(A)): 
		if A[min_idx] > A[j]: 
			min_idx = j 		 
	A[i], A[min_idx] = A[min_idx], A[i] 
print"After Sorting ", 
print(A)

