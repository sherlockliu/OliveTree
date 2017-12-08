from framework.handler.olive_handler import OliveHandler
import app.demo.routes

routes = ()

# all routes goes here...
routes += app.demo.routes.url_pattern
routes += (
    (r'.*', OliveHandler),
)
