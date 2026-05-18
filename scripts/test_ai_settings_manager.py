from core.ai.config.ai_settings import (
    AISettingsManager,
)


def main() -> None:
    manager = AISettingsManager()

    runtime = manager.get_runtime_settings()

    provider = manager.get_provider_settings(runtime.default_provider)

    print()

    print("AI Settings Manager")

    print("-------------------")

    print()

    print(f"Default Provider: " f"{runtime.default_provider}")

    print(f"Fallback Provider: " f"{runtime.fallback_provider}")

    print(f"Dry Run Enabled: " f"{runtime.dry_run_enabled}")

    print(f"Prompt Version: " f"{runtime.prompt_version}")

    print()

    print(f"Provider Model: " f"{provider.model_name}")

    print(f"Temperature: " f"{provider.temperature}")

    print(f"Max Tokens: " f"{provider.max_tokens}")

    print()


if __name__ == "__main__":
    main()
