"""
This script runs the DemoFormProject application using a development server.
"""

from os import environ
from DemoFormProject import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.config['SECRET_KEY'] = '1w234567'
    app.run(HOST, PORT)
