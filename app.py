#!flask/bin/python
import os
from app import app

if __name__ == '__main__':
    app.logger.debug(os.getenv('HOST'))
    app.run(
        host=os.getenv('HOST', '0.0.0.0'),
        port=5000,
        debug=True
    )
