from core.config import settings
from core.gunicorn import Application, get_app_options
from main import main_app


def main():
    app = Application(
        application=main_app,
        options=get_app_options(
            host=settings.gunicorn.host,
            port=settings.gunicor.port,
            timeout=settings.gunicorn.timeout,
            workers=settings.gunicorn.workers,
        ),
    )
    app.run()


if __name__ == "__main__":
    main()
