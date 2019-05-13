#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
### Utils > NetUtils
###
import socket
import ipaddress
from six.moves.urllib.parse import urlparse


class NetUtils:

    @staticmethod
    def is_valid_ip(string):
        """Check if given string represents a valid IP address"""
        try:
            ipaddress.ip_address(string)
            return True
        except:
            return False


    @staticmethod
    def is_valid_port(string):
        """Check if given string represents a valid port number"""
        try:
            port = int(string)
            return (0 <= port <= 65535)
        except:
            return False


    @staticmethod
    def get_port_from_url(url):
        """Return port from URL"""
        parsed = urlparse(url)
        if parsed.port:
            return int(parsed.port)
        else:
            return 443 if parsed.scheme == 'https' else 80


    @staticmethod
    def dns_lookup(host):
        """
        Get IP corresponding to a given hostname 
        Return the first IPv4 in the list of IPs if available, otherwise the first IPv6
        """
        ip_list = list()
        try:
            ip_list = list(set(str(i[4][0]) for i in socket.getaddrinfo(host, 80)))
        except:
            return None
        if len(ip_list) == 0:
            return None

        for ip in ip_list:
            if type(ipaddress.ip_address(ip)) == ipaddress.IPv4Address:
                return ip
        return ip_list[0]


    @staticmethod
    def reverse_dns_lookup(ip):
        """Get hostname from IP if reverse DNS entry exists"""
        try:
            return socket.gethostbyaddr(ip)[0]
        except:
            return ip


    @staticmethod
    def get_local_ip_address():
        """Get the IP address of whichever interface is used to connect to the network"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
        except:
            return '127.0.0.1'