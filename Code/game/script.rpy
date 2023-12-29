define gg = Character("Дима", color="#a1a1a1")
define girl = Character("Девушка", color="#e948ec")
define senior = Character("Сеньор", color="#3ee7e7")
define boss = Character("Директор", color="#46e631")
define player = Character(None, kind=nvl)


image office = "images/backgrounds/bg_office.png"
image workplace = "images/backgrounds/bg_workplace.png"
image urfu = "images/backgrounds/bg_urfu.png"
image home = "images/backgrounds/bg_home_gg.png"
image boss_office = "images/backgrounds/bg_boss_office.png"
image bg_scene = "images/backgrounds/bg_scene.png"
image machine_image = "images/backgrounds/bg_coffee.png"
image park = "images/backgrounds/bg_park.png"
image room = "images/backgrounds/bg_room.png"


image gg_image:
    "images/characters/ch_gg.png"
    zoom 0.4
    ycenter 1.0

image girl_image:
    "images/characters/ch_girl.png"
    zoom 0.4
    ycenter 1.0

image boss_image:
    "images/characters/ch_boss.png"
    zoom 0.4
    ycenter 1.0

image senior_image:
    "images/characters/ch_senior.png"
    zoom 0.4
    ycenter 1.0


transform left:
    xcenter 0.2
    ycenter 1.0

transform right:
    xcenter 0.8
    ycenter 1.0

transform center:
    xcenter 0.5
    ycenter 1.0


label start:
    call episode_1 
    call episode_2
    call episode_3
    call episode_4
    call episode_5
    call episode_6
    call episode_7
    call episode_8
    call show_end_credit

    return