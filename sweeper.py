import sweepF

print()
print("Welcome to Edward's lidl minesweeper!")
print()

replay = 'Y'
while replay.lower() == 'y':
	loss = False
	print('Designate the dimensions for this battlefield.')
	rows = int(input('How many rows are there? '))
	while rows <= 0:
		print('Rows must be greater than 0.')
		rows = int(input('How many rows are there? '))
	columns = int(input('How many columns are there? '))
	while columns <= 0:
		print('Columns must be greater than 0.')
		columns = int(input('How many columns are there? '))

	print('Possible difficulties:')
	print('1. Easy')
	print('2. Intermediate')
	print('3. Advanced')
	print('4. Custom')
	difficulty = int(input('Input a difficulty number: '))

	board = sweepF.make_board(rows, columns)
	puzzle = sweepF.mine_layer(rows, columns, difficulty)

	solved = False
	while not solved:
		temp = []
		for row in board:
			print(row)
		try:
			row = int(input('Which row would you like to choose'+\
					'(f to flag)? '))
			col = int(input('Which column would you like to choose'+\
					'(f to flag)? '))
			coord = sweepF.Coord(row, col)
			board = sweepF.coord_checker(puzzle, board, coord)
		except:
			flagR = int(input('Which row do you want to flag? '))
			flagC = int(input('Which column do you want to flag? '))
			flagCoord = sweepF.Coord(flagR, flagC)
			board = sweepF.flagger(puzzle, board, flagCoord)
		try:
			if board.lower() == 'y' or board.lower() == 'n':
				loss = True
				replay = board
		except:
			pass
		solved = sweepF.checker(board)

	if not loss:
		for row in board:
			print(row)
		print('You win! GG!')
		replay = input('Replay (Y/N)? ')
