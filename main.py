# -*- encoding: utf-8 -*-
from typing import *
from app import app


if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True, threaded=True)