from django.http import JsonResponse
from datetime import datetime, timezone

def public_api(request):
    response_data = {
        "email": "erickochieng830@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z",  # Proper ISO 8601 UTC
        "github_url": "https://github.com/Erick-Ochieng56/HNG12-api"
    }
    return JsonResponse(response_data)

# The T separates the date and time. The Z indicates that the time is in UTC.
