"""
WinLoseMenu class for creating a window to display win/lose/draw results and options.
This class provides functionalities to display a win/lose/draw banner and buttons for
replay, main menu, and quitting.
"""

import arcade.gui
import arcade.gui.widgets
import arcade
import time

class WinLoseMenu(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):
    """Acts like a fake view/window."""

    def __init__(self, theme_manager, winner, game_manager, game_stats=None):
        """
        Initialize the WinLoseMenu window.
        Parameters:
        - theme_manager: An instance of ManageTheme class for managing themes.
        - winner (str): The winner of the game ('black', 'white', or 'draw').
        - game_manager: An instance of ManageGame class for managing game states.
        - game_stats (dict): Dictionary containing game statistics (optional).
        """
        super().__init__(size_hint=(1, 1))

        theme = theme_manager.theme
        self.light_square_color, self.dark_square_color = theme_manager.get_theme(theme)
        self.result = ""
        self.back_clicked = False
        self.game_stats = game_stats if game_stats else {}

        # Store screen dimensions for drawing outline
        self.screen_width, self.screen_height = arcade.get_display_size()

        # Setup frame which will act like the window.
        frame = self.add(arcade.gui.UIAnchorLayout(width=600, height=500, size_hint=None))
        frame.with_padding(all=20)

        # Set winner text
        if winner == "black":
            winner_text = "BLACK WINS!"
        elif winner == "white":
            winner_text = "WHITE WINS!"
        else:
            winner_text = "DRAW!"

        # Get theme colors
        bg_color, _, _ = theme_manager.get_background(theme)

        # Set background based on theme
        frame.with_background(color=bg_color)

        # Create winner title label
        winner_label = arcade.gui.UITextArea(
            text=winner_text,
            width=520,
            height=60,
            font_size=32,
            font_name="Kenney Blocks",
            text_color=self.light_square_color
        )

        # Create statistics text if available
        stats_text = ""
        if self.game_stats:
            stats_text = (
                f"Total Moves: {self.game_stats.get('total_moves', 0)}\n"
                f"Game Duration: {self.game_stats.get('game_duration', 'N/A')}\n"
                f"White Captures: {self.game_stats.get('white_captures', 0)}\n"
                f"Black Captures: {self.game_stats.get('black_captures', 0)}\n"
                f"White Time: {self.game_stats.get('white_time_remaining', 'N/A')}\n"
            )

        # Create statistics label
        stats_label = arcade.gui.UITextArea(
            text=stats_text,
            width=520,
            height=150,
            font_size=14,
            font_name="Kenney Blocks",
            text_color=self.light_square_color
        )

        # The type of event listener we used earlier for the button will not work here.
        replay_button = arcade.gui.UIFlatButton(text="Replay",
                                                width=520)

        # Button layout for centered buttons
        button_layout = arcade.gui.UIBoxLayout(vertical=False, space_between=10)

        menu_button = arcade.gui.UIFlatButton(text="Main Menu",
                                              width=255)

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=255)

        button_layout.add(menu_button)
        button_layout.add(quit_button)

        # Main vertical layout
        widget_layout = arcade.gui.UIBoxLayout(align="center", space_between=15, vertical=True)

        # Add winner title
        widget_layout.add(winner_label)
        widget_layout.add(stats_label)
        widget_layout.add(replay_button)
        widget_layout.add(button_layout)

        frame.add(child=widget_layout, anchor_x="center", anchor_y="center")

        @replay_button.event("on_click")
        def on_click_switch_button(event):
            """
            Event handler for the Replay button.
            Parameters:
            - event: The event object.
            """
            game_manager.set_game_type("Replay")
            self.parent.remove(self)

        @menu_button.event("on_click")
        def on_click_switch_button(event):
            """
            Event handler for the Main Menu button.
            Parameters:
            - event: The event object.
            """
            game_manager.set_game_type("Main_Menu")
            self.parent.remove(self)

        @quit_button.event("on_click")
        def on_click_switch_button(event):
            """
            Event handler for the Quit button.
            Parameters:
            - event: The event object.
            """
            time.sleep(.15)
            arcade.exit()

    def do_render(self, surface):
        """Override to draw double outline around the menu."""
        # Draw the UI elements first
        super().do_render(surface)

        # Calculate menu position (centered on screen)
        menu_width = 600
        menu_height = 500
        center_x = self.screen_width // 2
        center_y = self.screen_height // 2

        # Draw outer outline (thicker, offset)
        arcade.draw_rectangle_outline(
            center_x=center_x,
            center_y=center_y,
            width=menu_width + 20,
            height=menu_height + 20,
            color=self.light_square_color,
            border_width=3
        )

        # Draw inner outline
        arcade.draw_rectangle_outline(
            center_x=center_x,
            center_y=center_y,
            width=menu_width + 10,
            height=menu_height + 10,
            color=self.light_square_color,
            border_width=2
        )