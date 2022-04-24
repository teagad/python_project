from main_logic import Game_logic


def start_game():
    game = Game_logic()
    game.choosing_tamagochi()
    game.event_loop_of_choosing_tamagochi()
    game.draw_background()
    # placing tamagochi picture
    game.place_tamagochi_picture()
    # making text box
    game.making_textbox()
    # render at position stated in arguments
    game.render_textboxes()
    # starting event
    # events
    game.main_event_loop()


start_game()
