import re

def parse_acl_config(acl_config, acl_names=None):
    acl_pattern = re.compile(r"ip access-list (?:standard|extended) (\S+)\n((?: .*\n)+)")

    acls = {}
    acl_matches = acl_pattern.finditer(acl_config)

    for acl_match in acl_matches:
        acl_name = acl_match.group(1)
        if acl_names is None or acl_name in acl_names:
            aces = acl_match.group(2).strip().split("\n")
            acls[acl_name] = aces

    return acls

acl_config = """
ip access-list extended ACL_1
  permit tcp 192.168.1.0 0.0.0.255 10.0.0.0 0.0.0.255 eq 80
  permit udp 192.168.1.0 0.0.0.255 10.0.0.0 0.0.0.255 eq 53
  deny ip any any
  permit udp host 10.10.10.1 any
!
ip access-list extended ACL_2
  permit tcp any any
  deny ip any any

ip access-list standard ACL_3
  permit icmp any any
"""

# Provide specific ACL names to parse or leave it as None to parse all ACLs
acls_to_parse = ["ACL_1", "ACL_3"]
acls = parse_acl_config(acl_config)
print(acls)
