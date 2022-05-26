from exif import Image
with open('WechatIMG932.jpeg', 'rb') as image_file:
    my_image = Image(image_file)
    my_image.has_exif
    exifInfo = my_image.list_all()
    print(my_image.has_exif)