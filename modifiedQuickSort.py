#!/usr/bin/python

from insertionSort import insertionSort
## MODIFIED QUICK SORT

# Input : Array of Integers - arr
# Output : Returns sorted array

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

#Generic Function to swap two elements at index 1,2
def swap(arr,index1,index2) :
	temp = arr[index1]
	arr[index1] = arr[index2]
	arr[index2] = temp
