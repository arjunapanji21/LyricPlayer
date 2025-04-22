#!/usr/bin/env python3
import sys
import time
from typing import List, Tuple
import os
import pygame


def play_mp3(file_path: str) -> None:
    """
    Initialize and play an MP3 file.
    
    Args:
        file_path: Path to the MP3 file
    """
    if not os.path.exists(file_path):
        print(f"Error: MP3 file not found at {file_path}")
        return False
    
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        return True
    except Exception as e:
        print(f"Error playing MP3: {e}")
        return False


def display_typed_lyrics(
    lyrics: List[Tuple[str, float]],
    line_delays: List[float],
    title: str = "",
    signature: str = "",
    mp3_file: str = None,
    start_delay: float = 0.0
) -> None:
    """
    Display lyrics with a typing animation effect and optional MP3 playback.
    
    Args:
        lyrics: List of (line, char_delay) tuples
        line_delays: Delay after each line in seconds
        title: Optional title to display before lyrics
        signature: Optional signature to display after lyrics
        mp3_file: Optional path to MP3 file to play
        start_delay: Delay before starting lyrics display (seconds)
    """
    # Play the MP3 file if provided
    music_playing = False
    if mp3_file:
        music_playing = play_mp3(mp3_file)
    
    # Wait for the start delay
    if start_delay > 0:
        time.sleep(start_delay)
    
    if title:
        print(f"\n{title}")
    
    for i, (line, char_delay) in enumerate(lyrics):
        print(end="🎵 ", flush=True)
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_delay)
        
        # Add delay after each line
        time.sleep(line_delays[min(i, len(line_delays) - 1)])
        print()
    
    if signature:
        print(signature)
    
    # If music is playing, wait for user to stop it
    if music_playing:
        print("\nPress Ctrl+C to stop the music and exit...")
        try:
            # Keep program running while music plays
            while pygame.mixer.music.get_busy():
                time.sleep(1)
        except KeyboardInterrupt:
            # Clean exit when user presses Ctrl+C
            pygame.mixer.music.stop()
            pygame.mixer.quit()


def main() -> None:
    # Song configuration
    lyrics = [
        ("I've always been true...", 0.075), # line 1
        ("I've waited so long...", 0.075), # line 2
        ("Just to come hold you...", 0.075), # line 3
        ("I'm making it through...", 0.075), # line 4
        ("It's been far too long...", 0.075), # line 5
        ("We've proven our love...", 0.075), # line 6
        ("Over time's so strong...", 0.075), # line 7
        ("In all that we do...", 0.075), # line 8
        ("The stars in the night...", 0.075), # line 9
        ("They lend me their light...", 0.075), # line 10
        ("To bring me closer...", 0.075), # line 11
        ("To heaven with you...", 0.075), # line 12
        ("Tiktok: arjunaaprakarsa", 0.075), # line 12
    ]
    
    line_delays = [
        1.0, # line 1
        1.0, # line 2
        1.5, # line 3
        1.5, # line 4
        1.0, # line 5
        0.5, # line 6
        1.5, # line 7
        1.0, # line 8
        1.0, # line 9
        0.5, # line 10
        1.0, # line 11
        1.0, # line 12
    ]
    
    title = "## Gunslinger by Avenged Sevenfold ##"
    signature = ""
    
    # Path to your MP3 file - change this to your actual file path
    mp3_file = "gunslinger.mp3"
    
    # Delay before starting to display lyrics (adjust to sync with music)
    start_delay = 0
    
    # display_typed_lyrics(lyrics, line_delays, title, signature, mp3_file, start_delay)
    display_typed_lyrics(lyrics, line_delays, title)


if __name__ == "__main__":
    main()