import os
import sys
from os import getcwd
from os.path import join, abspath, dirname
import webview
from api import Api

api = Api()
debug = True

index_html_path = ''

if getattr(sys, 'frozen', False):
    index_html_path = abspath(dirname(join(getcwd(), '_internal/assets/')))
    print(index_html_path)
    print(abspath(join(index_html_path, 'index.html')))
    debug = False
else:
    index_html_path = abspath(dirname(__file__))
    print(index_html_path)

api.db_path = join(index_html_path, 'words_alpha.sqlite')

print('(App): App started with Test Backend.')
window = webview.create_window('CFuen Labs Detonary', abspath(join(index_html_path, 'index.html')), js_api=api)
# window = webview.create_window('CFuen Labs Detonary', html=index_html_file.read(), js_api=api)
api.window = window
webview.start(http_server=True, debug=debug)
# webview.start(http_server=True, debug=True)
print('(App): Bye!')
