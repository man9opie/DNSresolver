For Part A:
I used dns.message, dns.query, dns.radatatype, dns.rdataclasss, dns.name and dns.datetime library.
The program will ask user to enter a website and try to look for its ip address.
In order to get the ip address of the website, I first look for its root server, and then i used a while loop which
break when the ip address or cname is found. 