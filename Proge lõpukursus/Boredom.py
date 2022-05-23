class Monster:
    def __init__(self, hp, ad, ap, dex, defence, luck):
        self.hp = hp
        self.ad = ad
        self.ap = ap
        self.dex = dex
        self.defence = defence
        self.luck = luck

    def attack(self, ad, luck, enemy_defence):
        

