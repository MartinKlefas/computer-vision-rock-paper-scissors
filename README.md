# Computer Vision RPS

# Milestone 1
Setup the environment, and installed the required packages.

# Milestone 2

Created a simple TensorFlow model using Google Teachable Machine. This has been added to the project, but not yet linked in a meaningful way.
- Unfortunately teachable machine gave poor user feedback, which meant it looked like it had crashed a few times. Running overnight fixed this.
- creating a model via tflite model maker was also considered, but this seems to only run on docker and linux.
    - next step is to try this out by making a docker, or imaging  a local machine to linux

# Milestone 3

Download a simplified test case to check model predictions
Changed model output to be more human readable by interrogating the numpy array that the predictor produces.

# Milestone 4

Made some seriously unmodularised code to play a strict and text-based version of Rock Paper Scissors.
There are 4 functions, to fit the 4 tasks:
-get_computer_choice()
    -Picks at random from a hard-coded list
    -could be one line, but isn't

-get_user_choice()
    -Accepts user inputs and strictly checks against a second copy of hard-coded list
    -performs no sanitisation of inputs, and makes no attempt to correct minor input issues

-get_winner(computer_choice, user_choice)
    -accepts two inputs:
        -computer_choice (String) - representing the computers selected option from Rock, Paper or Scissors
        -user_choice (String) - representing the users selected option from Rock, Paper or Scissors
    -uses multple nested ifs to print out hard coded messages, stores the same messages over and over to satisfy the automated verification tools used.

-play()
    -inexplicably needs to be there just to call the other functions from within a function.