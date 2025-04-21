# 🎵 Lyrics Player

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

A stylish terminal-based lyrics display with typing animation effects. Create beautiful, animated lyric displays in your terminal with customizable speeds and formatting.

![Demo Animation](https://via.placeholder.com/650x300?text=Lyrics+Player+Demo)

## ✨ Features

- 🖨️ Typewriter-style animation for lyrics display
- ⏱️ Customizable character and line delay timings
- 🎨 Simple formatting with custom prefixes
- 🔄 Clean, modular code structure for easy modification
- 📱 Perfect for social media content creation

## 🚀 Installation

No external dependencies needed! Just clone and run:

```bash
git clone https://github.com/arjunapanji21/LyricPlayer.git
cd LyricPlayer
python main.py
```

## 🎮 Usage

```python
from lyrics_display import display_typed_lyrics

# Define your lyrics and timing
lyrics = [
    ("> Line one of your favorite song", 0.06),
    ("> Second line with different timing", 0.05),
]

line_delays = [0.4, 0.5]  # Delays after each line
title = "## Your Favorite Song by Artist ##"
signature = "// Your social media handle"

# Display the lyrics
display_typed_lyrics(lyrics, line_delays, title, signature)
```

## 🔧 Customization

### Change the song
Edit the `lyrics` list in `main()` to include your favorite lyrics:

```python
lyrics = [
    ("> First line of your song", 0.06),
    ("> Second line goes here", 0.05),
    # Add more lines...
]
```

### Adjust timing
- Modify the second value in each lyric tuple to change character typing speed
- Change values in the `line_delays` list to adjust pauses between lines

### Styling
- Change the prefix (`>`) to any character(s) you prefer
- Customize the title format and signature

## 📝 Creating Content

Perfect for creating:
- TikTok lyric videos (screen record your terminal)
- Discord/Slack music sharing
- Terminal-based music players
- Creative coding projects

## 📜 License

MIT License - Feel free to modify and distribute as you wish!

## 🙌 Credits

Created by: Arjuna Panji Prakarsa  
Social: [@arjunaaprakarsa](https://tiktok.com/@arjunaaprakarsa)

---

<p align="center">Made with ❤️ for music lovers</p>