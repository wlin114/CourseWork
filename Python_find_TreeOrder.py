#given preorder and inorder to find postorder

def _postorder(preorder, inorder):
	if len(inorder) <= 1:
		return inorder
	if len(preorder) <=1:
		return preorder
	indexNum = preorder[0]
	index = inorder.index(indexNum)
	left = inorder[:index]
	right = inorder[index+1:]
	leftString = _postorder(preorder[1:], left)
	rightSttring = _postorder(preorder[index+1:], right)
	return leftString + rightSttring + [indexNum]

def postorder(preorder, inorder):
	print _postorder(preorder, inorder)

postorder([1,2,3,5], [2,1,3,5])
postorder([7,1,0,3,2,5,4,6,9,8,10], [0,1,2,3,4,5,6,7,8,9,10])