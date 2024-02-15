from src.views.http_types.http_response import HttpResponse


def error_handle(err: Exception, status: int) -> HttpResponse:
    response = {"error": {"status": status, "message": f'{err}'}}
    return HttpResponse(status_code=status, body=response)
