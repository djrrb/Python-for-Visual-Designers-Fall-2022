
fill(1, 0, 0)
rect(0, 0, 100, 100)
with savedState():
    fontSize(100)
    text('hello world', (200, 200))
fontSize(12)
fill(0)
text('this is more text', (200, 500))