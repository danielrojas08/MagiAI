import webbrowser
new = 2
tabURL = 'https://www.youtube.com/results?search_query=';
term = input("Youtube Search Querty: ")
webbrowser.open(tabURL+term, new=new);