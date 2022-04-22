class Exif():
    def __init__(self):
        self.relevant_info = ['make','model','software','datetime','gps_longitude','gps_longitude_ref', 'gps_latitude','gps_latitude_ref']
        with open('cuboulder.jpg', 'rb') as image_file:
            self.my_image = Image(image_file)
        self.tags_found = [tag for tag in self.relevant_info if tag in self.my_image.list_all()]
    
    
    def device_make(self):
        print("make - " + str(self.my_image.make))
        
    def device_model(self):
        print("model - " + str(self.my_image.model))
        
    def device_software(self):
        print("software - " + str(self.my_image.software))
        
    def image_datetime(self):
        print("datetime - " + str(self.my_image.datetime))

    def gps_coordinates(self):
        lat = 1
        long = 1
        gps_data = {
            'gps_latitude': self.my_image.gps_latitude,
            'gps_latitude_ref': self.my_image.gps_latitude_ref,
            'gps_longitude': self.my_image.gps_longitude,
            'gps_longitude_ref': self.my_image.gps_longitude_ref,
        }
        for k, v in gps_data.items():
            print(k, v)

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
        if self.tags_found:
            print("Relevant exif data was found in this image\n")
            image_exifdata = self.my_image.list_all()
            if 'make' in image_exifdata:
                self.device_make()
            if 'model' in image_exifdata:
                self.device_model()
            if 'software' in image_exifdata:
                self.device_software()
            if 'datetime' in image_exifdata:
                self.image_datetime()
            if 'gps_latitude' in image_exifdata:
                self.gps_coordinates()
        else:
            print("No relevant exif data found in this image")
            
    def deleteExif(self, delete_list):
        if embedded_exif:
            for i in range(len(delete_list)):
                if (delete_list[i] in self.relevant_info) and (self.relevant_info[i] in self.my_image):
                    pass
