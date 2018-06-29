#!/usr/bin/python3


import dns
import dns.resolver
import sys

resolver = dns.resolver.Resolver()

#---------------- NS record fuction begins ---------------------------

def dnsNS(domain):
 try:
     result = resolver.query(domainname,'NS')
     for i in result:
      print('\n\t\t',result[0],'\n')
 except dns.resolver.NoNameservers:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.resolver.NXDOMAIN:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.resolver.NoAnswer:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.exception.Timeout:
        print('\nThe connection hit a timeout. Are you connected to the internet?\n')
        sys.exit()

#---------------- TXT record fuction begins ---------------------------
 
def dnsTXT(domain):
 try:
     result = resolver.query(domainname,'TXT')
     for i in result:
      print('\n\t\t',result[0],'\n')
 except dns.resolver.NoNameservers:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.resolver.NXDOMAIN:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.resolver.NoAnswer:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.exception.Timeout:
        print('\nThe connection hit a timeout. Are you connected to the internet?\n')
        sys.exit()

#---------------- MX record fuction begins ---------------------------

def dnsMX(domain):
 try:
     result = resolver.query(domainname,'MX')
     for i in result:
      print('\n\t\t',result[0],'\n')
 except dns.resolver.NoNameservers:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.resolver.NXDOMAIN:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.resolver.NoAnswer:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.exception.Timeout:
        print('\nThe connection hit a timeout. Are you connected to the internet?\n')
        sys.exit()

#---------------- CNAME record fuction begins ---------------------------

def dnsCNAME(domain):
 try:
     result = resolver.query(domainname,'CNAME')
     for i in result:
      print('\n\t\t',result[0],'\n')
 except dns.resolver.NoNameservers:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.resolver.NXDOMAIN:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.resolver.NoAnswer:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.exception.Timeout:
        print('\nThe connection hit a timeout. Are you connected to the internet?\n')
        sys.exit() 


#---------------- A record fuction begins ---------------------------

def dnsA(domain):
 try: 
    result = resolver.query(domainname,'A')
    for i in result:
     print('\n\t\t',result[0],'\n')
 except dns.resolver.NoNameservers:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.resolver.NXDOMAIN:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.resolver.NoAnswer:
        print('\nError: \nDomain Not Valid, Check You Have Entered It Correctly\n')
        sys.exit()
 except dns.exception.Timeout:
        print('\nThe connection hit a timeout. Are you connected to the internet?\n')
        sys.exit()

ns=True
while ns:
    print ("""
    1.A Record \n
    2.NS Record\n
    3.MX Record\n
    4.CNAME Record\n
    5.TXT Record
    """)
    ans=input("Please enter right choice \t") 
    if ans=="1": 
      print("\n A record \n")
      domainn = input('Please enter the domainname : \t')
      domainname = domainn.strip()
      dnsA(domainname)
      break      
 
    elif ans=="2":
      print("\n NS record \n")
      domainn = input('Please enter the domainname : \t')
      domainname = domainn.strip()
      dnsNS(domainname)      
            
      break

    elif ans=="3":
      print("\n MX record \n") 
      domainn = input('Please enter the domainname : \t')
      domainname = domainn.strip()
      dnsMX(domainname)
      break 

    elif ans=="4":
      print("\n CNAME record \n")
      domainn = input('Please enter the domainname : \t')
      domainname = domainn.strip()
      dnsCNAME(domainname) 
      break

    elif ans=="5":
      print("\n TXT record \n")
      domainn = input('Please enter the domainname : \t')
      domainname = domainn.strip()
      dnsTXT(domainname)
      break

    elif ans !="":
      print("\n Not Valid Choice Try again \n")
      break
