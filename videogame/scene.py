# Erik Williams
# CPSC 386-02
# 2023-03-23
# epwilliams@csu.fullerton.edu
# @EPW80
#
# Lab 00-00
#
# This my pygame project!
#

"""Scene objects for making games with PyGame."""

import pygame
pygame.init()
pygame.font.init()

import rgbcolors


class Scene:
    """Base class for making PyGame Scenes."""

    def __init__(self, screen, background_color, soundtrack=None):
        """Scene initializer"""
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(background_color)
        self._frame_rate = 60
        self._is_valid = True
        self._soundtrack = soundtrack
        self._render_updates = None

    def draw(self):
        """Draw the scene."""
        self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        """Process a game event by the scene."""

        if event.type == pygame.QUIT:
            print("Good Bye!")
            self._is_valid = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("Bye bye!")
            self._is_valid = False

    def is_valid(self):
        """Is the scene valid? A valid scene can be used to play a scene."""
        return self._is_valid

    def render_updates(self):
        """Render all sprite updates."""

    def update_scene(self):
        """Update the scene state."""

    def start_scene(self):
        """Start the scene."""
        if self._soundtrack:
            try:
                pygame.mixer.music.load(self._soundtrack)
                pygame.mixer.music.set_volume(0.2)
            except pygame.error as pygame_error:
                print("Cannot open the mixer?")
                raise SystemExit("broken!!") from pygame_error
            pygame.mixer.music.play(-1)

    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

    def frame_rate(self):
        """Return the frame rate the scene desires."""
        return self._frame_rate


class PressAnyKeyToExitScene(Scene):
    """Empty scene where it will invalidate when a key is pressed."""

    def process_event(self, event):
        """Process game events."""
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            self._is_valid = False


class PolygonTitleScene(PressAnyKeyToExitScene):
    """Scene with a title string and a polygon."""

    def __init__(
        self,
        screen,
        title,
        title_color=rgbcolors.ghostwhite,
        title_size=72,
        background_color=rgbcolors.papaya_whip,
        soundtrack=None,
    ):
        """Initialize the scene."""
        # TODO: Have the super/parent class initialized
        # TODO: Ask pygame for the default font at title_size size. Use the font to render the string title and assign this to an instance variable named self._title in the color title_color.
        # TODO: Ask pygame for the default font at 18 point size. Use the font to render the string 'Press any key.' in the color black. Assign the rendered text to an instance variable named self._press_any_key.
        super().__init__(screen, background_color, soundtrack)
        self._title_font = pygame.font.Font(None, title_size)
        self._title = self._title_font.render(title, True, title_color)
        self._press_any_key_font = pygame.font.Font(None, 32)
        self._press_any_key = self._press_any_key_font.render(
            "Press any key.", True, rgbcolors.black
        )

    def draw(self):
        """Draw the scene."""
        # TODO: Have the super/parent class draw first before
        # drawing yourself.
        # TODO: Draw a 100 pixel by 100 pixel rectangle that has it's center located 100 pixels below the center of the window.
        # TODO: Blit the title text to the center of the window.
        # TODO: Blit the press any key message to the bottom of the window. The text should be centered horizontally and be 50 pixels above the bottom edge of the window.
        super().draw()
        rect = pygame.Rect(0, 0, 100, 100)
        rect.center = (
            self._screen.get_width() // 2,
            self._screen.get_height() // 2 + 100,
        )
        pygame.draw.rect(self._screen, rgbcolors.yellow, rect)
        title_pos = self._title.get_rect(
            center=(self._screen.get_width() // 2, self._screen.get_height() // 2)
        )
        self._screen.blit(self._title, title_pos)
        press_any_key_pos = self._press_any_key.get_rect(
            midbottom=(self._screen.get_width() // 2, self._screen.get_height() - 200)
        )
        self._screen.blit(self._press_any_key, press_any_key_pos)

    def update_scene(self):
        pass
