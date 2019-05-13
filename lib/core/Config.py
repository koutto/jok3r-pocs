#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
### Core > Config
###
import colored
import os


TOOL_BASEPATH = os.path.dirname(os.path.realpath(__file__+'/../..'))

BANNER = colored.stylize("""

POCEXEC
Exploits Runner for Jok3r
   
""", colored.fg('light_green') + colored.attr('bold'))

EXPLOITS_CONF = 'exploits.conf'
SUPPORTED_TYPES = ('rce-blind', 'rce-standard')

# Command to execute on remote system depending on exploit type and remote OS
CMD = {
	'rce-blind': {
		'linux': '/bin/ping -c 4 [LOCALIP]',
		'windows': 'ping [LOCALIP]',
	},
	'rce-standard': {
		'linux': 'echo "Command run from Exploit"',
		'windows': 'echo "Command run from Exploit"',
	},
}


# Matching pattern for successful exploits
MATCHING_PATTERN_RCE_BLIND = 'Captured ICMP traffic:[\s\S]*?ICMP echo request.*\n.*ICMP echo reply'