#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import ipaddress
import os
import re

from lib.core.Config import *
from lib.utils.ArgParseUtils import LineWrapRawTextHelpFormatter
from lib.utils.NetUtils import NetUtils


class ArgumentsParser:

    formatter_class = lambda prog: LineWrapRawTextHelpFormatter(
        prog, max_help_position=100)

    def __init__(self, settings):
        self.settings = settings

        self.parser = argparse.ArgumentParser(
            formatter_class=ArgumentsParser.formatter_class)
        self.parser.add_argument('-t', '--target', type=self.check_arg_target, 
            dest='target', help='Target IP:PORT or URL')
        self.parser.add_argument('-s', '--ssl', dest='ssl', default=False,
            help='Enable SSL/TLS')
        self.parser.add_argument('-e', '--exploit', type=self.check_arg_exploit,
            dest='exploit', help='Exploit to use')
        self.parser.add_argument('-l', '--list', dest='list', action='store_true', default=False,
            help='Display list of exploits')

        self.args = self.parser.parse_args()
        self.check_args()


    def check_arg_target(self, target):
        # Case where URL is provided
        if target.lower().startswith('http'):
            self.check_arg_url(target)

        # Otherwise consider format is IP:PORT
        else:
            if ':' in target:
                self.check_arg_ip_port(target)
            else:
                raise argparse.ArgumentTypeError('Invalid format. Must be either URL or IP:PORT')

        return target


    def check_arg_url(self, url):
        url = str(url)
        regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
            r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if not regex.match(url):
            raise argparse.ArgumentTypeError('Invalid URL submitted')
        # Add http:// prefix if necessary
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://{0}'.format(url)
        # Remove potential ending slash at end of URL
        while url.endswith('/'):
            url = url[:-1]
        return url


    def check_arg_ip_port(self, ip_port):
        ip, port = ip_port.split(':', maxsplit=1)
        if not NetUtils.is_valid_port(port):
            raise argparse.ArgumentTypeError('Invalid port number')
        if not NetUtils.is_valid_ip(ip):
            raise argparse.ArgumentTypeError('Invalid IP address')

        return ip, port


    def check_arg_exploit(self, exploit):
        if self.settings.get_exploit(exploit) is None:
            raise argparse.ArgumentTypeError('Unsupported exploit. Check --list')
        return exploit

    def check_args(self):
        if self.args.list is False:
            if self.args.target is None:
                self.parser.error('Target is required (--target)')
            elif self.args.exploit is None:
                self.parser.error('Exploit name is required (--exploit)')
        return