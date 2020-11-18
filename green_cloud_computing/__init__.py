import threading
from time import sleep
from datetime import datetime, timedelta
import pytz
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
			startTime = pytz.utc.localize(datetime.now()-timedelta(minutes=3))
			if record.image_time < startTime:
				try: # handle failure of record deletion
					record.delete()
					print(record.image_url) 
					if os.path.exists(record.image_url):
						os.remove(record.image_url)
					else:
						print("The file does not exist")
				except:
					pass
		sleep(100)

t = threading.Thread(target = threaded_function, name='file_deletion_thread', daemon=True)
t.start()