from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    app.run(
        debug=True,
        host=os.getenv('FLASK_RUN_HOST', '127.0.0.1'),
        port=5200,
        use_reloader=False
    )
