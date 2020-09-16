def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "Facebook’s PyGraph is an Open Source Framework for Capturing Knowledge in Large Graphs"
    time.sleep(2)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()                         # line 14, 15 will execute line 2-5
print("Search Started")
next(search)                                # resume from line 7
print("Next method run")
search.send("Facebook")                     # resume from line 7

search.close()                              # free all the captured resources