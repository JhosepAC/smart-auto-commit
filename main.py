from core.config.settings import settings


def main():
    print(settings.application.name)
    print(settings.ai.model)
    print(settings.logging.level)


if __name__ == "__main__":
    main()
