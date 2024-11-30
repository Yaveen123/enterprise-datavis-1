import csv 

# remove the existing files inside the folder. 
# from: 'Blueicefield' (2011) "How to delete the contents of a folder?" Accessed on Nov 30, 2024, https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder 
import os
import glob
files = glob.glob('extracted_data/*')
for f in files:
    os.remove(f)


def generate_dates(init_yr, init_month, monthly_step): #generates the dates used to extract data from
    month = init_month
    year = init_yr
    toreturn = []
    num_of_dates = ((2013 - init_yr) * 12)//monthly_step

    for i in range(num_of_dates): # for the number of dates,
        month += monthly_step     # increase the month by the specified num of steps
        if month > 12:            # except if it's above 12
            month = 1             # then we go back to january
            year += 1             # and increment the year by 1

        # the data in the CSV file has a leading 0 for the month. 
        if month < 10:
            toreturn.append(f'{year}-0{month}-01')
        else:
            toreturn.append(f'{year}-{month}-01')
    
    return toreturn

dates = generate_dates(1743, 1, 12) 
print(dates)

for i in dates:
    # open the main file, and then create a new file 
    with open('GlobalLandTemperaturesByCountry.csv', 'r') as csvfile, open(f'extracted_data/{i}.csv', 'w+') as towrite: 
        
        mainreader = csv.reader(csvfile, delimiter=',', quotechar='|') # open the CSV file into something I can allow python to read. 
        #From Python (2023) "csv CSV - File Reading and Writing" Accessed 30 Nov 2024 https://docs.python.org/3/library/csv.html 
        
        writer = csv.writer(towrite)

        for row in mainreader:
            if row[0] == i:
                writer.writerow(row)
    towrite.close()
