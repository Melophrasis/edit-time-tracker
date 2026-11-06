import os
from datetime import datetime
import time

AUDIO_FOLDER = r"/workspaces/edit-time-tracker/audio_folder"

def data_input():
    while True: 
        for entry in os.scandir(AUDIO_FOLDER):
            if entry.is_file():
                info = entry.stat()
                current = (info.st_mtime, info.st_size)
                if entry.name in seen and seen[entry.name] != current:
                    print(f"EDITED: {entry.name}")
                seen[entry.name] = current
        time.sleep(3)


