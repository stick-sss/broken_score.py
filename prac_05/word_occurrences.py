def main():
    dictf = {}
    text = input("Text: ")
    each = text.split()
    for i in each:
        times = dictf.get(i,0)
        dictf[i] = times + 1

    each = list(dictf.keys())
    each.sort()

    for word in each:
        print("{:{}} : {}".format(word, 10, dictf[word]))

if __name__ == '__main__':
    main()