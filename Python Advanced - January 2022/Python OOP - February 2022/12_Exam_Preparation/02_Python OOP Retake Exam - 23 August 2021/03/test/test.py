from unittest import TestCase, main

from project.library import Library


class LibraryTest(TestCase):

    def setUp(self) -> None:
        self.my_library = Library('JediArchives')

    def test_init_valid_data(self):
        self.assertEqual('JediArchives', self.my_library.name)
        self.assertEqual('JediArchives', self.my_library._Library__name)
        self.assertEqual({},self.my_library.books_by_authors)
        self.assertEqual({},self.my_library.readers)

    def test_init_invalid_data(self):
        with self.assertRaises(ValueError) as ex:
            my_library = Library('')
        self.assertEqual('Name cannot be empty string!',str(ex.exception))

    def test_add_book_non_existing_author(self):
        author='Messner'
        book='Murdering the impossible'
        self.assertEqual({},self.my_library.books_by_authors)
        self.my_library.add_book(author,book)
        self.assertTrue(author in self.my_library.books_by_authors)
        self.assertTrue(book in self.my_library.books_by_authors[author])

    def test_add_book_existing_author(self):
        author='Messner'
        books=['Murdering the impossible','My life at the limit',]
        new_book='Solo: Nanga Parbat'
        self.assertEqual({},self.my_library.books_by_authors)
        self.my_library.books_by_authors[author]=books
        self.my_library.add_book(author,new_book)
        expected=['Murdering the impossible','My life at the limit','Solo: Nanga Parbat',]
        self.assertEqual(expected,self.my_library.books_by_authors[author])

    def test_add_reader_not_existing(self):
        self.assertEqual({},self.my_library.readers)
        new_reader='Padawan'
        self.my_library.add_reader(new_reader)
        self.assertTrue(new_reader in self.my_library.readers)
        self.assertEqual([],self.my_library.readers[new_reader])

    def test_add_reader_already_existing(self):
        my_library = Library('JediArchives')
        readers={'Padawan':[]}
        my_library.readers=readers
        result=my_library.add_reader('Padawan')
        self.assertEqual("Padawan is already registered in the JediArchives library.",result)

    def test_rent_book_non_existing_user(self):
        reader='Padawan'
        author='Messner'
        book='Murdering the impossible'
        result=self.my_library.rent_book(reader,author,book)
        self.assertEqual('Padawan is not registered in the JediArchives Library.',result)
        self.assertFalse(reader in self.my_library.readers)

    def test_rent_book_existing_user_missing_author(self):
        reader='Padawan'
        author='Messner'
        book='Murdering the impossible'
        self.my_library.readers[reader]=[]
        self.assertTrue(reader in self.my_library.readers)
        result=self.my_library.rent_book(reader,author,book)
        self.assertEqual(f'JediArchives Library does not have any {author}\'s books.',result)

    def test_rent_book_existing_user_and_author_missing_book(self):
        reader='Padawan'
        author='Messner'
        books=['Murdering the impossible','My life at the limit',]
        self.my_library.readers[reader]=[]
        self.my_library.books_by_authors[author]=books
        book_to_rent='Solo: Nanga Parbat'
        result=self.my_library.rent_book(reader,author,book_to_rent)
        expected=f'JediArchives Library does not have {author}\'s "{book_to_rent}".'
        self.assertEqual(expected,result)

    def test_rent_book_existing_book_user_and_book(self):
        reader='Padawan'
        author='Messner'
        books=['Murdering the impossible','My life at the limit',]
        self.my_library.readers[reader]=[]
        self.my_library.books_by_authors[author]=books
        book_to_rent='Murdering the impossible'
        self.my_library.rent_book(reader, author, book_to_rent)

        self.assertEqual([{'Messner':'Murdering the impossible'},],self.my_library.readers[reader])
        self.assertEqual(['My life at the limit',],self.my_library.books_by_authors[author])


if __name__ == '__main__':
    main()
