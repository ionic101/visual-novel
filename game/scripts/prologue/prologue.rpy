image sc_prologue = "sc_prologue.png"


label prologue:
    call start_prologue
    call graduation
    call meet_with_parents

    return


label start_prologue:
    scene sc_prologue

    $ renpy.pause(delay_time, hard=True)

    return


label graduation:
    scene urfu with dissolve

    "Эхх, вот и закончилась студенческая жизнь"
    "А вроде только недавно я был первокурсником, надо же, как быстро время летит"
    "Ну ладно, торжественная часть закончилась, с одногрупниками попрощался, можно и навести родителей"

    return


label meet_with_parents:
    scene home_parents with dissolve

    gg "Мам, пап, я дома!"
    dad "О, а вот и наш выпускник!"
    dad "Ну давай, рассказывай, что у тебя по планам?"
    gg "Да вот, собираюсь попытаться пройти стажировку в какую-нибудь IT-компанию"
    dad "Попытаться?!"
    dad "А я сразу же говорил, что надо было поступать на электрика. Электрики всегда нужны. Всегда на них есть спрос"
    dad "А что ты сейчас будешь делать? Хрен еще устроишься на работу. Зря потратил 4 года своей жизни на какую-то подставку под кружку"
    gg "Пап, ты слишком преувеличиваешь! Я смогу устроиться на работу, вот увидишь!"

    "После нескольких минут ссоры со своим отцом я оконочательно решил, что мне надо вернуться в Екатеринбург, чтобы доказать, что я смогу устроиться на работу"

    return
