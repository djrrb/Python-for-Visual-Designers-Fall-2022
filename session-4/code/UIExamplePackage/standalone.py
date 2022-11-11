# https://forum.drawbot.com/topic/257/ui-with-update-function/7?lang=en-US

import vanilla
import drawBot
from AppKit import NSColor


# create a custom controller calss
class MyController:
    
    def __init__(self):
        # use vanilla to create a window
        self.w = vanilla.Window((800, 800), minSize=(200, 200))
        # add a text box
        self.w.textSizeText = vanilla.TextBox((10, 10, -10, 22), "Text Size:")
        # add a slider
        self.w.textSize = vanilla.Slider((80, 10, -10, 22), value=20, minValue=8, maxValue=50)
        # add a button and set the hit callback to `drawIt`
        self.w.update = vanilla.Button((150, 40, -150, 22), "Update", callback=self.drawIt)
        
        self.w.colors = vanilla.ColorWell((10, 60, -750, -700),color=NSColor.redColor())
        
        self.w.checkBox = vanilla.CheckBox((60, 80, -10, 20), "use color", value=True)
        
        # add a drawBot preview
        self.w.preview = drawBot.ui.drawView.DrawView((0, 120, 0, 0))
        self.w.open() # open the window        
         
    def drawIt(self, sender):
        # the callback when ever the button is hit
        # get the font size from the slider
        fontSize = self.w.textSize.get()
   
        # start a new drawing
        drawBot.newDrawing()
        # add a page
        drawBot.newPage(100, 100)
        # set a font size
        drawBot.fontSize(fontSize)
        # draw some thext
        drawBot.text(f"{fontSize}pt Hello foo bar", (10, 10))
        
        if self.w.checkBox.get():
            color = self.w.colors.get()
        else:
            color = 0
            
        fill(color)
        rect(0,50,self.w.textSize.get(), 30)
        
        # get the pdf document
        pdf = drawBot.pdfImage()
        # set the pdf document in the preview
        self.w.preview.setPDFDocument(pdf)
        # clean up
        drawBot.endDrawing() 

# open your controller
MyController()