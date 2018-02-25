#First budget csv
import csv

file_csv = "raw_data/budget_data_1.csv"

with open(file_csv, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    
    monthcount = []
    totalrevenue = []
    revenuechange = []
    
    next(csvreader)
    
    for row in csvreader:
        
        monthcount.append(row[0])
        totalrevenue.append(int(row[1]))
        
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:",len(monthcount))
    print("Total Revenue: $", sum(totalrevenue))
    
    for i in range(1, len(monthcount)):
        revenuechange.append(totalrevenue[i] - totalrevenue[i-1])
        avgrevenuechange = sum(revenuechange)/len(totalrevenue)
        
        greatestinc = max(revenuechange)
        greatestdec = min(revenuechange)
        
        dategreatestinc = str(monthcount[revenuechange.index(max(revenuechange))])
        dategreatestdec = str(monthcount[revenuechange.index(min(revenuechange))])
          
    print("Average Revenue Change: $", avgrevenuechange)
    print("Greatest Increase in Revenue: ", dategreatestinc, " ($",greatestinc,")")
    print("Greatest Decrease in Revenue: ", dategreatestdec, " ($",greatestdec,")")
    
    
#Second budget csv
    
file_csv = "raw_data/budget_data_2.csv"

with open(file_csv, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    
    monthcount = []
    totalrevenue = []
    revenuechange = []
    
    next(csvreader)
    
    for row in csvreader:
        
        monthcount.append(row[0])
        totalrevenue.append(int(row[1]))
        
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:",len(monthcount))
    print("Total Revenue: $", sum(totalrevenue))
    
    for i in range(1, len(monthcount)):
        revenuechange.append(totalrevenue[i] - totalrevenue[i-1])
        avgrevenuechange = sum(revenuechange)/len(totalrevenue)
        
        greatestinc = max(revenuechange)
        greatestdec = min(revenuechange)
        
        dategreatestinc = str(monthcount[revenuechange.index(max(revenuechange))])
        dategreatestdec = str(monthcount[revenuechange.index(min(revenuechange))])
          
    print("Average Revenue Change: $", avgrevenuechange)
    print("Greatest Increase in Revenue: ", dategreatestinc, " ($",greatestinc,")")
    print("Greatest Decrease in Revenue: ", dategreatestdec, " ($",greatestdec,")")