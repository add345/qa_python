from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #name = [
      #  'Лев Толстой «Война и мир», Pоман',
      #  'Уильям Фолкнер «Звук и ярость», Роман',
      #  'Джейн Остен «Гордость и предубеждение», Роман',
       # 'Габриель Гарсиа Маркес «Сто лет одиночества», Роман',
        #'Джон Толкин «Властелин колец», Фантастика'
   # ]

    @pytest.mark.parametrize(
        'name',
       [
          'Лев Толстой «Война и мир»',
          'Джон Толкин «Властелин колец»',
          'Николай Васильевич Гоголь «Ревизо́р»'
       ]
)
    def test_add_new_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
            'name',
            [
                'Фэнни Флэгг «Жареные зеленые помидоры в кафе "Полустанок"»',
                'Мэри Энн Шеффер, Энни Бэрроуз «Клуб любителей книг и пирогов из картофельных очистков Мэри Энн Шеффер, Энни Бэрроуз»'
                'Сельма Лагерлёф «Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции Сельма Лагерлёф»'
            ]
)
    def test_negative_add_new_book(self, name):
            collector = BooksCollector()
            collector.add_new_book(name)
            assert len(collector.get_books_genre()) == 0

    def test_negative1_add_new_book(self):
        name = 'Николай Васильевич Гоголь «Ревизо́р»'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
            'name,genre',
            [
                ['Имя', 'Детективы'],
                ['Имя2', 'Мультфильмы']
            ]
    )
    def test_set_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    @pytest.mark.parametrize(
            'name,genre',
            [
                ['Имя', 'Роман']
            ]
    )
    def test_negative_set_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == ''

    @pytest.mark.parametrize(
            'name,genre',
            [
                ['Джон Толкин «Властелин колец»', 'Фантастика']
            ]
    )
    def test_get_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.books_genre[name] = genre
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'name, name2,genre',
        [
            ['Книга1', 'Книга2', 'Роман']
        ]
    )
    def test_get_books_with_specific_genre(self, name, name2, genre):
        collector = BooksCollector()
        collector.genre.append(genre)
        collector.books_genre[name] = genre
        collector.books_genre[name2] = genre
        assert len(collector.get_books_with_specific_genre(genre)) == 2

    def test_get_books_with_specific_genre_2(self):
            collector = BooksCollector()

            collector.books_genre = {
                'Головоломка': 'Мультфильмы',
                'Оно': 'Ужасы',
                'Гарри Поттер': 'Фантастика',
                'Мумий Тролль': 'Мультфильмы'
            }
            assert len(collector.get_books_with_specific_genre('Мультфильмы')) == 2

    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.books_genre = {
            'Головоломка': 'Мультфильмы',
            'Оно': 'Ужасы',
            'Гарри Поттер': 'Фантастика',
            'Мумий Тролль': 'Мультфильмы'
        }
        assert collector.get_books_genre() == collector.books_genre
