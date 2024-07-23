define credit = renpy.file("scripts/end_credit/end_credit.txt").read().decode("utf-8").replace('\r', '')

define credit_time_show = 40.0
define music_fadeout = 5.0
define screen_fadeout = 5.0
define screen_delay = 1.0

define audio.end_credit_music = "sounds/last_summer.mp3"


image end_credit:
    Text('{size=50}' + credit)
    anchor (0.5, 0.0)
    pos (0.5, 1.0)
    linear credit_time_show ypos 0.0 yanchor 1.0


label show_end_credit:
    $ _dismiss_pause = False

    play music end_credit_music fadein 5.0

    scene park with Fade(1.0, 1.0, 5.0)

    show end_credit

    $ _dismiss_pause = True

    $ renpy.pause(credit_time_show)

    hide end_credit

    $ renpy.pause(screen_delay)

    scene black with Dissolve(screen_fadeout)

    stop music fadeout music_fadeout

    $ renpy.pause(music_fadeout)

    return
