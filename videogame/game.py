# Erik Williams
# CPSC 386-02
# 2023-03-23
# epwilliams@csu.fullerton.edu
# @EPW80
#
# Lab 00-00
#
# This is my pygame project!
#

"""Game objects to create PyGame based games."""

import os
import warnings
import pygame

import rgbcolors
from scene import PolygonTitleScene


def main():
    """Run the game."""
    game = MyVideoGame()
    game.run()


def display_info():
    """Print out information about the display driver and video information."""
    print(f'The display is using the "{pygame.display.get_driver()}" driver.')
    print("Video Info:")
    print(pygame.display.Info())


class VideoGame:
    """Base class for creating PyGame games."""

    def __init__(
        self,
        window_width=800,
        window_height=800,
        window_title="My Awesome Game",
    ):
        """Initialize a new game with the given window size and window title"""
        pygame.init()
        self._window_size = (window_width, window_height)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(self._window_size)
        self._title = window_title
        pygame.display.set_caption(self._title)
        self._game_is_over = False
        if not pygame.font:
            warnings.warn("Fonts disabled.", RuntimeWarning)
        if not pygame.mixer:
            warnings.warn("Sound disabled.", RuntimeWarning)
        self._scene_graph = None

    @property
    def scene_graph(self):
        """Return the scene graph representing all the scenes in the game."""
        return self._scene_graph

    def build_scene_graph(self):
        """Build the scene graph for the game."""
        self._scene_graph = [PolygonTitleScene(self._screen, title="Scene")]
        return self._scene_graph

    def run(self):
        """Run the game; the main game loop."""
        self.build_scene_graph()
        scene_iterator = iter(self.scene_graph)
        while not self._game_is_over:
            try:
                current_scene = next(scene_iterator)
            except StopIteration:
                break
            current_scene.start_scene()
            while current_scene.is_valid():
                self._clock.tick(current_scene.frame_rate())
                for event in pygame.event.get():
                    current_scene.process_event(event)
                    if event.type == pygame.QUIT:
                        self._game_is_over = True
                    current_scene.update_scene()
                    current_scene.draw()
                    pygame.display.flip()
        self.quit()

    def quit(self):
        """Quit the game."""
        self._game_is_over = True
        pygame.quit()


class MyVideoGame(VideoGame):
    """Show a colored window with a colored message and a polygon."""

    def __init__(self):
        """Init the Pygame demo."""
        super().__init__(window_title="Scene Demo")
        self._main_dir = os.path.abspath(os.path.dirname(__file__))
        self._data_dir = os.path.join(self._main_dir, "data")
        self.build_scene_graph()
        # print(f"Our main directory is {self._main_dir}")
        # print(f"Our data directory is {self._data_dir}")

    def build_scene_graph(self):
        """Build scene graph for the game demo."""
        self._scene_graph = [
            PolygonTitleScene(
                self._screen,
                title="Welcome to my scene",
                title_color=rgbcolors.light_sky_blue,
                background_color=rgbcolors.hot_pink,
                soundtrack="videogame/data/tune.mp3"
            )
        ]
        return self._scene_graph

    def run(self):
        """Run the game; the main game loop."""
        scene_iterator = iter(self.scene_graph)
        while not self._game_is_over:
            try:
                current_scene = next(scene_iterator)
            except StopIteration:
                break
            current_scene.start_scene()
            while current_scene.is_valid():
                self._clock.tick(current_scene.frame_rate())
                for event in pygame.event.get():
                    current_scene.process_event(event)
                    if event.type == pygame.QUIT:
                        self._game_is_over = True
                    current_scene.update_scene()
                    current_scene.draw()
                    pygame.display.flip()
        self.quit()
