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
    scene scene_image

    #ГГ как-то исправляет проблему

    "ГГ исправляет проблему перед защитой продукта"

    show boss_image with dissolve

    boss "Ну, [gg.name], ну молодец!"
    boss "А теперь занимайте все свои места!"

    hide boss_image with dissolve

    "{i}*начинается презентация проекта*"

    boss "Уважаемые гости, коллеги, представители СМИ!"
    boss "Я рад приветствовать вас на этом важном мероприятии, где я хочу представить вам наш новый проект – \"Систему социального рейтинга\"."
    boss "Эта инновационная система была разработана нашей командой экспертов в области информационных технологий с целью отслеживания и анализа действий людей в реальной жизни и интернете для создания уникального рейтинга, основанного на их поступках."
    boss "Наша \"Система социального рейтинга\" основана на анализе всех доступных данных о сотрудниках, клиентах или гражданах, и с помощью современных алгоритмов машинного обучения оценивает их действия."
    boss "Мы учитываем не только их активности в социальных сетях, но и личное взаимодействие, например, на работе или в кругу семьи. Таким образом, мы создаем объективную и надежную среду для оценки поведения и достижений каждого."
    boss "Однако, я понимаю, что возникают сомнения и опасения. Определение человеческих поступков и их сопоставление могут быть этическими и приватными вопросами для многих."
    boss "Поэтому мы придаем высший приоритет защите частной жизни и конфиденциальности данных. Мы строго соблюдаем все законодательные нормы и регуляции, и наша система разработана с учетом принципов прозрачности и справедливости."
    boss "В заключение, я хотел бы подчеркнуть, что наша компания \"Абрис\" всегда стремится быть инновационной и полезной для общества. \"Система социального рейтинга\" – это наш вклад в развитие информационных технологий и создание новых возможностей."
    boss "Мы гордимся тем, что можем предложить нашему правительству инструмент, который поможет им принимать более обоснованные и продуктивные решения."
    boss "Спасибо за внимание, и я уверен, что наша \"Система социального рейтинга\" будет иметь значительный положительный вклад в общество!"

    #звуки аплодисментов

    return
