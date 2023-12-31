define mother = Character("Мама", color="#da8a09")


image sc_episode_2 = "images/episodes/episode_2.png"
image phone = "images/objects/phone.png"
image phone_call = "images/objects/phone_call.png"

label episode_2:
    call start_episode_2
    call call_parents
    stop bgm
    return


label start_episode_2:
    scene sc_episode_2

    $ renpy.pause(delay_time, hard=True)

    return


label call_parents:
    scene home with dissolve
    show gg_blissful with dissolve
    play bgm "sounds/bg_main_music.mp3" volume 2
    "Ну вот и всё… Ещё один этап жизни позади. Это было славное время. Столько тёплых воспоминаний о студенческой жизни. Эх… Пройти бы ещё раз это всё. Я уже скучаю по своим друзьям. "
    stop bgm
    hide gg_blissful
    call phone_call
    play bgm "sounds/bg_main_music.mp3" volume 2
    gg "-Алло"
    mother "-Алло, сынок привет!"
    gg "-Привет мам…"
    mother "-У тебя какой-то грустный голос. Что-то случилось?"
    gg "-Нет всё в порядке, просто немного устал, сегодня был очень насыщенный день."
    mother "-Это точно! Сынок, мы с папой хотели тебя поздравить! Ты большой молодец! Мы гордимся тобой! Сын-программист. Мне все знакомые на работе завидуют."
    gg "-Ахах спасибо большое мам. Если бы не вы…"
    mother "-Ой да знаем, знаем. Ни раз нам это говорил. Ну что, пора бы и тебе начать работать над своим будущим. Как настрой? Боевой? Что там с работой? Пади любая контора такого программиста с руками и ногами оторвёт."
    gg "-Нуу… Если честно мне пока не поступало никаких предложений…"
    mother "-Баа... Сынок, не расстраивай ни меня ни папу, я же постоянно тебе толдычу Если гора не идёт к Магомеду…"
    gg "-Да знаю я! Просто… Просто мне нужно немного времени определиться."
    mother "-[gg.name], ты уж постарайся, ладно? Мы с папой столько в тебя вложили и хотим, чтобы ты оправдал наши надежды."
    gg "-Хорошо мам. Я обязательно это сделаю. Обещаю. Я очень устал и ещё не ужинал так что…"
    mother "-Ладно, ладно, сыночек, не буду тебя задерживать. Если будут какие-то новости, ты обязательно пиши, звони, не забывай уж своих стариков."
    gg "-Конечно мам. Я позвоню. Пока."
    mother "-Хорошего вечера. Пока-пока."

    #окончания звонка

    show gg_blissful
    "Эхх… А ведь на самом деле мама права… Я уже столько лет сижу у родителей на шее. Надо действовать. Ведь как говорил классик: \"безделье — игрушка дьявола\". Я прямо сейчас сяду и найду работу! Просто вот так сяду и найду!"
    hide gg_blissful

    return

label phone_call:
    play sound "sounds/phone_ring.mp3" loop

    show phone:
        xpos 850
        ypos 425

        # Анимация тряски телефона
        linear 0.1 xpos 840
        linear 0.1 ypos 430
        linear 0.1 xpos 860
        linear 0.1 ypos 420
        linear 0.1 xpos 850
        linear 0.1 ypos 425

        # Пауза для эффекта тряски
        pause 0.5

        repeat

    pause 2.0

    hide phone

    show phone_call with dissolve

    pause 2.0

    stop sound
    hide phone_call with Dissolve(0.5)

    return