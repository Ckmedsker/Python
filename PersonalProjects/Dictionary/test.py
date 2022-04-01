#           for line in lines:
#               if line.strip("\n") == text:
#                   destroy_main(widgets, recent_searches_list)
#                   word_page(text)
#           with open(FILE1, "r") as recent_searches:
#               searches = recent_searches.readlines()
#               searches.append(f"{text}\n")
#               print(searches)
#           with open(FILE1, "w+") as write_searches:
#               for i, j in enumerate(searches):
#                   if j != text:
#                       write_searches.write(searches[i])
#           with open(FILE1, "w+") as fp:
#               for i in searches:
#                   if i.strip("\n") == text:
#                       fp.write(f"{i}\n")