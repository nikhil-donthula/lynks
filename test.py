import webbrowser


url1 = "youtube.com"

chrome_path =  r'C:\Program Files\Google\Chrome\Application\chrome.exe'

webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url1)