# console_pacman.py

import os

# Mapa: # = pared, . = punto, P = Pac-Man, G = fantasma
import random

maze = [
    list("############################"),
    list("#.............##...........#"),
    list("#.####.#####.##.#####.####.#"),
    list("#.#  #.#   #.##.#   #.#  #.#"),
    list("#.####.#####.##.#####.####.#"),
    list("#..........................#"),
    list("#.####.##.########.##.####.#"),
    list("#.####.##.########.##.####.#"),
    list("#......##....##....##......#"),
    list("######.##### ## #####.######"),
    list("     #.##### ## #####.#     "),
    list("     #.##          ##.#     "),
    list("     #.## ###  ### ##.#     "),
    list("######.## #      # ##.######"),
    list("      .   #      #   .      "),
    list("######.## #      # ##.######"),
    list("     #.## ######## ##.#     "),
    list("     #.##          ##.#     "),
    list("     #.## ######## ##.#     "),
    list("######.## ######## ##.######"),
    list("#............##............#"),
    list("#.####.#####.##.#####.####.#"),
    list("#.####.#####.##.#####.####.#"),
    list("#...##................##...#"),
    list("###.##.##.########.##.##.###"),
    list("###.##.##.########.##.##.###"),
    list("#......##....##....##......#"),
    list("#.##########.##.##########.#"),
    list("#.##########.##.##########.#"),
    list("#..........................#"),
    list("############################")
]

pacman_pos = [1, 1]
ghost_pos = [5, 8]
score = 0

def print_maze():
    for i, row in enumerate(maze):
        line = ""
        for j, col in enumerate(row):
            if [i, j] == pacman_pos:
                line += "C"
            elif [i, j] == ghost_pos:
                line += "G"
            else:
                line += col
        print(line)

def move_pacman(direction):
    global score
    x, y = pacman_pos
    dx, dy = 0, 0
    if direction == "w": dx = -1
    elif direction == "s": dx = 1
    elif direction == "a": dy = -1
    elif direction == "d": dy = 1

    new_x, new_y = x + dx, y + dy
    if maze[new_x][new_y] != "#":
        if maze[new_x][new_y] == ".":
            score += 10
        pacman_pos[0], pacman_pos[1] = new_x, new_y
        maze[new_x][new_y] = " "

def move_ghost():
    gx, gy = ghost_pos
    px, py = pacman_pos
    dx = 1 if px > gx else -1 if px < gx else 0
    dy = 1 if py > gy else -1 if py < gy else 0

    # Prioridad a movimientos verticales
    if maze[gx + dx][gy] != "#":
        ghost_pos[0] += dx
    elif maze[gx][gy + dy] != "#":
        ghost_pos[1] += dy

while True:
    print_maze()
    print(f"Score: {score}")
    if pacman_pos == ghost_pos:
        print("Game Over! El fantasma te atrapó 👻")
        break
    move = input("Move (w/a/s/d): ")
    move_pacman(move)
    move_ghost()