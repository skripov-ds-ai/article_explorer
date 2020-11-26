from random import choices
from smart_open import open
# from pprint import pprint


with open('categories.txt', 'r') as f:
    data = list(map(lambda x: x.strip().split('\t'), f.readlines()))
# data = list(map(lambda x: x.strip().split('\t'), s.split("\n")))

categories_to_long_name = dict(data)
# print(categories_to_long_name)


def get_random_categories(n=5):
    return choices(data, k=n)





