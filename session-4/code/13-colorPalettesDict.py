# define color palettes as a dictionary of dictionaries
# the lower-level dictionary maps color names to RGB color tuples
# the top-level dictionary maps palette names to palette dictionaries

myPalettes = {
    'primary':
        {
            'foreground': (1, 0, 0),
            'background': (0, 0, 1)
            },
            
    'darkmode':
        {
            'foreground': (1, 1, 1),
            'background': (0, 0, 0)
            },
            
    'lightmode':
        {
            'foreground': (0, 0, 0),
            'background': (1, 1, 1)
            },
            
    }

# loop through all the palettes
for myActivePalette in myPalettes:
    # make a new page
    newPage()

    # set the fill to the background color
    fill(*myPalettes[myActivePalette]['background'])
    # draw a background
    rect(0, 0, width(), height())

    # set fill to the foreground color
    fill(*myPalettes[myActivePalette]['foreground'])
    # draw a shape
    oval(200, 200, 600, 600)
