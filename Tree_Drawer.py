import turtle as t
import random

splitCount = int(input("How many splits per branch?"))
branchAngle = int(input("What's the angle between branches?"))
treeHeight = int(input("How tall is the tree?"))
trunkRatio = float(input("What's the ratio between Branches?"))
randomness = int(input("How much Randomness?"))
intialBranchLength = 100
speed = 0
intialAngle = (splitCount - 1) / 2 * branchAngle

screen = t.Screen()
t.teleport(0,-300)
t.left(90)
t.forward(intialBranchLength)
t.speed(speed)

def rotateTurtle(angle):
	t.right(angle)
	return angle

def randonizeAngle(angle):
	angle = angle + int (randomness * 2 * random.random()) - randomness
	return angle

def drawTree(RemainingHeight, branchLength):
	turtleAngle = 0
	if RemainingHeight == 0:
		return
	nextAngle = randonizeAngle(-intialAngle)
	turtleAngle += rotateTurtle(nextAngle)
	for i in range(splitCount):
		t.forward(branchLength)
		drawTree(RemainingHeight - 1, branchLength * trunkRatio)
		t.backward(branchLength)
		nextAngle = randonizeAngle(branchAngle)
		turtleAngle += rotateTurtle(nextAngle)
	turtleAngle += rotateTurtle(-turtleAngle)


drawTree(treeHeight - 1, trunkRatio * intialBranchLength)
t.backward(intialBranchLength)

screen.exitonclick()

