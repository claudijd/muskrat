import re


class Banner:
    def __init__(self, raw_string):
        self.raw_string = str(raw_string.rstrip())

        # WARNING: careful with ordering here, if unsure, put near the end
        self.os_map = {
            r'Ubuntu': 'ubuntu',
            r'6.6p1-5build1': 'ubuntu',
            r'CentOS': 'centos',
            r'RHEL|RedHat': 'redhat',
            r'FreeBSD': 'freebsd',
            r'Debian': 'debian',
            r'Windows|Microsoft': 'windows',
            r'Cisco': 'cisco',
            r'Raspbian': 'raspbian',
            r'ROS': 'ros',
            r'Raspbian': 'raspbian',
            r'Raspbian': 'raspbian',
            r'DOPRA': 'dopra'
        }

        # WARNING: careful with ordering here, if unsure, put near the end
        self.ssh_lib_map = {
            r'OpenSSH': 'openssh',
            r'LibSSH': 'libssh',
            r'ipssh': 'ipssh',
            r'Cisco': 'cisco',
            r'ROS': 'ros',
            r'DOPRASSH': 'doprassh',
            r'cryptlib': 'cryptlib',
            r'NOS-SSH': 'nosssh',
            r'pgp': 'pgp',
            r'ServerTech_SSH|Mocana SSH': 'sentryssh',
            r'mpssh': 'mpssh',
            r'dropbear': 'dropbear',
            r'RomSShell': 'romsshell',
            r'Flowssh': 'flowssh',
        }

    def ssh_version(self):
        pattern = r"SSH-(\d+[\.\d+]+)"
        match = re.search(pattern, self.raw_string)
        if match:
            return float(match[1])
        else:
            return "unknown"

    def os_guess(self):
        for pattern in self.os_map.keys():
            match = re.search(pattern, self.raw_string)
            if match:
                return self.os_map[pattern]

        return 'unknown'

    def ssh_lib_guess(self):
        for pattern in self.ssh_lib_map.keys():
            match = re.search(pattern, self.raw_string)
            if match:
                return self.ssh_lib_map[pattern]

        return 'unknown'
