#TIC TAC TOE
# global constants
import random
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
#Instructions
def instructions():
	"""Display Game Instructions """
	print(
	"""
	Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
	This will be a showdown between your human brain and my silicon processor.
	You will make your move known by entering a number, 0 - 8.
	The number
	will correspond to the board position as illustrated:
	0 | 1 | 2
	---------
	3 | 4 | 5
	---------
	6 | 7 | 8
	Prepare yourself, human.
	The ultimate battle is about to begin. \n
	"""
	)

#Challenge
def ask_yes_no(question):
	"""Ask a yes or no question."""
	response = None;
	while response not in ("y","n"):
		response = input(question).lower()

	return response #Python can return more than one value

def who_goes_first(answer):
	response = None;
	while response not in ("you","me"):
		response = input(answer).lower()

	if response=="you":
		human = O;
		com = X;
	else:
		human = X;
		com = O;

	return human,com;

def new_board():
	"""Create a New Board"""
	board = [];
	for square in range(NUM_SQUARES):
		board.append(EMPTY);
	return board;

def display_board():
	"""Display game board on screen."""
	print("\n\t", board[0], "|", board[1], "|", board[2])
	print("\t", "---------")
	print("\t", board[3], "|", board[4], "|", board[5])
	print("\t", "---------")
	print("\t", board[6], "|", board[7], "|", board[8], "\n")

def winner(board):
	"""Determine the game winner."""
	WAYS_TO_WIN = ((0, 1, 2),
	(3, 4, 5),
	(6, 7, 8),
	(0, 3, 6),
	(1, 4, 7),
	(2, 5, 8),
	(0, 4, 8),
	(2, 4, 6))

	for row in WAYS_TO_WIN:
		#print("In LOOp")
		if ((board[row[0]] == board[row[1]]) and (board[row[0]] == board[row[2]]) and (board[row[1]] == board[row[2]]) and (board[row[0]] != EMPTY or board[row[0]] != EMPTY or board[row[0]] != EMPTY)):
			winner = board[row[0]]
			return winner

	if EMPTY not in board:
		#print(board);
		return TIE;

	return None;

def legal_moves(board):
	moves = [];
	for square in range(NUM_SQUARES):
		if board[square] == EMPTY:
			moves.append(square)
	return moves;

def ask_number(question,low,high):
	"""Number in Range of 0 to 8"""
	num = None;
	print(question);
	while num not in range(low,high):
		num = int(input("Position:"));
	return num;

def human_move(board):
	print("Your Turn\n");
	print("Showing Legal Moves for You");
	possible = legal_moves(board);
	print(possible);

	move = None;
	while move not in possible:
		move = ask_number("\nEnter the Number where you want your move\n",0,NUM_SQUARES);
		if move not in possible:
			print("Are You Blind! Not Even Possible\n");
	print("Hmmm...");
	return move;

def com_move(board,com,human):
	print("My Turn\n");
	possible = legal_moves(board);
	move = None;
	BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
	temp_board = board[:];

	for move in possible:
		temp_board[move] = com;
		if winner(temp_board) == com:
			print("And now my FINAL DEAL\n");
			return move;
		temp_board[move] = EMPTY;

	move = None;

	for move in possible:
		temp_board[move] = human;
		if winner(temp_board) == human:
			print("You thought of Winning!");
			return move;
		temp_board[move] = EMPTY;

	move = None;

	for move in BEST_MOVES:
		if move in possible:
			print("I'll go for this",move)
			return move;


#main
print("The Game Instructiions are below");
instructions();
print("You know the Rules now, Lets Battle for Glory");
input("Press Enter Key to continue");

print("Do you have what it takes to defeat me");
answer = ask_yes_no("\nPlease enter 'y' or 'n': ");
if answer == "y":
	print("I'll show you, Moron!")
else:
	print("You already got defeated"); 

input("Enough Talking! Lets Go!!...Press Enter Key to Proceed to Battle");

human,com = who_goes_first("\nWho Goes First? You or Me...Type in 'you' or 'me'\n"); 

print("So you are",human,"and I am",com);

input("Let's go Baby! Press any key to continue");

board = new_board();
display_board();
turn = X;

while winner(board)==None:
		if turn == human:
			pos_human = human_move(board);
			board[pos_human] = human;
			display_board();
			turn = com;
		else:
			pos_com = com_move(board,com,human);
			board[pos_com] = com;
			display_board();
			turn = human;

win = winner(board);

if win == human:
	print("AAAAARRRRRGGGGHHH! You WON sadly!");
elif win == com:
	print("WHOWHOWHOWHO!! Get Lost!");
else:
	print("TIE! Lets do it Again");

print("Well Lets end the Game Now\n");
input("Press Enter Key to Exit");
