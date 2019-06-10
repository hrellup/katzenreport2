#!/usr/bin/env python
from PIL import Image
import math
import operator
import sys
import os
from datetime import datetime
import baseline


TH_ENTER=50
TH_EXIT=280
TH_NONE=300

BASE_ENTER = baseline.read('enter')
BASE_EXIT = baseline.read('exit')
BASE_NONE = baseline.read('none')

PATH_TEST = './IMG_TEST/'

def img_cmp(img):
  img = Image.open(img)
  img_crop = img.crop((158,16,280,216))
  h2 = img_crop.histogram()
  rms_enter = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, BASE_ENTER, h2))/len(h2))
  rms_exit = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, BASE_EXIT, h2))/len(h2))
  rms_none = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, BASE_NONE, h2))/len(h2))
  return (round(rms_enter), round(rms_exit), round(rms_none))

def classify(img):
	values = img_cmp(img)
	#str_enter = str(val_enter)
	#str_exit = str(val_exit)
	#str_none = str(val_none)
        erg = ("enter","exit","none")
        th = (TH_ENTER, TH_EXIT, TH_NONE)

        index = values.index(min(values))
        if values[index] <= th[index]:

          return erg[index], str(values)
        #
        # zweit kleinsen werte nochmal testen
        values2 = ( 999, values[1], values[2])

        index = values2.index(min(values2))
        if values2[index] <= th[index]:

          return erg[index],str(values), str(values2)

	#if val_enter <= TH_ENTER:
	#	return "enter", str_enter
	#if val_exit <= TH_EXIT:
	#	return "exit", str_exit
	#return "none", str_enter, str_exit
        #return erg[index], str(values)
        return erg[2], str(values), str(values2)
	

if __name__ == "__main__":
  for filename in os.listdir(PATH_TEST):
    if filename.endswith("jpg"):
      action = classify(PATH_TEST+filename)
      print str(action) + ":" + filename
		
