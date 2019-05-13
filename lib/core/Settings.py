#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
### Core > Settings 
###
"""

exploits.conf:
-------------
For each exploit:
[exploit_name]
type    = rce-blind | rce-standard
command = Command to run the exploit, with tags
success = String matching success (optional)

Supported Tags for command:
---------------------------
[IP]                : Target IP
[PORT]              : Target Port
[SSL true="value"]  : Replaced by "value" if SSL/TLS
[LOCALIP]           : Local IP
[CMD]               : Location for command to execute on remote system
                      Command will be repeated to try to execute Linux
                      command once, and then Windows command (assume, 
                      target OS is not known)
[CMDLINUX]          : Location for Linux command to execute
[CMDWINDOWS]        : Location for Windows command to execute
"""
import os
import traceback
import configparser
from datetime import datetime
from collections import defaultdict

from lib.core.Config import *
from lib.core.Exploit import Exploit
from lib.core.Exceptions import SettingsException
from lib.utils.DefaultConfigParser import DefaultConfigParser
from lib.utils.OutputUtils import OutputUtils


class Settings:

    def __init__(self):
        """
        Start the parsing of settings files and create the Settings object.

        :raises SettingsException: Exception raised if any error is encountered while 
            parsing files
        """
        self.exploits = list()

        # Check presence of exploits.conf files
        if not os.access(EXPLOITS_CONF, os.F_OK):
            raise SettingsException('Missing configuration file exploits.conf')

        # Parse configuration file
        self.__parse_conf_file()
    

    #------------------------------------------------------------------------------------

    def __parse_conf_file(self):
        parser = DefaultConfigParser()
        # Utf-8 to avoid encoding issues
        parser.read(EXPLOITS_CONF, 'utf8')

        for section in parser.sections():
            type_ = parser.safe_get(section, 'type', '', None)
            if type_ not in SUPPORTED_TYPES:
                raise SettingsException('Unsupported exploit type for [{}]'.format(type_))

            rawcmd = parser.safe_get(section, 'command', '', None)
            if not rawcmd:
                raise SettingsException('No command specified for [{}]'.format(rawcmd))

            description = parser.safe_get(section, 'description', '', None)
            success = parser.safe_get(section, 'success', '', None)

            exploit = Exploit(section, description, type_, rawcmd, success)
            self.exploits.append(exploit)


    def get_exploit(self, name):
        for xpl in self.exploits:
            if name.lower() == xpl.name.lower():
                return xpl
        return None


    def show_list_exploits(self):
        data = list()
        columns = [
            'Name',
            'Description',
            'Type',
        ]

        for xpl in self.exploits:
            data.append([
                xpl.name,
                xpl.description,
                xpl.type,
            ]) 

        OutputUtils.table(columns, data, hrules=False)


