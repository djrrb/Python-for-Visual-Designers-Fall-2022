# use hs
import os
import shutil

# make a new directory
# even if the directory already exists
os.makedirs('cats', exist_ok=True)

# copy the image to a new name inside the new directory
shutil.copy(
    'Juvenile_Ragdoll.jpg', 
    'cats/thisIsACopy.jpg'
)

