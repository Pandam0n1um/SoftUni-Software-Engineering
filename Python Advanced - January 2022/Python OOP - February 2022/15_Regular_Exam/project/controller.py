from project.common.validators import Validator
from project.player import Player


class Controller:
    VALID_SUSTENCANCE = ['Food', 'Drink']

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        added = []
        for player in args:
            if not player in self.players:
                self.players.append(player)
                added.append(player.name)
        return f"Successfully added: {', '.join(added)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if not sustenance_type in Controller.VALID_SUSTENCANCE:
            return
        supply, index = self.__get_last_supply_type(sustenance_type)
        player: Player = self.__get_player_by_name(player_name)
        if player is None:
            return
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy
        self.supplies.pop(index)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):

        result = ''

        player_one: Player = self.__get_player_by_name(first_player_name)
        player_two: Player = self.__get_player_by_name(second_player_name)
        winner: Player = player_one
        if player_one.stamina == 0:
            result += f"Player {player_one.name} does not have enough stamina."
        if player_two.stamina == 0:
            result += f"\nPlayer {player_two.name} does not have enough stamina."
        if result:
            return result
        if player_one > player_two:
            winner = self.__fight(player_two, player_one)
        else:
            winner=self.__fight(player_one, player_two)
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            try:
                player.stamina -= player.age * 2
            except ValueError:
                player.stamina = 0
        for player in self.players:
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = '\n'.join([str(player) for player in self.players])
        result += '\n'
        result += '\n'.join([supply.details() for supply in self.supplies])
        return result

    def __get_last_supply_type(self, type):
        #  for supply in self.supplies[::-1]:
        #      if supply.__class__.__name__ == type:
        #          needed_supply = supply
        #          self.
        #          return needed_supply
        #
        # Validator.raises_if_no_supply_left(type)
        needed_supply = None
        index = 0
        for i, supply in enumerate(self.supplies):
            if supply.__class__.__name__ == type:
                needed_supply = supply
                index = i
        if needed_supply == None:
            Validator.raises_if_no_supply_left(type)
        return needed_supply, index

    def __get_player_by_name(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def __fight(self, first_attacker, second_attacker):
        winner = first_attacker
        first_attacker_damage = first_attacker.stamina / 2


        try:
            second_attacker.stamina -= first_attacker_damage
        except ValueError:
            second_attacker.stamina = 0
            return winner
        second_attacker_damage = second_attacker.stamina / 2
        try:
            first_attacker.stamina -= second_attacker_damage
        except ValueError:
            first_attacker.stamina = 0
            winner = second_attacker
            return winner
        winner = first_attacker if second_attacker < first_attacker else second_attacker
        return winner
