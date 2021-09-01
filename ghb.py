"""
Модуль с тест приложением python.
"""

from kivy.app import App
import webbrowser
import sys


url = "https://edusite.ru/"
url1 = "https://netfolio.ru"


webbrowser.open_new(url)
webbrowser.open_new_tab(url1)
sys.exit(App) 

    