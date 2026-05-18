from core.bootstrap.application import Application
from core.exceptions.decorators import safe_execution


@safe_execution
def main():
    app = Application()

    app.bootstrap()


if __name__ == "__main__":
    main()
