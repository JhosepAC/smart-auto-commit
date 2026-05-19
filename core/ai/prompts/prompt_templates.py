COMMIT_GENERATION_TEMPLATE = """
You are an elite software architect.

Generate a professional conventional commit.

Rules:
- Output ONLY the commit.
- Use professional technical language.
- Be concise and deterministic.
- Avoid hallucinations.
- Respect conventional commits.

Repository Semantic Context:
{semantic_context}

Developer Intent:
{intent_context}

Technical Commit Context:
{commit_context}

Generate:
"""
