import os
import caer
import canaro
import numpy as np
import cv2 as cv
import gc

# when building deep computer vision ur model expect all data in same size
IMG_SIZE = (80, 80)
channel = 1
char_path = r'C:\Users\momon\Desktop\python learning\opencv\archive\simpsons_dataset'

char_dict = {}
for char in os.listdir(char_path):
    char_dict[char] = len(os.listdir(os.path.join(char_path, char)))


#sort in descending order

char_dict = caer.sort_dict(char_dict, descending=True)
# print(char_dict)

characters = []
count = 0
for i in char_dict:
    characters.append(i[0])
    count += 1
    if count >= 10:
        break

print(characters)

# Create the training data
train = caer.preprocess_from_dir(char_path, characters, channels=channel, IMG_SIZE=IMG_SIZE, isShuffle=True)
# this line grab all the files in each characters folder to make a training set for it