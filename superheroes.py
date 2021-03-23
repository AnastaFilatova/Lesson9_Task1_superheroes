import requests


def get_super_intell_Superhero():
    """ Определяет героя с самым высоким интеллектом"""

    superheroes = ['Hulk', 'Captain America', 'Thanos']
    name_list = []
    id_list = []
    for hero in superheroes:
        url = 'https://superheroapi.com/api/2619421814940190/search/' + hero
        response = requests.get(url).json()
        for i in response['results']:
            if i['name'] in superheroes:
                name_list.append(i['name'])
                id_list.append(i['powerstats']['intelligence'])
    intell_dict = dict(zip(name_list, id_list))
    sorted_tuples = sorted(intell_dict.items(), key=lambda item: item[1])
    return f'Самый высокий уровень интеллекта {sorted_tuples[0][1]} у героя по имени {sorted_tuples[0][0]}'


print(get_super_intell_Superhero())
