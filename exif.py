from exif import Image

def extractExif():
    relevant_info = ['make','model','software','datetime','gps_longitude','gps_longitude_ref', 'gps_latitude','gps_latitude_ref']
    with open('cat.jpg', 'rb') as image_file:
        my_image = Image(image_file)
    
    if my_image.has_exif:
        exif_data = {
            'make': my_image.make,
            'model': my_image.model,
            'software': my_image.software,
            'datetime': my_image.datetime,
            'gps_latitude': my_image.gps_latitude,
            'gps_latitude_ref': my_image.gps_latitude_ref,
            'gps_longitude': my_image.gps_longitude,
            'gps_longitude_ref': my_image.gps_longitude_ref,
        }
        print("This image has Exif Data")
        print("Exif data found\n")
        
        lat = 1
        long = 1
        image_exifdata = my_image.list_all()
        #print(my_image.list_all())
        for i in range(len(relevant_info)):
            if relevant_info[i] in image_exifdata:
                print(relevant_info[i] + ' -- ' + str(exif_data[relevant_info[i]]))
        if ('gps_longitude' and 'gps_longitude_ref' and 'gps_latitude' and 'gps_latitude_ref') in image_exifdata:
            
            if my_image.gps_latitude_ref == 'S':
                lat = -1
            if my_image.gps_longitude_ref == 'W':
                long = -1
                
            DD_lat = lat*(my_image.gps_latitude[0] + (my_image.gps_latitude[1]/60) + (my_image.gps_latitude[2]/3600))
            DD_long = long*(my_image.gps_longitude[0] + (my_image.gps_longitude[1]/60) + (my_image.gps_longitude[2]/3600))
            
            print("\nDecimal Degrees:")
            print("Latitude = " + str(DD_lat))
            print("Longitude = " + str(DD_long))
            
            
                
