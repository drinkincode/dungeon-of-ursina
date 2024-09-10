from ursina import *
from DoU.actors.actor import Actor
class PauseMenu(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            texture='white_cube',
            scale=(0.5, 0.3),
            color=color.gray,
            origin=(-0.5, 0.5),
            position=(-0.25, 0.15),
            enabled=False
        )

        self.resume_button = Button(
            parent=self,
            model='quad',
            texture='white_cube',
            origin=(-0.5, 0.5),
            scale=(0.4, 0.1),
            color=color.dark_gray,
            text='Resume',
            text_origin=(0, 0),
            text_color=color.white,
            on_click=self.resume_game
        )

        self.quit_button = Button(
            parent=self,
            model='quad',
            origin=(-2.0, 0.5),
            texture='white_cube',
            scale=(0.4, 0.1),
            color=color.dark_gray,
            text='Quit',
            text_origin=(0, 0),
            text_color=color.white,
            on_click=self.quit_game
        )

    def resume_game(self):
        self.enabled = False
        self.toggle_pause()
        # Add code to resume the game here

    def quit_game(self):
        application.quit()

    def toggle_pause(self):
        if self.enabled:
            for entity in scene.entities:
                if issubclass(type(entity), Actor):
                    entity.update = None  # Disable update function
        else:
            for entity in scene.entities:
                if issubclass(type(entity), Actor):
                    entity.update = entity.original_update  # Restore update function
