#Module to query internal and external DNS servers, so the resolution should match.

#Define the Modules I will use
import socket
import dns.resolver
import json



#Define the inputs
tiers= {"App": "" , "DB" : "-db", "Encore" : "-encore" , "MT" : "-mt"} #Tiers of sitecode I should query - I will use a dict
domain=".iii.com" #Domain that looking for Records for.
Resolvers= {"8.8.8.8": "_External","10.128.129.25": "_Internal"} # DNS resolvers to query list
records_list=["A","TXT"]
wildcard="*."
reverse_domain=".in-addr.arpa"


#Define the functions that will take inputs and do necessary checks

def resolve_fqdn_records(my_resolver,resolver,sitecode,resolutions):
    for tier in tiers:
            try:
                answer=my_resolver.query(sitecode+tiers[tier]+domain, "A")
                for data in answer:
                        print "The DNS resolution of %s%s%s is %s from %s " % (sitecode,tiers[tier],domain, data.address,resolver)
                        resolutions[tier+"_IP"+Resolvers[resolver]] = data.address
                        print resolutions


                answer=my_resolver.query(sitecode+tiers[tier]+domain, "TXT")
                for data in answer:
                        print "The DNS resolution of %s%s%s is %s from %s " % (sitecode,tiers[tier],domain, data.to_text(),resolver)
                        resolutions[tier+"_TXT"+Resolvers[resolver]] = data.to_text()

                if tiers[tier] == "":
                    answer=my_resolver.query(wildcard+sitecode+tiers[tier]+domain, "A")
                    for data in answer:
                            print "The DNS resolution of %s%s%s%s is %s from %s " % (wildcard,sitecode,tiers[tier],domain, data.address,resolver)
                            resolutions[tier+"_Wildcard"+Resolvers[resolver]] = data.address

            except:
                print "No dns entry for %s%s%s" % (sitecode,tiers[tier],domain)
                continue
    return resolutions


def set_resolver(dns_resolver):
    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = [dns_resolver]
    return my_resolver

def main(sitecode):
    resolutions={}
    for resolver in Resolvers:
        my_resolver=set_resolver(resolver)
        data=resolve_fqdn_records(my_resolver,resolver,sitecode,resolutions)
    with open(sitecode+".json", "w") as f:
        json.dump(data, f)
    return data

#Now create Sanity check functions, that checks the data collected - to perform useful task.
