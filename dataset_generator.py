import random
import csv

dataset_count = input("Datasets to generate:")
dataset_range = input("How many numbers in each dataset?:")

for dataset_id in range(1, int(dataset_count) + 1):
    dataset_directory = "DataSet/"
    dataset_name = "dataSet" + str(dataset_id) + ".txt"
    with open(dataset_name, mode='a') as dataset_file:
        for i in range(int(dataset_range)):
            dataset_file.write(str(random.randint(1, 100000)))
