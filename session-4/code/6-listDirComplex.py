import os

# what folder to list ('.' is current folder)
myBaseFolder = '.'

# what file types to draw
myAcceptedFileTypes = ['.pdf', '.jpg', '.png', '.tif', '.gif']

# loop through the files in he folder
for myFile in os.listdir(myBaseFolder):
    print(myFile)
    #if myFile.endswith('.png') or myFile.endswith('.jpg'):
    
    # this looks at the last 4 charcters of the file and sees if that string is in the myAcceptedFileTypes list
    if myFile[-4:] in myAcceptedFileTypes:
        print('\tthis is an image!')
        # if it's an image, get the full path
        myPath = os.path.join(myBaseFolder, myFile)    
        # now create the image
        myImage = ImageObject(myPath)
        # get the size
        newPage(*myImage.size())
        # draw it to canvas
        image(myImage, (0, 0))

