import os
import shutil

os.mkdir('cats')

shutil.copy(
    'Juvenile_Ragdoll.jpg', 
    'cats/thisIsACopy.jpg'
)

