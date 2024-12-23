from PIL import Image
#Open image using Image module
im = Image.open("E:/data/irs.jpg")
im.show()
print(im.mode)
image = im.convert("CMYK")
print(image.mode)
#1:1-bit pixels, black and white, where each pixel is either black or white.
#L:Grayscale images,8-bit pixels where each pixel has a value between 0 (black) and 255 (white)
#P	8-bit pixels, mapped to any other mode using a color palette.
#RGB:Color images, where each pixel is represented by three values: red, green, and blue.
#CMYK:Color images, where each pixel is represented by four values: cyan, magenta, yellow, and black.
#Show actual Image
im.show()
#Show rotated Image
im = im.rotate(55)
im.show()
im.save('E:/data/test.jpg')

# thumbnails
from PIL import Image
image = Image.open("E:/data/irs.jpg")
image.info  #Image info
image.format
image.mode
image.size  
image.width
image.height
image.thumbnail((90,90))
image.save('E:/data/thumbnail2.jpg','JPEG')
image1 = Image.open('E:/data/irs.jpg')
image1.show()

# merge the image horizentally
#to perform the merge operation, we need to make sure both images should be the same size.

from PIL import Image

# Load the images
image1 = Image.open("E:/data/img1.jpg")
image1.show()
image2 = Image.open("E:/data/img2.jpg")
image2.show()
# Get the dimensions of the images
width1, height1 = image1.size
width1, height1
width2, height2 = image2.size
width2, height2
# Create a new image with the combined width and the height of the tallest image
new_width = width1 + width2
new_height = max(height1, height2)
new_image = Image.new("RGB", (new_width, new_height))

# Paste the two images onto the new image
new_image.paste(image1, (0, 0))
new_image.paste(image2, (width1, 0))
new_image.show()
# Save the new image
new_image.save("E:/data/img53.jpg","JPEG")

# merge vertically

from PIL import Image

# Load the images
image1 = Image.open("E:/data/img1.jpg")
image2 = Image.open("E:/data/img2.jpg")

# Get the dimensions of the images
width1, height1 = image1.size
width1, height1
width2, height2 = image2.size
width2, height2
# Create a new image with the combined width and the height of the tallest image
new_width = max(width1, width2)
new_width
new_height = height1 + height2
new_height
new_image = Image.new("RGB", (new_width, new_height))
new_image

# Paste the two images onto the new image
new_image.paste(image1, (0, 0)) 
# first image (image1) being pasted starting from the top−left corner (0, 0)
# second image (image2) being pasted starting from the top−right corner of the first image (width1, 0). 
new_image.paste(image2, (0, height1))
new_image.show()
# Save the new image
new_image.save("E:/data/img54.jpg","JPEG",quality=57)
new_image.show()
# Change the resolution
#Changing the resolution of an image simply means reducing or increasing the 
#number of pixels in an image, without changing its dimensions or any other factor.
#the range of 0 to 100 where 95 is considered as best because 100 disables some portions of jpeg compression algorithm
#image_file.save() method have a parameter named quality, that specifies the resolution of an image

# Enhance Brightness of image
from PIL import Image
from PIL import ImageEnhance 
image = Image.open("E:/data/img1.jpg")
image.show()
curnt_bri = ImageEnhance.Brightness(image)
curnt_bri
new_bri = 1.5
  
# Brightness enhanced by  1.5 
af_brt = curnt_bri.enhance(new_bri) 
  
# shows updated image in image viewer 
af_brt.show()   

#Enhance Contrast of image

from PIL import Image 
from PIL import ImageEnhance 
  
# Opens the image file 
image = Image.open("E:/data/img1.jpg")
image.show()
  
 
# Enhance Contrast 
curr_con = ImageEnhance.Contrast(image) 
new_con = 0.3
  
# Contrast enhanced by a factor of 0.3 
af_cont = curr_con.enhance(new_con) 
  
# shows updated image in image viewer 
af_cont.show()   


# blur the image
from PIL import Image, ImageFilter
#Read the two images
image1 = Image.open('E:/data/img1.jpg')
blurImage = image1.filter(ImageFilter.BLUR)
blurImage.show()

#1.Blurs the image by setting each pixel to the average value of the pixels in a
#square box extending radius pixels in each direction.
from PIL import Image
 
image = Image.open('E:/data/img1.jpg')
 
# Blurring the image
im1 = im.filter(ImageFilter.BoxBlur(4))
 
# Shows the image in image viewer
im1.show() 
#2 Gaussian blur filter. The filter uses radius as a parameter and by changing the value 
#of this radius, the intensity of the blur over the image gets changed.GaussianBlur(radius=5)

from PIL import Image
 
image = Image.open('E:/data/img1.jpg')
 
# Blurring the image
im1 = im.filter(ImageFilter.GaussianBlur(4))
 
# Shows the image in image viewer
im1.show()

#Simple blur: It applies a blurring effect to the image as specified through a 
#specific kernel or a convolution matrix.

from PIL import Image
 
image = Image.open('E:/data/img1.jpg')
 
# Blurring the image
im1 = im.filter(ImageFilter.BLUR)
 
# Shows the image in image viewer
im1.show()

# croping the image

from PIL import Image

#Create an Image Object from an Image
im = Image.open('E:/data/img1.jpg')

#Display actual image
im.show()

#Crop
#Image.crop(left, upper, right, lower) that defines the area to be cropped using two points 
#in the coordinate system: (left, upper) and (right, lower) pixel values. Those two points 
#unambiguously define the rectangle to be cropped.
cropped = im.crop((5,46,150,150))

#Display the cropped portion
cropped.show()

#Save the cropped image
cropped.save('E:/data/img5.png')

# fliped the image
from PIL import Image
# Open an already existing image
imageObject = Image.open("E:/data/img1.jpg")

# Do a flip of left and right
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
imageObject.show()
hori_flippedImage = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
hori_flippedImage.show()
hori_flippedImage = imageObject.transpose(Image.ROTATE_90)
hori_flippedImage.show()
# Show the original image
imageObject.show()

# filter the image

from PIL import Image, ImageFilter

im = Image.open('E:/data/img1.jpg')

im1 = im.filter(ImageFilter.BLUR)
im1.show()

im2 = im.filter(ImageFilter.MinFilter(3))
im2.show()

######
from PIL import Image, ImageFilter

#Import all the enhancement filter from pillow

from PIL.ImageFilter import (BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)

#Create image object
img = Image.open('E:/data/img1.jpg')
#Applying the blur filter
img1 = img.filter(BLUR)
img1.save('E:/data/img7.png')
img1.show()

#################EDGE_ENHANCE_MORE
#Import required image modules
from PIL import Image, ImageFilter

#Import all the enhancement filter from pillow
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
#Create image object
img = Image.open('E:/data/img1.jpg')
#Applying the blur filter
img1 = img.filter(EDGE_ENHANCE_MORE)
img1.save('E:/data/img8.png')
img1.show()


###############################
#write text on image
from PIL import Image, ImageDraw,ImageFont
img = Image.open('E:/data/img1.jpg')
d1 = ImageDraw.Draw(img)
d1.text((200, 10), "Hello, i am fine", fill=(255, 0, 0))
img.show()
img.save("E:/data/img8.png")
