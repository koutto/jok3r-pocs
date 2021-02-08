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

# Supported vulnerability types
SUPPORTED_TYPES = (
    'rce', 
    'sqli',
    'path-trav',
)

# Command to execute on remote system depending on exploit type and remote OS
CMD = {
    'rce-blind': {
        'linux': '/bin/ping -c 4 [LOCALIP]',
        'linux2': '/usr/bin/ping -c 4 [LOCALIP]',
        'linux3': 'curl http://[LOCALIP]:8888/testexploit1337',
        'windows': 'ping /n 4 [LOCALIP]',
    },
    'rce-standard': {
        'linux': 'echo "Command run from Exploit"',
        'windows': 'echo "Command run from Exploit"',
    },
}


# Matching pattern for successful RCE exploit without command output in automatic mode
MATCHING_PATTERN_RCE_BLIND_ICMP = 'Captured ICMP traffic:[\s\S]*?ICMP echo request.*\n.*ICMP echo reply'
MATCHING_PATTERN_RCE_BLIND_HTTP = 'Captured HTTP traffic:[\s\S]*?GET /testexploit1337'