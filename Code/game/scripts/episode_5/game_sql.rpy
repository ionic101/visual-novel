init python:
    class Colors:
        blue = "2aaaff"
        white = "cccccc"
        green = "00916d"

    class Hint:
        idle_sprite = "images/SQL/vs_button_idle.png"
        hover_sprite = "images/SQL/vs_button_hover.png"
        color = Colors.white

        def __init__(self, text, status, comment=None, display_color=Colors.white):
            self.text = text
            self.comment = comment
            self.status = status
            self.display_color = display_color
    
    class HintMenu:
        def __init__(self, *hints):
            self.hints = list(hints)

    class CodeBlock:
        def __init__(self, text, color):
            self.text = text
            self.color = color

    class CodeLine:
        def __init__(self, hint_menus, code_blocks):
            self.hint_menus = hint_menus
            self.code_blocks = code_blocks
    
    class Code:
        def __init__(self, *code_lines):
            self.code_lines = code_lines
    
    sql_code = Code(
        CodeLine(
            hint_menus = [
                HintMenu(
                    Hint(text="*", status=True, comment="Верно, * - означает все столбцы, перейдём к следующей строчке", display_color=Colors.white),
                    Hint(text="FullName", status=False, comment="Неправильно, FullName - вернёт только значение из столбика с именем человека, а нам надо возвращать всю строчку целиком"),
                    Hint(text="Rating", status=False, comment="Неправильно, Rating - вернёт только значение из столбика с именем человека, а нам надо возвращать всю строчку целиком")
                )
            ],
            code_blocks = [
                CodeBlock("SELECT", Colors.blue)
            ]
        ),
        CodeLine(
            hint_menus = [
                HintMenu(
                    Hint(text="PeopleRating", status=True, comment="Верно, PeopleRating - Это и есть наша таблица", display_color=Colors.white),
                    Hint(text="Imprisonment", status=False, comment="Неправильно, Imprisonment - это таблица с данными о людях, заключенных под стражу"),
                    Hint(text="StaffMember", status=False, comment="Неправильно, StaffMember - это таблица с данными о работниках нашей компании")
                )
            ],
            code_blocks = [
                CodeBlock("FROM", Colors.blue)
            ]
        ),
        CodeLine(
            hint_menus = [
                HintMenu(
                    Hint(text="Rating", status=False),
                    Hint(text="FullName", status=True),
                ),
                HintMenu(
                    Hint(text="=", status=True),
                ),
                HintMenu(
                    Hint(text="\"Имя человека\"", status=True, display_color=Colors.green),
                ),
                HintMenu(
                    Hint(text="AND", status=True, display_color=Colors.blue),
                    Hint(text="OR", status=False, display_color=Colors.blue),

                )
            ],
            code_blocks = [
                CodeBlock("WHERE", Colors.blue)
            ]
        )
    )

    def get_skip_letters(line_index):
        return sum(map(lambda block: len(block.text), sql_code.code_lines[line_index].code_blocks))
    
    def todo(last_line_index, hint):
        hint_menu_statuses.append(hint)
        #sql_code.code_lines[last_line_index].code_blocks.insert(len(sql_code.code_lines[last_line_index].code_blocks) - 2, CodeBlock(hint.text, hint.display_color))
        sql_code.code_lines[last_line_index].code_blocks.append(CodeBlock(hint.text, hint.display_color))


define session_index = 0
define hint_menu_index = 0

define hint_menu_statuses = []
define code_blocks_copy = None

define start_x_pos = 560
define start_y_pos = 243

$ start_x_pos += 200

define font_size = 25
define letter_width = 15
define letter_height = 30
define button_height = 32




image bg_vs = "images/SQL/bg_screen.png"


label start_game_sql:
    
    scene bg_vs

    python:
        global hint_menu_statuses
        for line_index in range(len(sql_code.code_lines)):
            while True:
                hint_menu_statuses = []
                code_blocks_copy = sql_code.code_lines[line_index].code_blocks.copy()
                for hint_menu in sql_code.code_lines[line_index].hint_menus:
                    renpy.show_screen("CodeDisplay", line_index)
                    renpy.call_screen("HintDisplay", line_index, hint_menu)
                    renpy.hide_screen("CodeDisplay")
                
                renpy.show_screen("CodeDisplay", line_index)

                for hint_index, hint in enumerate(hint_menu_statuses):
                    if not hint.status:
                        if hint.comment is not None:
                            renpy.say(who=None, what=hint.comment)
                        else:
                            renpy.say(who=None, what="Что-то тут не так...")
                        sql_code.code_lines[line_index].code_blocks = code_blocks_copy
                        hint_menu_statuses = []
                        renpy.hide_screen("CodeDisplay")
                        break
                else:
                    if hint.comment is not None:
                        renpy.say(who=None, what=hint.comment)
                    else:
                        renpy.say(who=None, what="Вроде все правильно...")
                    renpy.hide_screen("CodeDisplay")

                    break
    "qweqwewe!"
    return



screen CodeDisplay(last_line_index):
    for line_index in range(last_line_index + 1):
        $ skip_letters = 0
        for code_block in sql_code.code_lines[line_index].code_blocks:
            $ new_xpos = start_x_pos + letter_width * skip_letters
            $ new_ypos = start_y_pos + button_height * line_index
            add Text(code_block.text, color=code_block.color, xpos=new_xpos, ypos=new_ypos, size=font_size, font="FiraCode-Light.ttf")
            $ skip_letters += len(code_block.text) + 1



screen HintDisplay(last_line_index, hint_menu):
    $ skip_letters = get_skip_letters(last_line_index)
    for hint_index, hint in enumerate(hint_menu.hints):
        $ new_xpos = start_x_pos + letter_width * skip_letters
        $ new_ypos = start_y_pos + letter_height * (last_line_index + 1) + button_height * hint_index
        imagebutton:
            xpos start_x_pos + letter_width * skip_letters
            ypos new_ypos
            idle hint.idle_sprite
            hover hint.hover_sprite

            action [Function(todo, last_line_index, hint), Return(), Hide("HintDisplay")]
            
    
        add Text(hint.text, color=hint.color, xpos=new_xpos, ypos=new_ypos)
