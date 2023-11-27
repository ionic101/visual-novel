image sc_episode_5 = "images/episodes/episode_5.png"


label episode_5:
    call start_episode_5
    call start_work
    call talking_with_director
    call task_2
    
    return


label start_episode_5:
    scene sc_episode_5

    $ renpy.pause(delay_time, hard=True)

    return

label start_work:
    scene office

    show senior_image at right
    show boss_image
    

    boss "- Познакомься, [gg.name], это твой наставник Ростислав Вадимович. Самый опытный разработчик, которого я только знаю. Уверен, ты многому у него научишься, и вы отлично сработаетесь."
    boss "Что ж, Ростислав, отдаю этого мальца в твои руки. Дерзайте! И не забывай, что уже не за горами представление проекта."
    
    hide boss_image with dissolve
    pause(0.5)
    hide senior_image
    show senior_image with dissolve
    pause(0.5)

    senior "-Что ж, [gg.name], тебе, наверное, очень хочется узнать над чем мы работаем. Я введу тебя в курс дела и дам первое задание."
    senior "Наш проект – это поистине грандиозная штука! Заказ сразу от нескольких государств! Я до сих пор не могу в это поверить…"
    senior "-Мы разрабатываем систему социального рейтинга (в сокращении ССР), наверное, ты мало об этом слышал. "
    senior "-Социальный рейтинг складывается из информации, полученной из официальных источников — налоговой, правоохранительных органов, правительственных структур, загсов, образовательных учреждений, компаний."   
    senior "А также из данных цифровых источников: истории поиска, онлайн-покупок и активности в соцсетях."
    senior "Кроме того, информацию получают через камеры видеонаблюдения и систему распознавания лиц. Камеры контролируют почти каждый шаг человека. Рейтинг рассчитывает искусственный интеллект."
    senior "- Вот такие пироги. Пока что это всё что тебе нужно и можно знать. Ты же у нас инженер программист?"
    senior "Вот твоё первое задание. Тебе нужно поработать над главной страницей сайта нашей системы. Сделай заголовок, краткое описание нашего проекта, вставь картинки. Оформи всё красиво. Как закончишь, отправишь мне на проверку"
    
    scene black with fade
    #мини-игра
    scene office with fade
    show senior_image with dissolve

    gg "-Ростислав Вадимович, я выполнил ваше задание"

    senior "-Ну-ка посмотрим…"
    senior "Хм…"
    senior "А мне нравится! Хорошая работа, [gg.name]. Раз уж у тебя так хорошо получается, нужно сделать ещё 28 страниц нашего будущего сайта. Дерзай!"

    gg "-Вот блин… Это мне много дней придётся работать с этой нудятиной…"
    
    scene black with fade
    "{i}Прошло несколько дней"
    scene office with fade
    show senior_image with dissolve
    pause 0.5

    gg "Ростислав Вадимович, я наконец-то выполнил выше задание! Вы уже видели новую версию нашего сайта на Git?"
    
    senior "-Нет, но сейчас обязательно проверю. Кстати, директор отдела хотел тебя видеть, обязательно загляни к нему"
    
    return


label talking_with_director:
    scene boss_office with fade
    show boss_image with dissolve

    boss "-Здравствуй, [gg.name]. Как тебе твоя работа?"
    boss "Наверное, Ростислав Вадимович во всю тебя эксплуатирует?"
    boss "Впрочем, это неважно, важно то, что хороший программист должен не только хорошо разрабатывать проект, но и защищать его перед заказчиком."
    boss "Нам с Вадимом очень нужен помощник, и, я думаю, ты подходящая для этого кандидатура. Если всё пройдёт гладко я в долгу не останусь."

    gg "-А если что-то пойдёт не так?"

    boss "-Уууу… Друг мой, лучше об этом не думать. Этот проект жизненно важен для нашей компании."
    boss "Ты знаешь кто заказчики этого проекта? О нет, лучше тебе не знать."
    boss "Надеюсь, ты меня услышал. Защита через ровно через месяц, так что никаких планов! Будь на готове и жди указаний!"

    gg "-Есть сер!"

    return


label task_2:
    scene office with fade
    show senior_image with dissolve

    senior "-Я проверил твою работу, всё отлично. Я думаю ты отлично попрактиковался писать frontend, пришла пора заняться “настоящим” программированием."
    senior "Твоя новая задача – подготовить базу данных в которой будет храниться информация о гражданах и их социальный рейтинг. Ты же работал с SQL?"

    gg "-Хмм… Ну даа… Правда, это было так давно, по-моему, на 2-ом курсе. Не уверен, что я…"

    senior "-Никаких но! Ты хороший программист, а не абы кто, и ты должен уметь это делать, так что разберёшься."

    gg "-Ростислав Вадимович, я сделаю всё что в моих силах"

    #minigame

    return