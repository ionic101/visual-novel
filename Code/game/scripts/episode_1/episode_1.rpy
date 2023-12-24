define rector = Character("Ректор", color="#1ada09")
define students = Character("Выпускники", color="#f5f120")

# Определение каналов для звука
define voice = 30
define sfx = 20
define bgm = 10

image sc_episode_1 = "images/episodes/episode_1.png"


label episode_1:
    call start_episode_1
    call graduation

    return


label start_episode_1:
    scene sc_episode_1 with fade

    $ renpy.pause(delay_time, hard=True)

    return


label graduation:
    scene urfu with dissolve

    play bgm "sounds/episode1_music.mp3" volume 0.5
    play music "sounds/1_graduation.mp3" volume 2 noloop
    rector "Уважаемые студенты! Поздравляю вас с этим великолепным достижением – получением диплома!"
    stop music
    play music "sounds/2_graduation.mp3" volume 2 noloop
    rector "Это значимый момент в вашей жизни, который подчеркивает ваш труд, упорство и стремление к знаниям."   
    stop music
    play music "sounds/3_graduation.mp3" volume 2 noloop
    rector "Вы прошли долгий и трудный путь обучения, полный вызовов и усилий. Теперь, держа в руках свой диплом, вы можете с гордостью смотреть на все, что достигли."
    stop music
    play music "sounds/4_graduation.mp3" volume 2 noloop
    rector "Ваше образование – это не только заслуга ваших преподавателей, но и результат ваших собственных усилий, целеустремленности и стремления к знаниям."
    stop music
    play music "sounds/5_graduation.mp3" volume 2 noloop
    rector "Вы стали не только обладателями диплома, но и членами нашего уважаемого образовательного сообщества."
    stop music
    play music "sounds/6_graduation.mp3" volume 2 noloop
    rector "Верьте в свои силы, идите вперед с уверенностью, развивайтесь и применяйте полученные знания в своей профессиональной деятельности."
    stop music
    play music "sounds/7_graduation.mp3" volume 2 noloop
    rector "Желаю вам успешной карьеры, интересных проектов и постоянного личностного роста!"
    stop music

    students "УРААА! РТФ — ЧЕМПИОН! РТФ — ЧЕМПИОН! РТФ — ЧЕМПИОН!"

    stop bgm

    return
