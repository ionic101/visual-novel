define gg = Character('Миша', color="#e8e813")
define d = Character("Директор", color="#e8132f")

image dark = "bg_dark.png"
image office = "bg_office.png"
image workplace = "bg_workplace.png"
image urfu = "bg_urfu.png"
image home = "bg_home.png"

image director_image:
    "ch_director.png"
    ypos 1700

label start:
    scene urfu

    show director_image

    gg "Вы создали новую игру Ren'Py."

    d "Хай!"

    

    gg "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
