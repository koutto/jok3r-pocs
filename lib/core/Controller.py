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
            # Instantiate Target using URL or IP:PORT
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

            # Get Exploit (or detection script) for selected vulnerability
            exploit = self.settings.get_exploit(self.args.vuln)

            # Check if specified mode is available for specified vuln
            if not exploit.is_mode_supported(self.args.mode):
                logger.error('Supplied mode ({mode}) is not supported for vulnerability {vuln}'.format(
                    mode=self.args.mode,
                    vuln=self.args.vuln))
                sys.exit(1)

            # Print title and main information
            OutputUtils.title('Vulnerability: {description}'.format(description=exploit.description))
            logger.info('Target product: {product}'.format(product=exploit.product))
            logger.info('Vulnerability type: {vuln}'.format(vuln=exploit.type))
            logger.info('Selected mode: {mode}'.format(mode=self.args.mode))
            if self.args.mode == 'exploit' and exploit.type == 'rce':
                logger.info('RCE output available: {rceoutput}'.format(
                    rceoutput='Y' if exploit.exploit_rce_output else 'N'))

            # Run exploit/detection script
            out = exploit.run(target, self.args.mode, self.args.cmd)

            if out is None:
                sys.exit(1)

            # Automatically check success when:
            # - Run in detection mode
            # - Run in exploit mode without --cmd provided (automatic exploit test)
            if self.args.mode == 'detect' or \
               (self.args.mode == 'exploit' and (not self.args.cmd or len(self.args.cmd) == 0)):
                if exploit.check_success(self.args.mode):
                    logger.success('{description}: Target is EXPLOITABLE !'.format(
                        description=exploit.description))
                    logger.info('Code available in: {directory}'.format(
                        directory=exploit.directory))
                else:
                    logger.error('{description}: Target seems NOT exploitable'.format(
                        description=exploit.description))

