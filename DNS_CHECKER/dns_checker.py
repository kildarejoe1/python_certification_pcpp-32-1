#Module to query internal and external DNS servers, so the resolution should match.

#Define the Modules I will use
import socket
import dns.resolver


#Define the inputs
tiers= {"App": "" , "DB" : "-db", "Encore" : "-encore" , "MT" : "-mt"} #Tiers of sitecode I should query - I will use a dict
sitecode=str(raw_input("Enter a sitcode: ")) #Get the customer sitecode from user
domain=".iii.com" #Domain that looking for Records for.
Resolvers= ["8.8.8.8","10.128.129.25"] # DNS resolvers to query list


#Define the functions that will take inputs and do necessary checks
def resolve_fqdn_A():
    for tier in tiers:
            try:
                fqdn=str(sitecode+tier+domain)
                ip_addr=socket.gethostbyname(sitecode+tier+domain)
                print("The IP address for %s%s%s is : %s" % (sitecode,tier,domain, ip_addr))
            except:
                print("%s%s%s did not resolve correctly" % (sitecode,tier,domain))
                continue #Move onto the next index in the list
#call the functions with input data and out put results



def set_resolver(dns_resolver):
    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = [dns_resolver]
    return my_resolver


def main():
    for resolver in Resolvers:
        my_resolver=set_resolver(resolver)
        answer=my_resolver.query('google.com', "A")
        for data in answer:
            print "The ip address as resolved by the dns resolvers %s is: %s" % ( resolver, data.address)


main()
