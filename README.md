# Algo-Project

## Requirement:

You need minimum python 3 latest or later version to run this code. To download python 3, please refer 

https://www.python.org/downloads/

Few other dependencies are required by the program like numpy and matplotlib. If they are not installed then run the below commands  

```
	pip3 install matplotlib
	Pip3 install numpy
```

## Execution :

### Step 1. Generate the data set. 

To generate the data set, please run the below command

```
python3 dataset_generator.py
```

User must provide the following inputs to generate the data set.
1. Datasets to generate : Number of datasets for which average to be taken.
2. How many numbers in each dataset : It is the maximum number of elements in each dataset from which inputs are taken. Give a number more or equal to 50,000

Note : For large dataset, testing might take more time for calculating the average execution time of each sorting algorithm

### Step 2. Execute a specific algorithm or all the algorithms and then compare their performances. 

To execute a sepecific algorithm or to compare the performace of all the algorithms, please run the below mentioned command

```
python3 compare.py
```

It will prompt you for the input like which algorithm do you want to run ?. 

Note: If you want to run or compare the performance for all the algorithms then please give input or select '6'.

```
Give inputs for following :
Select Sorting Algorithm to test :
1. Insertion Sort
2. Merge Sort
3. Heap Sort
4. In-Place Quick Sort
5. Modified Quick Sort
6. All Sorting Algorithms
```

Once you select the algorithm, it will again prompt you for data set input. For ex: For which data set do you want to run this algorithm ?. Sorted or random etc. 

```
Select Type of Data Set for sorting :
1. Random/Unsorted Input
2. Sorted Input
3. Reversely Sorted Input
```

Note: Please make sure you generate data set before running the executing or comparing the performance of all the algorithms. 
