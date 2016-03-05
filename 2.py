def print_board(board):

	print "O pinakas tou paixnidiou einai: \n"

	for i in range(3):
		print " ",
		for j in range(3):
			if board[i*3+j] == 1:
				print 'X',
			elif board[i*3+j] == 0:
				print 'O',	
			elif board[i*3+j] != -1:
				print board[i*3+j]-1,
			else:
				print ' ',
			
			if j != 2:
				print " | ",
		print
		
		if i != 2:
			print "-----------------"
		else: 
			print 
			
def print_instruction():
	print "Xrisimopoieiste tous akoloythous arithmous keliou gia na paiks	ete"
	print_board([2,3,4,5,6,7,8,9,10])
#	print_board([2,2,3])

def get_input(turn):

	valid = False
	while not valid:
		try:
			user = raw_input("Pou tha thelete na topothetisete " + turn + " (1-9)? ")
			user = int(user)
			if user >= 1 and user <= 9:
				return user-1
			else:
				print "Auth den einai egkurh kinisi! Ksanaprospathiste!\n"
				print_instruction()
		except Exception as e:
			print user + " Auth den einai egkurh kinisi! Ksanaprospathiste!\n"
		
def check_win(board):
	win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
	for each in win_cond:
		try:
			if board[each[0]-1] == board[each[1]-1] and board[each[1]-1] == board[each[2]-1]:
				return board[each[0]-1]
		except:
			pass
	return -1

def quit_game(board,msg):
	print_board(board)
	print msg
	quit()

def main():
	
	# Start Game
	# Change turns
	# Checks for winner
	# Quits and redo board
	
	print_instruction()

	board = []
	for i in range(9):
		board.append(-1)

	win = False
	move = 0
	while not win:

		# Print board
		print_board(board)
		print "Arithmos seiras " + str(move+1)
		if move % 2 == 0:
			turn = 'X'
		else:
			turn = 'O'

		# Get player input
		user = get_input(turn)
		while board[user] != -1:
			print " Auth den einai egkurh kinisi! To keli einai piasmeno. Ksanaprospathiste.\n"
			user = get_input(turn)
		board[user] = 1 if turn == 'X' else 0

		# Continue move and check if end of game
		move += 1
		if move > 4:
			winner = check_win(board)
			if winner != -1:
				out = "O nikitis einai " 
				out += "X" if winner == 1 else "O" 
				out += ""
				quit_game(board,out)
			elif move == 9:
				quit_game(board,"Den yparxei nikitis")

if __name__ == "__main__":
	main()
	
