#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from lib.core.Logger import logger
from lib.core.Target import Target
from lib.utils.OutputUtils import OutputUtils

class Controller:

    def __init__(self, args, settings):
        self.args = args
        self.settings = settings


    def run(self):

        if self.args.list:
            self.settings.show_list_exploits()

        else:
            if self.args.target.lower().startswith('http'):
                target = Target(
                    ip=None, 
                    port=None, 
                    url=self.args.target)
            else:
                ip, port = self.args.target.split(':', maxsplit=1)
                target = Target(
                    ip=ip,
                    port=port,
                    url=None,
                    ssl=self.args.ssl)

            exploit = self.settings.get_exploit(self.args.exploit)

            OutputUtils.title('Exploitation Attempt: {description}'.format(
                description=exploit.description))
            out = exploit.run(target)

            if out is None:
                sys.exit(1)

            if exploit.check_success():
                logger.success('{description}: Target is EXPLOITABLE !'.format(
                    description=exploit.description))
                logger.info('Exploit code available in: {directory}'.format(
                    directory=exploit.directory))

            else:
                logger.error('{description}: Target seems NOT exploitable'.format(
                    description=exploit.description))

