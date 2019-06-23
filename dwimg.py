#package for searching an image in google
from google_images_download import google_images_download 
#for downloading image
response = google_images_download.googleimagesdownload() 
#funciton for downloading images
def downloadimages(search_item,n_item): 
	arguments = {"keywords": search_item, "format": "jpg", "limit":n_item, "aspect_ratio": "panoramic"} 
	try: 
		response.download(arguments) 
	except FileNotFoundError: 
		pass

search_item=raw_input("What you want to search?, Please enter=")
n_item=int(raw_input("Enter number Images you want to search="))

downloadimages(search_item,n_item) 
print()
