class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------------------------------------------------
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_w = Runner('Name_w')             #создаем объект класса Runner
        for i in range(10):                     #вызываем метод 10 раз
            runner_w.walk()
        self.assertEqual(runner_w.distance, 50)       #сравнение distance с ожидаемым значением

    def test_run(self):
        runner_r = Runner('Name_r')
        for i in range(10):
            runner_r.run()
        self.assertEqual(runner_r.distance, 100)

    def test_challenge(self):
        run_chal1 = Runner('Name_ch1')
        run_chal2 = Runner('Name_ch2')
        for i in range(10):
            run_chal1.run()
            run_chal2.walk()
        self.assertNotEqual(run_chal1.distance, run_chal2.distance)

if __name__ == '__main__':
    unittest.main()









