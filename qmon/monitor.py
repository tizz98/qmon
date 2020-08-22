import psutil


class Monitor:
    @staticmethod
    def get_cpu_usage():
        """Returns the CPU percent usage, 0-100"""
        return psutil.cpu_percent()

    @staticmethod
    def get_memory_usage():
        """Returns the memory usage in bytes"""
        return psutil.virtual_memory().used

    @staticmethod
    def get_disk_usage(path="/"):
        """Returns the disk usage percent, 0-100"""
        return psutil.disk_usage(path).percent
