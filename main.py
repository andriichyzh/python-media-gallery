#!/usr/bin/env python

from webapp2 import Route, WSGIApplication


app = WSGIApplication([
    Route('/', handler='handlers.main.MainHandler'),
    Route('/assets', handler='handlers.assets.AssetsHandler')
], debug=True)
