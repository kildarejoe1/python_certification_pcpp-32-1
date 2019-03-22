#Module to query internal and external DNS servers, so the resolution should match.

#Define the Modules I will use
import socket
import dns.resolver


#Define the inputs
tiers= {"App": "" , "DB" : "-db", "Encore" : "-encore" , "MT" : "-mt"} #Tiers of sitecode I should query - I will use a dict
domain=".iii.com" #Domain that looking for Records for.
Resolvers= ["8.8.8.8","10.128.129.25"] # DNS resolvers to query list
records_list=["A","TXT"]
wildcard="*."


#Define the functions that will take inputs and do necessary checks
def resolve_fqdn_records(my_resolver,resolver,sitecode):
    open_file=open(sitecode+".txt", "w")
    for tier in tiers:
            try:
                answer=my_resolver.query(sitecode+tiers[tier]+domain, "A")
                for data in answer:
                        print "The DNS resolution of %s%s%s is %s from %s " % (sitecode,tiers[tier],domain, data.address,resolver)
                        open_file.write("The DNS resolution of %s%s%s is %s from %s \n" % (sitecode,tiers[tier],domain, data.address,resolver))
                answer=my_resolver.query(sitecode+tiers[tier]+domain, "TXT")
                for data in answer:
                        print "The DNS resolution of %s%s%s is %s from %s " % (sitecode,tiers[tier],domain, data.to_text(),resolver)
                        open_file.write("The DNS resolution of %s%s%s is %s from %s \n " % (sitecode,tiers[tier],domain, data.address,resolver))
                if tiers[tier] == "":
                    answer=my_resolver.query(wildcard+sitecode+tiers[tier]+domain, "A")
                    for data in answer:
                            print "The DNS resolution of %s%s%s%s is %s from %s " % (wildcard,sitecode,tiers[tier],domain, data.address,resolver)
                            open_file.write("The DNS resolution of %s%s%s%s is %s from %s " % (wildcard,sitecode,tiers[tier],domain, data.address,resolver))

            except:
                print "No dns entry for %s%s%s" % (sitecode,tiers[tier],domain)
                open_file.write("No dns entry for %s%s%s \n" % (sitecode,tiers[tier],domain))
                continue
    open_file.close()


def set_resolver(dns_resolver):
    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = [dns_resolver]
    return my_resolver

def main():
    sitecode=str(raw_input("Enter a sitcode: "))
    for resolver in Resolvers:
        my_resolver=set_resolver(resolver)
        resolutions=resolve_fqdn_records(my_resolver,resolver,sitecode)


main()
