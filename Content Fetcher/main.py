import wikipedia

#Retriving content form wikipedia
def fetch(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content

print(fetch('king'))