# import exifread

# with open("one.jpg", "rb") as f:
#     tags = exifread.process_file(f)
#     a = tags['Image Model']
#     image_model = tags.get('Image Model')
#     gps_latitude = tags.get('GPS GPSLatitude')
#     gps_longitude = tags.get('GPS GPSLongitude')
#     date_time_original = tags.get('EXIF DateTimeOriginal')
    
#     print(f"Model name: {a}")
#     print(f"Date and Time: {date_time_original}")   
#     print(f"Image Model: {image_model}")
    
#     if gps_latitude and gps_longitude:
#         lat_deg_num, lat_deg_denom = gps_latitude.values
#         lon_deg_num, lon_deg_denom = gps_longitude.values

#         latitude = lat_deg_num / lat_deg_denom
#         longitude = lon_deg_num / lon_deg_denom

#         print(f"GPS Latitude: {latitude}")
#         print(f"GPS Longitude: {longitude}")
#     else:
#         print("GPS coordinates not found in the EXIF data.")
  
  
  
# from exif import Image
  
# with open("lo.jpg","rb") as f:
#     img2 = Image(f)
#     # print(img2)
#     a=img2._gps_ifd_pointer
#     b=img2.make
#     c=img2.model
#     d=img2.gps_timestamp
#     e=img2.gps_datestamp
#     f=img2.datetime_original
#     g=img2.datetime
#     h=img2.gps_altitude_ref
#     j=img2.subsec_time_original
#     u=img2._gps_ifd_pointer

#     # print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
#     print(f)
#     print(h)
#     print(j)
#     print(u)

#     gps_info = img2.gps_altitude_ref
#     # gps_infos = img2.gps_longitude_ref
#     print(gps_info , "altibude")
#     # print(gps_infos , ";long")
#     # print(f"Make: {img.make}")


import PIL.Image
import PIL.ExifTags

oneimp = PIL.Image.open("lo.jpg")

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in oneimp._getexif().items()
    if k in PIL.ExifTags.TAGS
}

# print(exif)


north=exif['GPSInfo'][2]
east=exif['GPSInfo'][4]

lats=((((north[0] * 60)+north[1])*60)+north[2])/60/60
long=((((east[0] * 60)+north[1])*60)+north[2])/60/60


from gmplot import gmplot

gmap=gmplot.GoogleMapPlotter(lats , long , 12)

gmap.marker(lats , long, "cornflowerblue")
gmap.draw("jugal.html")



from geopy.geocoders import Nominatim

geoloc=Nominatim(user_agent="GetLoc")

locnames=geoloc.reverse(f"{lats} , {long}")

print(locnames.address)