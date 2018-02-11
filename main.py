# coding=utf-8
import os

from biqukan.biqukan import BiQuKan

if __name__ == '__main__':
    biqukan = BiQuKan()
    biqukan.download_chapter('1_1094', '17967679')

    biqukan.get_query('一念永恒').save_to_file()

    biqukan.get_index_type(1).save_to_file()
