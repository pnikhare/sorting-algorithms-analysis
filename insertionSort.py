import random
import numpy as np
from datetime import datetime 
import time
import timeit
import matplotlib.pyplot as plt
## INSERTION SORT

# Input : Array of Integers - arr
# Output : Returns sorted array

def insertionSort(arr,low,high) :
	for i in range(1,high+1):
		keyValue = arr[i]		
		j=i-1
		while j>=0 and keyValue<=arr[j]:
			arr[j+1]=arr[j]
			j=j-1
		arr[j+1]=keyValue
	#print(arr)
	return arr


def mergeSort(arr,low,high) :
	if low < high :
		mid = (low+high)//2
		mergeSort(arr,low,mid)
		mergeSort(arr,mid+1,high)
		_mergeInPlace(arr,low,mid,high)
	# print(arr)
	return arr
	
def _merge(arr,low,mid,high):
	list1 = arr[low:mid+1]
	list2 = arr[mid+1:high+1]
	
	index = low
	i,j=0,0
	
	while (i<len(list1) and j<len(list2)):
		if (list1[i] <= list2[j] ):
			arr[index]=list1[i]
			i=i+1
			index=index+1
		else :
			arr[index]=list2[j]
			j=j+1
			index=index+1
	if i==len(list1) and j<len(list2) :
		arr[index:high+1] = list2[j:]
	if j==len(list2) and i<len(list1) :
		arr[index:high+1] = list1[i:]
	return arr

def _mergeInPlace(arr,low,mid,high):
	
	start1,start2=low,mid+1
	
	while (start1<=mid and start2<=high):
		if (arr[start1]<=arr[start2] ):
			start1=start1+1
		else :
			val = arr[start2]
			index = start2
			while index!=start1 :
				arr[index] = arr[index-1]
				index = index-1
			arr[start1] = val
			start1= start1+1
			start2 = start2+1
			mid = mid+1

	return arr


def quickSort(arr,low,high) :
	if(low<high) :
		pivotIndex = _partition(arr,low,high)
		quickSort(arr,low,pivotIndex-1)
		quickSort(arr,pivotIndex+1,high)

	return arr


def _partition(arr,low,high) :
	## Pick first element as pivot element
	pivot = arr[low]
	#print(pivot,"low:",low,"high",high)
	i=low+1
	j=high
	
	while i<j :

		while i<=high and arr[i]<pivot :
			i=i+1
		while j>low and arr[j]>=pivot:
			j=j-1

		if i<j :
			swap(arr,i,j) 
	if arr[low]>arr[j] :
		swap(arr,low,j)
	#print(arr)
	return j

def modifiedQuickSort(arr,low,high) :
	if(low+10<=high) :
		if(low<high) :
			pivotIndex = _partitionModified(arr,low,high)
			modifiedQuickSort(arr,low,pivotIndex-1)
			modifiedQuickSort(arr,pivotIndex+1,high)
	else :
		insertionSort(arr,low,high)

	return arr
	

def _partitionModified(arr,low,high) :
	## Pick media of first ,middle,last element as pivot element
	pivotIndex = findMedian(arr,low,(low+high)//2,high)
	pivot = arr[pivotIndex]
	swap(arr,pivotIndex,high-1)
	
	i=low
	j=high-2
	#print(pivot,"low:",low,"high",high)
	
	while i<j :

		while arr[i]<pivot :
			i=i+1
		while arr[j]>=pivot:
			j=j-1
		if i<j :
			swap(arr,i,j)
		else :
			break
	#if(arr[i]>arr[high-1]):
	swap(arr,i,high-1)
	#print(arr)
	return i

def findMedian(arr,low,mid,high) :
	x= arr[low]-arr[mid]
	y= arr[mid]-arr[high]
	z= arr[low]-arr[high]

	if(x*y >=0) :
		#mid is median
		if (arr[low]>arr[high]) :
			swap(arr,low,high)
		
	elif x*z >0 :
		#high is median
		if(arr[low]>arr[mid]) :
			swap(arr,low,mid)
		swap(arr,mid,high)
		
	else:
		if(arr[mid]>arr[high]) :
			swap(arr,mid,high)
		swap(arr,low,mid)
	#print("after swap of med",arr)
	return mid


def heapSort(arr,low,high) :
	heap = []
	top = 0
	for i in range(0,high+1) :
		top=top+1
		_insertHeap(heap,top,arr[i])
	# print(heap)
	for i in range(0,high+1) :
		arr[i]=_removeHeap(heap,top)
		#sortedArr.append(_removeHeap(heap,top))
		top=top-1
	#arr = sortedArr
	#print(sortedArr)


def _removeHeap(heap,top):
	minimum = heap[0]
	heap[0] = heap[top-1]
	currentIndex = 1

	while currentIndex < top :
		## 2 child exist
		if currentIndex*2+1<=top :
			if heap[currentIndex-1]<=heap[currentIndex*2-1] and heap[currentIndex-1] <= heap[currentIndex*2] :
				return minimum
			else:
				if(heap[currentIndex*2] < heap[currentIndex*2-1]) :
					j=currentIndex*2 +1
				else:
					j=currentIndex*2
				swap(heap,currentIndex-1,j-1)
				currentIndex=j
		else:
			## one node
			if currentIndex*2<=top :
				if heap[currentIndex-1]<=heap[currentIndex*2-1] :
					swap(heap,currentIndex-1,currentIndex*2-1)
			return minimum
	return minimum


	
def _insertHeap(heap,currentIndex,value) :
	heap.append(value)
		
	while currentIndex>1 and heap[(currentIndex//2)-1] > heap[currentIndex-1] :
		swap(heap,currentIndex-1,(currentIndex//2)-1)
		currentIndex = currentIndex//2
	
#Generic Function to swap two elements at index 1,2
def swap(arr,index1,index2) :
	temp = arr[index1]
	arr[index1] = arr[index2]
	arr[index2] = temp


def main() :

	
	#### Random Input Generation and storing in file
	# INPUT_SIZE = 10000
	# inputFile = open("dataSet"+str(INPUT_SIZE)+".txt","w")
	# inputFile.writelines("%s\n" %random.randint(0,INPUT_SIZE) for x in range(0,INPUT_SIZE))
	# inputFile.close()

	### Reading the input From File and storing in Array
	# arr = []
	# inputFile = open("dataSet"+str(INPUT_SIZE)+".txt","r")
	# arr = np.loadtxt(inputFile,dtype=int)
	# #arr = [32,2,55,1,3,7,0,9,12,55,12,12]
	# inputFile.close()

	print("Select Sorting Algorithm to test :")
	print("1. Insertion Sort")
	print("2. Merge Sort")
	print("3. Heap Sort")
	print("4. In-Place Quick Sort")
	print("5. Modified Quick Sort")
	print("6. All Sorting Algorithms")

	func = []
	while len(func)==0 :
		algorithm = input("Enter the Algorithm number :")
		if algorithm ==6 :
			func = [item for item in range(1,7)]
			break
		if (algorithm>=1 or algorithm<=5) :
			func.append(algorithm)
			break
		print("Please Enter valid Input")
	print("selected:",func)
	
	size = [1000,2000,3000,4000,5000,10000,20000,30000,40000,50000]
	print("Random Genaration of DATASET started")
	
	for num in range(0,len(size)):
		INPUT_SIZE = size[num]
		inputFile = open("DataSet/dataSet"+str(INPUT_SIZE)+".txt","w")
		inputFile.writelines("%s\n" %random.randint(0,INPUT_SIZE) for x in range(0,INPUT_SIZE))
		inputFile.close()
	
	print("Random Genaration of DATASET Ended --")

	insert = []
	merge = []
	heap = []
	quick = []
	modifiedQuick = []
	for alg in func :
		if alg==1 :
			for num in range(0,len(size)):
				arr = []
				inputFile = open("DataSet/dataSet"+str(size[num])+".txt","r")
				arr = np.loadtxt(inputFile,dtype=int)
				inputFile.close()
				startTime = time.time()
				insertionSort(arr,0,len(arr)-1)
				endTime = time.time()
				timeElapsed = endTime-startTime
				insert.append(timeElapsed)
				print "Time elapsed in Execution of insertionSort :",timeElapsed," seconds"
				outputFile = open("Result/ResultSet.txt","w")
				outputFile.writelines("%s\n" %item for item in arr)
				outputFile.close()
		
		elif alg==2:
			for num in range(0,len(size)):
				arr = []
				inputFile = open("DataSet/dataSet"+str(size[num])+".txt","r")
				arr = np.loadtxt(inputFile,dtype=int)
				inputFile.close()
				startTime = time.time()
				mergeSort(arr,0,len(arr)-1)
				endTime = time.time()
				timeElapsed = endTime-startTime
				merge.append(timeElapsed)
				print "Time elapsed in Execution of MergeSort :",timeElapsed," seconds"
				outputFile = open("Result/ResultSet.txt","w")
				outputFile.writelines("%s\n" %item for item in arr)
				outputFile.close()
			

		elif alg==3 :
			for num in range(0,len(size)):
				arr = []
				inputFile = open("DataSet/dataSet"+str(size[num])+".txt","r")
				arr = np.loadtxt(inputFile,dtype=int)
				inputFile.close()
				startTime = time.time()
				heapSort(arr,0,len(arr)-1)
				endTime = time.time()
				timeElapsed = endTime-startTime
				heap.append(timeElapsed)
				print "Time elapsed in Execution of HeapSort :",timeElapsed," seconds"
				outputFile = open("Result/ResultSet.txt","w")
				outputFile.writelines("%s\n" %item for item in arr)
				outputFile.close()
		elif alg==4 :
			for num in range(0,len(size)):
				arr = []
				inputFile = open("DataSet/dataSet"+str(size[num])+".txt","r")
				arr = np.loadtxt(inputFile,dtype=int)
				inputFile.close()
				startTime = time.time()
				quickSort(arr,0,len(arr)-1)
				endTime = time.time()
				timeElapsed = endTime-startTime
				quick.append(timeElapsed)
				print "Time elapsed in Execution of QuickSort :",timeElapsed," seconds"
				outputFile = open("Result/ResultSet.txt","w")
				outputFile.writelines("%s\n" %item for item in arr)
				outputFile.close()
		elif alg ==5 :
			for num in range(0,len(size)):
				arr = []
				inputFile = open("DataSet/dataSet"+str(size[num])+".txt","r")
				arr = np.loadtxt(inputFile,dtype=int)
				inputFile.close()
				startTime = time.time()
				modifiedQuickSort(arr,0,len(arr)-1)
				endTime = time.time()
				timeElapsed = endTime-startTime
				modifiedQuick.append(timeElapsed)
				print "Time elapsed in Execution of modifiedQuickSort :",timeElapsed," seconds"
				outputFile = open("Result/ResultSet.txt","w")
				outputFile.writelines("%s\n" %item for item in arr)
				outputFile.close()

	plt.plot(size, insert, label = "Insertion Sort") 
	plt.plot(size, merge, label = "Merge Sort")
	plt.plot(size, heap, label = "Heap Sort")
	plt.plot(size, quick, label = "Quick Sort")
	plt.plot(size, modifiedQuick, label = "Modified Sort")
	plt.xlabel('x - axis') 
	plt.ylabel('y - axis') 
	plt.title('Two lines on same graph!') 
  	plt.legend()  	
	plt.show() 

	#insertionSort(arr,0,len(arr)-1)
	#mergeSort(arr,0,len(arr)-1)
	#quickSort(arr,0,len(arr)-1)
	#modifiedQuickSort(arr,0,len(arr)-1)
	#heapSort(arr,0,len(arr)-1)

	# x=[10000,50000]
	# y1 = [7.544484853744507,190.93317294120789]
	# y2 = [0.11221098899841309,0.44962191581726074]

	


if __name__ == "__main__" :
	main()

