from PIL import ImageFont
from scripts import *

font = ImageFont.truetype('YandexSDLight.ttf', size=18)

name = input("Введите имя персонажа: ")
print()

count = int(input("Количество модулей (от 1 до 6): "))
print()

p1, p2, p3, p4, p5, p6 = None, None, None, None, None, None
d1, d2, d3, d4, d5, d6 = None, None, None, None, None, None

if count == 1:
    p1 = create_path(mode_type(), parent_type())
    d1 = dops()
elif count == 2:
    p1 = create_path(mode_type(), parent_type())
    d1 = dops()
    p2 = create_path(mode_type(), parent_type())
    d2 = dops()
elif count == 3:
    p1 = create_path(mode_type(), parent_type())
    d1 = dops()
    p2 = create_path(mode_type(), parent_type())
    d2 = dops()
    p3 = create_path(mode_type(), parent_type())
    d3 = dops()
elif count == 4:
    p1 = create_path(mode_type(), parent_type())
    d1 = dops()
    p2 = create_path(mode_type(), parent_type())
    d2 = dops()
    p3 = create_path(mode_type(), parent_type())
    d3 = dops()
    p4 = create_path(mode_type(), parent_type())
    d4 = dops()
elif count == 5:
    p1 = create_path(mode_type(), parent_type())
    d1 = dops()
    p2 = create_path(mode_type(), parent_type())
    d2 = dops()
    p3 = create_path(mode_type(), parent_type())
    d3 = dops()
    p4 = create_path(mode_type(), parent_type())
    d4 = dops()
    p5 = create_path(mode_type(), parent_type())
    d5 = dops()
elif count == 6:
    p1 = create_path(mode_type(), parent_type())
    d1 = dops()
    p2 = create_path(mode_type(), parent_type())
    d2 = dops()
    p3 = create_path(mode_type(), parent_type())
    d3 = dops()
    p4 = create_path(mode_type(), parent_type())
    d4 = dops()
    p5 = create_path(mode_type(), parent_type())
    d5 = dops()
    p6 = create_path(mode_type(), parent_type())
    d6 = dops()

main_program(name, count, font=font, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5,
              d6=d6)
