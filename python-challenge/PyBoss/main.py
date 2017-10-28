
# coding: utf-8

# In[64]:


import csv

# Files to load and output (Remember to change these)
file_to_load = "raw_data/employee_data2.csv"
file_to_output = "raw_data/employee_new2.csv"

#Instantiate variables
new_dob = ''
firstname= []
lastname = []
birth = []
state_list= []
ss_num = []
eid = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as emp_data:
    reader_1 = csv.DictReader(emp_data)

# Pass row keys(column names) to new lists 
    for row in reader_1: 
        full_name = row['Name']
        name_list = full_name.split(" ")
        row['First Name'] = name_list[0]
        row['Last Name'] = name_list[1]
        
# Remove old Name column

        del row['Name']
        dob = row['DOB']
        dob_list = dob.split('-')
         
        row['DOB'] = dob_list[1] + '/' + dob_list[2] + '/' + dob_list[0]
        ssn = row['SSN']
        ssn_end = ssn[-4:]
        row['SSN'] = '***-**-'+ ssn_end
        
        row['State'] = us_state_abbrev[row['State']]
        
        eid.append(row['Emp ID'])
        
 # Pass in new column headings to lists

        state_list.append(row['State'])
        birth.append(row['DOB'])
        lastname.append(row['Last Name'])
        firstname.append(row['First Name'])
        ss_num.append(row['SSN'])
        
 #Build output file 

        cleanCSV = zip(eid,firstname,lastname,birth,ss_num,state_list)
        
        with open(file_to_output, 'w', newline="") as csvFile:

            csvWriter = csv.writer(csvFile, delimiter=',')

 # Write Headers into file
        
            csvWriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

# Write the zipped lists to a csv
            csvWriter.writerows(cleanCSV)
        
        

