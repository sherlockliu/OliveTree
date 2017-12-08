from framework.handler.olive_handler import OliveHandler


class DemoHanlder(OliveHandler):
    def get(self):
        self.write("This is the demo for OliveTree.")
