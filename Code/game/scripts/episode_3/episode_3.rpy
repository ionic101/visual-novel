image sc_episode_3 = "images/episodes/episode_3.png"


label episode_3:
    call start_episode_3
    call find_job

    return


label start_episode_3:
    scene sc_episode_3

    $ renpy.pause(delay_time, hard=True)

    return


label find_job:
    scene home with dissolve
    
    "Таакс… Надо бы посмотреть вакансии на сайте JobQuestHub.com"

    call screen ScreenMenu
    call screen Mail

    scene home

    "Вот и все! Резюме отправлено! Теперь жду ответного сообщения..."

    return
