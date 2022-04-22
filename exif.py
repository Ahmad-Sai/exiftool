from exif import Image

class Exif():
    def __init__(self):
        self.relevant_info = ['make','model','software','datetime','gps_longitude','gps_longitude_ref', 'gps_latitude','gps_latitude_ref']
        with open('cat.jpg', 'rb') as image_file:
            self.my_image = Image(image_file)
        self.embedded_exif = self.my_image.has_exif
    
    def extractExif(self):
        if self.embedded_exif:
            exif_data = {
                'make': self.my_image.make,
                'model': self.my_image.model,
                'software': self.my_image.software,
                'datetime': self.my_image.datetime,
                'gps_latitude': self.my_image.gps_latitude,
                'gps_latitude_ref': self.my_image.gps_latitude_ref,
                'gps_longitude': self.my_image.gps_longitude,
                'gps_longitude_ref': self.my_image.gps_longitude_ref,
            }
            print("This image has Exif Data")
            print("Exif data found\n")

            lat = 1
            long = 1
            image_exifdata = self.my_image.list_all()

            for i in range(len(self.relevant_info)):
                if self.relevant_info[i] in image_exifdata:
                    print(self.relevant_info[i] + ' -- ' + str(exif_data[self.relevant_info[i]]))
            if ('gps_longitude' and 'gps_longitude_ref' and 'gps_latitude' and 'gps_latitude_ref') in image_exifdata:

                if self.my_image.gps_latitude_ref == 'S':
                    lat = -1
                if self.my_image.gps_longitude_ref == 'W':
                    long = -1

                DD_lat = lat*(self.my_image.gps_latitude[0] + (self.my_image.gps_latitude[1]/60) + (self.my_image.gps_latitude[2]/3600))
                DD_long = long*(self.my_image.gps_longitude[0] + (self.my_image.gps_longitude[1]/60) + (self.my_image.gps_longitude[2]/3600))

                print("\nDecimal Degrees:")
                print("Latitude = " + str(DD_lat))
                print("Longitude = " + str(DD_long))


                
