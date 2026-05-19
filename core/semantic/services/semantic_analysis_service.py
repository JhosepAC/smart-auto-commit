from pathlib import Path

from core.logging.logger import (
    logger,
)
from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)
from core.semantic.ast.parser_registry import (
    ParserRegistry,
)

from core.semantic.heuristics.heuristic_engine import (
    HeuristicEngine,
)


class SemanticAnalysisService:
    """
    Execute semantic source analysis.
    """

    def __init__(
        self,
    ) -> None:
        self.registry = ParserRegistry()
        self.heuristic_engine = HeuristicEngine()

    def analyze_file(
        self,
        file_path: str | Path,
    ) -> ASTAnalysisResult | None:
        """
        Analyze source file.
        """

        path = Path(file_path)

        logger.info(("Running semantic " f"analysis for: {path}"))

        parser = self.registry.get_parser(path)

        if not parser:
            logger.warning(("No parser available " f"for: {path.suffix}"))

            return None

        result = parser.parse(path)

        heuristic_analysis = self.heuristic_engine.analyze(result)

        result.heuristic_analysis = heuristic_analysis

        logger.info(("Semantic analysis " "completed successfully"))

        return result
