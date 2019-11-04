import requests
from lxml import html, etree
from dateutil.parser import parse

from data_getter.parse_categories import get_random_categories

TEMPLATE = 'http://export.arxiv.org/api/query?search_query=all:%s&start=%d&max_results=%d'


def fill_template(category, start, max_results):
    return TEMPLATE % (category, start, max_results)


def get_info_from_entry(entry):
    url = entry.xpath('//id/text()')[0].strip()

    updated = entry.xpath('//updated/text()')[0].strip()
    published = entry.xpath('//published/text()')[0].strip()

    updated = parse(updated)
    published = parse(published)

    title = entry.xpath('//title/text()')[0].strip()
    summary = entry.xpath('//summary/text()')[0].strip().replace('\n', ' ').strip()
    categories = entry.xpath('//category/@term')
    categories = list(map(lambda x: x.strip(), categories))

    authors = entry.xpath('//author/name/text()')
    authors = list(map(lambda x: x.strip(), authors))

    d = {
        'url': url,
        'updated': updated,
        'published': published,
        'title': title,
        'summary': summary,
        'categories': categories,
        'authors': authors,
    }
    return d


def get_result(category, start, max_results):
    tmp = fill_template(category, start, max_results)
    r = requests.get(tmp)
    tree = html.fromstring(r.content)
    entries = tree.xpath('//entry')
    data = []
    for entry in entries:
        data.append(
            get_info_from_entry(etree.ElementTree(entry))
        )
    return data


from pprint import pprint

# print(fill_template('stat.TH', 100, 15))
# pprint(get_result('stat.TH', 100, 15))

