from PIL import Image, ImageDraw


def parent_type() -> int:
    """Returns number of module family"""
    famyly = "Семейство модуля (только числа):\n"
    "здоровье - 1\n"
    "защита   - 2\n"
    "крит.у   - 3\n"
    "крит.ш   - 4\n"
    "устой.   - 5\n"
    "атака    - 6\n"
    "эффект.  - 7\n"
    "скорость - 8:\n"

    try:
        mod_parent = int(input(famyly))
        return mod_parent
    except:
        print("Должны быть только целые числа от 1 до 8")
        return parent_type()


def mode_type() -> int:
    """Returns number of module type"""
    m_type = "Тип модуля\n"
    "квадрат - 1\n"
    "стрелка - 2\n"
    "ромб    - 3\n"
    "триугол.- 4\n"
    "круг    - 5\n"
    "крест   - 6:\n"
    try:
        mod_type = int(input(m_type))
        return mod_type
    except:
        print("Должны быть только целые числа от 1 до 8")
        return mode_type()


def create_path(mod: int, parent: int) -> str:
    """Creates path to correct module image"""
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


def dops() -> str:
    """Creates 3 strings for additional module abilities"""
    dop1 = input("Основа: ")
    dop2 = input("Допы 2: ")
    if dop2 == 0:
        dop2 = 'None'
    dop3 = input("Допы 3: ")
    if dop3 == 0:
        dop3 = 'None'
    print()
    return dop1 + "\n" + "Допы 1: " + dop2 + "\n" + "Допы 2: " + dop3 + "\n"


def main_program(name: str, count: int, font, p1: str = None, p2: str = None, p3: str = None, p4: str = None,
                  p5: str = None, p6: str = None, d1: str = None, d2: str = None, d3: str = None,
                  d4: str = None,
                  d5: str = None, d6: str = None) -> None:
    """Collects all the data and shows the finished picture."""
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
