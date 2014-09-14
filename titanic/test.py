# test.py

import sys
import os
import urllib
import csv as csv
import pandas as pd
import numpy as np

def get_data_files(dirname):
	# Get the filenames in the given directory
	filenames = os.listdir(dirname)

	# Check data is already there. Exit if not here
	if not( all(x in filenames for x in ['train.csv', 'test.csv'])):
		print 'where is the train.csv and test.csv data?'
		sys.exit(1)

	# # Import the training data using csv	
	# csv_file_object = csv.reader(open('train.csv', 'rb')) 
	# header = csv_file_object.next() 
	# data=[] 

	# for row in csv_file_object:
	# 	data.append(row)
	# data = np.array(data) 
	# print type(data)
	# print data[0:5, ]

	# Import training data using pandas
	# header = 0 because the header row is in row 0
	df = pd.read_csv('train.csv', header=0)
	print df.head(3)
	# print type(df)
	# print df.dtypes				# gives type of each column in df
	# print df.info()  			# gives type of each column in df and numb entries
	# print df.describe() 	# this is like R summary

	# # address column by name, then look at a few rows
	# print df['Age'][0:10]
	# print df.Age[0:10]
	# print type(df.Age)

	# # let's run a method on that column
	# print df.Age.mean()

	# Make a subset of the orig df by selecting some columns
	sex_class_age = df[ ['Sex', 'Pclass', 'Age']]

	# Filter some rows
	over60 = df[df['Age'] > 60]
	print over60

	# Another subset with row filtering
	test = df[df['Age'] > 60 ][['Sex', 'Pclass', 'Age', 'Survived']]
	print test


	# # CAN'T DOWNLOAD WITHOUT COOKIES
	# if not('train.csv') in filenames:
	# 	tfile = urllib.URLopener()
	# 	trainurl = 'http://www.kaggle.com/c/titanic-gettingStarted/download/train.csv'
	# 	tfile.retrieve(trainurl, 'train.csv', )

	# if not('test.csv') in filenames:
	# 	tfile = urllib.URLopener()
	# 	testurl = 'http://www.kaggle.com/c/titanic-gettingStarted/download/test.csv'
	# 	tfile.retrieve(testurl, 'test.csv')

	return

def main():
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: test.py [dir]";
    sys.exit(1)

  get_data_files(args[0])

if __name__ == "__main__":
  main()

