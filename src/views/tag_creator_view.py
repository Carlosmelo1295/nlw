from src.controller.tag_creator_controller import TagCrontroller
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:
    # "->" significa o tipo da resposta.
    def validade_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCrontroller()

        body = http_request.body
        product_code = body[0]['product_code']
        response = tag_creator_controller.create(product_code)
        return HttpResponse(status_code=200, body=response)
