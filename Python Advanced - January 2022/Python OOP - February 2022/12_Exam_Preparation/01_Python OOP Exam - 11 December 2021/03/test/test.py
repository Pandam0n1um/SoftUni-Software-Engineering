from unittest import TestCase, main

from project.team import Team


class TeamTest(TestCase):

    def setUp(self) -> None:
        self.team = Team('Scarpa')
        self.team.members = {'Ondra': 29, 'Janja': 22}

    def test_init_correct_data(self):
        team = Team('Scarpa')
        self.assertEqual('Scarpa', team.name)
        self.assertEqual({}, team.members)

    def test_name_setter_with_non_alpha_chars_raises(self):
        with self.assertRaises(ValueError) as ex:
            team = Team('Scarpa_1999')
        self.assertEqual('Team Name can contain only letters!', str(ex.exception))

    def test_add_member_only_non_existing(self):
        new_non_existing_members = {'Midtbo': 33, 'Hoseok': 29}
        result = self.team.add_member(**new_non_existing_members)
        self.assertEqual('Successfully added: Midtbo, Hoseok', result)

    def test_add_member_some_existing(self):
        new_non_existing_members = {'Midtbo': 33, 'Ondra': 35}
        result = self.team.add_member(**new_non_existing_members)
        self.assertEqual('Successfully added: Midtbo', result)
        self.assertEqual(29, self.team.members['Ondra'])

    def test_remove_member_existing(self):
        climber_to_remove = 'Janja'
        result = self.team.remove_member(climber_to_remove)
        self.assertEqual(f'Member {climber_to_remove} removed', result)
        self.assertFalse(climber_to_remove in self.team.members)

    def test_remove_member_not_existing(self):
        climber_to_remove = 'Ghisolfi'
        self.assertFalse(climber_to_remove in self.team.members)
        result = self.team.remove_member(climber_to_remove)
        self.assertEqual(f"Member with name {climber_to_remove} does not exist", result)

    def test_gt_dunder(self):
        other_team = Team('LaSportiva')
        result = self.team > other_team
        self.assertEqual(True, result)

    def test_gt_dunder_return_false(self):
        other_team = Team('LaSportiva')
        other_climbers = {'Honnold': 36, 'Ghisolfi': 29, 'Noguchi': 33}
        other_team.members = other_climbers
        result = self.team > other_team
        self.assertEqual(False, result)

    def test_len_dunder(self):
        result = len(self.team)
        self.assertEqual(2, result)
        self.team.remove_member('Janja')
        result = len(self.team)
        self.assertEqual(1, result)

    def test_add_dunder(self):
        other_team = Team('LaSportiva')
        other_climbers = {'Honnold': 36, }
        other_team.members = other_climbers
        new_team = self.team + other_team

        self.assertEqual('ScarpaLaSportiva', new_team.name)
        self.assertEqual({'Ondra': 29, 'Janja': 22, 'Honnold': 36, }, new_team.members)

    def test_str_dunder(self):
        team_name = 'LaSportiva'
        team = Team(team_name)
        climbers = {'Ondra': 29, 'Ghisolfi': 29, 'Honnold': 36, }
        team.members = climbers

        expected = f"Team name: {team_name}" \
                   + "\nMember: Honnold - 36-years old" \
                   + "\nMember: Ghisolfi - 29-years old" \
                   + "\nMember: Ondra - 29-years old"

        result = str(team)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
