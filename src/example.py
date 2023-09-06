# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:42:58 2016

@author: utkarsh
"""

import sys
from FingerprintImageEnhancer import FingerprintImageEnhancer
import cv2
import os #this package makes the fingerprint_enhancer can process the images in a batch

if __name__ == '__main__':

    image_enhancer = FingerprintImageEnhancer()         # Create object called image_enhancer

    image_folder_path = '../images/' # create the folder path for the input images
    enhanced_folder_path = '../enhanced/' #create the folder path for the output enhanced images

    print("load images...")
    for img_name in os.listdir(image_folder_path): #loop through all the images in the input image folder
        print(f'Processing {img_name}...')

        img_path = os.path.join(image_folder_path, img_name)
        img = cv2.imread(img_path)
        if(len(img.shape)>2):                               # convert image into gray if necessary
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        out = image_enhancer.enhance(img)     # run image enhancer

        filename, file_extension = os.path.splitext(img_name) # enhanced images
        enhanced_img_name = f"{filename}_enhanced{file_extension}"

        enhanced_img_path = os.path.join(enhanced_folder_path, enhanced_img_name)
        image_enhancer.save_enhanced_image(enhanced_img_path)   # save output
    print("save result...")
