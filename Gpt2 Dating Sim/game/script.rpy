init python:
    import filechecker

define s = Character(_("Sexy Babe"), color="#696969")

label start:

    scene bg

    play music "audio/local forecast elevator.mp3"

    show img


    "welcome to my game, to exit type \"exit\""

    jump conversation

    return

label conversation:
    $ intext = renpy.input("")
    if intext.lower() == "exit" or intext.lower() == "escape":
        return
    else:
        $ generated = filechecker.writeRead(intext)
        show img talk
        s "%(generated)s"
        show img
        jump conversation
