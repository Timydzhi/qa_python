import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_new_book_has_empty_genre(self, collector):

        collector.add_new_book('Властелин колец')

        assert collector.get_book_genre('Властелин колец') == ''


    def test_set_book_genre_valid_genre_book_has_genre(self, collector):

        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')

        assert collector.get_book_genre('Властелин колец') == 'Фантастика'


    def test_get_book_genre_unknown_book_returns_none(self, collector):

        assert collector.get_book_genre('Властелин колец') is None


    @pytest.mark.parametrize(
        'genre, expected_books',
        [
            ['Фантастика', ['Властелин колец']],
            ['Детективы', ['Шерлок Холмс']]
        ]
    )
    def test_get_books_with_specific_genre_valid_genre_returns_books(self, genre, expected_books, collector):

        collector.add_new_book('Властелин колец')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_genre_books_returns_dictionary(self, collector):

        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')

        assert collector.get_books_genre() == {
            'Властелин колец': 'Фантастика'
        }

    def test_get_books_for_children_books_without_age_rating_returns(self, collector):

        collector.add_new_book('Властелин колец')
        collector.add_new_book('Оно')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_for_children() == ['Властелин колец']

    def test_add_book_in_favorites_added_book_is_in_favorites(self, collector):

        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')

        assert 'Властелин колец' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_added_book_is_deleted(self, collector):

        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')

        assert 'Властелин колец' not in collector.get_list_of_favorites_books()
