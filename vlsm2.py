import ipaddress

# Input for IP, MASK and network
netinit = input("Enter the network IP: ")
maskinit = int(input("Enter the mask prefix: "))
netreq = int(input("Enter the number of networks that you need: "))

# Hosts
hosts = []
for i in range(netreq):
    host = int(input(f"Hosts that you need for network {i+1}: "))
    hosts.append(host)

# Sort hosts to use VLSM
hosts = sorted(hosts, reverse=True)

# Function to find the mask
def maskdefined(h):
    y = 0
    while (2 ** y - 2) < h:
        y += 1
    return 32 - y

# Convert the net in an object
network = ipaddress.ip_network(f"{netinit}/{maskinit}", strict=False)
net_address = int(network.network_address)

# Calculate and show the networks
for i, hostx in enumerate(hosts):
    required_mask = maskdefined(hostx)
    subnet_mask = required_mask
    subnet_size = 2 ** (32 - required_mask)
    
    net_addr = net_address
    first_ip = net_address + 1
    last_ip = net_address + subnet_size - 2
    broadcast_ip = net_address + subnet_size - 1
    
    # We need to verify if the ip exceed the ipv4 range
    try:
        net_addr_ip = ipaddress.IPv4Address(net_addr)
        first_ip_ip = ipaddress.IPv4Address(first_ip)
        last_ip_ip = ipaddress.IPv4Address(last_ip)
        broadcast_ip_ip = ipaddress.IPv4Address(broadcast_ip)
    except ipaddress.AddressValueError as e:
        print(f"Error: {e}")
        break
    
    print(f"\nNetwork {i+1}:")
    print(f"Network IP: {net_addr_ip}/{subnet_mask}")
    print(f"First Usable IP: {first_ip_ip}")
    print(f"Last Usable IP: {last_ip_ip}")
    print(f"Broadcast IP: {broadcast_ip_ip}")
    
    net_address += subnet_size