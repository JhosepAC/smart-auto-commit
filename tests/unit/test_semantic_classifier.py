from core.git.semantic_change_classifier import (
    SemanticChangeClassifier,
)


def test_classify_changes():
    classifier = SemanticChangeClassifier(".")

    classification = classifier.classify_changes()

    assert classification is not None


def test_commit_type():
    classifier = SemanticChangeClassifier(".")

    classification = classifier.classify_changes()

    assert isinstance(
        classification.commit_type,
        str,
    )


def test_confidence_score():
    classifier = SemanticChangeClassifier(".")

    classification = classifier.classify_changes()

    assert classification.confidence_score > 0
