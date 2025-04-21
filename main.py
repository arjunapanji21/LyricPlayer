#!/usr/bin/env python3
import sys
import time
from typing import List, Tuple


def display_typed_lyrics(
    lyrics: List[Tuple[str, float]],
    line_delays: List[float],
    title: str = "",
    signature: str = ""
) -> None:
    """
    Display lyrics with a typing animation effect.
    
    Args:
        lyrics: List of (line, char_delay) tuples
        line_delays: Delay after each line in seconds
        title: Optional title to display before lyrics
        signature: Optional signature to display after lyrics
    """
    if title:
        print(f"\n{title}")
    
    for i, (line, char_delay) in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_delay)
        
        # Add delay after each line
        time.sleep(line_delays[min(i, len(line_delays) - 1)])
        print()
    
    if signature:
        print(signature)


def main() -> None:
    # Song configuration
    lyrics = [
        ("> 'Cause with all these things we do", 0.06),
        ("> It don't matter when I'm coming home to you", 0.05),
        ("> I reach towards the sky", 0.06),
        ("> I've said my goodbyes", 0.06),
        ("> My heart's always with you now", 0.05),
        ("> I won't question why so many have died", 0.05),
        ("> My prayers have made it through, yeah", 0.05),
        ("> 'Cause with all these things we do", 0.06),
        ("> It don't matter when I'm coming home to you", 0.05),
    ]
    
    line_delays = [0.4, 0.5, 0.3, 0.3, 0.4, 0.4, 0.5, 0.3, 0.6]
    title = "## Gunslinger by Avenged Sevenfold ##"
    signature = "// Tiktok: arjunaaprakarsa"
    
    display_typed_lyrics(lyrics, line_delays, title, signature)


if __name__ == "__main__":
    main()