import threading
from time import sleep
from datetime import datetime, timedelta
import pytz
from django.conf import settings
import os

def threaded_function():
	importing = True
	while (importing):
		try:
			from image_processing.models import imagesDB
			importing = False
		except: 
			pass

	while True:
		for record in imagesDB.objects.all():
			startTime = pytz.utc.localize(datetime.now()-timedelta(minutes=15))
			print(startTime)
			print(datetime.now())
			print(record.image_time)
			if record.image_time < startTime:
				try: # handle failure of record deletion
					record.delete()
					print(record.image) 
					image_url= os.path.join(settings.MEDIA_ROOT,str(record.image))
					if os.path.exists(image_url):
						os.remove(image_url)
					else:
						print("The file does not exist")
				except:
					pass
		sleep(600)

t = threading.Thread(target = threaded_function, name='file_deletion_thread', daemon=True)
t.start()