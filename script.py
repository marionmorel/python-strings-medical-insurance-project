medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here

# Task 1
print(medical_data)

# Task 2
updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)

# Task 3
num_records = 0

# Task 4
for character in updated_medical_data:
  if character == "$":
    num_records += 1

# Task 5
print("There are {} medical records in the data.".format(num_records))

# Task 6
medical_data_split = updated_medical_data.split(';')
print(medical_data_split)

# Task 7
medical_records = []

# Task 8
for record in medical_data_split:
  medical_records.append(record.split(','))
print(medical_records)

# Task 9
medical_records_clean = []

# Task 10
for record in medical_records:
  record_clean = []

# Task 11
  for item in record:
    record_clean.append(item.strip())

# Task 12
  medical_records_clean.append(record_clean)

# Task 13
print(medical_records_clean)

# Task 14
for record in medical_records_clean:
  
# Task 15
  print(record[0].upper())

# Task 16
names = []
ages = []
bmis = []
insurance_costs = []

# Task 17
for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

# Task 18
print(names, ages, bmis, insurance_costs)

# Task 19
total_bmi = 0

# Task 20
for bmi in bmis:
  total_bmi += float(bmi)

# Task 21
average_bmi = round((total_bmi / len(bmis)), 2)
print("Average BMI: {}".format(average_bmi))

# Task 22

# Calculate the average insurance cost
total_insurance_cost = 0
for cost in insurance_costs:
  total_insurance_cost += float(cost.strip('$'))

# Print out individual strings with a for loop
for i in range(len(medical_records_clean)):
  print("{} is {} years old with a BMI of {} and an insurance cost of {}".format(medical_records_clean[i][0].split(" ")[0], medical_records_clean[i][1], medical_records_clean[i][2], medical_records_clean[i][3]))