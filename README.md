# 🎈 Bloons Tower Defense (Python Edition)

A tower defense game inspired by the classic **Bloons TD** series, built in **Python** with full graphics, animations and gameplay using the pygame library.

---


## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Install & Run](#install--run)

---

## Features

- 🎯 **Tower placement**: multiple tower types with distinct behaviors.
- 🧠 **balloons waves**: progressive wave system with varied bloon types.
- 🎨 **Custom graphics & animations**: sprites for towers, projectiles and effects.
- 🗺️ **Multiple maps/modes** with different paths and layouts.
- 🛠️ **Modular OOP codebase**: towers, shots, levels and UI are separated for easy extension.

---

## Screenshots
```markdown
![Home Screen](images/home_screen_screenshot.png)
![Menu Screen](images/menu_screen_screenshot.png)
![Normal Game](images/normal_game_screenshot.png)
![Sandbox Game](images/sandbox_game_screenshot.png)
```
---

## Project structure

```
BloonsTD/
├── images/                # Sprites, backgrounds, GUI assets
├── sounds/                # Sound effects & music
├── gameplay/              # Game logic: towers, shots, bloons, levels
│   ├── buttons/
│   ├── effects/
│   ├── game_modes/
│   ├── screen_states/
│   ├── shots/
│   └── towers/
├── utils/                 # Helpers and utilities
├── main.py                # Game entry point
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── LICENSE
```

---

## Getting started

### Prerequisites

- Python 3.8 or newer installed. Verify with:

```bash
python --version
# or
python3 --version
```

- (Recommended) Create and use a virtual environment to avoid dependency conflicts.

### Install & Run

1. Clone the repository:

```bash
git clone https://github.com/guybiran123/BloonsTD.git
cd BloonsTD
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python main.py
# or
python3 main.py
```

---

*Enjoy the game*
