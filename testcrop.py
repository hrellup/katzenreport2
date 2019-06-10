#!/usr/bin/env python
from PIL import Image
import math
import operator
import sys
import os
from datetime import datetime
import baseline


TH_ENTER=120
TH_EXIT=190


PATH = './IMG_NONE/'





if __name__ == "__main__":

    for filename in os.listdir(PATH):
            if filename.endswith("jpg"):
                img = Image.open(PATH+filename)
                cropped = img.crop((158,16,280,216))
                cropped.save(PATH+"crop_"+filename)

