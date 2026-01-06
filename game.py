import arcade
import tutorial as t
import setting as s

import board

import menu

from theme_manager import ManageTheme
from sound_manager import ManageSound

import arcade.gui.widgets
import arcade.gui.widgets
from arcade.experimental.uistyle import UIFlatButtonStyle

SCREEN_WIDTH, SCREEN_HEIGHT = arcade.get_display_size()

CENTER_WIDTH = SCREEN_WIDTH // 2
CENTER_HEIGHT = SCREEN_HEIGHT // 2

# Set the dimensions of the chessboard
ROWS = 8
COLS = 8
SQUARE_WIDTH = 800 // ROWS
SQUARE_HEIGHT = 800 // COLS

# Define Button default style
default_style = {
    "normal": UIFlatButtonStyle(
        font_size=12,
        font_name=("calibri", "arial"),
        font_color=arcade.color.BRUNSWICK_GREEN,
        bg=arcade.color.WHITE,
        border=None,
        border_width=0,
    ),
    "hover": UIFlatButtonStyle(
        font_size=12,
        font_name=("calibri", "arial"),
        font_color=arcade.color.WHITE,
        bg=arcade.color.BRUNSWICK_GREEN,
        border=None,
        border_width=2,
    ),
    "press": UIFlatButtonStyle(
        font_size=12,
        font_name=("calibri", "arial"),
        font_color=arcade.color.WHITE,
        bg=arcade.color.BRUNSWICK_GREEN,
        border=arcade.color.ARMY_GREEN,
        border_width=2,
    ),
    "disabled": UIFlatButtonStyle(
        font_size=12,
        font_name=("calibri", "arial"),
        font_color=arcade.color.WHITE,
        bg=arcade.color.COOL_GREY,
        border=arcade.color.ASH_GREY,
        border_width=2,
    )
}


class GameView(arcade.View):
    def __init__(self, theme):
        super().__init__()

        # Define Managers
        global theme_manager, game_manager, sound_manager

        # Open Managers
        theme_manager = ManageTheme("default")
        sound_manager = ManageSound(1)

        self.manager = arcade.gui.UIManager()
        self.logo = arcade.load_texture("banners/game_banner.png")
        self.settings_png = arcade.load_texture("assets/settings_cog.png")
        self.tutorial_png = arcade.load_texture("assets/Black_question_mark.png")

        player_button = arcade.gui.UIFlatButton(x=CENTER_WIDTH - 125,
                                                y=CENTER_HEIGHT,
                                                width=250,
                                                height=60,
                                                text="Player vs Player",
                                                style=default_style)

        computer_easy_button = arcade.gui.UIFlatButton(x=CENTER_WIDTH - 125,
                                                       y=CENTER_HEIGHT - 70,
                                                       width=250,
                                                       height=60,
                                                       text="Player vs AI (Easy)",
                                                       style=default_style)

        computer_medium_button = arcade.gui.UIFlatButton(x=CENTER_WIDTH - 125,
                                                          y=CENTER_HEIGHT - 140,
                                                          width=250,
                                                          height=60,
                                                          text="Player vs AI (Medium)",
                                                          style=default_style)

        computer_hard_button = arcade.gui.UIFlatButton(x=CENTER_WIDTH - 125,
                                                        y=CENTER_HEIGHT - 210,
                                                        width=250,
                                                        height=60,
                                                        text="Player vs AI (Hard)",
                                                        style=default_style)

        return_button = arcade.gui.UIFlatButton(x=CENTER_WIDTH - 125,
                                                y=CENTER_HEIGHT - 280,
                                                width=250,
                                                height=60,
                                                text="Return to Main Menu",
                                                style=default_style)

        settings_button = arcade.gui.UITextureButton(x=SCREEN_WIDTH - (SQUARE_WIDTH // 2) - 30,
                                                     y=(SCREEN_HEIGHT - SQUARE_HEIGHT // 2) - 60,
                                                     width=60,
                                                     height=60,
                                                     texture=self.settings_png)

        tutorial_button = arcade.gui.UITextureButton(x=(SCREEN_WIDTH - (SQUARE_WIDTH // 2) * 3) - 30,
                                                     y=(SCREEN_HEIGHT - SQUARE_HEIGHT // 2) - 60,
                                                     width=60,
                                                     height=60,
                                                     texture=self.tutorial_png)

        # Theme selection buttons
        default_theme_button = arcade.gui.UIFlatButton(x=CENTER_WIDTH - 270,
                                                       y=CENTER_HEIGHT - 375,
                                                       width=120,
                                                       height=50,
                                                       text="Default",
                                                       style=self.get_theme_button_style(arcade.color.ALMOND))

        pink_theme_button = arcade.gui.UIFlatButton(x=CENTER_WIDTH - 130,
                                                     y=CENTER_HEIGHT - 375,
                                                     width=120,
                                                     height=50,
                                                     text="Pink",
                                                     style=self.get_theme_button_style(arcade.color.CAMEO_PINK))

        ocean_theme_button = arcade.gui.UIFlatButton(x=CENTER_WIDTH + 10,
                                                      y=CENTER_HEIGHT - 375,
                                                      width=120,
                                                      height=50,
                                                      text="Ocean",
                                                      style=self.get_theme_button_style(arcade.color.PALE_ROBIN_EGG_BLUE))

        midnight_theme_button = arcade.gui.UIFlatButton(x=CENTER_WIDTH + 150,
                                                         y=CENTER_HEIGHT - 375,
                                                         width=120,
                                                         height=50,
                                                         text="Midnight",
                                                         style=self.get_theme_button_style(arcade.color.QUEEN_BLUE))

        @player_button.event("on_click")
        def on_click_switch_button(event):
            sound_manager.play_button_sound()
            game_view = board.Board("player")
            self.window.show_view(game_view)

        @computer_easy_button.event("on_click")
        def on_click_switch_button(event):
            sound_manager.play_button_sound()
            game_view = board.Board("computer", difficulty=1)
            self.window.show_view(game_view)

        @computer_medium_button.event("on_click")
        def on_click_switch_button(event):
            sound_manager.play_button_sound()
            game_view = board.Board("computer", difficulty=2)
            self.window.show_view(game_view)

        @computer_hard_button.event("on_click")
        def on_click_switch_button(event):
            sound_manager.play_button_sound()
            game_view = board.Board("computer", difficulty=3)
            self.window.show_view(game_view)

        @return_button.event("on_click")
        def on_click_switch_button(event):
            sound_manager.play_button_sound()
            game_view = menu.MenuView(theme_manager.theme, sound_manager.get_volume())
            self.window.show_view(game_view)

        @settings_button.event("on_click")
        def on_click_switch_button(event):
            sound_manager.play_button_sound()
            settings_menu = s.SettingsMenu(
                "Settings",
                "Volume",
                theme_manager,
                sound_manager
            )
            self.manager.add(
                settings_menu
            )

        @tutorial_button.event("on_click")
        def on_click_switch_button(event):
            sound_manager.play_button_sound()
            tutorial_menu = t.SubMenu(
                "Tutorial Menu"
            )
            self.manager.add(
                tutorial_menu
            )

        @default_theme_button.event("on_click")
        def on_click_switch_button(event):
            sound_manager.play_button_sound()
            theme_manager.set_theme("default")

        @pink_theme_button.event("on_click")
        def on_click_switch_button(event):
            sound_manager.play_button_sound()
            theme_manager.set_theme("pink")

        @ocean_theme_button.event("on_click")
        def on_click_switch_button(event):
            sound_manager.play_button_sound()
            theme_manager.set_theme("ocean")

        @midnight_theme_button.event("on_click")
        def on_click_switch_button(event):
            sound_manager.play_button_sound()
            theme_manager.set_theme("midnight")

        self.manager.add(tutorial_button)
        self.manager.add(settings_button)

        self.manager.add(player_button)
        self.manager.add(computer_easy_button)
        self.manager.add(computer_medium_button)
        self.manager.add(computer_hard_button)

        self.manager.add(default_theme_button)
        self.manager.add(pink_theme_button)
        self.manager.add(ocean_theme_button)
        self.manager.add(midnight_theme_button)

        self.manager.add(return_button)

        # Create theme manager object and set theme
        theme_manager = ManageTheme(theme)

    def get_theme_button_style(self, color):
        """Return styled button properties for theme buttons."""
        return {
            "normal": UIFlatButtonStyle(
                font_size=12,
                font_name=("calibri", "arial"),
                font_color=arcade.color.BLACK,
                bg=color,
                border=None,
                border_width=0,
            ),
            "hover": UIFlatButtonStyle(
                font_size=12,
                font_name=("calibri", "arial"),
                font_color=arcade.color.WHITE,
                bg=color,
                border=arcade.color.WHITE,
                border_width=2,
            ),
            "press": UIFlatButtonStyle(
                font_size=12,
                font_name=("calibri", "arial"),
                font_color=arcade.color.WHITE,
                bg=color,
                border=arcade.color.BLACK,
                border_width=2,
            ),
            "disabled": UIFlatButtonStyle(
                font_size=12,
                font_name=("calibri", "arial"),
                font_color=arcade.color.WHITE,
                bg=arcade.color.COOL_GREY,
                border=arcade.color.ASH_GREY,
                border_width=2,
            )
        }

    def on_show_view(self):
        """ This is run once when we switch to this view """
        # Enable the UIManager when the view is showm.
        self.manager.enable()

    def on_draw(self):
        self.clear()
        arcade.start_render()

        # Make even squares

        r = SCREEN_HEIGHT // SQUARE_WIDTH
        c = SCREEN_WIDTH // SQUARE_HEIGHT

        theme = theme_manager.theme
        bg_color, black_capture_bg, white_capture_bg = theme_manager.get_background(theme)
        light_square_color, dark_square_color = theme_manager.get_theme(theme)

        for row in range(r + 1):
            for col in range(c + 1):
                x = col * SQUARE_WIDTH
                y = row * SQUARE_HEIGHT

                if (row + col) % 2 == 0:
                    color = light_square_color
                else:
                    color = dark_square_color

                arcade.draw_rectangle_filled(x + SQUARE_WIDTH // 2, y + SQUARE_HEIGHT // 2, SQUARE_WIDTH, SQUARE_HEIGHT,
                                             color)

        arcade.draw_rectangle_outline(center_x= CENTER_WIDTH,
                                      center_y=CENTER_HEIGHT - 110,
                                      width=295,
                                      height=380,
                                      color=arcade.color.WHITE,
                                      border_width=4)

        arcade.draw_rectangle_outline(center_x=CENTER_WIDTH,
                                      center_y=CENTER_HEIGHT - 110,
                                      width=275,
                                      height=360,
                                      color=bg_color,
                                      border_width=3)

        arcade.draw_rectangle_filled(center_x=CENTER_WIDTH,
                                     center_y=CENTER_HEIGHT - 110,
                                     width=270,
                                     height=355,
                                     color=black_capture_bg)

        # Draw theme selection label
        arcade.draw_text("Board Theme:",
                         CENTER_WIDTH,
                         CENTER_HEIGHT + 180,
                         arcade.color.WHITE,
                         font_size=18,
                         anchor_x="center",
                         font_name="Kenney Blocks",
                         bold=True)

        self.logo.draw_sized(center_x=CENTER_WIDTH, center_y=CENTER_HEIGHT + 100, width=700, height=580)
        self.manager.draw()

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()