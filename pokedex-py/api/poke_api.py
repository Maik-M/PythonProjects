import requests


class PokeApi:
    def __init__(self):
        """Classe que recebe os vbalores da PokeApi"""
        self.api_site = ''

        # Listas
        self.pokemon = None
        self.abilities_list = []
        self.type_list = []
        self.stats_list = []
        self.height = ''
        self.poke_id = ''
        self.sprite = ''
        self.weight = ''

    def api_values(self, pokemon):
        """Recebe o nome do pokémon concatena ao site e devolve um json"""
        self.pokemon = str(pokemon).replace(' ', '')
        self.api_site = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon}'
        res = requests.get(self.api_site)
        return res.json()

    def get_values(self, pokemon):
        """Resgata os valores do Pokémon"""
        values = self.api_values(pokemon)
        self.abilities_list = [ability['ability']['name'].title() for ability in values['abilities']]  # Lista de Skills
        self.type_list = [type_p['type']['name'] for type_p in values['types']]  # Lista de tipos
        self.stats_list = [stats for stats in values['stats']]
        self.height = float(int(values['height']) / 10)  # Altura
        self.weight = float(int(values['weight']) / 10)  # Peso
        self.poke_id = values['id']  # ID
        self.sprite = values['sprites']['front_default']  # Imagem do Sprite

    def get_sprite_image(self):
        """Resgata a imagem do Sprite do Pokémon"""
        response = requests.get(self.sprite, stream=True)
        response.raw.decode_content = True
        return response.raw.read()
