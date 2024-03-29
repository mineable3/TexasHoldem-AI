

class Constants:


#AI=======================================================

  #the absolute value percent a weight can mutate by
  FACTOR_OF_MUTATION = .005

  #the number of decimals a weight should have
  PRECISION_OF_WEIGHTS = 5

  #a number to make the outputs either bigger or smaller like scientific notation
  #DON'T CHANGE THIS NUMBER
  #THE AI HAS BEEN TRAINING WITH IT AND WILL HAVE TO RETRAIN IF IT CHANGES
  OUTPUT_SCALE_FACTOR = .001

  #the number of decimals in the ai's output
  OUTPUT_PRECISION = 0

  #DON'T CHANGE THIS BOOLEAN
  #THIS WOULD ERASE ALL OF THE TRAINING THE AI HAS DONE SO FAR
  RANDOMIZE_WEIGHTS = False

  #time in minutes
  TIME_TO_TRAIN = .3
  IS_TRAINING = True

#game======================================================
  STARTING_CASH = 500
  ANTE = 10
  BIG_BLIND_AMOUNT = 30

  #how many rounds have to pass before everyone's money gets reset to STARTING_CASH
  ROUNDS_UNTIL_DEFLATION = 1001

  #how many rounds have to pass before it records the stats for a round
  RECORDING_ROUND = 1

  PRINT_ENABLED = False

  BUFFERING_SCREEN_FPS = 0.1
