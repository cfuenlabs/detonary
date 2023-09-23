import webview
from testAPI import Api

api = Api()

print('🐍 (App): App started with Test Backend.')
window = webview.create_window('CFuen Labs Detonary', 'index.html', js_api=api)
api.window = window
webview.start(http_server=True, debug=True)
print('🐍 (App): Bye!')