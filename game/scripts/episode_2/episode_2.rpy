image sc_episode_2 = "sc_episode_2.png"
image sc_end_game = "sc_end_game.png"

label episode_2:
    call start_episode_2
    call end_game

    return


label start_episode_2:
    scene sc_episode_2

    $ renpy.pause(delay_time, hard=True)

    return

label end_game:
    scene sc_end_game with dissolve

    $ renpy.pause(delay_time, hard=True)
    $ renpy.pause ()

    return