import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results:
            print(res)

    def test_run1(self):
        t1 = Tournament(90, self.r1, self.r3)
        self.all_results = t1.start()
        self.assertTrue(sorted(self.all_results.items())[-1][1] == self.r3.name)

    def test_run2(self):
        t2 = Tournament(90, self.r2, self.r3)
        self.all_results = t2.start()
        self.assertTrue(sorted(self.all_results.items())[-1][1] == self.r3.name)

    def test_run3(self):
        t3 = Tournament(90, self.r1, self.r2, self.r3)
        self.all_results = t3.start()
        self.assertTrue(sorted(self.all_results.items())[-1][1] == self.r3.name)

if __name__ == '__main__':
    unittest.main()