import inspect
from typing import Any

from chili import is_dataclass, init_dataclass
from chocs import HttpRequest
from chocs import HttpResponse
from chocs.middleware.middleware import Middleware, MiddlewareHandler
from chocs.routing import Route


class ParsedBodyMiddleware(Middleware):
    def __init__(self, strict: bool = False):
        self.strict = strict

    def handle(self, request: HttpRequest, next: MiddlewareHandler) -> HttpResponse:
        route = request.route
        if route and "parsed_body" in route.attributes:
            self._map_parsed_body(request, route)

        return next(request)

    def _map_parsed_body(self, request: HttpRequest, route: Route) -> None:
        if not inspect.isclass(route.attributes["parsed_body"]):
            return

        if not hasattr(request.parsed_body, "__getitem__") or not hasattr(request.parsed_body, "__iter__"):
            return

        body = request.parsed_body

        strict = route.attributes["strict"] if "strict" in route.attributes else self.strict
        constructor = route.attributes["parsed_body"]
        request._parsed_body = None

        if not strict:

            def _get_non_strict_parsed_body() -> Any:
                if not is_dataclass(constructor):
                    raise ValueError(
                        f"parsed_body argument expects valid dataclass type to be passed, {constructor} was given."
                    )
                return init_dataclass(body, constructor)  # type: ignore

            request._parsed_body_getter = _get_non_strict_parsed_body

            return

        def _get_strict_parsed_body() -> Any:
            return constructor(**body)

        request._parsed_body_getter = _get_strict_parsed_body


__all__ = ["ParsedBodyMiddleware"]
