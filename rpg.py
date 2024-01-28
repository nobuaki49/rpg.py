import random

class Slime:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power
    
    def attack(self, hero):
        damage = random.randint(1, self.power)
        hero.hp -= damage
        print("スライムが", damage, "のダメージを与えた！")
        
class Hero:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power
    
    def attack(self, slime):
        damage = random.randint(1, self.power)
        slime.hp -= damage
        print("勇者が", damage, "のダメージを与えた！")
        
slime = Slime(10, 3)
hero = Hero(10, 2)

while slime.hp > 0 and hero.hp > 0:
    hero.attack(slime)
    if slime.hp <= 0:
        print("スライムを倒した！")
        break
    slime.attack(hero)
    if hero.hp <= 0:
        print("勇者は倒れた...")

