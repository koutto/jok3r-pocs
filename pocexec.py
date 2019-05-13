#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import colored
import sys
import traceback

from lib.core.ArgumentsParser import ArgumentsParser
from lib.core.Config import *
from lib.core.Controller import Controller
from lib.core.Exceptions import *
from lib.core.Logger import logger
from lib.core.Settings import Settings


class Program:

    def __init__(self):

        print(colored.stylize(BANNER, colored.attr('bold')))

        # Parse exploits.conf settings file
        try:
            settings = Settings()
        except SettingsException as e:
            logger.error(e)
            sys.exit(1)

        # Parse command-line arguments
        arguments = ArgumentsParser(settings)

        # Controller
        try:
            controller = Controller(arguments.args, settings)
            controller.run()
        except KeyboardInterrupt:
            logger.error('Canceled by the user')
            sys.exit(0)


if __name__ == '__main__':
    main = Program()