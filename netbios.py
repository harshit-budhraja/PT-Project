from nmb.NetBIOS import NetBIOS

def queryNam(name):
    n = NetBIOS(broadcast=True, listen_port=0)
    ip = n.queryName(name, timeout=30)
    return ip

name = "Computer-Name"
ip = queryNam(name)
print (ip)
