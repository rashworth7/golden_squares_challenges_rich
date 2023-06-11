from lib.track_list import Music
import pytest

def test_create_class_instance():
    music = Music()
    assert music.track_list == []

def test_display_empty_list():
    music = Music()
    assert music.display_tracks() == "There are currently no tracks on the list"

def test_add_single_track_to_list():
    music = Music()
    music.add_track("Yellow") 
    assert music.track_list == ["Yellow"]

def test_add_two_tracks():
    music = Music()
    music.add_track("Yellow")
    music.add_track("Paradise")
    assert music.track_list == ["Yellow", "Paradise"]

def test_display_tracks_when_songs_on_list():
    music = Music()
    music.add_track("Yellow")
    music.add_track("Paradise")
    assert music.display_tracks() == ["Yellow", "Paradise"]

def test_add_track_already_on_list():
    music = Music()
    music.add_track("Yellow")

    with pytest.raises(Exception) as err:
        music.add_track("Yellow")
    
    assert str(err.value) == "Track is already on the list"

def test_remove_track_from_list():
    music = Music()
    music.add_track("Yellow")
    music.remove_track("Yellow")
    assert music.track_list == []

def test_remove_track_from_list_not_on_list():
    music = Music()

    with pytest.raises(Exception) as err:
        music.remove_track("Yellow")
    
    assert str(err.value) == "That track is not on the list"