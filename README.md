# trA rorriM | Mirror Art
## Zenith Fortier - PFDA Final Project

**Repository Url** - https://github.com/ZenithFortier/pfda_final_project
**Video Presentation Url** - 

### Summary
The user inputs some text and a list of colors into the console, and the program begins drawing a work of art that is mirrored across both the x-axis and y-axis. The lines are drawn live over time, changing direction based on each letter of the user input. Once all letters have been drawn, the program exports the final image as a .png file and closes.

### Technical Info
The majority of the program is built in `Pygame`, using a custom-built Turtle class. While originally I was going to use Python's built in `turtle` module, it ended up being far too limited for what I needed. 

The color selection is based on the `Pygame` color library, and will automatically prompt the user to retype a color if a matching color was not found. The colors are assigned one color per turtle; if the user types more or less than 4 colors, the list will be automatically trimmed to the first 4, or appended so that an entered color may be assigned to more than one turtle.

To create the angle-to-letter dictionary, I divided 360 by 26 to get roughly 13 degrees per letter, and thus assigned each letter to a multiple of 13. The `math` module is then used to increment x and y values along that angle, while a global time variable controls when to move to the next angle in the list. By multiplying by -1, the mirrored coordinates were created, allowing for four simultaneous turtles that are always symmetrical. 

The final image is saved by converting the `Pygame` display surface to a `Pillow` image, before saving it with the `os` module. Since the image is saved based on a truncated version of the user word input, duplicate words are saved with a number designation. This allows users to recreate the same word multiple times in different colors without overwriting previous versions.

Requires installing `Pygame` and `Pillow` libraries.

### Future Considerations
If I were to work on this further, I would like to have some sort of UI built, rather than force the user to interface directly with the console. I would also like to have more customization options such as different line weights and more than four turtles, which I was not able to get to due to the difficulties I faced in creating the turtles from scratch. I also would consider adding the ability to change resolution and have a less clunky full screen option.

Overall, I am happy with this version as a solid proof-of-concept and functional generator that I can use to create art of my own.