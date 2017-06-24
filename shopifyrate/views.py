from django.http.response import HttpResponse


def health_check(_):
    res = HttpResponse("Your app is Working!     ")
    res.status_code = 200
    res['Content-Length'] = 10
    return res
