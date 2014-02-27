'''
Created on 2013-9-16

@author: ezonghu
'''
cmd = '''localadmin@ubuntu1:~$ quantum port-create --name "MGC-PL-4" --mac-address 00:02:B3:BC:FB:A1 net69
'''
result = '''Created a new port:
+----------------------+---------------------------------------------------------------------------------------+
| Field                | Value                                                                                 |
+----------------------+---------------------------------------------------------------------------------------+
| admin_state_up       | True                                                                                  |
| binding:capabilities | {"port_filter": true}                                                                 |
| binding:vif_type     | ovs                                                                                   |
| device_id            |                                                                                       |
| device_owner         |                                                                                       |
| fixed_ips            | {"subnet_id": "e862d0aa-7db6-4737-866d-ebb7ca50b01b", "ip_address": "169.254.69.131"} |
| id                   | 0e5bee7f-e83e-41c1-b88b-9ff6c7eebdb7                                                  |
| mac_address          | 00:02:B3:BC:FB:A1                                                                     |
| name                 | MGC-PL-4                                                                              |
| network_id           | 7254bda9-e34c-4da8-806b-7636a0895bcf                                                  |
| security_groups      | 33992b3b-c2cb-4708-9109-bfef610d9e84                                                  |
| status               | DOWN                                                                                  |
| tenant_id            | 71f8f0bdcd2c440885e84ec6dcc32e30                                                      |
+----------------------+---------------------------------------------------------------------------------------+
'''
import optparse
def parse_args():
    usage = """usage: %prog -
this is the hello client generator.
Run it like this:
    python openstack_net.py -a MGC_SC_1 -m "00:02:B3:BC:FB:A1" -t net69,net70,net71,net82 -n 4 -f 3 -z "nova:ubuntu1" -i SC_1
"""
    parser = optparse.OptionParser(usage)
    parser.add_option('-a', '--name', dest='name', help='virtual Machine Name')
    parser.add_option("-m", "--firstmac", dest="firstmac" , help="first Mac Address")
    parser.add_option('-t', '--net', dest='net', help='vnet name')
    parser.add_option("-n", "--num", dest="num", help="vNIC number")

    parser.add_option("-f", "--flavor", dest="flavor" , type='int', help="flavor number")
    parser.add_option("-z", "--zone", dest="zone" , help="zone name")
    parser.add_option("-i", "--image", dest="image" , help="image name")

    options, _others = parser.parse_args()

    if options.name is None:
        parser.error("virtual Machine Name is missing")

    if options.firstmac is None:
        parser.error("first Mac Address is missing")

    if options.net is None:
        parser.error("vnet name is missing")
    if options.flavor is None:
        parser.error("flavor number is missing")
    if options.zone is None:
        parser.error("zone Name is missing")
    if options.image is None:
        parser.error("image is missing")

    return options


class quantum_port(object):
    def __init__(self, result):
        import re
        bound = re.compile("^\+-+\+-+\+$")
        seperate = re.compile("^\|(.*)\|(.*)\|$")
        bound_flag = 0
        for line in result.split('\n'):
            m = bound.match(line)
            if m is not None:
                bound_flag += 1

            if bound_flag == 2:
                s = seperate.match(line)
                if s is not None:
                    attr = s.group(1).strip()
                    value = s.group(2).strip()
                    setattr(self, attr, value)



def run_cmd(cmd):
    print cmd
    import subprocess
    proc = subprocess.Popen([cmd], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return proc.communicate()

def create_port(name, mac, net, fun=None):
    cmd = 'quantum port-create --name "%s" --mac-address %s %s' % (name, mac, net)
    if fun is None:
        res, err = run_cmd(cmd)
    else:
        fun(cmd)
        return quantum_port(result)
    if err == "":
        return quantum_port(res)
    else:
        print err
        return

def nova_boot(image, flavor, zone, nics, name, fun=None):
    cmd_pre = 'nova boot --image %s --flavor %s --availability-zone %s ' % (image, flavor, zone)
    nic_pre = '--nic port-id=%s '
    total_nic = ''
    for port_id in nics:
        total_nic += nic_pre % port_id

    cmd = cmd_pre + total_nic + name
    if fun is None:
        res, err = run_cmd(cmd)
    else:
        fun(cmd)
        return
    if err == "":
        return res
    else:
        print err
        return

def generate_macs(firstmac, number):
    firstmac_num = 0
    for i in firstmac.split(":"):
        sub = int(i, 16)
        firstmac_num = firstmac_num * 256 + sub

    mac_num_list = []
    for i in range(number):
        mac_num_list.append(firstmac_num+i)
    mac_str_list = []
    for mac in mac_num_list:
        mac_str = []
        for i in range(6):
            mac_str.insert(0, "%02X" % (mac % 256))
            mac = mac // 256
        mac_str_list.append(":".join(mac_str))
    return mac_str_list

def main(fun=None):
    Options = parse_args()
    print Options.__dict__
    first_mac_list = Options.firstmac.split(',')
    num_list = Options.num.split(',')
    mac_list = []
    for first_mac, num in zip(first_mac_list, num_list):
        mac_list.extend(generate_macs(first_mac, int(num)))

    net_list = Options.net.split(",")
    port_list = []
    for mac, net in zip(mac_list, net_list):
        print "try to create port, mac:%s, net:%s" % (mac, net)
        port = create_port(Options.name, mac, net, fun)
        if port is None:
            print "create failure"
            import sys
            sys.exit(-1)
        else:
            print "create sucess"
            port_list.append(port)

    nics = []
    for port in port_list:
        nics.append(port.id)

    print "try to boot %s" % Options.name
    print nova_boot(Options.image, Options.flavor, Options.zone, nics, Options.name, fun)



def test():
    q = quantum_port(result)
    print q.__dict__
    print q.id
    print generate_macs("00:02:B3:BC:FB:A1",100)
    def run_cmd(cmd):
        print cmd
    main(run_cmd)



if __name__ == "__main__":
    main()

