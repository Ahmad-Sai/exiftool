from exif import Image
from PIL import Image as pilIMG

class Exif():
    def __init__(self):
        self.relevant_info = ['make','model','software','datetime','gps_longitude','gps_longitude_ref', 'gps_latitude','gps_latitude_ref']
        with open('bigman.jpg', 'rb') as image_file:
            self.my_image = Image(image_file)
        self.tags_found = [tag for tag in self.relevant_info if tag in self.my_image.list_all()]
        print(self.tags_found)
    
    
    def device_make(self):
        # retrievs make, model, and software tags embedded in image. Falls back silently if 1 or all of the tags are not found
        device_data = {}
        try:
            device_data['make'] = self.my_image.make
        except:
            pass
        try:
            device_data['model'] = self.my_image.model
        except:
            pass
        try: 
            device_data['software'] = self.my_image.software
        except:
            pass
        
        # prints key value pairs for the tags found
        for k, v in device_data.items():
            print(k +  " - " + str(v))
    
    # prints date and time embedded in the image
    def image_datetime(self):
        print("date & time - " + str(self.my_image.datetime))

    def gps_coordinates(self):
        lat = 1
        long = 1
        gps_data = {
            'Latitude': self.my_image.gps_latitude,
            'Latitude Direction': self.my_image.gps_latitude_ref,
            'Longitude': self.my_image.gps_longitude,
            'Longitude Direction': self.my_image.gps_longitude_ref,
        }
        for k, v in gps_data.items():
            print(k +  " - " + str(v))

        if self.my_image.gps_latitude_ref == 'S':
            lat = -1
        if self.my_image.gps_longitude_ref == 'W':
            long = -1

        DD_lat = lat*(self.my_image.gps_latitude[0] + (self.my_image.gps_latitude[1]/60) + (self.my_image.gps_latitude[2]/3600))
        DD_long = long*(self.my_image.gps_longitude[0] + (self.my_image.gps_longitude[1]/60) + (self.my_image.gps_longitude[2]/3600))

        print("\nDecimal Degrees:")
        print("Latitude = " + str(DD_lat))
        print("Longitude = " + str(DD_long))
    
    def extractExif(self):
        if self.tags_found:     # if the important exif data not found, then tags_found will be empty
            print("Relevant exif data was found in this image\n")
            image_exifdata = self.my_image.list_all()
            if 'make' or 'model' or 'software' in image_exifdata:
                self.device_make()
            if 'datetime' in image_exifdata:
                self.image_datetime()
            if 'gps_latitude' in image_exifdata:
                self.gps_coordinates()
        else:
            print("No relevant/dangerous exif data found in this image")
        
        # uncomment the following and repeat for whatever tags you like, then save the image
        #self.my_image.make = 'Change to whatever you like'
        

        #with open('IMG-noexif.jpg', 'wb') as new_image_file:
        #        new_image_file.write(self.my_image.get_file())
            
    def deleteExif(self):
        if self.my_image.has_exif:
            data = self.my_image.list_all()
            print(data)
            for tag in data:
                del self.my_image[tag]
            with open('IMG-noexif.jpg', 'wb') as new_image_file:
                new_image_file.write(self.my_image.get_file())
                

# instantiate class object and perform extraction
exif = Exif()
exif.extractExif()

# delete relevant/dangerous exif metadata and save the new image under name 'IMG-noexif.jpg'
exif.deleteExif()
