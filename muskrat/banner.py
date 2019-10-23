import re


class Banner:
    def __init__(self, raw_string):
        self.raw_string = raw_string

    def ssh_version(self):
        pattern = r"SSH-(\d+[\.\d+]+)"
        match = re.search(pattern, self.raw_string)
        if match:
            return float(match[1])
        else:
            return "unknown"
