import os

# what folder to list ('.' is current folder)

myBaseFolder = '.' # the folder to search

# the formats we can draw to canvas
myAcceptedFileTypes = ['.pdf', '.jpg', '.png', '.tif', '.gif']

# loop through all files
for myFile in os.listdir(myBaseFolder):
    print(myFile)
    # now check all acceptedFileTypes against current filetype
    for myAcceptedFileType in myAcceptedFileTypes:
        print('\ttesting file type', myAcceptedFileType)
        # if we have a match to the accepted file type
        if myFile.endswith(myAcceptedFileType):
            print('\t\tthis is a image! draw it')
            # make a full path
            myPath = os.path.join(myBaseFolder, myFile)
            # define image
            myImage = ImageObject(myPath)
            # make canvas that size
            newPage(*myImage.size())
            # draw image
            image(myImage, (0, 0))
            # once we have drawn the image, we don’t have to keep testing
            # so we can break the loop and move on to the next item
            break

