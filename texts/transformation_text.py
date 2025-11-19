
dell = ["Комплектация", "Справедливая", "От ", "Без пробега",
        "Растаможен", "В кредит", "Максимальная", "Проверенный", "Скидки",
        "В трейд-ин", "-"]


def transform_text(some_text: list[str]) -> list[str]:
    print("принял:", len(some_text))

    filtered_text = [
        item for item in some_text
        if item != "" and not any(item.startswith(word) for word in dell)
    ]
    print("вернул:", len(filtered_text))
    print(filtered_text)
    return filtered_text
