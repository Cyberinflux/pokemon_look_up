import requests

def fetch_kanto_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=151'
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        for pokemon in pokemon_data['results']:
            fetch_pokemon_details(pokemon['url'])
    else:
        print(f"Failed to retrieve data: {response.status_code}")

def fetch_pokemon_details(pokemon_url):
    response = requests.get(pokemon_url)

    if response.status_code == 200:
        poke_data = response.json()
        name = poke_data['name']
        poke_id = poke_data['id']
        types = [type_info['type']['name'] for type_info in poke_data['types']]
        print(f"ID: {poke_id}, Name: {name}, Types: {', '.join(types)}")
    else:
        print(f"Failed to retrieve Pokémon details: {response.status_code}")

if __name__ == "__main__":
    fetch_kanto_pokemon()