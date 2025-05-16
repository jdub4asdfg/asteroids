# Asteroids in pygame
This is my second project in the Boot.dev Backend Developer Learning Path.

In this project, I made use of what I learnt in the Object Oriented Programming Course to create an Asteroids game using pygame.

Note that the project right now is very bare bones but I will be improving on it as I get better at programming! Check out the To-Do list at the bottom to see what changes I've planned.

## How to play
Clone the repository and run

`python3 main.py`

Press `W` to move forward, `S` to move backward, `D` to rotate clockwise,`A` to rotate counter clockwise and `SPACE` to shoot.

## Game logic
Asteroids represented by circles, spawn randomly at random sizes on each edge of the window.

There are 3 sizes of asteroids: Large, medium and small.

Shooting asteroids causes them to split into 2 smaller sized asteroids. For example:

- Shooting a large asteroid causes it to split into 2 medium asteroids.

- Shooting a medium asteroid causes it to split into 2 small asteroids.

- Shooting a small asteroid causes it to disappear.

Note that asteroids that split from the shot asteroid travel fasterand move in slight tangents from the shot asteroid.

There is a rate limit on shooting but you can just hold down `SPACE` to shoot on cooldown.

The player is represented by a triangle and dies when it touches an asteroid.

Have fun!

## Future To-Dos
- [ ] Add a start menu
- [ ] Add and display scores and the high score 
- [ ] Prevent player from going offscreen
- [ ] Add a death screen with a restart and quit button
