import sys
from typing import Any
import playsound


def play_sound(audio_file_path: str):
    """Play a sound from audio path"""
    playsound.playsound(audio_file_path)


def log(message: Any):
    """Print a message without newline"""
    sys.stdout.write(str(message))
    sys.stdout.flush()
