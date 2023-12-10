image sc_episode_6 = "images/episodes/episode_6.png"


label episode_6:
    call start_episode_6
    call project_presentation

    return


label start_episode_6:
    scene sc_episode_6

    $ renpy.pause(delay_time, hard=True)

    return


label project_presentation:
    scene bg_scene with dissolve

    boss "До выступления осталось 5 минут. У нас точно всё готово?"
    show boss_image with dissolve

    senior " Всё на высоте, но на всякий случай, проверим оборудование ещё раз, а вы пока повторите текст."
    show senior_image at left with dissolve

    senior "[gg.name], проверь, пожалуйста, ПК, с которого мы будем демонстрировать проект."

    gg "Секундочку, сейчас всё будет."

    jump global_problem

    return


label global_problem:
    scene workplace with dissolve

    senior "Чёрт возьми, этого нам не хватало…"
    boss "Это ещё что такое *****. НЕМЕДЛЕННО ВСЁ ИСПРАВИТЬ!!! ВЫ НЕ ПОНИМАЕТЕ!!! ТАМ ТАКИЕ ЛЮДИ!!! ДА НАС ВСЕХ…"
    
    gg "Прошу, успокойтесь, пожалуйста, я знаю что делать."

    $ choose_1 = 1
    $ choose_2 = 1
    $ choose_3 = 1

    jump choose_solution

    return


label choose_solution:
    menu:
        "Проверить соединение монитора и видеокарты" if choose_1:
            $ choose_1 = 0
            call solution_1

        "Перезагрузить ПК" if choose_2:
            $ choose_2 = 0
            call solution_2

        "Провести диагностику" if choose_3:
            $ choose_3 = 0
            call solution_3

    return


label solution_1:
    gg "Необходимо проверить соединение монитора и видеокарты!"

    senior "Сейчас…"

    scene workplace with Fade(0.5, 1.0, 0.5)

    senior "Нет, дело в чем-то другом."

    jump choose_solution

    return


label solution_2:
    gg "Необходимо просто перезагрузить ПК!"

    senior "А поумнее ничего не смог придумать?! Если бы в этой жизни всё было так просто…"

    jump choose_solution

    return


label solution_3:
    gg "Давайте произведём диагностику системы."

    senior "А вот это звучит здраво! Действуй!"

    scene workplace with Fade(0.5, 1.0, 0.5)

    "{i}Произошла ошибка, связанная с работой видеокарты. Проверьте настройки видеокарты или обновите видеодрайверы"

    gg "Делов-то. Ща пофиксим"

    scene workplace with Fade(0.5, 1.0, 0.5)

    gg "Я переустановил драйвера видеокарты, сейчас комп перезагрузится и будет работать как часы"

    boss "ФУУУХ… Похоже, мы спасены!"

    return
