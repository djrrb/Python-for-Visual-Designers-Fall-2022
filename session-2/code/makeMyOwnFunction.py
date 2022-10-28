def myCenteredRect(myX, myY, myW, myH):
    print(myX, myY, myW, myH)
    rect(
        myX-myW/2,
        myY-myH/2,
        myW,
        myH
        )

myCenteredRect(0, 0, 250, 250)

translate(width()/2, height()/2)

myCenteredRect(0, 0, 250, 250)

myCenteredRect(250, 250, 80, 110)
