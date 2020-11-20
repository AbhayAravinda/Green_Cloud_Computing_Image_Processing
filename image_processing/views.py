from django.shortcuts import render, redirect
from django.conf import settings

from .models import imagesDB
from .forms import imageForm

from os import path
import numpy as np
import cv2


def index(request):
    context = {'form':imageForm()}
    return render(request, "frontend.html", context)


def upload_image(request):
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            option = form.cleaned_data.get("option")
            image = form.cleaned_data.get("image")
            obj = imagesDB.objects.create(
                image=image
            )
            obj.save()
            
            s=path.join(settings.MEDIA_ROOT,str(obj.image))
            
            img = cv2.imread(s)
            # # GrayScale
            if option == 'grayscale':
                img_out = cv2.imread(s, 0)
            
            # # Histogram equalization
            elif option == 'histogram':
                img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
                img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
                img_out = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

            # # Gaussian Blur
            elif option == 'gaussian_blur':
                img_out = cv2.GaussianBlur(img, (7, 7), 0)

            # # Brightness Increase
            elif option == 'brightness_increase':
                img_out = cv2.convertScaleAbs(img, alpha=1.5, beta=0)

            # # Brightness Decrease
            elif option == 'brightness_decrease':
                img_out = cv2.convertScaleAbs(img, alpha=0.5, beta=0)

            # # Color inversion
            elif option == 'color_inversion':
                img_out = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # # Negative image
            elif option == 'negative_image':
                img_out = cv2.bitwise_not(img)

            # # Sepia Effect
            elif option == 'sepia':
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                normalized_gray = np.array(gray, np.float32)/255
                sepia = np.ones(img.shape)
                sepia[:, :, 0] = 153 * normalized_gray # B
                sepia[:, :, 1] = 204 * normalized_gray # G
                sepia[:, :, 2] = 255 * normalized_gray # R

                img_out = np.array(sepia, np.uint8)

            # # Contrast Limited Adaptive Histogram Equalization (CLAHE)
            elif option == 'clahe':
                image_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                clahe = cv2.createCLAHE(clipLimit=5)
                img_out = clahe.apply(image_bw) + 30
            cv2.imwrite(s, img_out)
            
            return redirect('http://127.0.0.1:8000'+settings.MEDIA_URL+str(obj.image))
    return redirect(index)
