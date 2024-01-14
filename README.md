<p align="center">
    <img width="500px" src="./Detonary_Transparent_Thin.png">
</p>

<!-- python pywebview -->

<p align="center">
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
<a href="https://pywebview.flowrl.com/"><img src="https://img.shields.io/badge/PyWebview-455b66?style=for-the-badge&logo=python&logoColor=83c99e"/></a>
</p>

<p align="center">
A bombastic word search engine to train for the Roblox game Word Bomb!
</p>

# What?

Detonary is a desktop app for looking up words you can use in the Roblox game Word Bomb. All you gotta do is search up a combination of letters and the app will return a neat list of words (sorted alphabetically and, by default, will show you words that begin with an 'A' first).

The app is optimized to be as fast as possible (You will be able to access a list with thousands of words in seconds!) and will continue to improve on it's performance as new releases roll out.

# Why?

I would take the time to look for the words online myself, but other than being a fun project that can help me become a better software engineer, an efficient (blazingly fast 🤓) app that you can launch locally to explore new words between Word Bomb matches is much more comfy than having to look up through slow online dictionaries.

# How?

This app is powered by
- PyWebview: A framework for building desktop apps with Python as a Backend and Web Technologies as the Frontend/UI 🐍
- An SQLite3 database that contains 40k english words 🗃️
- A Lua Script that fills the database up with 40k english words taken from [a .txt file I found online](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) 🌙
- Love and a passion for both Roblox and Software Engineering ❤️

# I want it!

- Go to the [releases](https://github.com/cfuenlabs/detonary/releases) page and grab the lastest release, which will be a .zip file with an executable called `detonary.exe` and a folder called `_internal` with bunch of stuff in it.

- Extract the contents wherever you like, ignore that the `_internal` folder exists and click on the `detonary.exe` executable file to start the app

- Type letters and enjoy word-searching!

# I want to help!

If you want to help, there's two main things you can do to volunteer without contributing code:

- Try to test as much word results from Detonary as possible (By using them in Word Bomb) and, if you happen to find any words that don't work and haven't yet been reported as a [GitHub Issue](https://github.com/cfuenlabs/detonary/issues), open an issue reporting any words you find! (If you find more than just 1 word, open an issue and report the batch of unsupported words you discovered, rather than opening 1 individual issue for every word you find)

- Use the app as you normally would and report any bugs you find as a [GitHub Issue](https://github.com/cfuenlabs/detonary/issues)