from unittest import TestCase, main

from project.movie import Movie


class MovieTest(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('StarWars', 1977, 9.7)

    def test_valid_init(self):
        self.assertEqual('StarWars', self.movie.name)
        self.assertEqual(1977, self.movie.year)
        self.assertEqual(9.7, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_init_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            movie = Movie('', 1977, 9.7)
        self.assertEqual('Name cannot be an empty string!', str(ex.exception))

    def test_init_invalid_year_raises(self):
        with self.assertRaises(ValueError) as ex:
            movie = Movie('StarWars', 977, 9.7)
        self.assertEqual('Year is not valid!', str(ex.exception))

    def test_add_actor_valid_scenario(self):
        self.movie.actors = ['Mark Hamill']
        new_actor = 'Harrison Ford'
        self.movie.add_actor(new_actor)
        self.assertEqual(['Mark Hamill', 'Harrison Ford'], self.movie.actors)

    def test_add_actor_existing_raises(self):
        self.movie.actors = ['Mark Hamill']
        new_actor = 'Mark Hamill'
        result = self.movie.add_actor(new_actor)
        self.assertEqual(f"{new_actor} is already added in the list of actors!", result)

    def test_dunder_gt_rating_comparison_movie_higher(self):
        self.other_movie = Movie('Lord of the Rings', 2001, 9.3)
        result = self.movie > self.other_movie
        self.assertEqual(f'"{self.movie.name}" is better than "{self.other_movie.name}"', result)

    def test_dunder_gt_rating_comparison_other_movie_higher(self):
        self.other_movie = Movie('Lord of the Rings', 2001, 9.9)
        result = self.movie > self.other_movie
        self.assertEqual(f'"{self.other_movie.name}" is better than "{self.movie.name}"', result)

    def test_dunder_repr(self):
        self.movie.actors = ['Fischer','Hamill']
        expected = f"Name: StarWars\nYear of Release: 1977\nRating: 9.70\nCast: Fischer, Hamill"
        result = str(self.movie)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
