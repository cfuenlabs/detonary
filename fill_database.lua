local sqlite3 = require("lsqlite3")

local function create_db()
    local conn = sqlite3.open('words_alpha.sqlite')
    local file = io.open('tables.sql', 'r')
    local sql = file:read("*a")
    file:close()
    conn:exec(sql)
    conn:close()
end

local function word_list_process()
    local conn = sqlite3.open('words_alpha.sqlite')
    print('🐍 (API): Loading words_alpha.txt (Word list)...')
    local i = 0  -- Initialize i outside the loop
    for line in io.lines('words_alpha.txt') do
        i = i + 1  -- Increment i for each iteration
        line = line:sub(1, -2)
        local word_html = '<div class="Word">'
        for j = 1, #line do
            word_html = word_html .. '<span class="Letter Typed">' .. line:sub(j, j) .. '</span>'
        end
        word_html = word_html .. '</div>'
        conn:exec(string.format("INSERT OR REPLACE INTO Words (word, html) VALUES ('%s', '%s')", line, word_html))
        print(string.format("🐍 (fill_database): \"%s\", %d (%.2f%%) read", line, i, (i / 370105) * 100))
        print(string.format("🐍 (fill_database): \"%s\" html: \n%s", line, word_html))
    end
    conn:close()
end

create_db()
word_list_process()