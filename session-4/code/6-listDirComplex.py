import os

myBaseFolder = '/Users/david/Dropbox (Personal)/Public/Python-for-Visual-Designers-Fall-2022/session-3/challenges'

myAcceptedFileTypes = ['.pdf', '.jpg', '.png', '.tif', '.gif']

for myFile in os.listdir(myBaseFolder):
    print(myFile)
    #if myFile.endswith('.png') or myFile.endswith('.jpg'):
    if myFile[-4:] in myAcceptedFileTypes:
        print('\tthis is a png!')
        myPath = os.path.join(myBaseFolder, myFile)

        myImage = ImageObject(myPath)
        newPage(*myImage.size())
        image(myImage, (0, 0))

