import rt_with_exceptions
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            atlet1 = rt_with_exceptions.Runner("Piter", -7)
            for i in range(1, 11):
                atlet1.walk()
                dist = atlet1.distance
            self.assertEqual(dist, 50)
            logging.info(f'test walk выполнен успешно')
        except:
            logging.warning(f'Неверная скорость для Runner')


    def test_run(self):
        try:
            atlet2 = rt_with_exceptions.Runner(2222, 10)
            for i in range(1, 11):
                atlet2.run()
                dist = atlet2.distance
            self.assertEqual(dist, 100)
            logging.info(f'test run выполнен успешно')
        except:
            logging.warning(f'Неверный тип данных для объекта Runner')



if __name__ == '__main__':

    unittest.main()

