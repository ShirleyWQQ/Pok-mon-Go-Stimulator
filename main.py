class Pokemon_card:
  def __init__(self, name, level, current_exp, pok_type, max_health, health, knocked_out = False):
    self.name = name
    self.level = level
    self.current_exp = current_exp
    self.pok_type = pok_type
    self.max_health = max_health
    self.health = health
    self.knocked_out = knocked_out

  def basic_stats(self):
    if self.knocked_out == False:
      print("{name} is now level {num1} and its type is {type1}. It's current HP is {num2}.")
  
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
    if self.pok_type == "Water":
      if opponent.pok_type == "Fire":
        damage = 2 * self.level
      elif opponent.pok_type == "Water" or opponent.pok_type == "Grass":
        damage = 0.5 * self.level
      elif opponent.pok_type == "Electric" or opponent.pok_type == "Ice":
        damage = self.level
    elif self.pok_type == "Fire":
      if opponent.pok_type == "Fire" or opponent.pok_type == "Water":
        damage = 0.5 * self.level
      elif opponent.pok_type == "Grass" or opponent.pok_type == "Ice":
        damage = 2 * self.level
      elif opponent.pok_type == "Electric":
        damage = self.level
    elif self.pok_type == "Electric":
      if opponent.pok_type == "Electric" or opponent.pok_type == "Grass":
        damage = 0.5 * self.level
      elif opponent.pok_type == "Water":
        damage = 2 * self.level
      elif opponent.pok_type == "Fire" or opponent.pok_type == "Ice":
        damage = self.level
    elif self.pok_type == "Grass":
      if opponent.pok_type == "Fire" or opponent.pok_type == "Grass":
        damage = 0.5 * self.level
      elif opponent.pok_type == "Water":
        damage = 2 * self.level
      elif opponent.pok_type == "Electric" or opponent.pok_type == "Ice":
        damage = self.level
    elif self.pok_type == "Ice":
      if opponent.pok_type == "Fire" or opponent.pok_type == "Water" or opponent.pok_type == "Ice":
        damage = 0.5 * self.level
      elif opponent.pok_type == "Grass":
        damage = 2 * self.level
      elif opponent.pok_type == "Electric" or opponent.pok_type == "Ice":
        damage = self.level
    print("Your {name1} caused {num} damage to opponent's {name2}!".format(name1 = self.name, num = damage, name2 = opponent.name))
    opponent.health -= damage

    if opponent.health <= 0:
      opponent.health = 0
      opponent.is_knocked = True
      self.current_exp += 50
      print("The opponent's {name1} has been knocked out by your {name2}. Your {name2} has gained 50 EXP. Congratulations!".format(name1 = opponent.name, name2 = self.name))
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

  def current_info(self):
    print("{name} now has {num} potions left, ".format(name = self.name, num = self.potions) + "and his/her current available pokemon is {name1}.".format(name1 = self.current_pokemon.name))
    print("{name}'s list of available (not knocked out yet) pokemons are: ".format(name = self.name))
    for temp in self.pokemons:
      if temp.knocked_out == False:
        print(temp.name)

  
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
        return
    print("The pokemon that you input is not contained in your list of pokemons. Please enter a pokemon that is in your list!")

  def trainer_attack(self, rival):
    self.current_pokemon.attack(rival.current_pokemon)
    #print("{name1}'s pokemon {name2} has attacked {name3}!".format(name1 = self.name, name2 = self.current_pokemon.name, name3 = rival.current_pokemon.name))

jigg = Pokemon_card("jigglypuff", 2, 0, "Fire", 20, 20)
pikachu = Pokemon_card("pikachu", 3, 0, "Electric", 30, 30)
meowf = Pokemon_card("meowf", 2, 0, "Grass", 29, 29)
spiff = Pokemon_card("spiffamungus", 3, 0, "Ice", 40, 40)
trainer_1 = Trainer([jigg, pikachu, meowf, spiff], 10, pikachu, 'Sam')
trainer_2 = Trainer([jigg, meowf, spiff], 10, jigg, 'Lucy')
trainer_1.current_info()
trainer_2.current_info()
trainer_1.trainer_attack(trainer_2)
trainer_2.trainer_attack(trainer_1)
trainer_1.switch_pokemon(meowf)
trainer_2.switch_pokemon(spiff)

#pikachu.dec_health(29)
#jigg.dec_health(17)
#meowf.dec_health(27.5)
#pikachu.attack(spiff)
#pikachu.attack(jigg)
#pikachu.attack(meowf)

    
  

