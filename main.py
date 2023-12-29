# -*- encoding: utf-8 -*-
from typing import *
from app import app, db

from app.models import *


@app.shell_context_processor
def relate_shell_context() -> Dict[str, Any]:
    return {
        'app': app,
        'db': db,
        'User': User,
        'Post': Post,
    }


if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True, threaded=True)
