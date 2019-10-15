import getpass
import os
"""
satisync.py - Probably not a good idea

But we're doing it anyway.
"""

SAVEGAME_DIR_PREUSER = "Games/epic-games-store/drive_c/users"
SAVEGAME_DIR_POSTUSER = "Local Settings/Application Data/FactoryGame/Saved/SaveGames"

class Satisync:
    """
    I'll find a good excuse for this later.
    """

    def __init__(self):
        self.savedir = os.path.join(
            os.getenv("HOME"),
            SAVEGAME_DIR_PREUSER,
            getpass.getuser(),
            SAVEGAME_DIR_POSTUSER
        )

def do_the_thing():
    """
    Cow goes moo.
    """
    sync = Satisync()

if "__name__" == "__main__":
    do_the_thing()