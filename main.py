from functools import reduce


def characters_filter(list_of_characters, key, value):
    return list(filter(lambda item: item[key] == value, list_of_characters))


def team_power(list_of_characters):
    return sum(map(lambda item: item["power"], list_of_characters), 0)


def team_power_2(list_of_characters, advantage):
    return reduce((lambda total,item: total + item["power"]), list_of_characters, advantage)