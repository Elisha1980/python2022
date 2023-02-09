from statistics import mean
#read a CSV file
import csv

with open("pima.csv", "r", newline='') as file:
     data_2d=list(csv.reader(file))
     print(data_2d)















