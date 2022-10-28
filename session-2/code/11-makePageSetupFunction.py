# set aside some code to reuse over and over again
def myPageSetup():
    newPage('Letter')
    font('Comic Sans MS')
    fontSize(100)
    translate(100, 100)

# call the function to run that block of code
myPageSetup()
text('hello', (0, 0))

# again
myPageSetup()
text('world', (0, 0))

# and again and again and again
myPageSetup()
myPageSetup()
myPageSetup()
myPageSetup()
rect(0, 0, 200, 200)