#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
### Core > ScriptTemplates
###

SCRIPT_RCE_BLIND = """
#!/usr/bin/env bash

print_title() {{
        BOLD=$(tput bold ; tput setaf 4)
        NORMAL=$(tput sgr0)
        echo "$BOLD $1 $NORMAL"
}}

print_info() {{
        BOLD=$(tput bold)
        BLUE=$(tput setaf 4)
        NORMAL=$(tput sgr0)
        echo "$BOLD$BLUE[~] $NORMAL$1 $NORMAL"
}}
cd {exploit_dir}

print_info "Running tcpdump in background to try to capture ICMP requests if service is vuln..."
sudo sh -c "tcpdump -U -i any -w /tmp/dump.pcap icmp &"
sleep 3

print_info "Running command: {command}"
{command}

print_info "Wait a little bit..."
sleep 5
PID=$(ps -e | pgrep tcpdump)
print_info "Kill tcpdump (PID=$PID)"
sudo kill -9 $PID 
sleep 2

print_info "Captured ICMP traffic:"
echo
sudo tcpdump -r /tmp/dump.pcap
echo
print_info "Delete capture"
sudo rm /tmp/dump.pcap

"""