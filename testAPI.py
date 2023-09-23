import sqlite3
import threading
import time


class Api:
    prompt_results = []
    window = None

    def __init__(self) -> None:
        print('🐍 (API): Test Backend API started.')

    def hi(self):
        print('🐍 (API): Hi from Python!')

    def log(self, m):
        print(f'☕ (JS): {m}')

    def get_prompt_results(self):
        return self.prompt_results

    # TODO: save everything in an HTML_Words table as a series of spans (htmx philosophy!)
    def word_list_process(self):
        conn = sqlite3.connect('words_alpha.sqlite')
        self.cursor = conn.cursor()
        print('🐍 (API): Loading words_alpha.txt (Word list)...')
        with open('words_alpha.txt', 'r') as word_list_file:
            for i, line in enumerate(word_list_file):
                line = line[0:-1]
                word_list_load_progress = int((100 / 370105) * i)
                self.cursor.execute(
                    'INSERT OR REPLACE INTO Words (word) VALUES (?)', (line,))
                print(
                    f"🐍 (API): \"{line}\", {i+1} ({word_list_load_progress}%) read")
        conn.commit()
        conn.close()

    def search_prompt(self, prompt):
        print(len(self.prompt_results))
        conn = sqlite3.connect('words_alpha.sqlite')
        self.cursor = conn.cursor()
        print(f"🐍 (API): Searching words for prompt '{prompt}'")
        self.cursor.execute(
            f"SELECT word FROM Words WHERE word LIKE '{prompt}%' OR word LIKE '%{prompt}%' OR word LIKE '%{prompt}'")
        prompt_results = self.cursor.fetchall()
        print(f"🐍 (API): Query finished {len(prompt_results)}")
        conn.commit()
        conn.close()
        print(f"🐍 (API): DB Closed")
        self.prompt_results = prompt_results

    def threaded_prompt_search(self, prompt):
        thread = threading.Thread(target=self.search_prompt, args=(prompt,))
        thread.start()

    def _interval(self, time_ms, js_string):
        while True:
            self.window.evaluate_js(js_string)
            time.sleep(int(time_ms/1000))

    def set_interval(self, time_ms, js_string):
        thread = threading.Thread(target=self._interval, args=(time_ms, js_string))
        thread.start()
