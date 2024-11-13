# AlphaWar

**AlphaWar** is an EEG-based game where two players use their brain's alpha waves to engage in a virtual tug-of-war. Harness the power of hyper-scanning technology and battle your opponent by focusing your mind and increasing your alpha wave activity!

## How It Works

1. Two OpenBCI boards are connected to the computer using a custom class built off the BrainFlow library.
2. Players wear EEG headsets, and the game measures their **alpha wave** activity (8-12 Hz) during each epoch.
3. The player with higher alpha power pulls the virtual rope *towards* their side.
4. The game ends when the rope reaches one player’s side, determining the winner.

## Running The Game
1. **Open `AlphaWar.py` in VSCode:**
   - Any config adjustments will be at the top of script, immediately after imports
2. **Adjust Configuration:**
   - Adjust player names - this can be any string 
   - Adjust the board ID: 
     - `BoardIds.SYNTHETIC_BOARD.value` is used for testing - this uses *Simulated data*
     - `BoardIds.CYTON_BOARD.value` should be used if using the OpenBCI Cyton Boards
   -  (Optional) Adjust serial port:
      -  This sets each board to be a specific player, leave them as *None* to automatically detect and connect.
3. **Select Environment & Start the Game:**
   - Press `ctrl + shift + p`, then enter/select "Python: Select Interpreter" -> find and select "Python"
   - When you have `AlphaWar.py` open, click the small 'play' arrow in the top right to start the game.

## Game Controls
- **Space Bar**: Replay the game after a match.
- **Escape**: Quit the game.

## Notes

- Focus on calming your mind to increase alpha waves—practice mindfulness for a competitive edge!

## Installation

1. **Clone the repository:**
   `
   git clone https://github.com/YourRepo/AlphaWar.git
   cd AlphaWar
   `

2. **Setup the game:**
   - Ensure you have Python and the required libraries installed. Install dependencies using:
     `
     pip install -r requirements.txt
     `


## Credits

This is a fork of the [original repository](https://github.com/KyaMas/AlphaWar)

This game was developed during a hackathon by:

- [Kya Masoumi-Ravandi](https://github.com/KyaMas)
- Can Sozuer
- Shihui Gao
- Noof Al Shehhi
- Danella Calina

For more information on their project check out `Hackathon Presentation.pptx`
