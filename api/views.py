from django.http import JsonResponse
from datetime import datetime
import pytz

def public_api(request):
    response_data = {
        "email": "erickochieng830@gmail.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/yourusername/your-repo"
    }
    return JsonResponse(response_data)

# The T separates the date and time. The Z indicates that the time is in UTC.
