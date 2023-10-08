

class Constants:


#AI=======================================================

  #the absolute value percent a weight can mutate by
  FACTOR_OF_MUTATION = .015

  #the number of decimals a weight should have
  PRECISION_OF_WEIGHTS = 3

  #a number to make the outputs either bigger or smaller like scientific notation
  OUTPUT_SCALE_FACTOR = .001

  #the number of decimals in the ai's output
  OUTPUT_PRECISION = 0

  RANDOMIZE_WEIGHTS = False

  #time in minutes
  TIME_TO_TRAIN = .1

#game======================================================
  STARTING_CASH = 500
  ANTE = 10
  BIG_BLIND_AMOUNT = 30

  #how many rounds have to pass before everyone's money gets reset to STARTING_CASH
  ROUNDS_UNTIL_DEFLATION = 100

  #how many rounds have to pass before it records the stats for a round
  RECORDING_ROUND = 10

  PRINT_ENABLED = False
