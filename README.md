# Python Strings: Medical Insurance Project
## Data Scientist: Analytics - Codedademy

You are a doctor who needs to clean up medical patient records, which are currently stored in one large string.

In this project, you will use your new knowledge of Python strings to obtain and clean up medical data so that it is easier to read and analyze.

Let’s get started!

### Tasks

#### Working with Strings

1. First, take a look at the code in <code>script.py</code>.

The string <code>medical_data</code> stores the medical records for ten individuals. Each record is separated by a <code>;</code> and contains the name, age, BMI (body mass index), and insurance cost for an individual, in that order.

Print <code>medical_data</code> to see the output in the terminal

2. We want the insurance costs to be represented in US dollars.

Replace all instances of <code>#</code> in <code>medical_data</code> with <code>$</code>. Store the result in a variable called <code>updated_medical_data</code>.

Print <code>updated_medical_data</code>.

3. We want to calculate the number of medical records in our data.

Create a variable called <code>num_records</code> and initialize it at 0.

4. Next, write a <code>for</code> loop to iterate through the <code>updated_medical_data</code> string. Inside of the loop, add <code>1</code> to <code>num_records</code> when the current character is equal to <code>$</code>.

5. Outside of the loop, print <code>num_records</code> with the following message:

```
There are {num_records} medical records in the data.
```

#### Splitting Strings

6. The medical data in its current form is difficult to analyze. An essential job for a data scientist is to clean up data so that it’s easy to work with.

Let’s start off by splitting the <code>updated_medical_data</code> string into a list of each medical record. Remember that each medical record is separated by a <code>;</code> in the string.

Store the result in a variable called <code>medical_data_split</code> and print this variable.

7. Our data is now stored in a list, but it is still hard to read. Let’s split each medical record into its own list.

First, define an empty list called <code>medical_records</code>.

8. Next, iterate through <code>medical_data_split</code> and for each record, split the string after each comma (<code>,</code>) and append the split string to <code>medical_records</code>.

Print <code>medical_records</code> after the loop.

#### Cleaning Data

9. Our data is now slightly more readable. However, it is not properly formatted – it contains unnecessary whitespace.

To fix this, let’s start by creating an empty list called <code>medical_records_clean</code>.

10. Next, use a <code>for</code> loop to iterate through <code>medical_records</code>.

Inside of the loop, create an empty list called <code>record_clean</code>. We’ll use this list to store a formatted version of each medical record.

11. After the <code>record_clean</code> variable, create a nested <code>for</code> loop that goes through each <code>record</code>:

```
for item in record:
``` 

Inside of this loop, append <code>item.strip()</code> to <code>record_clean</code> to remove any whitespace from the string.

12. Finally, we need to add each cleaned up record to <code>medical_records_clean</code>.

Outside of the nested <code>for</code> loop, append <code>record_clean</code> to <code>medical_records_clean</code>.

13. Print <code>medical_records_clean</code> outside of the <code>for</code> loops to see the output.

You should see output that is formatted and much easier to read.

#### Analyzing Data

14. Our data is now clean and ready for analysis.

For example, to print out the names of each of the ten individuals, we can use the following loop:

```
for record in medical_records_clean:
  print(record[0])
```

Add this loop to your code and click “Save.”

15. You want all of the names in the medical records to be in uppercase characters.

In the <code>for</code> loop, update <code>record[0]</code> before the print statement so that all of the characters are uppercase.

Click “Save” to see the result.

16. Let’s store each name, age, BMI, and insurance cost in separate lists.

To start, create four empty lists:

* <code>names</code>
* <code>ages</code>
* <code>bmis</code>
* <code>insurance_costs</code>
 
17. Next, iterate through <code>medical_records_clean</code> and for each record:

* Append the name to <code>names</code>.
* Append the age to <code>ages</code>.
* Append the BMI to <code>bmis</code>.
* Append the insurance cost to <code>insurance_costs</code>.

18. Print <code>names</code>, <code>ages</code>, <code>bmis</code>, and <code>insurance_costs</code> outside of the loop.

Make sure the output is what you expect.

19. Now that all of our data is in separate lists, we can easily perform analysis on that data. Let’s calculate the average BMI in our dataset.

First, create a variable called <code>total_bmi</code> and set it equal to 0.

20. Next, use a <code>for</code> loop to iterate through <code>bmis</code> and add each <code>bmi</code> to <code>total_bmi</code>.

Remember to convert bmi to a float.

21. After the for loop, create a variable called <code>average_bmi</code> that stores the <code>total_bmi</code> divided by the length of the <code>bmis</code> list.

Print out <code>average_bmi</code> with the following message:

```
Average BMI: {average_bmi}
```

#### Extra

22. Congratulations! In this project, you used Python strings to transform and clean up medical data.

As a data scientist, it’s important that you have clean and accurate data before you analyze it. You now have a better idea of the data preparation process moving forward.

If you’d like extra practice with Python strings, here are some suggestions to get you started:

* Calculate the average insurance cost in <code>insurance_costs</code>. You will have to remove the <code>$</code> in order to calculate this.
* Write a for loop that outputs a string for each individual in the following format:

```
Marina is 27 years old with a BMI of 31.1 and an insurance cost of $7010.0.
Markus is 30 years old with a BMI of 22.4 and an insurance cost of $4050.0
...
...
```

Happy coding!