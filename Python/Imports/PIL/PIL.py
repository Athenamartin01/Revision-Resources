#used for image editing and creation 
import PIL

New_Image = PIL.Image.new(mode = "RGB", size = (1000,1000))
# This creates a new png file, Default Black. 

Old_Image = PIL.Image.open("Path to png file")

Image_Copy = New_Image.copy()
#Copies an image

New_Image.paste(Image_Copy, (100,100))
#pastes the image onto the newly created one starting on pixel (100,100) 
    
New_Image.save("Path to png file")
#Saves the image to a new file location