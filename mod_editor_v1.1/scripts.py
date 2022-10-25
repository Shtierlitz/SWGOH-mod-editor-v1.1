from PIL import Image, ImageDraw


def parent_type():
    mod_parent = int(input("Семейство модуля\n"
                           "здоровье - 1\n"
                           "защита   - 2\n"
                           "крит.у   - 3\n"
                           "крит.ш   - 4\n"
                           "устой.   - 5\n"
                           "атака    - 6\n"
                           "эффект.  - 7\n"
                           "скорость - 8:\n"))

    if not 1 <= mod_parent <= 8:
        mod_parent = int(input("Семейство модуля\n"
                               "здоровье - 1\n"
                               "защита   - 2\n"
                               "крит.у   - 3\n"
                               "крит.ш   - 4\n"
                               "устой.   - 5\n"
                               "атака    - 6\n"
                               "эффект.  - 7\n"
                               "скорость - 8:\n"))
    print()
    return mod_parent


def mode_type():
    mod_type = int(input("Тип модуля\n"
                         "квадрат - 1\n"
                         "стрелка - 2\n"
                         "ромб    - 3\n"
                         "триугол.- 4\n"
                         "круг    - 5\n"
                         "крест   - 6:\n"))
    if not 1 <= mod_type <= 6:
        mod_type = int(input("Тип модуля\n"
                             "квадрат - 1\n"
                             "стрелка - 2\n"
                             "ромб    - 3\n"
                             "триугол.- 4\n"
                             "круг    - 5\n"
                             "крест   - 6:\n"))
    print()
    return mod_type


def create_path(mod, parent):
    dir_path = None
    file_name = None

    if parent == 1:
        dir_path = "Mods/health"
    elif parent == 2:
        dir_path = "Mods/deffence"
    elif parent == 3:
        dir_path = "Mods/crit_damage"
    elif parent == 4:
        dir_path = "Mods/crit_chance"
    elif parent == 5:
        dir_path = "Mods/tenasity"
    elif parent == 6:
        dir_path = "Mods/attack"
    elif parent == 7:
        dir_path = "Mods/potency"
    elif parent == 8:
        dir_path = "Mods/speed"

    if mod == 1:
        file_name = "/square.png"
    elif mod == 2:
        file_name = "/arrow.png"
    elif mod == 3:
        file_name = "/rhom.png"
    elif mod == 4:
        file_name = "/tria.png"
    elif mod == 5:
        file_name = "/circle.png"
    elif mod == 6:
        file_name = "/cross.png"
    return dir_path + file_name


def dops():
    dop1 = input("Основа: ")
    dop2 = input("Допы 2: ")
    if dop2 == 0:
        dop2 = 'None'
    dop3 = input("Допы 3: ")
    if dop3 == 0:
        dop3 = 'None'
    print()
    return dop1 + "\n" + "Допы 1: " + dop2 + "\n" + "Допы 2: " + dop3 + "\n"


def main_programm(name, count, font, p1=None, p2=None, p3=None, p4=None, p5=None, p6=None, d1=None, d2=None, d3=None, d4=None,
         d5=None, d6=None):

    # отступы
    img_size = 128
    upper_space = 40

    # фон
    img = Image.new('RGBA', (500, (img_size * 6) + 20), color=('#fff'))

    # Название персонаэа
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img_size + upper_space, 0),
        name,
        font=font,
        fill='#000')

    # Условия модулей
    if count == 1:
        img1 = Image.open(p1)
        img.paste(img1, (0, 10))
        draw_text.text(
            (img_size + 20, 10 + upper_space),
            d1,
            font=font,
            fill='#000')
    elif count == 2:
        img1 = Image.open(p1)
        img.paste(img1, (0, 10))
        draw_text.text(
            (img_size + 20, 10 + upper_space),
            d1,
            font=font,
            fill='#000')
        img2 = Image.open(p2)
        img.paste(img2, (0, img_size + 10))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size),
            d2,
            font=font,
            fill='#000')
    elif count == 3:
        img1 = Image.open(p1)
        img.paste(img1, (0, 10))
        draw_text.text(
            (img_size + 20, 10 + upper_space),
            d1,
            font=font,
            fill='#000')
        img2 = Image.open(p2)
        img.paste(img2, (0, img_size + 10))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size),
            d2,
            font=font,
            fill='#000')
        img3 = Image.open(p3)
        img.paste(img3, (0, (img_size + 10) + img_size))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size * 2),
            d3,
            font=font,
            fill='#000')
    elif count == 4:
        img1 = Image.open(p1)
        img.paste(img1, (0, 10))
        draw_text.text(
            (img_size + 20, 10 + upper_space),
            d1,
            font=font,
            fill='#000')
        img2 = Image.open(p2)
        img.paste(img2, (0, img_size + 10))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size),
            d2,
            font=font,
            fill='#000')
        img3 = Image.open(p3)
        img.paste(img3, (0, (img_size + 10) + img_size))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size * 2),
            d3,
            font=font,
            fill='#000')
        img4 = Image.open(p4)
        img.paste(img4, (0, (img_size + 10) + img_size * 2))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size * 3),
            d4,
            font=font,
            fill='#000')
    elif count == 5:
        img1 = Image.open(p1)
        img.paste(img1, (0, 10))
        draw_text.text(
            (img_size + 20, 10 + upper_space),
            d1,
            font=font,
            fill='#000')
        img2 = Image.open(p2)
        img.paste(img2, (0, img_size + 10))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size),
            d2,
            font=font,
            fill='#000')
        img3 = Image.open(p3)
        img.paste(img3, (0, (img_size + 10) + img_size))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size * 2),
            d3,
            font=font,
            fill='#000')
        img4 = Image.open(p4)
        img.paste(img4, (0, (img_size + 10) + img_size * 2))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size * 3),
            d4,
            font=font,
            fill='#000')
        img5 = Image.open(p5)
        img.paste(img5, (0, (img_size + 10) + img_size * 3))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size * 4),
            d5,
            font=font,
            fill='#000')
    elif count == 6:
        img1 = Image.open(p1)
        img.paste(img1, (0, 10))
        draw_text.text(
            (img_size + 20, 10 + upper_space),
            d1,
            font=font,
            fill='#000')
        img2 = Image.open(p2)
        img.paste(img2, (0, img_size + 10))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size),
            d2,
            font=font,
            fill='#000')
        img3 = Image.open(p3)
        img.paste(img3, (0, (img_size + 10) + img_size))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size * 2),
            d3,
            font=font,
            fill='#000')
        img4 = Image.open(p4)
        img.paste(img4, (0, (img_size + 10) + img_size * 2))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size * 3),
            d4,
            font=font,
            fill='#000')
        img5 = Image.open(p5)
        img.paste(img5, (0, (img_size + 10) + img_size * 3))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size * 4),
            d5,
            font=font,
            fill='#000')
        img6 = Image.open(p6)
        img.paste(img6, (0, (img_size + 10) + img_size * 4))
        draw_text.text(
            (img_size + 20, 10 + upper_space + img_size * 5),
            d6,
            font=font,
            fill='#000')

    img.show()
    return
