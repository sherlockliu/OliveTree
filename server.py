# -*- coding: utf-8 -*-

import os

from olive.app_config import APPLICATION_SETTINGS
from olive.app_config import ROOT_LOCATION
from olive.routes import routes
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.web import Application


def start_server():
    define('port', default=8000, help='run on the given port', type=int)
    define("database", default="Young", help="database to use", type=str)
    define("debug", default=False, help="whether is debug mode", type=bool)

    parse_command_line()

    APPLICATION_SETTINGS.update({
        "debug": options.debug,
        "template_path": os.path.join(
            ROOT_LOCATION,
            "app" if options.debug else "templates"
        )
    })
    application = Application(
        handlers=routes,
        **APPLICATION_SETTINGS
    )

    http_server = HTTPServer(application, xheaders=True)
    http_server.listen(options.port)

    IOLoop.instance().start()


if __name__ == '__main__':
    start_server()
