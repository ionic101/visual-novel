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
    scene workplace with dissolve
    
    "Таакс… Посмотрим, что тут у нас."
    "1с – это кринж."
    "Педагогика точно не моё."
    "Тестировщик?"
    "Хмм…"
    "Ну даже не знаю. И зарплата не особо большая."
    "Backend, кстати, как вариант."
    "Опа а это что у нас такое. 120000!!! А вот с этого момента по подробнее."

    #обзор профессии

    "Хмм… Ну что ж… Это отличный вариант для меня! А главное, я подхожу по всем параметрам!"
    "Осталось только написать резюме."

    #создание резюме

    return
