class Pokemon_card:
  def __init__(self, name, level, current_exp, attribute, max_health, health, knocked_out):
    self.name = name
    self.level = level
    self.current_exp = current_exp
    self.attribute = attribute
    self.max_health = max_health
    self.health = health
    self.knocked_out = knocked_out
  
  def dec_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.knocked_out = True
      print('{name} has been knocked out.'.format(name = self.name))
    else:
      print('{name} has taken {amount1} damage, it now has {amount2} health.'.format(name = self.name, amount1 = amount, amount2 = self.health))

  def restore_full_hp(self):
    if self.knocked_out == False:
      self.health = self.max_health
    else:
      print("This Pokémon has been knocked out! Please use 'revive' instead.")
    
  def revive(self):
    if self.knocked_out == True:
      self.knocked_out = False
      self.health = self.max_health
      print("{name} has been revived! Full HP ({num} points) has been restored.".format(name = self.name, num = self.max_health))

  def gain_health(self, amount):
    if self.knocked_out == True:
      print("This Pokémon has been knocked out! Please use 'revive' instead.")
      return
    self.health += amount
    if self.health > self.max_health:
      self.health = self.max_health
      print("{name}'s HP has been fully restored.".format(name = self.name))
    else:
      print("Successfully gained {num1} HP! {name} now has {num2} HP.".format(num1 = amount, name = self.name, num2 = self.health))
    
# Attack function
  def attack(self, opponent):
    if self.health == 0:
      print("{name} is already being knocked out and can't attack anymore.".format(name = self.name))
      return
    if opponent.health == 0:
      print("{name} is already being knocked out and can't be attacked.".format(name = opponent.name))
      return
    damage = 0
    if self.type == "Water":
      if opponent.type == "Fire":
        damage = 2 * self.level
      elif opponent.type == "Water" or opponent.type == "Grass":
        damage = 0.5 * self.level
      elif opponent.type == "Electric" or opponent.type == "Ice":
        damage = self.level
    elif self.type == "Fire":
      if opponent.type == "Fire" or opponent.type == "Water":
        damage = 0.5 * self.level
      elif opponent.type == "Grass" or opponent.type == "Ice":
        damage = 2 * self.level
      elif opponent.type == "Electric":
        damage = self.level
    elif self.type == "Electric":
      if opponent.type == "Electric" or opponent.type == "Grass":
        damage = 0.5 * self.level
      elif opponent.type == "Water":
        damage = 2 * self.level
      elif opponent.type == "Fire" or opponent.type == "Ice":
        damage = self.level
    elif self.type == "Grass":
      if opponent.type == "Fire" or opponent.type == "Grass":
        damage = 0.5 * self.level
      elif opponent.type == "Water":
        damage = 2 * self.level
      elif opponent.type == "Electric" or opponent.type == "Ice":
        damage = self.level
    elif self.type == "Ice":
      if opponent.type == "Fire" or opponent.type == "Water" or opponent.type == "Ice":
        damage = 0.5 * self.level
      elif opponent.type == "Grass":
        damage = 2 * self.level
      elif opponent.type == "Electric" or opponent.type == "Ice":
        damage = self.level
    print("Your {name1} caused {num} damage to opponent's {name2}!".format(name1 = self.name, num = damage, name2 = opponent.name))
    opponent.health -= damage

    if opponent.health <= 0:
      opponent.health = 0
      opponent.is_knocked = True
      self.current_exp += 50
      print("The opponent's {name1} has been knocked out bu your {name2}. Your {name2} has gained 50 EXP. Congratulations!".format(name1 = opponent.name, name2 = self.name))
    else:
      print("Opponent's {name} now has {num} HP.".format(name = opponent.name, num = opponent.health))
    if self.current_exp >= 100:
      self.level += 1
      self.current_exp -= 100
      print("Your {name} levels up! It is now level {num}.".format(name = self.name, num = self.level))


class Trainer:
  def __init__(self, pokemons, potions, current_pokemon, name):
    self.pokemons = pokemons
    self.potions = potions
    self.current_pokemon = current_pokemon
    self.name = name
  
  def use_potion(self):
    if self.potions == 0:
      print("You have no more potions.")
      return
    self.potions -= 1
    if self.current_pokemon.knocked_out == False:
      self.current_pokemon.health = self.current_pokemon.max_health
      print("The HP of {name1}'s pokemon {name2} has been fully restored.".format(name1 = self.name, name2 = self.current_pokemon.name))
    elif self.current_pokemon.knocked_out == True:
      self.current_pokemon.revive()
      print("{name1}'s pokemon {name2} has been revived.".format(name1 = self.name, name2 = self.current_pokemon.name))
  
  def switch_pokemon(self, new_pokemon):
    if new_pokemon.knocked_out == True:
      print("This pokemon has been knocked out! Please try another.")
    for temp in self.pokemons:
      if temp == new_pokemon:
        self.current_pokemon = new_pokemon
        print("{name1} has successfully switched his/her active pokemon into {name2}.".format(name1 = self.name, name2 = new_pokemon.name))
    
from replit import db

    
  

