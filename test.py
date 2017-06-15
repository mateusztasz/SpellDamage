import unittest
from spell_damage import damage


class TestDamageComputation(unittest.TestCase):

    def test_incorrect_spell_no_fe(self):
        inStr = 'jejeai'
        expected_result = 0
        self.assertEqual(damage(inStr), expected_result)

    def test_incorrect_spell_no_ai(self):
        inStr = 'dadsafeokokok'
        expected_result = 0
        self.assertEqual(damage(inStr), expected_result)

    def test_incorrect_spell_ai_before_fe(self):
        inStr = 'aioooofe'
        expected_result = 0
        self.assertEqual(damage(inStr), expected_result)

    def test_multiple_fe(self):
        inStr = 'fedaifeneai'
        expected_result = 0
        self.assertEqual(damage(inStr), expected_result)

    def test_one(self):
        inStr = 'fedaineai'
        # pomylili sie w instrukcji
        # policzyli 'fe' jako 2, a powinno byc 1
        # dlatego expected_result to 10, a nie 11
        expected_result = 10
        self.assertEqual(damage(inStr), expected_result)

    def test_two(self):
        inStr = 'feeai'
        expected_result = 2
        self.assertEqual(damage(inStr), expected_result)

    def test_three(self):
        inStr = 'feaineain'
        expected_result = 7
        self.assertEqual(damage(inStr), expected_result)

    def test_four(self):
        inStr = 'jee'
        expected_result = 0
        self.assertEqual(damage(inStr), expected_result)

    def test_five(self):
        inStr = 'fdafafeajain'
        expected_result = 1
        self.assertEqual(damage(inStr), expected_result)

    def test_six(self):
        inStr = 'fexxxxxxxxxxai'
        expected_result = 0
        self.assertEqual(damage(inStr), expected_result)

    def test_M_seven(self):
        inStr = 'fejneeeai'
        expected_result = 2
        self.assertEqual(damage(inStr), expected_result)

    def test_M_eight(self):
        inStr = 'fedaidaidaiai'
        expected_result = 18
        self.assertEqual(damage(inStr), expected_result)

if __name__ == '__main__':
    unittest.main()
