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
    """
    Command object is used for detection command and exploit command
    """
    def __init__(self, 
                 rawcmd, 
                 type_,
                 exploit_rce_output=True):
        """
        :param str rawcmd: Raw command-line (with tags)
        :param str type_: Vulnerability type (e.g. rce/sqli)
        :param bool exploit_rce_output: Indicates if RCE exploit is blind (no command output) or not
            (for exploit command for RCE only)
        """
        self.rawcmd = rawcmd
        self.type = type_
        self.exploit_rce_output = exploit_rce_output


    def get_cmdline(self, target, rce_command=''):
        """
        :param Target target: Target instance
        :param str rce_command: Command to execute on vulnerable system through RCE vuln
        """
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

        # Replace tag [BASEURL]
        pattern = re.compile('\[BASEURL\]', re.IGNORECASE)
        baseurl = target.url.split('//')[0]+'//'+target.url.split('//')[1].split('/')[0]
        cmdline = pattern.sub(str(baseurl), cmdline)       

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
        if m:
            if target.ssl == True:
                cmdline = pattern.sub(m.group('option'), cmdline)
            else:
                cmdline = pattern.sub('', cmdline)
        
        # Replace tag [CMD]
        if '[cmd]' in cmdline.lower():
            try:
                pattern = re.compile('\[CMD\]', re.IGNORECASE)

                # If command provided by user, replace tag by this command, otherwise
                # use the predefined commands for automatic test
                if len(rce_command) > 0:
                    cmdline = pattern.sub(rce_command, cmdline)
                else:
                    if self.type == 'rce' and not self.exploit_rce_output:
                        cmdline_lin = pattern.sub(CMD['rce-blind']['linux'], cmdline)
                        cmdline_lin2 = pattern.sub(CMD['rce-blind']['linux2'], cmdline)
                        cmdline_lin3 = pattern.sub(CMD['rce-blind']['linux3'], cmdline)
                        cmdline_win = pattern.sub(CMD['rce-blind']['windows'], cmdline)
                        cmdline = '{0}; {1}; {2}; {3}'.format(cmdline_lin, cmdline_lin2, cmdline_lin3, cmdline_win)
                    else:
                        cmdline = pattern.sub(CMD['rce-standard']['linux'], cmdline)

            except Exception as e:
                raise CommandException(e)

        # Special case where Linux/Windows command line differ
        elif '[cmdlinux]' in cmdline.lower() or '[cmdwindows]' in cmdline.lower():
            try:
                pattern_linux = re.compile('\[CMDLINUX\]', re.IGNORECASE)
                pattern_windows = re.compile('\[CMDWINDOWS\]', re.IGNORECASE)

                # If command provided by user, replace both tag by this command, otherwise
                # use the predefined commands for automatic test
                if len(rce_command) > 0:
                    cmdline = pattern_linux.sub(rce_command, cmdline)
                    cmdline = pattern_windows.sub(rce_command, cmdline)
                else:
                    if self.type == 'rce' and not self.exploit_rce_output:
                        # Replace [CMDLINUX]
                        cmdline_lin = pattern_linux.sub(CMD['rce-blind']['linux'], cmdline)
                        cmdline_lin2 = pattern_linux.sub(CMD['rce-blind']['linux2'], cmdline)
                        cmdline_lin3 = pattern_linux.sub(CMD['rce-blind']['linux3'], cmdline)
                        cmdline = '{0}; {1}; {2}'.format(cmdline_lin, cmdline_lin2, cmdline_lin3)

                        # Replace [CMDWINDOWS]
                        cmdline = pattern_windows.sub(CMD['rce-blind']['windows'], cmdline)
                    else:
                        # Replace [CMDLINUX]
                        cmdline = pattern_linux.sub(CMD['rce-standard']['linux'], cmdline)  

                        # Replace [CMDWINDOWS]
                        cmdline = pattern_windows.sub(CMD['rce-standard']['windows'], cmdline)                        
            except Exception as e:
                raise CommandException(e)

        # Replace tag [LOCALIP]
        localip = NetUtils.get_local_ip_address()
        if localip == '127.0.0.1':
            raise CommandException('Unable to get local IP address')
        pattern = re.compile('\[LOCALIP\]', re.IGNORECASE)
        cmdline = pattern.sub(localip, cmdline)

        return cmdline

