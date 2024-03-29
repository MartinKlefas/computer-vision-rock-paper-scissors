
# Computer Vision Rock Paper scissors
This project is part of the AICore Python fundamentals course is intended to teach the basics of computer vision and automated classification models. It's an early stage project, and so the classification success rate of the model isn't rigorously assessed. The model training steps are done using an external black-box tool, but this is entirely adequate for a simple classification scenario, and similar to what might be used in an embedded machine or similar. 

# Part 1

Create a simple TensorFlow model using Google Teachable Machine. This has been added to the project, but not yet linked in a meaningful way.
- Unfortunately teachable machine gave poor user feedback, which meant it looked like it had crashed a few times. Running overnight fixed this.
- creating a model via tflite model maker was also implemented, the code for doing so is collated [in this repository](https://github.com/MartinKlefas/tensorflow_trainer)

# Part 2

Interpret and test the output of the TFLite model, so that it can be passed to the game code in a human readable format, and so more easily debugged. Create the game itself, first accepting input from the command line, to test functionality independently of the CV model.

Code a terminal based RPS game - implemented in [manual_rps.py](manual_rps.py). There are 4 functions, to fit the 4 tasks:
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
Marry together the "Game" code and the "Vision" code such that the game can be played as intended showing signs to the computer webcam. This was implemented in [camera_rps.py](camera_rps.py) This concluded the AICore tutorial Scenario.
The below shows a player giving the paper sign to the camera in advance of their turn.
![In game shot showing player giving "Paper" sign](Screenshot.png?raw=true "Screenshot of a player showing Paper to the game")

# Part 4
Take into account ties, and make the game a "best of 5 rounds" - implementing better feedback on win/lose conditions to make the game more easily played. Feed back to the player what their gestures have been interpretted as, and introduce things like round timers so that the gameplay is more paced and controlled.

# Todo:
- retrain neural net to be more robust
    - Firstly understand current model performance
    - Implement Train and Validation datasets, and measure the training progress with something like TensorBoard
- refactor game itself into object oriented approach, for future ease of expansion
- GUI?
