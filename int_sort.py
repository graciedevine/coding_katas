def super_size(n):
    if len(str(n)) == 1:
        return n
    else:
        n = str(n)
        li = list(n)
        list_sorted = sorted(li, reverse=True)
        list_separated = "".join(list_sorted)
        return int(list_separated)


print(super_size(279))

# https://stackoverflow.com/questions/57273897/how-to-convert-each-character-of-a-string-into-individual-elements-of-list-eleme?noredirect=1&lq=1
# https://stackoverflow.com/questions/12453580/how-to-concatenate-items-in-a-list-to-a-single-string