
# coding: utf-8

# In[23]:


import csv

# Files to load and output (Remember to change these)
file_to_load = "raw_data/election_data_2.csv"
file_to_output = "analysis/voter_analysis_2.txt"

#Instantiate variables
voter_count = 0
candidate_set = set()
correy_vote = 0
khan_vote = 0
otooley_vote = 0
li_vote = 0
total_vote = 0
khan_vote_perc = 0
li_vote_perc = 0
otooley_vote_perc = 0
correy_vote_perc = 0
winner =''

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as voter_data:
    reader_1 = csv.DictReader(voter_data)

# Talley votes per candidate and total vote   
    for row in reader_1: 
        voter_count += 1
        candidate_set.add((row['Candidate']))
        if row['Candidate'] == 'Khan':
            khan_vote +=1
        elif row['Candidate'] == "O'Tooley":
            otooley_vote +=1
        elif row['Candidate'] == 'Li':
            li_vote +=1
        elif row['Candidate'] == 'Correy':
            correy_vote +=1
            
            
# Find winner

final_vote_talley = {'Correy':correy_vote,'Khan':khan_vote,'Li':li_vote,"O'Tooley":otooley_vote}
winner = max(final_vote_talley.keys(), key=(lambda k: final_vote_talley[k]))

# Vote percentages
total_vote = khan_vote + otooley_vote + li_vote + correy_vote
khan_vote_perc = khan_vote/total_vote *100
li_vote_perc = li_vote/total_vote *100
otooley_vote_perc = otooley_vote/total_vote *100
correy_vote_perc = correy_vote/total_vote *100

# Write report 
with open(file_to_output, 'w') as f: 

    f.write('Election Results\n')
    f.write('-------------------------\n')
    f.write('Total Votes: ' + str(total_vote)+ '\n')
    f.write('-------------------------\n')
    f.write("Khan:       {:.2f}%   ({})".format( khan_vote_perc, khan_vote)+'\n')
    f.write("Li:         {:.2f}%   ({})".format( li_vote_perc, li_vote) + '\n')
    f.write("Correy:     {:.2f}%   ({})".format( correy_vote_perc, correy_vote) + '\n')
    f.write("O'Tooley:    {:.2f}%   ({})".format( otooley_vote_perc, otooley_vote)+ '\n')
    f.write('-------------------------\n')
    f.write('     Winner: ' + winner + '\n')
    f.write('-------------------------')
    
f.close()

# Print report to console 

print("```")
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_vote))
print('-------------------------')
print("Khan:       {:.2f}%   ({})".format( khan_vote_perc, khan_vote))
print("Li:         {:.2f}%   ({})".format( li_vote_perc, li_vote))
print("Correy:     {:.2f}%   ({})".format( correy_vote_perc, correy_vote))
print("O'Tooley:    {:.2f}%   ({})".format( otooley_vote_perc, otooley_vote))
print('-------------------------')
print('     Winner: ' + winner)
print('-------------------------')
print("```")        
        
        

