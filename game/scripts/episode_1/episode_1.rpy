define friend = Character("Знакомый", color="#138ce8")
image sc_episode_1 = "sc_episode_1.png"


label episode_1:
    call start_episode_1
    call find_job

    return


label start_episode_1:
    scene sc_episode_1

    $ renpy.pause(delay_time, hard=True)

    return


label find_job:
    scene home_gg with dissolve

    "Хорошо что у меня были накопления, чтобы снять квартиру на первое время"
    "Так, надо бы посмотреть, вдруг мне кто-то из работадателей ответил по поводу моей заявки"

    menu:
        "Проверить почту":
            pass
    
    "Хм..."
    "Пришло на почту приглашение на второй этап отбора"
    "Думаю было бы неплохо подготовиться"

    menu:
        "Посмотреть рекомендацию по подготовке":
            pass
    
    "Истребитель мне в ангар..."
    "Тут половина того, что написано, я впервые вижу"
    "Что же делать? Я так точно не попаду на стажировку"
    "Хотя..."
    "Как же я мог забыть? У меня один знакомый работает в этой IT-компании"

    "Но вспомнит ли он меня? А вдруг он не поможет мне с трудоустройством? Как-то неудобно..."

    menu:
        "Позвонить знакомому":
            call call_friend
        "Попытаться пройти на стажировку самому":
            call job_selection
    
    "На следующий неделе начинается моя первая работа в этой компании..."

    return


label call_friend:
    "*звуки гудка*"

    friend "Але..."
    gg "Привет, это [gg.name], помнишь меня? Мы с тобой учились на одном потоке по математике"
    friend "Оооо, привет [gg.name], конечно помню"

    "Несколько минут мы общались, рассказывали друг-другу, как поживаем, но потом я вспомнил, зачем я позвонил"

    gg "Слушай, а ты можешь мне помочь с трудоустройством в компанию?"
    friend "Я попробую поговорить со своим начальником, но не могу гарантировать, что получиться договориться"
    friend "Давай я тебе перезвоню через дня 2 и сообщу, получилось ли договориться или нет?"
    gg "Хорошо, буду ждать твоего звонка"

    "На этой фразе у нас закончился диалог"

    "Через дня 2, как и было обещано, мне позвонил знакомый"
    friend "Здарова, у меня для тебя есть хорошая и плохая новость"
    friend "Хорошая - я договорился с начальником и тебя могут взять на стажировку"

    "Тут я чуть не воскликнул от радости"
    gg "А какая плохая?"

    friend "Плохая - тебе придется работать на пол-ставки"
    "Для меня это не было плохой новостью. Я готов был работать за любые деньги, главное - чтобы по моей специальности"

    "Я поблагодарил своего знакомого и мы все обсудили по поводу моего трудоустройства"

    return


label job_selection:
    "Ну, надеюсь у меня все получится"
    "Причем у меня еще есть в запасе 4 дня"

    scene dark with dissolve
    "*прошло 4 дня*"
    scene home_gg with dissolve
    
    "Это конец"
    "Я ни к чему не подготовился"
    "Последняя надежда на гугл"
    "Но вдруг они заподозрят в подглядывании?"
    "Или все же попробовать самому ответить?"

    menu:
        "Исопльзовать гугл":
            "Нет, с гуглом я буду очень долго возиться с поиском ответа"
            "Надо найти другой способ"
            "Ну конечно же!"
            "Буду использовать Chat-gpt, зря подписку что-ли купил?"
            "Причем в новостях я где-то видел, что один человек смог с помощью этого ИИ пройти собеседование"
        "Самому отвечать на вопросы":
            "Нет, с гуглом я буду очень долго возиться с поиском ответа"
            "Буду сам отвечать!"
    
    "Ну, с Богом!"

    scene dark with dissolve
    "*после собеседования*"
    scene home_gg with dissolve

    "Надо же, насколько все просто было, даже гугл не потребовался!"
    "Все же хорошая подготовка была в вузе!"

    "Через несколько дней пришло письмо о приглашении на стажировку"

    return