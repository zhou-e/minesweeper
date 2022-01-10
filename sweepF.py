import random

class Coord():
	'''
	Coordinate for a designated spot in the puzzle
	'''
	def __init__(self, row, col):
		self.row = row
		self.col = col

def make_board(dimX = 8, dimY = 8):
	puzzle = []
	for y in range(dimY):
		temp = []
		for x in range(dimX):
			temp.append('?')
		puzzle.append(temp)
	return puzzle

def mine_layer(rows, columns, difficulty):
	puzzle = []
	for y in range(rows):
		temp = []
		for x in range(columns):
			temp.append('0')
		puzzle.append(temp)
	try:
		if difficulty < 4:
			mines = (difficulty+1)*10
		elif difficulty == 4:
			mines = int(input('How many mines do you want? '))
		else:
			print('Alright then. Expert it is.')
			mines = 50
	except ValueError as e:
		print(e)
		mines = 20
	except:
		print('Bruh, why you gotta break my program like this.')
		mines = 20

	if mines > len(puzzle)*len(puzzle[0]):
		for i in range(len(puzzle)):
			for index in range(len(puzzle[i])):
				puzzle[i][index] = '*'
		return puzzle

	mineCount = 0
	while mineCount < mines:
		coord = Coord(random.randint(0, len(puzzle)-1), random.randint(0, len(puzzle[0])-1))
		if puzzle[coord.row][coord.col] != '*':
			puzzle[coord.row][coord.col] = '*'
			mineCount += 1
	return puzzle

def surround(puzzle, coord):
	count = 0
	for row in range(max(coord.row-1, 0), min(coord.row+2, len(puzzle))):
		for col in range(max(coord.col-1, 0), min(coord.col+2, len(puzzle[0]))):
			if puzzle[row][col] == '*':
				count += 1
	return count

def spot_zero(puzzle, board, zeros):
	tracker = False
	for row in range(max(zeros[-1][0]-1, 0), min(zeros[-1][0]+2, len(puzzle))):
		for col in range(max(zeros[-1][1]-1, 0), min(zeros[-1][1]+2, len(puzzle[0]))):
			count = surround(puzzle, Coord(row,col))
			if count == 0 and board[row][col] != ' ' and puzzle[row][col] != '*':
				board[row][col] = ' '
				if not (row, col) in zeros:
					zeros.append((row, col))
				tracker = True
			elif board[row][col] == ' ':
                                pass
			elif puzzle[row][col] == '*':
                                board[row][col] = '*'
			else:
				board[row][col] = repr(count)
	if not tracker:
		zeros.pop(-1)
	return (board, zeros)

def coord_checker(puzzle, board, coord):
	zeros = []
	if puzzle[coord.row][coord.col] == '*':
		for row in puzzle:
			print(row)
		print('OOF, you died. Try agane?')
		return input('Y/N ')
	else:
		count = surround(puzzle, coord)
		if count == 0:
			zeros.append((coord.row, coord.col))
			while len(zeros) > 0:
				tup = spot_zero(puzzle, board, zeros)
				board = tup[0]
				zeros = tup[1]
		else:
			board[coord.row][coord.col] = repr(count)
	return board

def flagger(puzzle, board, coord):
	if puzzle[coord.row][coord.col] == '*':
		board[coord.row][coord.col] = 'f'
	else:
		print('You lose, big idiot! Try again?')
		return input('Y/N ')
	return board

def checker(puzzle):
	for row in puzzle:
		if '?' in row:
			return False
	return True
