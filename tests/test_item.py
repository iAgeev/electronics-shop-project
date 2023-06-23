"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Товар 1", 10.0, 2)
item2 = Item("Товар 2", 20.0, 4)
item3 = Item("Товар 3", 30.0, 6)


def test_all_instances():
    instances = Item.all
    assert len(instances) == 3
    assert item1 in instances
    assert item2 in instances
    assert item3 in instances


def test_calculate_total_price():
    assert item1.calculate_total_price() == 20.0
    assert item2.calculate_total_price() == 80.0


def test_apply_discount():
    assert item1.price == 10.0  # Проверка, что цена осталась неизменной
    assert item3.price == 30.0  # Проверка, что цена осталась неизменной

    item1.pay_rate = 0.9  # Установить скидку 10%
    item1.apply_discount()
    assert item1.price == 9.0  # Проверка, что цена обновлена с учетом скидки

