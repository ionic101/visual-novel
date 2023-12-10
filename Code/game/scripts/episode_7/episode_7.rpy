image sc_episode_7 = "images/episodes/episode_7.png"


label episode_7:
    call start_episode_7
    call company_party
    call walking

    return


label start_episode_7:
    scene sc_episode_7

    $ renpy.pause(delay_time, hard=True)

    return


label company_party:
    scene office with dissolve

    show boss_image with dissolve

    boss "Здравствуй, [gg.name], как тебе наш праздничный банкет?"
    

    gg "Все работники потрудились на славу и это заслуженная награда."

    boss "Ну естественно! Мы произвели фурор! Заказчик доволен, наш продукт начнут внедрять в повседневную жизнь уже со дня на день"
    boss "Ты очень мне помог, и я, какобещал, тебя за это награжу. Одной премией ты не отделаешься, теперь ты будешь главнымразработчиком этого проекта. Нужно совершенствовать систему и поддерживать её постояннуюработу."

    gg "Погодите… А как же Ростислав Вадимович?"
    boss "А что Ростислав? Он уволился по собственному желанию."
    gg "Но почему????"
    boss ": Видите ли этот проект противоречит его моральным ценностям. Где он раньше то был. Ну ничего, я уверен его жизнь будет полна “счастья” после таких выходок! Ха-ха."
    gg "….."
    boss "Он видимо не понимает какое сладкое будущее ждёт нас – создателей этого проекта. Ну что ж отдохни и расслабься сегодня, ты заслужил, но впереди ещё много работы."

    hide boss_image with dissolve

    "{i}*Вдалеке офиса я замечаю кого-то уже знакомого*"
    "О боже кто это…"
    "{i}*Время как будто остановилось, а сердце начало биться всё быстрее и быстрее*"
    "Какая изящная походка, какие милые черты лица… А глаза… Глаза — это искры, которые разжигают во мне пламя страсти. А какая красивая у неё…"

    show girl_image with dissolve

    girl "Привет!"
    gg "Ой… Пр.. Привет."
    girl "Извини, что побеспокоила тебя, ты, видимо, был погружён в какие-то свои мысли… Просто я увидела, что ты тоже здесь без компании, и хотела бы скрасить твоё одиночество, если ты не против конечно"
    gg "Конечно я не против! Как тебя зовут?"
    girl "Адель, а тебя?"
    gg "[gg.name]. А ты из какого отдела?"
    girl "Я из аналитики. А тебя даже и спрашивать не буду… Уже по всей компании расползся слух об увольнении Ростислава и твоём назначении на должность"
    gg "Даа, жаль этого добряка…"
    girl "Полностью согласна, он хоть и был занудой, но всегда оставался человеком. Может ну этот скучный корпоратив, пойдём прогуляемся?"
    gg "Конечно, я только за!"

    return



label walking:
    scene park with fade

    show girl_image with dissolve

    girl "Слушай, а как у тебя так быстро получилось добиться успеха в своей сфере?"
    gg "Ну знаешь, я просто стремился к своей цели, долго работал, учился, и вот теперь я главный разработчик гос проекта, гуляю под луной с очень красивой девушкой"

    girl "Ой, ты меня смущаешь… Я вообще не к этому вела! А вот почему ты решил стать программистом?"

    gg "Нууу… Мне всегда нравились компы и всё такое, да и вообще я хотел создавать что-то, что-то, что будет полезным для общества, чтобы упростить повседневный быт. Люди должны меньше времени уделять чему-то сложному и скучному. Нужно наслаждаться жизнью."

    girl "Это верно, правда, в последние дни меня не покидает одна мысль… Всем кажется, что если навести жёсткий порядок твёрдой рукой, такой как наша ССР, жить нам будет комфортнее и безопаснее, но нет ли риска, что эта комфортность очень быстро пройдёт, и эта рука начнёт нас быстро душить?"

    gg "Ого, какие мысли… Я даже как-то и не думал о таком. В любом случае, я уверен, что законопослушным гражданам нечего бояться. У нашей системы прекрасные алгоритмы анализа. Всё это сделано ради нашего умиротворения и спокойствия."

    girl "Может быть, ты и прав. Только время расставит всё на свои места. Кстати, о времени, к сожалению, мне уже пора бежать, надеюсь я не испортила нашу прогулку своим занудством."

    gg "Конечно нет, ты не только красотка, но ещё и отличный собеседник. Ещё увидимся!"

    girl "Пока-пока!"


    return
