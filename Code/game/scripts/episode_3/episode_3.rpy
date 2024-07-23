image sc_episode_3 = "images/episodes/episode_3.png"


label episode_3:
    call start_episode_3
    call find_job
    stop music
    return


label start_episode_3:
    scene sc_episode_3

    $ renpy.pause(delay_time, hard=True)

    return


label find_job:
    scene home with dissolve
    show gg_image
    play music "sounds/bg_main_music.mp3"
    "Таакс… Надо бы посмотреть вакансии на сайте JobQuestHub.com"
    hide gg_image
    stop music
    play music "sounds/bg_rave.mp3"

    call screen ScreenMenu
    stop music
    play music "sounds/print_(8c).mp3" noloop
    call screen Mail
    stop music
    play music "sounds/bg_main_music.mp3"
    scene home

    show gg_image
    "Вот и все! Резюме отправлено! Теперь жду ответного сообщения..."
    hide gg_image
    return
