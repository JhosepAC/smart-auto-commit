COMMIT_GENERATION_TEMPLATE = """
You are a senior software engineer.

Analyze the repository changes and generate a professional
Conventional Commit message.

Repository:
{repository_name}

Branch:
{branch_name}

Semantic Change Type:
{semantic_type}

Changed Files:
{changed_files}

Summary:
{commit_summary}

Requirements:
- Use Conventional Commits
- Be concise
- Be technically accurate
- Maximum 72 characters
- Use present tense
- Focus on engineering intent
"""
