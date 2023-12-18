from collections import defaultdict
from typing import Dict, List, Optional
import re

def parse_acl_config(acl_config: str, acl_names: Optional[List[str]] = None) -> Dict[str, List[str]]:
    """
    Parses an ACL configuration string and returns a dictionary of ACLs.

    Args:
        acl_config (str): The ACL configuration string to parse.
        acl_names (list, optional): A list of ACL names to parse. Defaults to None.

    Returns:
        dict: A dictionary containing the parsed ACLs. The keys are the ACL names, and the values are lists of ACEs.
              If acl_names is provided, the dictionary only contains the specified ACLs, and if an ACL name is not found,
              it has an empty list as the value.
    """
    acls = {}
    try:
        acl_pattern = re.compile(r"ip access-list (?:standard|extended) (\S+)\n((?: .*\n)+)", re.MULTILINE)
        acl_matches = acl_pattern.finditer(acl_config)
        # Additional code to handle exceptions
        for acl_match in acl_matches:
            acl_name = acl_match.group(1)
            if acl_names is None or acl_name in acl_names:
                aces = acl_match.group(2).strip().split("\n")
                acls[acl_name] = aces
        if acl_names:
            for name in acl_names:
                if name not in acls:
                    acls[name] = []  # Return an empty list for ACLs not found
        return acls
    
    except Exception as e:
        print(e)
    finally:
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
acls_to_parse = ["ACL_1", "ACL_3"]  # ACL_4 doesn't exist in the configuration
acls = parse_acl_config(acl_config, acls_to_parse)
print(acls)