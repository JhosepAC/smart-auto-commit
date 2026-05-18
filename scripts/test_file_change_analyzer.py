from core.git.file_change_analyzer import (
    FileChangeAnalyzer,
)


def main() -> None:
    analyzer = FileChangeAnalyzer()

    files = [
        "main.py",
        "pyproject.toml",
        "README.md",
        "core/git/diff_engine.py",
    ]

    print()

    print("File Change Analyzer")

    print("--------------------")

    print()

    for file_path in files:
        analysis = analyzer.analyze_file(file_path)

        print(f"File: {analysis.file_path}")

        print(f"Language: {analysis.language}")

        print(f"Category: {analysis.category}")

        print(f"Importance: " f"{analysis.importance_score}")

        print()

    print()


if __name__ == "__main__":
    main()
