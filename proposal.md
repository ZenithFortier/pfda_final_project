# trA rorriM

## Repository
https://github.com/ZenithFortier/pfda_final_project

## Description
The program draws and exports a procedural abstract linework image using user input word(s) to determine the movement direction of the line. 
The image is mirrored across multiple lines of symmetry to create a Mandala effect.

## Features
- User inputs text to create Mandala art
	- The letters will have a dictionary corrosponding to some angle/direction/quality which can be given to the drawing turtle(s) in sequence.
- User selects colors, line weight, and lines of symmetry to be used 
	- Queue a list of qualities that can be fed to the turtle(s) as each step executes.
- Save/Export user creations
	- Using file I/O processes save the created drawing as an image to the user's computer. Possibly capture drawing timelapse as animation sequence?

## Challenges
- Need deeper understanding of the turtle module.
- Creating ways for the user to control the various aspects such as line weight and color?
- Possible interactions between Pillow, Pygame's draw functions, and the turtle module?

## Outcomes
Ideal Outcome:
- The program is a fully functional art generator with UI. The user input is displayed on the screen below the drawing surface, with a toggle for whether or not it should be included in the exported image(s) and a small selection of font options. The user can select each letter to change the color and line thickness it will draw. The canvas' total lines of symmetry is configurable by the user. A start button will create the drawing, and the user can export both a final image and a timelapse of the process.

Minimal Viable Outcome:
- The program successfully generates a Mandala image from the user's text input. The user can type a word and a color into the console, and the drawing will be made from that word in that color, along some set number of lines of symmetry.

## Milestones

- Week 1
  1. Create dictionary
  2. Set up basic turtle functions

- Week 2
  1. Expand turtle functions
  2. Create file export system

- Week N (Final)
  1. Implement button UI
  2. Implement timelapse creation