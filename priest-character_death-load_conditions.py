class Priest(Character):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.last_healing = datetime.datetime.now() - datetime.timedelta(minutes=2)


    def take_damage(self, enemy) -> int:
        Printer.info(enemy.name + " senses the holiness of " + self.name + " and chooses not to attack!")
        return 0

    def heal(self, target) -> Optional[int]:
        if datetime.datetime.now() - self.last_healing < datetime.timedelta(minutes = 2):
            Printer.alert(self.name + " hasn't recovered from the last healing!")
            return None
        self.last_healing = datetime.datetime.now()
        amt = random.randint(0, 25)
        target.health += amt
        return amt
        

@staticmethod
def load_conditions() -> None:
    with open('./item_attributes', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            Item.CONDITIONS.append(row)
            
class CharacterDeathException(Exception):
    def __init__(self, st, character) -> None:
        super().__init__(st)
        self.character = character