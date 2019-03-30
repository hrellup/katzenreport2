#!/usr/bin/env python
from PIL import Image
import math
import operator
import sys
import os
from datetime import datetime
import json

PATH_ENTER = './IMG_ENTER/'
PATH_EXIT = './IMG_EXIT/'

FILENAME = 'baseline.txt'

def avg(path):
	histo_list = []
	for filename in os.listdir(path):
		img = Image.open(path+filename)
		histo_list.append(img.histogram())		
	hist_len = len(histo_list) *1.0
	baseline = [round(sum(x)/hist_len,2) for x in zip(*histo_list)]
	return baseline
	
def read(record):
	with open(FILENAME) as json_file:  
		data = json.load(json_file)
	return data[record]
	

def write(data):
	with open(FILENAME, 'w') as outfile:  
		json.dump(data, outfile)


if __name__ == "__main__":

	BASE_ENTER = avg(PATH_ENTER)
	BASE_EXIT = avg(PATH_EXIT)
	
	data = {}
	data['enter'] = BASE_ENTER
	data['exit'] = BASE_ENTER
	
	write(data)
	print read('enter')
	print read('exit')
	
