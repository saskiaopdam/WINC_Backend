# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line


class Player:
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

        for i in [speed, endurance, accuracy]:
            if i > 1 or i < 0:
                raise ValueError("Should be a number between 0 and 1")

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        speed = self.speed
        endurance = self.endurance
        accuracy = self.accuracy
        values = [speed, endurance, accuracy]

        if speed == max(values) or values.count(speed) > 1:
            return "speed", self.speed
        if endurance == max(values) or values.count(endurance) > 1:
            return "endurance", self.endurance
        if accuracy == max(values) or values.count(accuracy) > 1:
            return "accuracy", self.accuracy


bob = Player('Super Bob', 0.3, 0.1, 0.3)
player1 = Player('Mega Bob', 0.7, 0.8, 0.4)
player2 = Player('Top Bob', 0.7, 0.5, 0.9)
print(bob.introduce())
print(bob.strength())


class Commentator:
    player = Player('Super Bob', 0.3, 0.1, 0.3)

    speed = getattr(player, 'speed')
    endurance = getattr(player, 'endurance')
    accuracy = getattr(player, 'accuracy')

    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        return player.speed + player.endurance + player.accuracy

    def compare_players(self, player1, player2, speed):
        name1 = player1.name
        name2 = player2.name
        speed1 = getattr(player1, speed)
        speed2 = getattr(player2, speed)
        strength1 = player1.strength()
        strength2 = player2.strength()
        total1 = self.sum_player(player1)
        total2 = self.sum_player(player2)

        # if speed1 > speed2:
        #     return name1
        # if speed2 > speed1:
        #     return name2
        # if speed1 == speed2:
        #     if strength1 > strength2:
        #         return name1
        #     if strength2 > strength1:
        #         return name2
        #     if strength1 == strength2:
        #         if total1 > total2:
        #             return name1
        #         if total2 > total1:
        #             return name2
        #         if total1 == total2:
        #             return "These two players might as well be twins!"

        # case 1 speed
        if speed1 > speed2:
            return name1
        elif speed2 > speed1:
            return name2

        # case 2 strength
        if strength1 > strength2:
            return name1
        elif strength2 > strength1:
            return name2

        # case 3 sum_player
        if total1 > total2:
            return name1
        elif total2 > total1:
            return name2
        else:
            return "These two players might as well be twins!"


ray = Commentator('Ray Hudson')
print(ray.name)
print(ray.sum_player(bob))
print(ray.compare_players(player1, player2, 'speed'))
