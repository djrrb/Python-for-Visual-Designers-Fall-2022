# set a variable font as the font
font('CondorVariable-VF.ttf')
# make the size bigger
fontSize(100)

# move to the middle bottom
translate(width()/2, 40)

# set a starting weight value
myWeightValue = 200

# make a loop
for myNumber in range(10):
    # set the canvas font variations
    fontVariations(wdth=80, wght=myWeightValue, ital=0.0)

    # draw the text
    text('Variable!', (0, 0), align="center")
    # move up before drawing the next one
    translate(0, 96)
    # augment the weight value so the next one is heavier
    myWeightValue += 80