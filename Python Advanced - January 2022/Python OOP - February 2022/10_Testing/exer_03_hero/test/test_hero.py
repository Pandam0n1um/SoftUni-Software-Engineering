from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):

    def setUp(self):
        self.my_hero = Hero('Yoda', 2, 85.5, 15)
        self.enemy = Hero('Emperor', 3, 25, 7)

    def test_initialization_with_correct_data(self):
        self.assertEqual('Yoda', self.my_hero.username)
        self.assertEqual(2, self.my_hero.level)
        self.assertEqual(85.5, self.my_hero.health)
        self.assertEqual(15, self.my_hero.damage)

    def test_battle_same_instance_raises(self):
        with self.assertRaises(Exception) as ex:
            self.my_hero.battle(self.my_hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle_with_negative_health_raises(self):
        self.my_hero.health = -15
        with self.assertRaises(ValueError) as ex:
            self.my_hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0."
                         " You need to rest",
                         str(ex.exception))

    def test_battle_enemy_with_negative_health_raises(self):
        self.enemy.health = -15
        with self.assertRaises(ValueError) as ex:
            self.my_hero.battle(self.enemy)
        self.assertEqual("You cannot fight Emperor. He needs to rest", str(ex.exception))

    def test_battle_draw_scenario(self):
        self.enemy.damage = 55
        result = self.my_hero.battle(self.enemy)
        self.assertEqual('Draw', result)

    def test_battle_win_scenario(self):
        self.enemy.damage = 3
        result = self.my_hero.battle(self.enemy)
        self.assertEqual('You win', result)
        self.assertEqual(3, self.my_hero.level)
        self.assertEqual(81.5, self.my_hero.health)
        self.assertEqual(20, self.my_hero.damage)

    def test_battle_lose_scenario(self):
        self.my_hero.damage = 1
        self.enemy.damage = 25
        result = self.my_hero.battle(self.enemy)
        self.assertEqual('You lose', result)
        self.assertEqual(4, self.enemy.level)
        self.assertEqual(10.5, self.my_hero.health)
        self.assertEqual(28, self.enemy.health)
        self.assertEqual(30, self.enemy.damage)

    def test_str_dunder(self):
        expected = f"Hero Yoda: 2 lvl\n" \
                   "Health: 85.5\n" \
                   "Damage: 15\n"
        self.assertEqual(expected, str(self.my_hero))


if __name__ == '__main__':
    main()
