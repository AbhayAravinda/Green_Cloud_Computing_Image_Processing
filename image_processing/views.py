# TODO: Sort these imports in order and clear out unwanted ones

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import imagesDB
import json
from django.http import JsonResponse
import random
import string
import os
from django.http import HttpResponse
from django.conf import settings
 

import base64
from django.core.files.base import ContentFile

import numpy as np
import cv2


def index(request):
    return render(request, "frontend.html")


def upload_image(request):
    input_json =  json.loads(request.body)
    base64_image =  input_json['base64_image']
    process = input_json['process']

    file_format, encoded_string = base64_image.split(';base64,') 
    file_extension = file_format.split('/')[-1] 
    random_string = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(10)))
    decoded_image = ContentFile(base64.b64decode(encoded_string), name=random_string+'.' + file_extension)
    print(file_extension)

    fs = FileSystemStorage()
    saved_name = fs.save(decoded_image.name, decoded_image) 
    
    image_put = imagesDB(
        image_name=saved_name, image_url=settings.MEDIA_ROOT+'/'+saved_name)
    image_put.save()


    # Use opencv and edit the image
    s=settings.MEDIA_ROOT+'/'+saved_name
    img=cv2.imread(s)
    
    
    #GrayScale
    if process=='grayscale':
        img_out=cv2.imread(s,0)

    #Histogram Equilization (along Y axis)
    elif process=='histogram':
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        img_out = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    #Gaussian Blur
    elif process=='gaussian_blur':
        img_out = cv2.GaussianBlur(img, (7, 7), 0)

    #Brightness Increase
    elif process=='brightness_increase':
        alpha=1.5
        beta=0
        img_out=cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    #Brightness Decrease
    elif process=='brightness_decrease':
        alpha=0.5
        beta=0
        img_out=cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    #Color inversion
    elif process=='color_inversion':
        img_out = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    #Negative image
    elif process=='negative_image':
        img_out = cv2.bitwise_not(img)
    
    #Sepia Effect
    elif process=='sepia':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        normalized_gray = np.array(gray, np.float32)/255
        sepia = np.ones(img.shape)
        sepia[:,:,0] *= 153 #B
        sepia[:,:,1] *= 204 #G
        sepia[:,:,2] *= 255 #R
        sepia[:,:,0] *= normalized_gray #B
        sepia[:,:,1] *= normalized_gray #G
        sepia[:,:,2] *= normalized_gray #R
        img_out=np.array(sepia, np.uint8)
    
    #Contrast Limited Adaptive Histogram Equalization (CLAHE)
    elif process=='clahe':
        image_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        clahe = cv2.createCLAHE(clipLimit = 5) 
        img_out = clahe.apply(image_bw) + 30
    
    #Write
    cv2.imwrite(s, img_out) 


    return JsonResponse({'processed_image_url':('http://127.0.0.1:8000'+settings.MEDIA_URL+saved_name)})
