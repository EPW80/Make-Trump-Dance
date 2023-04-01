# Make Trump Dance

Make Trump Dance is a simple and entertaining game developed using the Pygame library. The game showcases a main menu with a title and a dancing Trump GIF at the center of the screen. Background music plays during the main menu scene, adding a fun atmosphere to the game.

## Prerequisites

Before running the game, ensure that you have Python 3.8 or higher installed on your system. Additionally, you'll need to install the Pygame and Pillow libraries using the following commands:

```
It's recommended to create and activate a virtual environment before installing the libraries:
pip install pygame
pip install pillow


python3 -m venv env
source env/bin/activate
Running the Game
To run the game, navigate to the videogame folder and run the game.py script:

cd videogame
python game.py
Upon launching the game, you'll see the main menu scene with the title and the dancing Trump GIF. Press any key to exit the game.
```

## Project Structure

The project is organized into the following files and folders:

game.py: The main script to run the game. This file initializes the Pygame library, sets up the game window, and manages the game loop.
scene.py: This file contains the Scene classes used to create and manage different scenes in the game.
rgbcolors.py: A file containing RGB color definitions to be used throughout the project.
videogame/data: A folder containing the background music file for the main menu scene.
videogame/frames: A folder containing the frames of the dancing Trump GIF.

## Demo

![](./videogame/data/demo.gif)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Pygame: The library used to create the game.
CPSC 386-02: The course for which this project was developed.
Pillow: The library used for image manipulation.
