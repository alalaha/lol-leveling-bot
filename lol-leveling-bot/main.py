#   @author: Mitchell Levesque                                                          #
#   @desc  : A program for the game League of legends which will automatically queue    #
#            a player for intermediate bots, attack move on the enemy nexus until game  #
#            ends, and then repeat.                                                     #

import listener
import gui

if __name__ == '__main__':
    listener.create_thread()
    print("This program now uses a CLI!")
