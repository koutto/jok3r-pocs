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

sudo rm -f /tmp/dump.pcap
sudo rm -f /tmp/httptraffic.log
PID=$(ps -e | pgrep -f -x 'python3 -m http.server 8888')
sudo kill -9 $PID 2> /dev/null

print_info "Running tcpdump in background to try to capture ICMP requests if service is vuln..."
sudo sh -c "tcpdump -U -i any -w /tmp/dump.pcap icmp &"
sleep 2
print_info "Alternatively, running HTTP server (port 8888/tcp) in background to try to capture HTTP requests if service is vuln..."
python3 -m http.server 8888 &> /tmp/httptraffic.log &
sleep 2

{command}

print_info "Wait a little bit..."
sleep 5
PID=$(ps -e | pgrep tcpdump)
print_info "Kill tcpdump (PID=$PID)"
sudo kill -9 $PID 2> /dev/null

PID=$(ps -e | pgrep -f -x 'python3 -m http.server 8888')
print_info "Kill python3 -m http.server (PID=$PID)"
sudo kill -9 $PID 2> /dev/null
sleep 2

print_info "Captured ICMP traffic:"
echo
sudo tcpdump -r /tmp/dump.pcap
echo
print_info "Delete capture"
sudo rm -f /tmp/dump.pcap
echo

print_info "Captured HTTP traffic:"
echo
cat /tmp/httptraffic.log
echo
print_info "Delete capture"
sudo rm -f /tmp/httptraffic.log
echo

"""