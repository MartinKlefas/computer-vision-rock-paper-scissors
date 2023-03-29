
# Computer Vision Rock Paper Sciccors
This project is part of the AICore Python fundamentals course is intended to teach the basics of computer vision and automated classification models. It's an early stage project, and so the classification success rate of the model isn't rigorously assessed. The model training steps are done using an external black-box tool, but this is entirely adequate for a simple classification scenario, and similar to what might be used in an embedded machine or similar. 

# Part 1

Create a simple TensorFlow model using Google Teachable Machine. This has been added to the project, but not yet linked in a meaningful way.
- Unfortunately teachable machine gave poor user feedback, which meant it looked like it had crashed a few times. Running overnight fixed this.
- creating a model via tflite model maker was also implemented, the code for doing so is collated [in this repository](https://github.com/MartinKlefas/tensorflow_trainer)

# Part 2

Interpret and test the output of the TFLite model, so that it can be passed to the game code in a human readable format, and so more easily debugged. Create the game itself, first accepting input from the command line, to test functionality independently of the CV model.

There are 4 functions, to fit the 4 tasks:
- get_computer_choice()
    - Picks at random from a hard-coded list
    - could be one line, but isn't

- get_user_choice()
    - Accepts user inputs and strictly checks against a second copy of hard-coded list
    - performs no sanitisation of inputs, and makes no attempt to correct minor input issues
 
- get_winner(computer_choice, user_choice)
    - accepts two inputs:
        - computer_choice (String) - representing the computers selected option from Rock, Paper or Scissors
        - user_choice (String) - representing the users selected option from Rock, Paper or Scissors
    - uses multple nested ifs to print out hard coded messages, as this task was automatically graded

- play()
    - overseer function to control game-flow.

It's worth noting that some of the code is structured oddly in order to pass the automated verification that's applied to it.

# Part 3
Marry together the "Game" code and the "Vision" code such that the game can be played as intended showing signs to the computer webcam. This concluded the AICore tutorial Scenario.

![In game shot showing player giving "Paper" sign](Screenshot.png?raw=true "Screenshot of a player showing Paper to the game")


# Todo:
- refactor into object oriented approach
- retrain neural net to be more robust
- GUI?
