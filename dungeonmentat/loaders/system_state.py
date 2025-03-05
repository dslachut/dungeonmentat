import sqlite3

import platformdirs

def create_system_state(CONN: sqlite3.Connection):
    """Create a SQLite3 file in which to store system state information.

    Args:
        CONN (sqlite3.Connection): The SQLite database used for configuration info.
    """
    return


def load_system_state():
    """Loads system state information from disk.

    Config info is stored in a SQLite database in a platform-dependent user config location. If the db, or any value
    that should be there, doesn't exist, it will be created with a default value or a value from a CLI flag.
    """
    data_path = platformdirs.user_data_path('dungeonmentat', roaming=True, ensure_exists=True)
    with sqlite3.Connection(data_path/"conf.db") as CONN:
        create_system_state(CONN)
