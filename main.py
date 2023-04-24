import requests

response = requests.post('https://pokemonbattle.me:9104/pokemons', headers={"trainer_token":"338f0f1f914339cd9207f6b30f457963"}, json={
    "name": "Малышка",
    "photo": "https://dolnikov.ru/pokemons/albums/053.png"
})

print(response.text)

response = requests.put('https://pokemonbattle.me:9104/pokemons', headers={"trainer_token":"338f0f1f914339cd9207f6b30f457963"}, json={
    "pokemon_id": "9535",
    "name": "Лапочка",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})

print(response.text)


response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers={"trainer_token":"338f0f1f914339cd9207f6b30f457963"}, json={
    "pokemon_id": "9535",
})

print(response.text)