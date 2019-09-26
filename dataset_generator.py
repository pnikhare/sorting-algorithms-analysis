import random
import csv

dataset_count = input("Datasets to generate:")
dataset_range = input("How many numbers in each dataset?:")

for dataset_id in range(1, int(dataset_count) + 1):
    dataset_name = "dataset_" + str(dataset_id) + "_" + str(dataset_count) + "_unsorted.csv"
    with open(dataset_name, mode='w') as dataset_file:
        dataset_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(int(dataset_range)):
            dataset_writer.writerow([random.randint(1, 100000)])

