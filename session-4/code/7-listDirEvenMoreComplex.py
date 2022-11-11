import os

myBaseFolder = '/Users/david/Dropbox (Personal)/Public/Python-for-Visual-Designers-Fall-2022/session-3/challenges'

myAcceptedFileTypes = ['.pdf', '.jpg', '.png', '.tif', '.gif']

for myFile in os.listdir(myBaseFolder):
    print(myFile)
    #if myFile.endswith('.png') or myFile.endswith('.jpg'):
    for myAcceptedFileType in myAcceptedFileTypes:
        print('testing file type', myAcceptedFileType)
        if myFile.endswith(myAcceptedFileType):
            print('\tthis is a image!')
            myPath = os.path.join(myBaseFolder, myFile)

            myImage = ImageObject(myPath)
            newPage(*myImage.size())
            image(myImage, (0, 0))
            break

