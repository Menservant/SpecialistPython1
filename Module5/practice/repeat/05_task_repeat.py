# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.
import math


def pagination(num_items, items_on_page):
    last_page = num_items % items_on_page
    return last_page



