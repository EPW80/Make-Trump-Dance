"""Scene objects for making games with PyGame."""

import pygame
import rgbcolors

pygame.init()
pygame.font.init()

from gif_converter import frames


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
            print("America first!")
            self._is_valid = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("America first!")
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

        super().__init__(screen, background_color, soundtrack)
        self._title_font = pygame.font.Font(None, title_size)
        self._title = self._title_font.render(title, True, title_color)
        self._press_any_key_font = pygame.font.Font(None, 22)
        self._press_any_key = self._press_any_key_font.render(
            "Move your mouse", True, rgbcolors.white
        )

        new_width = 100
        new_height = 100

        self.rect = pygame.Rect(0, 0, new_width, new_height)
        self.rect.center = (
            self._screen.get_width() // 2,
            self._screen.get_height() // 2,
        )

        self._frames = [
            pygame.image.load(f"frames/frame_{i}.png") for i in range(len(frames))
        ]
        self._current_frame = 0

    def draw(self):
        """Draw the scene."""
        super().draw()
        frame = self._frames[self._current_frame]

        gif_position = (
            (self._screen.get_width() - frame.get_width()) // 2,
            (self._screen.get_height() - frame.get_height()) // 2,
        )

        self._screen.blit(frame, gif_position)

        title_pos = self._title.get_rect(
            midbottom=(
                self._screen.get_width() // 2,
                self._screen.get_height() // 2 - 350,
            )
        )
        self._screen.blit(self._title, title_pos)
        press_any_key_pos = self._press_any_key.get_rect(
            midtop=(
                self._screen.get_width() // 2,
                self._screen.get_height() // 2 + 200,
            )
        )
        self._screen.blit(self._press_any_key, press_any_key_pos)

    def update_scene(self):
        self._current_frame = (self._current_frame + 1) % len(self._frames)
