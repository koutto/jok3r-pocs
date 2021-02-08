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
product = Vulnerable product name
description = Vulnerability description (required)
type    = Vulnerability type: rce / sqli ...
detection_cmd = Command to run vulnerability detection, tags supported
detection_success = String matching success on detection command output (required if detection_cmd defined)
exploit_cmd = Command to run exploit, tags supported
exploit_rce_output = Indicates if RCE exploit returns command output or is blind. true|false (required for type == rce)
exploit_success = String matching exploit success, used for RCE with output in automatic mode (no --cmd)

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
            # Vulnerable product name
            product = parser.safe_get(section, 'product', '', None)
            if not product:
                raise SettingsException('No vulnerable product name specified for ' \
                    '[{}]'.format(section))

            # Vulnerability description
            description = parser.safe_get(section, 'description', '', None)
            if not description:
                raise SettingsException('Missing vulnerability description for ' \
                    '[{}]'.format(section))

            # Vulnerability type
            type_ = parser.safe_get(section, 'type', '', None)
            if type_ not in SUPPORTED_TYPES:
                raise SettingsException('Unsupported vulnerability type for [{}]'.format(section))

            # Detection command
            detection_rawcmd = parser.safe_get(section, 'detection_cmd', '', None)

            # Detection command output success
            detection_success = parser.safe_get(section, 'detection_success', '', None)
            if detection_rawcmd and len(detection_rawcmd) > 0 and not detection_success:
                raise SettingsException('Missing "detection_success" for [{}] since ' \
                    '"detection_cmd" is defined'.format(section))

            # Exploit command
            exploit_rawcmd = parser.safe_get(section, 'exploit_cmd', '', None)

            # Exploit RCE output
            exploit_rce_output = parser.safe_get_boolean(section, 'exploit_rce_output', True)

            # Exploit command output success (for auto test when exploit_rce_output == True)
            exploit_success = parser.safe_get(section, 'exploit_success', '', None)
            if exploit_rawcmd and \
               len(exploit_rawcmd) > 0 and \
               exploit_rce_output and \
               not exploit_success:
                raise SettingsException('Missing "exploit_success" for [{}] since '
                    '"exploit_cmd" is defined and "exploit_rce_output=true"'.format(section))


            exploit = Exploit(
                section, 
                product,
                description, 
                type_, 
                detection_rawcmd, 
                detection_success,
                exploit_rawcmd,
                exploit_rce_output,
                exploit_success)
            self.exploits.append(exploit)


    def get_exploit(self, name):
        """
        :param str name: Vulnerability name
        """
        for xpl in self.exploits:
            if name.lower() == xpl.name.lower():
                return xpl
        return None


    def show_list_exploits(self):
        data = list()
        columns = [
            'Product',
            'Name',
            'Type',
            'Detect',
            'Exploit',
            'RCE out',
            'Description',
        ]

        for xpl in self.exploits:
            if xpl.type == 'rce' and xpl.is_mode_supported('exploit'):
                rce_out = 'Y' if xpl.exploit_rce_output else 'N'
            else:
                rce_out = 'N/A'

            data.append([
                xpl.product,
                xpl.name,
                xpl.type,
                'Y' if xpl.detection_rawcmd else 'N',
                'Y' if xpl.exploit_rawcmd else 'N',
                rce_out,
                xpl.description,
            ]) 

        OutputUtils.table(columns, data, hrules=False)


