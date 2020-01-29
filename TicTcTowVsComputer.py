from tkinter import *
import pickle
import os
import operator

def raiseFrame(frame):
    #receive next page and show it on screen
    
    frame.tkraise()


def scoreBoard():
    #create a score board window, get scores list  from 'scoresLoad()' func and display it.
    
    #lists for names and scores
    scoresLabels=[None] * 11
    namesLabels=[None] * 11
    
    #### GUI ###
    root = Tk()
    root.title("Tic Tac Toe Scoreboard")
    root.resizable(0, 0)
    
    mainPage = Frame(root)
    
    #layout- frames and grid
    playersInfoFrame = Frame(mainPage)
    playersInfoFrame.pack(fill="both", expand=True, padx=20, pady=20)
    
    namesFrame = Frame(playersInfoFrame)
    scoresFrame = Frame(playersInfoFrame)

    mainPage.grid(row=0, column=0,  sticky='news')
    namesFrame.grid(row=1, column=0,  sticky='news')
    scoresFrame.grid(row=1, column=1,  sticky='news')
    
    #close button
    closeButton = Button(mainPage, text="Close", command=root.destroy)
    
    #labels
    titleLabel = Label(playersInfoFrame, text="Tic Tac Toe Scoreboard",font='bold')
    titleLabel.grid(row=0, columnspan=2,  sticky='news', pady=20)
    
    #create name and score labels
    for i in range(0,11) :
        namesLabels[i] = Label(namesFrame, text= " ")
        scoresLabels[i] = Label(scoresFrame, text= " ")

    #show name and score labels
    namesLabels[0].pack()
    scoresLabels[0].pack()
    
    #set 'name' and 'score' headers
    namesLabels[0].configure(text="Name",font='bold')
    scoresLabels[0].configure(text="Score",font='bold')   
    
    #get sorted score board from 'scoresLoad()' func.
    sortedScoreBoard=scoresLoad()
    
    
    if sortedScoreBoard: #if there is a score board
        i=1
        for score in sortedScoreBoard[:10]: #for every score
            namesLabels[i].pack() #show name label
            scoresLabels[i].pack() #show score label
            namesLabels[i].configure(text=score[0]) #set label to current name
            scoresLabels[i].configure(text=score[1]) #set label to current score
            i+=1
        
    #show close button
    closeButton.pack(pady=20)
    
    #display page
    raiseFrame(mainPage)
    root.mainloop()
    
def scoresLoad():
    # load scores list from 'scoresListFile.pkl' file into 'scoresList'
    
    if os.path.isfile('scoresListFile.pkl'): #check if 'scoresListFile.pkl' file is in the folder
        with open("scoresListFile.pkl", "rb") as f:
            scoresList = pickle.load(f) #load scores into 'scoresList'
        sortedScoreBoard = sorted(scoresList.items(), key=operator.itemgetter(1)) #sort 'scoresList' by ascending scores order
        sortedScoreBoard.reverse() # reveres 'sortedScoreBoard' to descending order
        return sortedScoreBoard
      
scoreBoard()