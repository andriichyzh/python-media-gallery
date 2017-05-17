
from framework.request_handler import TemplateRequestHandler
from models.assets import Assets


class MainHandler(TemplateRequestHandler):

    def get(self):
        assets = Assets.query().order(-Assets.timestamp).fetch()
        self.render('main.html', {'assets': assets})
