#!/usr/bin/python


## MERGE SORT

# Input : Array of Integers - arr
# Output : Returns sorted array


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
			arr[start1+1:start2+1]=arr[start1:start2]
			# while index!=start1 :
			# 	arr[index] = arr[index-1]
			# 	index = index-1
			arr[start1] = val
			start1= start1+1
			start2 = start2+1
			mid = mid+1

	return arr
