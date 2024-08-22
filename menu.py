from ursina import *

class MainMenu(Ursina):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show_menu()

    def show_menu(self):
        self.start_button = Button(text='Start Game', scale=(0.3, 0.1), position=(0, 0.2))
        self.instructions_button = Button(text='Instructions', scale=(0.3, 0.1), position=(0, 0))
        self.exit_button = Button(text='Exit', scale=(0.3, 0.1), position=(0, -0.2))

        self.start_button.on_click = self.start_game
        self.instructions_button.on_click = self.show_instructions
        self.exit_button.on_click = self.exit_game

    def start_game(self):
        self.clear()
        from game import Game
        game = Game()

    def show_instructions(self):
        self.start_button.disable()
        self.instructions_button.disable()
        self.exit_button.disable()

        instructions_panel = Entity(parent=camera.ui, model='quad', scale=(0.8, 0.6), color=color.black66, z=-1)
        instructions_text = Text("Use arrow keys or WASD to move.\n\nCollect the loot and reach the exit.",
                                 parent=instructions_panel, origin=(0, 0), scale=1.5, color=color.white)
        
        back_button = Button(text='Back', parent=instructions_panel, scale=(0.2, 0.1), position=(0, -0.3))
        back_button.on_click = self.go_back

    def go_back(self):
        destroy(Entity)
        self.show_menu()

    def exit_game(self):
        application.quit()
