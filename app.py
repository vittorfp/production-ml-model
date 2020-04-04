#!flask/bin/python
import os
from app import app

if __name__ == '__main__':
    app.logger.debug(os.getenv('HOST'))
    app.run(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        debug=True
    )
