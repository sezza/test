# This code to take exported data from ilastik 
# and process into a collated csv file

"""
Columns: 
a	frame					[0]
b	labelimageId			[1]
c	trackId					[2]
d	Size_in_pixels_0		[3]	
e	Total_Intensity_0		[4]	red channel
f	Mean_Intensity_0		[5] red channel
g	Center_of_the_object_0	[6]	
h	Center_of_the_object_1	[7]
i	Total_Intensity_0		[8] green channel
j	Mean_Intensity_0		[9] green channel
"""

import csv, numpy

#---------------SOURCE-FILES--------------------------------
#here enter file names for CSV files exported from ilastik
RED_export = 's1_red_CSV-Table.csv'
GREEN_export = 's1_gfp_CSV-Table.csv'

#here enter file name for output CSV file
OUTPUT_csv = "s1_collated_data.csv"

#---------------CREATE-FILE-OBJECTS-------------------------

f1 = open(RED_export) # open file
csv_f1 = csv.reader(f1) #file object

f2 = open(GREEN_export) #file object
csv_f2 = csv.reader(f2) #file object

#---------------COLLATE-DATA--------------------------------
col_1 = []
col_2 = []
col_3 = []
col_4 = []
col_5 = []
col_6 = []
col_7 = []
col_8 = []
col_9 = []
col_10 = []

# get data from red file
csv_f1.next() # skip first row
for row in csv_f1:
	col_1.append(row[0]) # frame (col A)
	col_2.append(row[1]) # trackId (col C)
	col_3.append(row[2]) # lineageId (col D)
	col_4.append(row[41]) # Size_in_pixels_0 (col AP)
	col_5.append(row[21]) # Total_Intensity_0 (col V)
	col_6.append(row[30]) # Mean_Intensity_0 (col AE)
	col_7.append(row[44]) # Center_of_the_object_0 (col AS)
	col_8.append(row[45]) # Center_of_the_object_1 (col AT)

# get data from green file
csv_f2.next() # skip first row
for row in csv_f2:
	col_9.append(row[21]) # Total_Intensity_0 (col V)
	col_10.append(row[30]) # Mean_Intensity_0 (col AE)


data_to_write = [col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, col_10]

transposed = numpy.transpose(data_to_write)

#---------------WRITE-FILE----------------------------------
with open (OUTPUT_csv, "w") as csv_file:
	csv_append = csv.writer(csv_file)
	csv_append.writerows(transposed)


f1.close()
f2.close()
csv_file.close()