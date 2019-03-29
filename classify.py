from PIL import Image
import math
import operator
import sys
import os
from datetime import datetime
import baseline


TH_ENTER=120
TH_EXIT=190

BASE_ENTER = baseline.read('enter')
BASE_EXIT = baseline.read('exit')

PATH_TEST = './IMG_TEST/'

def img_cmp(img):
  img = Image.open(img)
  h2 = img.histogram()
  rms_enter = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, BASE_ENTER, h2))/len(h2))
  rms_exit = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, BASE_EXIT, h2))/len(h2))
  return (round(rms_enter), round(rms_exit))

def classify(img):
	val_enter, val_exit = img_cmp(img)
	str_enter = str(val_enter)
	str_exit = str(val_exit)
	
	
	if val_enter <= TH_ENTER:
		return "enter", str_enter
	if val_exit <= TH_EXIT:
		return "exit", str_exit
	return "none", str_enter, str_exit
	

if __name__ == "__main__":

    for filename in os.listdir(PATH_TEST):
		if filename.endswith("jpg"):
			action = classify(PATH_TEST+filename)
			print str(action) + ":" + filename
		