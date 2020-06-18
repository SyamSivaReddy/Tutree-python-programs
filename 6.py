
def printMax(arr, n, k): 
	max = 0
	
	for i in range(n - k + 1): 
		max = arr[i] 
		for j in range(1, k): 
			if arr[i + j] > max: 
				max = arr[i + j] 
		print(str(max) + " ", end = "") 

arr =[8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
n = len(arr) 
k = 4
printMax(arr, n, k) 

