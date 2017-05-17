import jinja2
import os

from webapp2 import RequestHandler


class TemplateRequestHandler(RequestHandler):

    template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
    template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

    def render(self, template, data):
        template = self.template_env.get_template(template)
        html = template.render(data)
        self.response.write(html)
