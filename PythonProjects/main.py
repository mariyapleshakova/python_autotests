import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '553f626a2b9f1cb95fc270caabe6ef54'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}


body_create = {
    "name": "Kikki",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "151620",
    "name": "Kikki55",
    "photo_id": 2
}

body_add_pokeboll = {
  "message": "Покемон пойман в покебол",
  "id": "151620"
}

'''response_create = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

'''response_add_pokeboll = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeboll)
print (response_add_pokeboll.text)'''