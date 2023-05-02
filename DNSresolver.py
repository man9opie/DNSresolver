import dns.message
import dns.query
import dns.rdatatype
import dns.rdataclass
import dns.name
import datetime

## root servers
root_servers = [
        '198.41.0.4',
        '199.9.14.201',
        '192.33.4.12',
        '199.7.91.13',
        '192.203.230.10',
        '192.5.5.241',
        '192.112.36.4',
        '198.97.190.53',
        '192.36.148.17',
        '192.58.128.30',
        '193.0.14.129',
        '199.7.83.42',
        '202.12.27.33'
    ]


domain_name = input('Please Enter the website: ')
text = None
response = None
total_time = 0
found = False
root = None
index = 0
count = 0

if '.' not in domain_name:  
    print("ERROR, you may enter the website wrong")
    exit()

## find root server
for server in root_servers:
    count+=1
    if count > 100:
        print("ERROR, you may enter the website wrong")
    query = dns.message.make_query(domain_name, dns.rdatatype.A)
    response = dns.query.udp(query, server)
    ##print(response)
    total_time += float(response.time)
    if response.additional:
        if "AAAA" in str(response.additional[index]):
            index += 1
        ##print(response.additional[index])
        root = server
        found = True
        break


## if server found then continue
if found:
    

    server = str(response.additional[index])
    server_a = server.split("IN A ")
    new_server = server_a[-1]

    index = 0
    ##print(new_server)
    
    
    ## keep looping until find the ip
    while True:
        query = dns.message.make_query(domain_name, dns.rdatatype.A)
        response = dns.query.udp(query, new_server)
        total_time += float(response.time)
        ##print(response)
        if response.answer:
            ##print(response.answer)
            text = str(response)
            break
        if response.additional:
            ##print(response.additional[0])
            if "AAAA" in str(response.additional[index]):
                index += 1
            server = str(response.additional[index])
            server_a = server.split("IN A ")
            new_server = server_a[-1]
            continue
    ##if found:

    ## check it is contain c name or not
    text_a = text.split("ANSWER")
    text = text_a[-1]
    text_a = text.split(";")
    text = text_a[0]
    
    total_time =total_time*1000
    file1 = open(r"C:\Users\a1069\Desktop\myfile.txt","w")

## output every thing to file
    print("Question section:\n")
    file1.write("Question section:\n\n");
    print(str(response.question[0]))
    file1.write(str(response.question[0]));
    print("\n\nAnswer section:")
    file1.write("\n\nAnswer section:\n");
    print(text)
    file1.write(text+"\n");
    print("Query time: "+str(total_time) + 'ms')
    file1.write("Query time: "+str(total_time) + 'ms'+"\n");
    print("When: "+str(datetime.datetime.now()))
    file1.write("When: "+str(datetime.datetime.now())+"\n");
    file1.close()
else:
    print("ERROR, can not find the ip address by the given website")




