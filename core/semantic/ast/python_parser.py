import ast
from pathlib import Path

from core.semantic.analyzers.architecture_detector import (
    ArchitectureDetector,
)
from core.semantic.analyzers.endpoint_detector import (
    EndpointDetector,
)
from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
    ASTClass,
    ASTFunction,
    ASTImport,
)
from core.semantic.ast.base_parser import (
    BaseASTParser,
)


class PythonASTParser(
    BaseASTParser,
):
    """
    Python semantic AST parser.
    """

    SUPPORTED_EXTENSIONS = {
        ".py",
    }

    FRAMEWORK_IMPORTS = {
        "fastapi": "FastAPI",
        "flask": "Flask",
        "django": "Django",
    }

    def __init__(
        self,
    ) -> None:
        self.endpoint_detector = EndpointDetector()

        self.architecture_detector = ArchitectureDetector()

    def parse(
        self,
        file_path: Path,
    ) -> ASTAnalysisResult:
        """
        Parse Python AST.
        """

        source = file_path.read_text(
            encoding="utf-8",
        )

        tree = ast.parse(source)

        functions = []

        classes = []

        imports = []

        frameworks = set()

        endpoints = []

        for node in ast.walk(tree):
            if isinstance(
                node,
                ast.FunctionDef,
            ):
                extracted_function = self._extract_function(node)

                functions.append(extracted_function)

                endpoints.extend(self.endpoint_detector.detect(node))

            elif isinstance(
                node,
                ast.AsyncFunctionDef,
            ):
                extracted_function = self._extract_async_function(node)

                functions.append(extracted_function)

                endpoints.extend(self.endpoint_detector.detect(node))

            elif isinstance(
                node,
                ast.ClassDef,
            ):
                classes.append(self._extract_class(node))

            elif isinstance(
                node,
                (
                    ast.Import,
                    ast.ImportFrom,
                ),
            ):
                extracted_imports = self._extract_imports(node)

                imports.extend(extracted_imports)

                for imported in extracted_imports:
                    framework = self.FRAMEWORK_IMPORTS.get(imported.module.lower())

                    if framework:
                        frameworks.add(framework)

        architectural_components = self.architecture_detector.detect(classes)

        return ASTAnalysisResult(
            file_path=str(file_path),
            language="Python",
            functions=functions,
            classes=classes,
            imports=imports,
            detected_frameworks=(list(frameworks)),
            endpoints=endpoints,
            architectural_components=(architectural_components),
        )

    def _extract_function(
        self,
        node: ast.FunctionDef,
    ) -> ASTFunction:
        """
        Extract function node.
        """

        return ASTFunction(
            name=node.name,
            is_async=False,
            decorators=[
                self._get_decorator_name(decorator)
                for decorator in (node.decorator_list)
            ],
            arguments=[argument.arg for argument in (node.args.args)],
            line_number=node.lineno,
        )

    def _extract_async_function(
        self,
        node: ast.AsyncFunctionDef,
    ) -> ASTFunction:
        """
        Extract async function node.
        """

        return ASTFunction(
            name=node.name,
            is_async=True,
            decorators=[
                self._get_decorator_name(decorator)
                for decorator in (node.decorator_list)
            ],
            arguments=[argument.arg for argument in (node.args.args)],
            line_number=node.lineno,
        )

    def _extract_class(
        self,
        node: ast.ClassDef,
    ) -> ASTClass:
        """
        Extract class node.
        """

        methods = [
            child.name
            for child in node.body
            if isinstance(
                child,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                ),
            )
        ]

        return ASTClass(
            name=node.name,
            base_classes=[self._resolve_name(base) for base in node.bases],
            methods=methods,
            decorators=[
                self._get_decorator_name(decorator)
                for decorator in (node.decorator_list)
            ],
            line_number=node.lineno,
        )

    def _extract_imports(
        self,
        node: ast.AST,
    ) -> list[ASTImport]:
        """
        Extract import nodes.
        """

        imports = []

        if isinstance(
            node,
            ast.Import,
        ):
            for imported in node.names:
                imports.append(
                    ASTImport(
                        module=imported.name,
                        imported_names=[],
                        line_number=node.lineno,
                    )
                )

        elif isinstance(
            node,
            ast.ImportFrom,
        ):
            imports.append(
                ASTImport(
                    module=node.module or "",
                    imported_names=[imported.name for imported in (node.names)],
                    line_number=node.lineno,
                )
            )

        return imports

    def _get_decorator_name(
        self,
        decorator: ast.AST,
    ) -> str:
        """
        Resolve decorator name.
        """

        if isinstance(
            decorator,
            ast.Name,
        ):
            return decorator.id

        return ast.dump(decorator)

    def _resolve_name(
        self,
        node: ast.AST,
    ) -> str:
        """
        Resolve AST node name.
        """

        if isinstance(
            node,
            ast.Name,
        ):
            return node.id

        return ast.dump(node)
