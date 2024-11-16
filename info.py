def about_me():
    character_description = {"имя": "Шрек",
                             "возраст": "30",
                             "место жительства": "болото, в окрестностях государства Дюлок",
                             "общее описание": "огромный и милый зелёный огр."}
    strings = []
    for key, item in character_description.items():
        strings.append("{}: {}".format(key.capitalize(), item))
    result = ".\n".join(strings)
    return result


def family_me():
    character_family = {"жена": "Принцесса Фиона",
                        "дети": "Фаркл, Фергус и Фелиция"}
    strings = []
    for key, item in character_family.items():
        strings.append("{}: {}".format(key.capitalize(), item))
    result = ".\n".join(strings)
    return result


def hobby_me():
    character_hobby = {"*": "Ну что, вот мои любимые дела и каждодневная рутина*",
                       "1.": "Защищаю свой дом, я очень люблю своё болото и делаю все возможное, чтобы сохранить его "
                            "в безопасности",
                       "2.": "Провожу время со своими друзьями",
                       "3.": "Быть одному, я предпочитаю уединение и спокойствие, поэтому я часто ухожу от своих "
                            "друзей, чтобы отдохнуть и поразмыслить",
                       "4.": "Люблю свою семью, я глубоко привязан к своим огрятам",
                       "**": "ну вот и собственно всё!**"}
    strings = []
    for key, item in character_hobby.items():
        strings.append("{} {}".format(key.capitalize(), item))
    result = ".\n".join(strings)
    return result

def friends_me():
    character_friends = {"": "У меня есть один лучший друг, который всегда со мной!!",
                         "Осёл": "Лучший друг и мой помощник, муж Драконихи.",
                         "Он часто меня раздражает, но несмотря на это мы все равно всегда вместе.": ""}
    strings = []
    for key, item in character_friends.items():
        strings.append("{} {}".format(key.capitalize(), item))
    result = "\n".join(strings)
    return result


def foods_me():
    character_foods = {"1.": "Поросенок с яблоками. Я люблю жареного поросенка с яблоками в качестве основного блюда.",
                       "2.": "Пирог с мясом. Я обожаю пирог с мясом, особенно если он хорошо приправлен и сочный.",
                       "3.": "Жареная курочка."}
    strings = []
    for key, item in character_foods.items():
        strings.append("{} {}".format(key.capitalize(), item))
    result = "\n".join(strings)
    return result