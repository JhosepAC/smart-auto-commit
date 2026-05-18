from core.git.semantic_change_classifier import (
    SemanticChangeClassifier,
)


def main() -> None:
    classifier = SemanticChangeClassifier(".")

    classification = classifier.classify_changes()

    print()

    print("Semantic Change Classifier")

    print("--------------------------")

    print()

    print(f"Commit type: " f"{classification.commit_type}")

    print(f"Confidence: " f"{classification.confidence_score}")

    print()

    print(f"Detected patterns: " f"{classification.detected_patterns}")

    print()

    print(f"Reasoning: " f"{classification.reasoning}")

    print()


if __name__ == "__main__":
    main()
