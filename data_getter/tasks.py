# import logging
# from data_getter.celery import celery
# from data_getter.process_data import *
#
#
# @celery.task(name="load_data_task")
#
# def load_data_task():
#     data = []
#     for cat in [
#         'math.CT'
#         'stat.TH',
#         'stat.ML',
#         'math.QA',
#         'math.MP',
#         'eess.IV',
#         'math.CA',
#         'math.FA'
#     ]:
#         # print(fill_template(cat, 700, 100))
#         data1 = get_result(cat, 700, 100)
#         data.extend(data1)
#
#     for datum in data:
#         # logging.info(datum)
#         transaction_single_article(datum)
