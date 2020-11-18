from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import imagesDB
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
 
from datetime import datetime, timedelta
from time import sleep 

# OpenCV
import numpy as np
import cv2
from PIL import Image


def index(request):
    return render(request, "frontend.html")


def upload_image(request):
    uploaded_file = request.FILES['filename']
    fs = FileSystemStorage()
    saved_name = fs.save(uploaded_file.name, uploaded_file) 
    
    for record in imagesDB.objects.all():
        time_elapsed = datetime.now() - record.image_time
        if time_elapsed > timedelta(hours=1):
            record.delete()
        print(record.image_url) 
        


    image_put = imagesDB(
        image_name=uploaded_file.name, image_url=settings.MEDIA_ROOT+'/'+saved_name)
    image_put.save()


    # Use opencv and edit the image
    s=settings.MEDIA_ROOT+'/'+saved_name
    img=cv2.imread(s)
    
    
    #GrayScale
    if process=='GrayScale':
        img_out=cv2.imread(s,0)

    #Histogram Equilization (along Y axis)
    elif process=='Histogram_Equilization':
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        img_out = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    #Gaussian Blur
    elif process=='Image_Blur':
        img_out = cv2.GaussianBlur(img, (7, 7), 0)

    #Brightness Increase
    elif process=='Brightness_Increase':
        alpha=1.5
        beta=0
        img_out=cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    #Brightness Decrease
    elif process=='Brightness_Decrease':
        alpha=0.5
        beta=0
        img_out=cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    #Color inversion
    elif process=='Color_Inversion':
        img_out = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    #Negative image
    elif process=='Negarive_Image':
        img_out = cv2.bitwise_not(img)
    
    #Sepia Effect
    elif process=='Sepia_Effect':
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
    elif process=='CLAHE':
        image_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        clahe = cv2.createCLAHE(clipLimit = 5) 
        img_out = clahe.apply(image_bw) + 30
    
    #Write
    cv2.imwrite(s, img_out) 


    return redirect('http://127.0.0.1:8000'+settings.MEDIA_URL+saved_name)
