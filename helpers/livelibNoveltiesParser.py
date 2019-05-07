# coding=utf-8
from bs4 import BeautifulSoup


def parse(content):
    soup = BeautifulSoup(content, 'lxml')
    books = list()
    for item in soup.find(id="books-novelties").find_all(class_="swiper-slide"):
        book = {'errors': []}
        book['id'] = get_id(item, book)
        book['title'] = get_title(item, book)
        book['author'] = get_author(item, book)
        book['img'] = get_img(item, book)
        book['rating'] = get_rating(item, book)
        books.append(book)
    return books


def get_id(item, book):
    # noinspection PyBroadException
    try:
        url = item.find("img")['data-pagespeed-lazy-src']
        url_array = url.split('/')
        item_id = url_array[4]
        return item_id
    except Exception:
        add_error(book, 'id')
        return 0


def get_img(item, book):
    # noinspection PyBroadException
    try:
        url = item.find("img")['data-pagespeed-lazy-src']
        url_array = url.split('/')
        url_array[5] = '200'
        url = '/'.join(url_array)
        return url
    except Exception as e:
        print(e)
        add_error(book, 'url')
        return ''


def get_title(item, book):
    # noinspection PyBroadException
    try:
        title = item.find(class_="swiper-book-name").text
        return title
    except Exception:
        add_error(book, 'title')
        return ''


def get_author(item, book):
    # noinspection PyBroadException
    try:
        author = item.find(class_="swiper-author").text
        return author
    except Exception:
        add_error(book, 'author')
        return ''


def get_rating(item, book):
    # noinspection PyBroadException
    try:
        rating = item.find(itemprop="ratingValue").text
        return rating
    except Exception:
        add_error(book, 'rating')
        return ''


def add_error(book, error):
    book['errors'].append(error)
