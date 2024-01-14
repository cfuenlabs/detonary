import sqlite3
import threading
import time


class Api:
    prompt_results = []
    window = None
    claimed = False
    db_path = ''

    def __init__(self) -> None:
        print('(API - log): Test Backend API started.')

    def hi(self):
        print('(API - log): Hi from Python!')

    def log(self, m):
        print(f'(JS - log): {m}')

    def get_prompt_results(self):
        if self.claimed == False:
            self.claimed = True
            return self.prompt_results
        else:
            return None

    def search_prompt(self, prompt):
        print(len(self.prompt_results))
        conn = sqlite3.connect(self.db_path)
        self.cursor = conn.cursor()
        print(f"(API - search_prompt): Searching words for prompt '{prompt}'")
        self.cursor.execute(
            f"SELECT SUBSTR(word, 1,1) AS first_letter, GROUP_CONCAT(html, '') FROM Words WHERE word LIKE '{prompt}%' OR word LIKE '%{prompt}%' OR word LIKE '%{prompt}' GROUP BY first_letter;")
        prompt_results = self.cursor.fetchall()
        print(
            f"(API - search_prompt): Query finished, string is {len(prompt_results)} chars long")
        conn.commit()
        conn.close()
        print(f"(API - search_prompt): DB Closed")
        self.prompt_results = prompt_results
        self.claimed = False

    # def load_font_shitty(self, path):
    #     with open(path, 'rb') as font_file:
    #         print(f'''
    #         const fontab = new ArrayBuffer({font_file.read()});
    #         const newFont = new FontFace(fontab);
    #         document.fonts.add(newFont);
    #         ''')
    #     
    #         self.window.evaluate_js(f'''
    #         const fontab = new ArrayBuffer({font_file.read()});
    #         const newFont = new FontFace(fontab);
    #         document.fonts.add(newFont);
    #         ''')

    def threaded_prompt_search(self, prompt):
        thread = threading.Thread(target=self.search_prompt, args=(prompt,))
        thread.start()

    def _interval(self, time_ms, js_string):
        while True:
            self.window.evaluate_js(js_string)
            time.sleep(int(time_ms/1000))

    def set_interval(self, time_ms, js_string):
        thread = threading.Thread(
            target=self._interval, args=(time_ms, js_string))
        thread.start()
