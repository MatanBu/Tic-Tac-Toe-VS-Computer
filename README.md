# Tic-Tac-Toe-VS-Computer
Tic Tac Toe game for one player vs computer, which should be competitive, with a simple GUI for a better game experience.

* The software was written in a single file (with multiple functions) in order to fit the exercise requirements.

Solution plan:
=
	i. General idea:
  
		Create GUI for displaying the game board, represent every square as a button and each player in his turn press on available button.
		Create a function to check if there is a winner after every move, or tie when game ends.
		Implement algorithm for competitive computer-side (acoording to the given wikipedia algorithm).
		
	ii. Solution components:
  
		playersArr: list of two lists contains players details and moves.
			
		currentPlayer: the player which plays in this turn.
		
		stepsCounter: count how many moves done.
		
		FUNC raiseFrame(frame): receive next page and show it on screen.	
			
		FUNC mainScreen(): set the first screen of the game (players name).
			player1Name, player2Name: players name from input.	
		
		FUNC startButtonFunc(): called when start button clicked. check and save players name.
			player1Info, player1Info: players name in uppercase to check if input accepted (only letters).	
		
		FUNC gameScreen(): set the game screen, including game board and randomize starting player.
		
		FUNC boardButtonClick(num): receive clicked button number, make player move, draw it on board and call function to check win/tie.
			winnerPlayer: receive from checkWinner() func. if there is winner or tie.
		
		FUNC boardUpdate(num,sign): receive button number and player sign X/O to update the board.
		
		FUNC computerMove(): manage computer move- if first turn: randomize square, else: call computerAlgorithm() func.
			select: contain the computer selected square.
			
		FUNC computerAlgorithm(): 12 steps algorithm (from wikipedia) to determine computer best move.
			toSelect: contain the computer selected square.
			myMoves, opponentMoves: lists contains user moves and computer moves.
			allMoves: list contain all moves.
			winCombination: tuples caontains winning combination for check if there is a winner.
			match: contain intersection of tup1 and tup2.
			matchList: previous match converted to list.
			firstRow, secRow: two rows cross each other and matchList is the common square.
			combinations: list of lists of corner square with two empty rows.
			flag: to check if all squares empty.
			corners: list of corner squares.
			
		FUNC checkResult(): call checkWinner() func. and if needed handle winning/tie messages and program exit.
			winnerPlayer: variable to store winner player index or special index for tie.
			
		FUNC checkWinner(): check if there is a winner or a tie.
			winner: variable to store winner player index or special index for tie.
			winCombination: tuples caontains winning combination for check if there is a winner.
			disabledCounter: count the number of disabled squares to check if it's  A tie.
							
Running instructions:
=
	Inside code file folder open Command line (cmd) and write: 'python ex3.py' and press ENTER.
	
	NOTICE: On each game end, the scores saved into 'scoresListFile.pkl' file.
	In order to load this file into score board (ex4) this file must be in the same folder with 'ex4.py',
	So it better to locate 'ex2.py', 'ex3.py', 'ex4.py' and 'scoresListFile.pkl' in the same folder.
