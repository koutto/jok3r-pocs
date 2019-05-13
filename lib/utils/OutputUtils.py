#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
### Utils > Output Utils
###
import colored
import prettytable


class OutputUtils:

    @staticmethod
    def colored(string, color=None, highlight=None, attrs=None):
        """Apply styles to a given string"""
        # Colors list: https://pypi.org/project/colored/
        return colored.stylize(string, (colored.fg(color) if color else '') + \
                                       (colored.bg(highlight) if highlight else '') + \
                                       (colored.attr(attrs) if attrs else ''))

    @staticmethod
    def table(columns, data, hrules=True):
        """
        Print a table. Supports multi-row cells.
        :param columns: An iterable of column names (strings)
        :param data: An iterable containing the data of the table
        :param hrules: Boolean for horizontal rules
        """
        columns = map(lambda x:OutputUtils.colored(x, attrs='bold'), columns)
        table = prettytable.PrettyTable(
            hrules=prettytable.ALL if hrules else prettytable.FRAME, 
            field_names=columns)
        for row in data:
            table.add_row(row)
        table.align = 'l'
        print(table)


    @staticmethod
    def title(title):
        """Print title"""
        msg  = '\n'
        msg += '-'*80 + '\n'
        msg += ' {title}\n'.format(title=title)
        msg += '-'*80 + '\n'
        print(OutputUtils.colored(msg, color='light_green', attrs='bold'))