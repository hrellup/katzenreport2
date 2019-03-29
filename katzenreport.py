import sys

import classify
import sendmail




def do(image):

  result = classify.classify(image)
  print result
  if result[0] in ('enter',):
    sendmail.go(image, result)
		

if __name__ == "__main__":
	img = "TEST.jpg"
	do(img)
