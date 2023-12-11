define offset = 0.11
define start_y = 0.25

define slot1 = False
define slot2 = False
define slot3 = False
define slot4 = False
define slot5 = False

image screen_job_1 = "images/JobHunter/slot1/bg_screen1.png"
image screen_job_2 = "images/JobHunter/slot2/bg_screen2.png"
image screen_job_3 = "images/JobHunter/slot3/bg_screen3.png"
image screen_job_4 = "images/JobHunter/slot4/bg_screen4.png"
image screen_job_5 = "images/JobHunter/slot5/bg_screen5.png"


screen ScreenMenu:
    image "images/JobHunter/bg_site.png"

    imagebutton:
        xalign 0.5
        yalign start_y + offset * 0
        if not slot1:
            idle "images/JobHunter/slot1/slot1_idle.png"
            hover "images/JobHunter/slot1/slot1_active.png"
            action Call("slot1_screen")
        else:
            idle "images/JobHunter/slot1/slot1_clicked.png"
        
        
    imagebutton:
        xalign 0.5
        yalign start_y + offset * 1
        if not slot2:
            idle "images/JobHunter/slot2/slot2_idle.png"
            hover "images/JobHunter/slot2/slot2_active.png"
            action Call("slot2_screen")
        else:
            idle "images/JobHunter/slot2/slot2_clicked.png"
    imagebutton:
        xalign 0.5
        yalign start_y + offset * 2
        if not slot3:
            idle "images/JobHunter/slot3/slot3_idle.png"
            hover "images/JobHunter/slot3/slot3_active.png"
            action Call("slot3_screen")
        else:
            idle "images/JobHunter/slot3/slot3_clicked.png"
    imagebutton:
        xalign 0.5
        yalign start_y + offset * 3
        if not slot4:
            idle "images/JobHunter/slot4/slot4_idle.png"
            hover "images/JobHunter/slot4/slot4_active.png"
            action Call("slot4_screen")
        else:
            idle "images/JobHunter/slot4/slot4_clicked.png"
    imagebutton:
        xalign 0.5
        yalign start_y + offset * 4
        if not slot5:
            idle "images/JobHunter/slot5/slot5_idle.png"
            hover "images/JobHunter/slot5/slot5_active.png"
            action [Call("slot5_screen"), Return(), Hide("ScreenMenu")]
        else:
            idle "images/JobHunter/slot5/slot5_clicked.png"
    



screen Mail:
    image "images/JobHunter/mail/bg_mail_screen.png"

    add Text("ООО \"Абрис\"", slow_cps=50, xpos=560, ypos=250, color=(0, 0, 0))
    
    add Text("Резюме на вакансию \"Инженер-программист\"", slow_cps=50, xpos=560, ypos=310, color=(0, 0, 0))

    add Text('''    Программист без опыта работы. Окончил УрФУ ИРИТ-РТФ
по направлению Информатика и вычислительная техника.
Основные навыки включают владение языками
программирования, такими как python, C#, C++, а также
использование различных инструментов разработки и систем
управления версиями, таких как Git. Знание принципов
объектно-ориентированного программирования и базовых
алгоритмов''', slow_cps=50, xpos=480, ypos=400, color=(0, 0, 0), layout="tex")

    imagebutton:
        xpos 460
        ypos 730
        idle "images/JobHunter/mail/send_button.png"
        action [Return(), Hide("Mail")]
    


label slot1_screen:
    scene screen_job_1

    $ slot1 = True

    "1С - полный кринж"

    call screen ScreenMenu

    return

label slot2_screen:
    scene screen_job_2

    $ slot2 = True

    "Педагогика точно не моё"

    call screen ScreenMenu

    return

label slot3_screen:
    scene screen_job_3

    $ slot3 = True
    
    "Тестировщик. Хмм… Ну даже не знаю. И зарплата не особо большая"

    call screen ScreenMenu

    return

label slot4_screen:
    scene screen_job_4

    $ slot4 = True
    
    "Backend, кстати, как вариант"

    call screen ScreenMenu

    return

label slot5_screen:
    scene screen_job_5

    $ slot5 = True
    
    "Опа а это что у нас такое. 120000!!! А вот с этого момента по подробнее"
    "Хмм… Ну что ж… Это отличный вариант для меня! А главное, я подхожу по всем параметрам! Осталось только написать резюме"

    return
