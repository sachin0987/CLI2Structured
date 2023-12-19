import re

def get_interface_acls(interface_config_output, interface_names, acl_names):
    acl_information = {}
    for interface_name in interface_names:
        # Regular expression pattern to match ACLs applied to the interface
        acl_pattern = rf"interface {interface_name}\s*([\s\S]*?)(?=^interface|\Z)"

        # Search for the ACL pattern in the interface configuration output
        match = re.search(acl_pattern, interface_config_output, re.MULTILINE)

        if match:
            acl_config = match.group(1)
            all_acls = re.findall(r"ip access-group (\S+) (in|out)", acl_config)
            configured_acls = [acl[0] for acl in all_acls]
            
            acl_status = {acl_name: acl_name in configured_acls for acl_name in acl_names}
            other_acls = [acl for acl in configured_acls if acl not in acl_names]
            
            acl_information[interface_name] = {
                'acl_status': acl_status,
                'other_acls': other_acls
            }
        else:
            acl_information[interface_name] = {
                'acl_status': {},
                'other_acls': []
            }

    return acl_information

# Example usage with provided interface config output for two interfaces
interface_config_output = """
interface GigabitEthernet1/1/1
 description Some description
 ip address 192.168.1.1 255.255.255.0
 ip access-group test_acl in
 ip access-group another_acl out
!

interface GigabitEthernet1/1/2
 description Another interface
 ip address 10.0.0.1 255.255.255.0
 ip access-group example_acl in
!
"""

interface_names_to_check = ["GigabitEthernet1/1/1", "GigabitEthernet1/1/2"]
acl_names_to_check = ["test_acl", "another_acl", "example_acl"]

acl_information = get_interface_acls(interface_config_output, interface_names_to_check, acl_names_to_check)
print(acl_information)