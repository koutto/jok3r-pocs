# jok3r-pocs
Standalone POCs/Exploits from various sources for Jok3r


```
+------------------+--------------------------+-----------+--------+---------+---------+---------------------------------------------------------------------------------------------------------------+
| Product          | Name                     | Type      | Detect | Exploit | RCE out | Description                                                                                                   |
+------------------+--------------------------+-----------+--------+---------+---------+---------------------------------------------------------------------------------------------------------------+
| Adobe Coldfusion | coldfusion-cve-2017-3066 | rce       | N      | Y       | N       | Adobe Coldfusion BlazeDS Deserialize RCE [CVE-2017-3066 - CVSS=9.8]                                           |
| Drupal           | drupal-cve-2014-3704     | sqli      | N      | Y       | N/A     | SQL Injection in Drupal 7.x <= 7.31 allowing admin creation - Drupalgeddon [CVE-2014-3704 - CVSS=7.5]         |
| Drupal           | drupal-cve-2018-7600     | rce       | N      | Y       | Y       | Drupal 7.x <= 7.57 Unauthenticated RCE - Drupalgeddon2 [CVE-2018-7600 - CVSS=9.8]                             |
| Drupal           | drupal-cve-2019-6340     | rce       | N      | Y       | Y       | Drupal 8.x <= 8.6.9 REST Services Unauthenticated RCE [CVE-2019-6340 - CVSS=8.1]                              |
| JBoss            | jboss-cve-2015-7501      | rce       | N      | Y       | N       | JBoss Deserialize RCE [CVE-2015-7501 - CVSS=9.8]                                                              |
| JBoss            | jboss-cve-2017-7504      | rce       | N      | Y       | N       | JBoss 4.x JBossMQ JMS Deserialize RCE [CVE-2017-7504 - CVSS=9.8]                                              |
| JBoss            | jboss-cve-2017-12149     | rce       | Y      | Y       | N       | JBoss 5.x/6.x Deserialize RCE [CVE-2017-12149 - CVSS=9.8]                                                     |
| Jenkins          | jenkins-cve-2015-8103    | rce       | N      | Y       | N       | Jenkins CLI RMI Java Deserialize RCE [CVE-2015-8103 - CVSS=9.8]                                               |
| Jenkins          | jenkins-cve-2016-0792    | rce       | N      | Y       | N       | Jenkins Groovy XML RCE [CVE-2016-0792 - CVSS=8.8]                                                             |
| Jenkins          | jenkins-cve-2017-1000353 | rce       | N      | Y       | N       | Jenkins <= 2.56, LTS <= 2.46.1 Java Deserialize Unauthenticated RCE [CVE-2017-1000353 - CVSS=9.8]             |
| Jenkins          | jenkins-cve-2018-1000861 | rce       | N      | Y       | N       | Jenkins <= 2.153, LTS <= 2.138.3 Unauthenticated RCE via method invokation [CVE-2018-1000861 - CVSS=9.8]      |
| Magento          | magento-2.2-sqli         | sqli      | N      | Y       | N/A     | Magento 2.2.0 <= 2.3.0 Unauthenticated SQLi - user/admin session ID retrieval [CVE-2019-7139 - CVSS=9.8]      |
| Ruby on Rails    | rails-cve-2018-3760      | path-trav | N      | Y       | N/A     | Path Traversal/File Content Disclosure Vulnerability [CVE-2018-3760 - CVSS=7.5]                               |
| Ruby on Rails    | rails-cve-2019-5418      | path-trav | Y      | Y       | N/A     | Path Traversal/File Content Disclosure Vulnerability [CVE-2019-5418 - CVSS=7.5]                               |
| Ruby on Rails    | rails-cve-2019-5420      | rce       | N      | Y       | Y       | File Content Disclosure (CVE-2019-5418) + RCE (CVE-2019-5420) On Ruby on Rails [CVE-2019-5420 - CVSS=9.8]     |
| Apache Struts2   | struts-cve-2017-9805     | rce       | Y      | Y       | N       | Apache Struts2 REST Plugin XStream Remote Code Execution [CVE-2017-9805 - CVSS=8.1]                           |
| Apache Struts2   | struts-cve-2018-11776    | rce       | Y      | Y       | N       | Apache Struts2 Remote Code Execution [CVE-2018-11776 - CVSS=8.1]                                              |
| Apache Tomcat    | tomcat-cve-2017-12617    | rce       | Y      | N       | N/A     | Apache Tomcat JSP Upload Bypass RCE via PUT method [CVE-2017-12617 - CVSS=8.1]                                |
| Oracle Weblogic  | weblogic-cve-2015-4852   | rce       | N      | Y       | N       | Weblogic T3(s) Deserialize RCE [CVE-2015-4852 - CVSS=9.8]                                                     |
| Oracle Weblogic  | weblogic-cve-2016-0638   | rce       | Y      | N       | N/A     | Weblogic T3 Deserialize [CVE-2016-0638 - CVSS=9.8]                                                            |
| Oracle Weblogic  | weblogic-cve-2016-3510   | rce       | N      | Y       | N       | Weblogic T3 Deserialize [CVE-2016-3510 - CVSS=9.8]                                                            |
| Oracle Weblogic  | weblogic-cve-2017-3248   | rce       | Y      | N       | N/A     | Weblogic RMI Registry UnicastRef Object Java Deserialization Remote Code Execution [CVE-2017-3248 - CVSS=9.8] |
| Oracle Weblogic  | weblogic-cve-2017-3506   | rce       | Y      | N       | N/A     | Weblogic WLS-WSAT XMLDecoder Deserialization Remote Code Execution [CVE-2017-3506 - CVSS=9.8]                 |
| Oracle Weblogic  | weblogic-cve-2017-10271  | rce       | Y      | Y       | N       | Weblogic WLS-WSAT RCE [CVE-2017-10271 - CVSS=7.5]                                                             |
| Oracle Weblogic  | weblogic-cve-2018-2628   | rce       | Y      | Y       | N       | Weblogic T3 Deserialize RCE [CVE-2018-2628 - CVSS=9.8]                                                        |
| Oracle Weblogic  | weblogic-cve-2018-2893   | rce       | Y      | N       | N/A     | Weblogic T3 Deserialize RCE [CVE-2018-2893 - CVSS=9.8]                                                        |
| Oracle Weblogic  | weblogic-cve-2018-2894   | rce       | Y      | N       | N/A     | Weblogic Unauthenticated Webshell deploiement [CVE-2018-2894 - CVSS=9.8]                                      |
| Oracle Weblogic  | weblogic-cve-2018-3191   | rce       | Y      | N       | N/A     | Weblogic T3 Deserialize RCE [CVE-2018-3191 - CVSS=9.8]                                                        |
| Oracle Weblogic  | weblogic-cve-2018-3245   | rce       | N      | Y       | N       | Weblogic T3 Deserialize RCE [CVE-2018-3245 - CVSS=9.8]                                                        |
| Oracle Weblogic  | weblogic-cve-2019-2725   | rce       | N      | Y       | N       | Weblogic WLS-WSAT RCE [CVE-2019-2725 - CVSS=9.8]                                                              |
| Oracle Weblogic  | weblogic-cve-2019-2729   | rce       | Y      | N       | N/A     | Weblogic WLS-WSAT RCE (webshell deploy) [CVE-2019-2729 - CVSS=9.8]                                            |
| Oracle Weblogic  | weblogic-cve-2019-2890   | rce       | Y      | N       | N/A     | Weblogic T3 Deserialize RCE [CVE-2019-2890 - CVSS=9.8]                                                        |
| Oracle Weblogic  | weblogic-cve-2020-2555   | rce       | N      | Y       | N       | Weblogic T3 Deserialize RCE [CVE-2020-2555 - CVSS=9.8]                                                        |
| Oracle Weblogic  | weblogic-cve-2020-2883   | rce       | N      | Y       | N       | Weblogic T3 Deserialize RCE [CVE-2020-2883 - CVSS=9.8]                                                        |
| Oracle Weblogic  | weblogic-cve-2020-14882  | rce       | N      | Y       | N       | Weblogic GET Request RCE [CVE-2020-14882 - CVSS=9.8]                                                          |
| IBM Websphere    | websphere-cve-2015-7450  | rce       | N      | Y       | N       | Websphere Deserialize RCE [CVE-2015-7450 - CVSS=9.8]                                                          |
+------------------+--------------------------+-----------+--------+---------+---------+---------------------------------------------------------------------------------------------------------------+

```