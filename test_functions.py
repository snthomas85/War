"""Tests for my functions.

Made sure that the play_game() function was callable, that the get_player() function's input was working correctly and had the correct type, and that both the player_flag_points and the computer_flag_points functions returned in the correct type (string).
"""

from functions import play_game, get_player, introduce, player_flag_points, computer_flag_points, cadet, general
import mock 
import builtins 

    
def test_play_game():
    assert callable(play_game)

def test_get_player():
    with mock.patch.object(builtins, 'input', lambda _: 'Shelby'):
        player = get_player()
        assert player == 'Shelby'
    assert type(player) == str     
    
def test_player_flag_points():
    assert type(player_flag_points(5)) == str
    assert player_flag_points(3) == '🏳️🏳️🏳️'

def test_computer_flag_points():
    assert type(computer_flag_points(5)) == str
    assert computer_flag_points(4) == '🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️'


    
    
    
    



                 
    