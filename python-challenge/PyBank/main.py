
# coding: utf-8

# In[7]:





# In[3]:


#Dependencies
import csv


# Files to load and output (Remember to change these)
file_to_load = "raw_data/budget_data_2.csv"
file_to_output = "analysis/budget_analysis_2.txt"

#Instantiate variables
row_count = 0
rev_sum = 0
rev_prev = 0
current_rev_change = 0
rev_change =[]
sum_of_deltas = 0
max_month =''
min_month = ''
max_of_deltas = 0
min_of_deltas = 1000000

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader_1 = csv.DictReader(revenue_data)

 # Calculate current delta and add current revenue to sum accumulator   
    for row in reader_1:
        month = (row['Date'])
        rev_sum = rev_sum + int(row['Revenue'])
        current_rev_change = int(row['Revenue']) - rev_prev

# Find extreme deltas

        if current_rev_change > max_of_deltas:
            max_of_deltas = current_rev_change
            max_month = row['Date']
        elif current_rev_change < min_of_deltas:
            min_of_deltas = current_rev_change
            min_month = row['Date']

# Update revenue array, reset 'previous' variable, and increment count variable
        rev_change.append(current_rev_change)        
        rev_prev = int(row['Revenue'])
        row_count += 1

# Calculate Average of the monthly changes

for x in rev_change:
    sum_of_deltas += x

ave_of_deltas = sum_of_deltas/row_count




with open(file_to_output, 'w') as f: 

    f.write('Financial Analysis\n')
    f.write('----------------------------\n')
    f.write ('Total Revenue: $' + str(rev_sum)+ '\n')
    f.write('Total Months: ' + str(row_count) + ' Months\n')
    f.write('Average Revenue Change: $' + str(ave_of_deltas) + '\n')
    f.write('Greatest Increase in Revenue: $' + str(max_of_deltas) + ' in '+ max_month + '\n')
    f.write('Greatest Decrease in Revenue:  $' + str(min_of_deltas) + ' in '+ min_month)
    
    
print('Financial Analysis')
print('----------------------------')
print ('Total Revenue: $' + str(rev_sum))
print('Total Months: ' + str(row_count) + ' Months ')
print('Average Revenue Change: $' + str(ave_of_deltas))
print('Greatest Increase in Revenue: $' + str(max_of_deltas) + ' in '+ max_month)
print('Greatest Decrease in Revenue:  $' + str(min_of_deltas) + ' in '+ min_month)    

f.close()

