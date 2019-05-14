#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
### Core > Command
###
import re
import regex
import urllib.parse

from lib.core.Config import *
from lib.core.Exceptions import CommandException
from lib.utils.NetUtils import NetUtils


class Command:

    def __init__(self, rawcmd, type_):
        self.rawcmd = rawcmd
        self.type = type_


    def get_cmdline(self, target):
        cmdline = self.rawcmd
        
        # Replace tag [IP]
        pattern = re.compile('\[IP\]', re.IGNORECASE)
        cmdline = pattern.sub(target.ip, cmdline)

        # Replace tag [PORT]
        pattern = re.compile('\[PORT\]', re.IGNORECASE)
        cmdline = pattern.sub(str(target.port), cmdline)

        # Replace tag [URL]
        pattern = re.compile('\[URL\]', re.IGNORECASE)
        cmdline = pattern.sub(str(target.url), cmdline)

        # Replace tag [URIPATH]
        pattern = re.compile('\[URIPATH\]', re.IGNORECASE)
        try:
            o = urllib.parse.urlparse(url)
            uripath = o.path or '/'
        except:
            uripath = '/'
        cmdline = pattern.sub(uripath, cmdline)

        # Replace tag [SSL true="..."]
        pattern = re.compile(
            r'\[SSL\s+true\s*=\s*[\'"](?P<option>.*?)[\'"]\s*\]', 
            re.IGNORECASE)

        m = pattern.search(cmdline)
        if target.ssl == True:
            cmdline = pattern.sub(m.group('option'), cmdline)
        else:
            cmdline = pattern.sub('', cmdline)
        
        # Replace tag [CMD]
        if '[cmd]' in cmdline.lower():
            try:
                pattern = re.compile('\[CMD\]', re.IGNORECASE)
                if CMD[self.type]['linux'] != CMD[self.type]['windows']:
                    cmdline_lin = pattern.sub(CMD[self.type]['linux'], cmdline)
                    cmdline_win = pattern.sub(CMD[self.type]['windows'], cmdline)
                    cmdline = '{0}; {1}'.format(cmdline_lin, cmdline_win)
                else:
                    cmdline = pattern.sub(CMD[self.type]['linux'], cmdline)

            except Exception as e:
                raise CommandException(e)
        elif '[cmdlinux]' in cmdline.lower() or '[cmdwindows]' in cmdline.lower():
            pattern = re.compile('\[CMDLINUX\]', re.IGNORECASE)
            cmdline = pattern.sub(CMD[self.type]['linux'], cmdline)

            pattern = re.compile('\[CMDWINDOWS\]', re.IGNORECASE)
            cmdline = pattern.sub(CMD[self.type]['windows'], cmdline)

        # Replace tag [LOCALIP]
        localip = NetUtils.get_local_ip_address()
        if localip == '127.0.0.1':
            raise CommandException('Unable to get local IP address')
        pattern = re.compile('\[LOCALIP\]', re.IGNORECASE)
        cmdline = pattern.sub(localip, cmdline)

        return cmdline

