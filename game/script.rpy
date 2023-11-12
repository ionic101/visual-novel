define gg = Character("Главный герой", color="#e8e813")
define dad = Character("Отец", color="#1dd90f")

image dark = "bg_dark.png"
image office = "bg_office.png"
image workplace = "bg_workplace.png"
image urfu = "bg_urfu.png"
image home_parents = "bg_home_parents.png"
image home_gg = "bg_home_gg.png"

define delay_time = 3

label start:
    call prologue
    call episode_1
    call episode_2

    return
