from pathlib import Path

# =========================================================
# APPLICATION
# =========================================================

APPLICATION_NAME = "smart-auto-commit"

APPLICATION_VERSION = "0.1.0"


# =========================================================
# DIRECTORIES
# =========================================================

ROOT_DIRECTORY = Path.cwd()

LOGS_DIRECTORY = ROOT_DIRECTORY / "logs"

CONFIG_DIRECTORY = ROOT_DIRECTORY / "config"

TESTS_DIRECTORY = ROOT_DIRECTORY / "tests"


# =========================================================
# GIT
# =========================================================

GIT_DIRECTORY_NAME = ".git"

DEFAULT_BRANCH = "main"


# =========================================================
# AI
# =========================================================

DEFAULT_AI_PROVIDER = "ollama"

DEFAULT_AI_MODEL = "deepseek-coder"


# =========================================================
# WATCHER
# =========================================================

DEFAULT_WATCHER_DEBOUNCE_SECONDS = 10
