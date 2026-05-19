import ast

from core.semantic.ast.ast_models import (
    ASTEndpoint,
)


class EndpointDetector:
    """
    Detect API endpoints.
    """

    HTTP_METHODS = {
        "get",
        "post",
        "put",
        "delete",
        "patch",
    }

    def detect(
        self,
        node: ast.FunctionDef | ast.AsyncFunctionDef,
    ) -> list[ASTEndpoint]:
        """
        Detect framework endpoints.
        """

        endpoints = []

        for decorator in node.decorator_list:
            if not isinstance(
                decorator,
                ast.Call,
            ):
                continue

            attribute = decorator.func

            if not isinstance(
                attribute,
                ast.Attribute,
            ):
                continue

            method_name = attribute.attr.lower()

            if method_name not in self.HTTP_METHODS:
                continue

            endpoint_path = "/"

            if decorator.args:
                argument = decorator.args[0]

                if isinstance(
                    argument,
                    ast.Constant,
                ):
                    endpoint_path = str(argument.value)

            endpoints.append(
                ASTEndpoint(
                    path=endpoint_path,
                    method=method_name.upper(),
                    function_name=node.name,
                    is_async=isinstance(
                        node,
                        ast.AsyncFunctionDef,
                    ),
                    line_number=node.lineno,
                )
            )

        return endpoints
