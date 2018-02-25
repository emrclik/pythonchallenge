import csv
#Election Data 1
file_csv = "raw_data/election_data_1.csv"

with open(file_csv, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    
    totalvotes = []
    cordin = []
    vestal = []
    torres = []
    seth = []
    totalcandidates = []
    
    next(csvreader)
    
    for row in csvreader:
        totalvotes.append(row[0])
        if row[2] == 'Cordin':
            cordin.append(row[2])
        if row[2] == 'Vestal':
            vestal.append(row[2])
        if row[2] == 'Torres':
            torres.append(row[2])
        if row[2] == 'Seth':
            seth.append(row[2])
        totalcandidates.append(len(cordin))
        totalcandidates.append(len(vestal))
        totalcandidates.append(len(torres))
        totalcandidates.append(len(seth))
        
    print("Election Results")
    print("-------------------------")
    print("Total Votes: ", len(totalvotes))
    print("-------------------------")
    print("Cordin: ", "{:.0%}".format(len(cordin)/len(totalvotes)), " ",len(cordin))
    print("Vestal: ", "{:.0%}".format(len(vestal)/len(totalvotes)), " ",len(vestal))
    print("Torres: ", "{:.0%}".format(len(torres)/len(totalvotes)), " ",len(torres))
    print("Seth: ", "{:.0%}".format(len(seth)/len(totalvotes)), " ",len(seth))
    print("-------------------------")
    
    if max(totalcandidates) == len(cordin):
        print("Winner: Cordin")
    elif max(totalcandidates) == len(vestal):
        print("Winner: Vestal")
    elif max(totalcandidates) == len(torres):
        print("Winner: Torres")
    elif max(totalcandidates) == len(seth):
        print("Winner: Seth")
    
#Election Data 2
file_csv = "raw_data/election_data_2.csv"

with open(file_csv, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    
    totalvotes = []
    li = []
    khan = []
    otooley = []
    correy = []
    totalcandidates = []
    
    next(csvreader)
    
    for row in csvreader:
        totalvotes.append(row[0])
        if row[2] == 'Li':
            li.append(row[2])
        if row[2] == 'Khan':
            khan.append(row[2])
        if row[2] == 'O\'Tooley':
            otooley.append(row[2])
        if row[2] == 'Correy':
            correy.append(row[2])
        totalcandidates.append(len(li))
        totalcandidates.append(len(khan))
        totalcandidates.append(len(otooley))
        totalcandidates.append(len(correy))
        
    print("Election Results")
    print("-------------------------")
    print("Total Votes: ", len(totalvotes))
    print("-------------------------")
    print("Li: ", "{:.0%}".format(len(li)/len(totalvotes)), " ",len(li))
    print("Khan: ", "{:.0%}".format(len(khan)/len(totalvotes)), " ",len(khan))
    print("O\'Tooley: ", "{:.0%}".format(len(otooley)/len(totalvotes)), " ",len(otooley))
    print("Correy: ", "{:.0%}".format(len(correy)/len(totalvotes)), " ",len(correy))
    print("-------------------------")
    
    if max(totalcandidates) == len(li):
        print("Winner: Li")
    elif max(totalcandidates) == len(khan):
        print("Winner: Khan")
    elif max(totalcandidates) == len(otooley):
        print("Winner: O\'tooley")
    elif max(totalcandidates) == len(correy):
        print("Winner: Correy") 
    
