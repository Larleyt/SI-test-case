import json
from itertools import islice
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.conf import settings

from .utils import lines


@api_view(["POST"])
def read_log(request):
    LOG_FILE_PATH = getattr(settings, "LOG_FILE_PATH")
    LOG_PORTION_SIZE = getattr(settings, "LOG_PORTION_SIZE")

    offset = int(request.data["offset"])
    data = []
    try:
        total_size = os.path.getsize(LOG_FILE_PATH)

        with open(LOG_FILE_PATH) as f:
            f.seek(offset)
            data = [
                json.loads(line)
                for line in islice(lines(f), LOG_PORTION_SIZE)
            ]
            next_offset = f.tell()

        return Response({
            "ok": "true",
            "next_offset": next_offset,
            "total_size": total_size,
            "messages": data
        })

    except IOError as e:
        return Response({
            "ok": "false",
            "reason": str(e)
        })

