from statistics import mean
#read a CSV file
with open("pima.csv", "r", newline='') as file:
   data=file.read() #file automatically closed at end of indent
   data_1d=data.split("\n") #split data on new line character returning a 1d list

   #split each element/line by further splitting on the occurance of the comma creating a 2D list
   data_2d=[]
   for line in data_1d:
      elements=line.split(',')
      data_2d.append(elements)

   #Cast the third and eighth(index 2 and 7) columns of row to integer
   for person in data_2d:
       person[2] = int(person[2])
       person[7] = int(person[7])
   #print(data_2d)
   #make 1D lists off the  BP and Age columns
   bp=[]
   age=[]
   for row in data_2d:
       bp.append(row[2])
       age.append(row[7])

   #calculate maximum,minimum,and average
   max_bp=max(bp)
   min_bp=min(bp)
   max_age = max(age)
   min_age = min(age)
   average_bp = mean(bp)
   average_age = mean(age)

   #print maximum,minimum,and average
   print("Maxmum BP is ", max_bp)
   print("Minimum BP is ",min_bp)
   print("Maxmum Age is ", max_age)
   print("Minimum Age is ", min_age)
   print(f"Average BP is,{average_bp:.0f}")
   print(f"Average Age is,{average_age:.0f}")















