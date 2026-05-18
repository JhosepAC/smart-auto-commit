from core.git.file_change_analyzer import (
    FileChangeAnalyzer,
)


def test_analyze_python_file():
    analyzer = FileChangeAnalyzer()

    analysis = analyzer.analyze_file("main.py")

    assert analysis.language == "Python"


def test_detect_documentation():
    analyzer = FileChangeAnalyzer()

    analysis = analyzer.analyze_file("README.md")

    assert analysis.is_documentation_file is True


def test_importance_score():
    analyzer = FileChangeAnalyzer()

    analysis = analyzer.analyze_file("core/git/diff_engine.py")

    assert analysis.importance_score > 0
