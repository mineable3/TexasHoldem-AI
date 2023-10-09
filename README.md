# What is this repository?
Texas Hold'em is a popular form of poker played with two pocket cards and five community cards.
The point of the game is to make as much money as possible by betting you have the best hand made from your pocket and community cards.
This is my attempt to enter the world of machine learning and build an AI to play Texas Hold'em.
Along with building an AI I'm also using this project to learn python, learn about neural networks, and hopefully win my school district's STEM fair.


# How to Use
I've tried my best to make everything a person would want to change inside of the Constants.py file.
The most important thing is the TIME_TO_TRAIN constant that changes the time the AI trains for.

### Training
* Adjust TIME_TO_TRAIN in Constants.py to the amount you want
* In the command line run `python Main.py` to start the training
* If the screen clears and nothing else happens, the AI is training.
* To double check everything is running, under TableStats find the player stats file and open it. If you see data being appended to the file that means hands are currently being played.
* When the training ends you will need t o copy and paste the contents of WeightsDump.txt into the constructor (*where the list of numbers is*).

