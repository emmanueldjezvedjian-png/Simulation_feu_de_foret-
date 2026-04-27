# 🔥 Forest Fire Simulation – Cellular Automaton

A forest fire simulation based on cellular automata, built with Python and Pygame.
The model simulates fire spread through a grid of trees, taking into account wind 
direction, wind speed, and various fire ignition patterns.

## Features

- **Cellular automaton engine** – each cell evolves based on its neighbors' states
- **Wind parameters** – set direction (North, South, East, West, North_East, etc.) 
  and speed in km/h
- **Fire seed types** – choose how the fire starts:
  - `solo` – single ignition point
  - `cube` – small square ignition zone
  - `horizontale` – full horizontal line
  - `verticale` – full vertical line
- **Custom grid dimensions** – define width and height of the forest grid
- **Tree density** – control the proportion of trees vs empty cells (0 to 1)
- **IGN map import** – load a real map image; the simulation automatically detects 
  green pixels to reconstruct the forest layout

## Tech Stack

- Python 3
- Pygame
- Pillow (PIL)
- NumPy

## Installation

```bash
git clone https://github.com/emmanueldjezvedjian-png/Simulation_feu_de_foret-.git
cd Simulation_feu_de_foret-
pip install -r requirements.txt
python Simulation_finale.py
```

## Usage

On launch, a configuration window allows you to set:
- Grid width & height
- Tree density (0–1)
- Fire seed type
- Wind direction & speed (km/h)
- Optional: load an IGN map image

## Team

- Emmanuel Djezvedjian
- Antonin Decolavre
- Elsa Rigolet
-Noé peluchon
