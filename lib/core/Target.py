#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
### Core > Target
###
from six.moves.urllib.parse import urlparse

from lib.core.Exceptions import TargetException
from lib.utils.NetUtils import NetUtils


class Target:

    def __init__(self, ip, port, url=None, ssl=False):
        self.ssl = ssl
        self.url = url
        if url:
            self.__init_with_url(url)
        else:
            self.__init_with_ip_port(ip, port, ssl)


    def __init_with_url(self, url):
        p = urlparse(url)
        if NetUtils.is_valid_ip(p.hostname):
            self.ip = p.hostname
        else:
            self.ip = NetUtils.dns_lookup(p.hostname)
        if not self.ip:
            raise TargetException('Unable to resolve {}'.format(p.hostname))

        self.port = NetUtils.get_port_from_url(url)
        if not NetUtils.is_valid_port(self.port):
            raise TargetException('Invalid port number {}'.format(self.port))

        if url.lower().startswith('https://'):
            self.ssl = True


    def __init_with_ip_port(self, ip, port, ssl):
        if not NetUtils.is_valid_ip(ip):
            raise TargetException('Invalid IP address')
        if not NetUtils.is_valid_port(port):
            raise TargetException('Invalid port number {}'.format(port))
            
        self.ip = ip
        self.port = port
        self.url = 'http{s}://{ip}:{port}'.format(
            s='s' if self.ssl else '',
            ip=self.ip,
            port=self.port)        