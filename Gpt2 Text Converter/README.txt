Requirements:

-Python 3.7.x
-Tensorflow 1.15.x

the 'gpt2thing.py' is a modified version of 'gpt-2-simple', so you can look at the documentation for that

the checkpoints and stuff are on the itch.io version, so if you want those get that one



i dont really know what else to put in here tbh



all it does is read from a text file, see if its gpt2s turn and then grabs the text and runs it through

it then writes the output back to the text file with a '0' at the beginning (the 0 means its renpys turn)

renpy then sees that its its turn and shows the user gpt2s output, then it takes the users input and writes it to the file with a '1' at the beginnning (like the 0, but it means gpt2s turn)