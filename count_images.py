import os


srcPath = './data/Foot Ulcer Segmentation Challenge/data new/augmented/'
history = './training_history/data new/'
augmFolders = os.listdir(srcPath)
subfolders = ['images/', 'labels/']
count = {}
for folder in augmFolders:
    image_directory = srcPath + folder + '/' + subfolders[0]
    count[folder] = len([file for file in os.listdir(image_directory) if file.endswith('png')])


import csv


with open('count.csv', 'w') as f:
    for key in count.keys():
        f.write("%s, %s\n" % (key, count[key]))