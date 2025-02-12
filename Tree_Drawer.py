import turtle as t

splitCount = int(input("How many splits per branch?"))
branchAngle = int(input("What's the angle between branches?"))
treeHeight = int(input("How tall is the tree?"))
trunkRatio = float(input("What's the ratio between Branches?"))
intialBranchLength = 100
speed = 0

intialAngle = (splitCount - 1) / 2 * branchAngle

screen = t.Screen()
t.teleport(0,-300)
t.left(90)
t.forward(intialBranchLength)
t.speed(speed)


def drawTree(RemainingHeight, branchLength):
	if RemainingHeight == 0:
		return
	t.left(intialAngle)
	for i in range(splitCount):
		t.forward(branchLength)
		drawTree(RemainingHeight - 1, branchLength * trunkRatio)
		t.backward(branchLength)
		t.right(branchAngle)
	t.left(branchAngle)
	t.left(intialAngle)


drawTree(treeHeight - 1, trunkRatio * intialBranchLength)

screen.exitonclick()

