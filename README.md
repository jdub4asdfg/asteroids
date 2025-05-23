# Asteroids in pygame
In this project, I made use of what I learnt in the Object Oriented Programming Course from Boot.dev to create an Asteroids game using Pygame.

Note that the project right now is very bare bones but I will be improving on it as I get better at programming! Check out the To-Do list at the bottom to see what changes I've planned.

## How to play
- Clone the repository using `git clone https://github.com/jdub4asdfg/asteroids.git`
- Install Pygame using `pip install -r requirements.txt`
- Run `python3 main.py` in your CLI.

Press `W` to move forward, `S` to move backward, `D` to rotate clockwise,`A` to rotate counter clockwise and `SPACE` to shoot.

## Game logic
Asteroids represented by circles, spawn randomly at random sizes on each edge of the window.

There are 3 sizes of asteroids: Large, medium and small.

Shooting asteroids causes them to split into 2 smaller sized asteroids. For example:
- Shooting a large asteroid causes it to split into 2 medium asteroids.
- Shooting a medium asteroid causes it to split into 2 small asteroids.
- Shooting a small asteroid causes it to disappear.

Note that asteroids that split from the shot asteroid travel faster and move in slight tangents from the shot asteroid.

There is a rate limit on shooting but you can just hold down `SPACE` to shoot on cooldown.

The player is represented by a triangle and dies when it touches an asteroid.

## Future To-Dos
- [ ] Add a start menu
- [ ] Add and display scores and the high score 
- [ ] Prevent player from going offscreen
- [ ] Add a death screen with a restart and quit button
