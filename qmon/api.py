from rest_framework.views import APIView
from rest_framework.response import Response
from qmon.monitor import Monitor

import humanize


class CpuAPIView(APIView):
    def get(self, request):
        return Response({"percent": Monitor.get_cpu_usage()})


class MemoryAPIView(APIView):
    def get(self, request):
        memory = Monitor.get_memory_usage()
        return Response(
            {"bytes_used": memory, "used_human": humanize.naturalsize(memory)}
        )


class DiskAPIView(APIView):
    def get(self, request):
        return Response({"percent_used": Monitor.get_disk_usage()})
