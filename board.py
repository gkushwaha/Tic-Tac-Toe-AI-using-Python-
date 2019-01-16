import random

board = [' ' for x in range(0, 10)]
#print(board)

def insertLetter(letter, pos):
	board[pos] = letter

def spaceIsFree(pos):
	return board[pos] == ' '

def printBoard(board):
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')

def isWinner(board, letter):
	#print(board)
	return ((board[7]==letter and board[8]==letter and board[9]==letter) or
	(board[4]==letter and board[5]==letter and board[6]==letter) or
	(board[1]==letter and board[2]==letter and board[3]==letter) or
	(board[1]==letter and board[4]==letter and board[7]==letter) or
	(board[2]==letter and board[5]==letter and board[8]==letter) or
	(board[3]==letter and board[6]==letter and board[9]==letter) or
	(board[1]==letter and board[5]==letter and board[9]==letter) or
	(board[3]==letter and board[5]==letter and board[7]==letter))


def playerMove():
	run = True
	while run:
		move=input("please select a position to place a X (1-9):")
		try:
			move=int(move)
			if move>0 and move<10:
				if spaceIsFree(move):
					run = False
					insertLetter('X', move)
				else:
					print('sorry the position has been taken')
			else:
				print('please enter in the range!')
					
		except:
			print("please enter a integer between 1-9")

def compMove():
	possibleMove = [x for x, letter in enumerate(board) if letter == ' ' and x!=0]
	move = 0

	#print (possibleMove)
	for a in ['O', 'X']:
		for i in possibleMove:
			boardCopy=board[:]
			boardCopy[i]=a
			if isWinner(boardCopy, a):
				move = i
				return move

	cornerMoveOpen = []
	for i in possibleMove:
		if i in [1, 3, 7, 9]:
			cornerMoveOpen.append(i)

	if len(cornerMoveOpen)>0:
		move = selectRandom(cornerMoveOpen)
		return move

	if 5 in possibleMove:
		move = i
		return move

	edgeOpen=[]
	for i in possibleMove:
		if i in [2, 4, 6, 8]:
			edgeOpen.append(i)

	if len(edgeOpen)>0:
		move = selectRandom(edgeOpen)
		return move


def selectRandom(OpenPosition):
	length = len(OpenPosition)
	r = random.randrange(0, length)
	return r

def isBoardFull(board):
	if board.count(' ')>1:
		return False
	else:
		return True


def main():
	print("welcome to Tic-Tac-Toe")
	printBoard(board)

	
	while not(isBoardFull(board)):
		
		if not(isWinner(board, 'X')):
			playerMove()
			printBoard(board)
			#print(isWinner(board, 'X'))
		else:
			print("Player X is the winner!!!")
			break

		if isWinner(board, 'O'):
			print("Sorry you loss!!")
			break
		else:
			move = compMove()
			if move == 0:
				print("Tie Game")
			else:
				#print(move)
				insertLetter('O', move)
				print("Computer placed an \'O\' in position", move, ":")
				printBoard(board)

	if isBoardFull(board):
		print("it's a tie")

if __name__ == '__main__':
    main()


