from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from .models import Partner

def partners(request):
    """This is view function which return json data of partner object

    Args:
        request (<HttpRequest:>):  HttpRequest object that contains metadata about the request

    Returns:
        Json data of partners
    """
    limit = int(request.GET.get('limit')) if request.GET.get('limit') else 20
    offset = int(request.GET.get('offset')) if request.GET.get('offset') else 0
    partners = Partner.objects.all()[offset:offset + limit]
    data = {
        "ok": True,
        "menbers": [{
            "id": partner.id,
            "real_name": partner.name,
            "tz": partner.timezone,
            "activity_periods": [{
                'start_time': activity.start_datetime.strftime("%b %-d %Y %H:%M%p"),
                'end_time': activity.end_datetime.strftime("%b %-d %Y %H:%M%p")
            } for activity in partner.activity_periods.all()]
        } for partner in partners]
    }
    return JsonResponse(data)

def index(request):
    return redirect('/admin/login/?next=/admin/')