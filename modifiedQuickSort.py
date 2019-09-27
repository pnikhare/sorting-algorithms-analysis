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
	arr[pivotIndex],arr[high-1]=arr[high-1],arr[pivotIndex]
		
	i=low+1
	j=high-2
	
	while (True) :

		while i<=high and arr[i]<pivot :
			i=i+1
		while j>low and arr[j]>=pivot:
			j=j-1
		if i<j :
			arr[i],arr[j]=arr[j],arr[i] 
		else :
			break
	arr[i],arr[high-1]=arr[high-1],arr[i] 
	return i

def findMedian(arr,low,mid,high) :
	if (arr[low] > arr[mid]) :
		arr[mid],arr[low]=arr[low],arr[mid]
	if (arr[low] > arr[high]) :
		arr[high],arr[low]=arr[low],arr[high]
	if (arr[mid] > arr[high]) :
		arr[mid],arr[high]=arr[high],arr[mid]
	return mid
