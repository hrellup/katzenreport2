#!/usr/bin/env python
import sys
import classify
import sendmail



def do(image):

  result = classify.classify(image)
  if result[0] in ('enter',):
    sendmail.go(image, result)

  if result[0] in ('exit',):
    sendmail.go(image, result)
		

if __name__ == "__main__":
	img =  str(sys.argv[1])
	do(img)
