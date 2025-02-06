def main():
    report()


def text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def number_of_words():
    count = 0
    words = text().split()
    for word in words:
        count += 1
    return count

def statistika():
    txt = text().lower()
    sta = {}
    for cha in txt:
        sta[cha] = 0
    for cha in txt:
        sta[cha] += 1
    return sta

def report():
    print("--- Begin report of books/frankenstein.txt ---")
    count = number_of_words()
    print(f"{count} words found in the document")
    print("")

    stat = statistika()
    tab = []
    j = 0
    for i in stat:
        if i.isalpha():
            tab.append({})
            tab[j]["char"] = i
            tab[j]["num"] = stat[i]
            j += 1

    def sort_on(dict):
        return dict["num"]
    tab.sort(reverse=True, key=sort_on)

    for i in tab:
        c = i["char"]
        n = i["num"]
        print(f"The '{c}' character was found {n} times")
    print("--- End report ---")
    
    

main()