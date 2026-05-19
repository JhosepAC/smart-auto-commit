from core.semantic.ast.ast_models import (
    RepositoryEvolutionProfile,
    RepositorySemanticContext,
    SemanticIntentProfile,
)

from core.semantic.intent.architectural_intent_analyzer import (
    ArchitecturalIntentAnalyzer,
)

from core.semantic.intent.behavioral_reasoner import (
    BehavioralReasoner,
)

from core.semantic.intent.developer_intent_detector import (
    DeveloperIntentDetector,
)

from core.semantic.intent.implementation_purpose_detector import (
    ImplementationPurposeDetector,
)

from core.semantic.intent.intent_synthesizer import (
    IntentSynthesizer,
)

from core.semantic.intent.semantic_goal_classifier import (
    SemanticGoalClassifier,
)


class IntentEngine:
    """
    Advanced semantic intent engine.
    """

    def __init__(
        self,
    ) -> None:
        self.intent_detector = DeveloperIntentDetector()

        self.architecture_analyzer = ArchitecturalIntentAnalyzer()

        self.behavioral_reasoner = BehavioralReasoner()

        self.goal_classifier = SemanticGoalClassifier()

        self.purpose_detector = ImplementationPurposeDetector()

        self.synthesizer = IntentSynthesizer()

    def analyze(
        self,
        context: RepositorySemanticContext,
        evolution_profile: RepositoryEvolutionProfile,
    ) -> SemanticIntentProfile:
        """
        Analyze semantic developer intent.
        """

        primary, secondary = self.intent_detector.detect(context)

        architectural_intention = self.architecture_analyzer.analyze(context)

        implementation_goal = self.purpose_detector.detect(context)

        semantic_objective = self.goal_classifier.classify(context)

        behavioral_reasoning = self.behavioral_reasoner.reason(evolution_profile)

        profile = SemanticIntentProfile(
            primary_intent=primary,
            secondary_intents=secondary,
            architectural_intention=(architectural_intention),
            implementation_goal=(implementation_goal),
            behavioral_reasoning=(behavioral_reasoning),
            semantic_objective=(semantic_objective),
            ai_intent_context="",
        )

        profile.ai_intent_context = self.synthesizer.build_context(profile)

        return profile
