import os
def main():
    while True:
        fname = getFileName()
        fh = open(fname, "r+", encoding="utf8")
        load(fh, fname)
def load(fh, fname):
    ind = 1
    items = {}
    try:
        for line in fh:
            items[line.strip()] = ind
            ind += 1
    except IOError as err:
            print("", end="")
    finally:
        processInfo(items, fh, fname)
def processInfo(items, fh, fname):
    edited = False
    numItemsChanged = 0
    while True: 
        empty = printItems(items)
        action = input(options(empty,edited)).lower()
        if action == 'a':
            empty = False
            edited = True
            add(items)
            numItemsChanged +=1
        elif action == 'd' and empty == False:
            num = int(input("Delete item number (or 0 to cancel): "))
            if num != 0:
                delete(items, num)
                edited = True
                if numItemsChanged > 0:
                    numItemsChanged -= 1
        elif action == 's' and edited == True:
            save(items, fname, numItemsChanged)
            numItemsChanged = 0
            edited = False
        elif action == 'q':
            if edited:
                if input("Save unchanged changes (y/n): ") == "y":
                    save(items, fname, numItemsChanged)
                    numItemsChanged = 0
                    edited = False
            quit(fh)
            return
        else:
            print("ERROR: invalid choice--enter one of 'AaDdSsQq")
            input("Press Enter to continue...")
def add(items):
    items[input("Add item: ")] = -1
    sort(items)
def quit(fh):
    fh.close()
def printItems(items):
    empty=True
    for item in sortedItems(items):
        if items[item] != 0:
            empty = False
            print(items[item], ": ", item, "\n", end="")
    if empty:
        print("-- no items are in the list --")
    return empty
def save(items, fname, numItemsChanged):
    fh = open(fname, "w", encoding="utf8")
    for item in sortedItems(items):
        if items[item] != 0:
            fh.write(item+"\n")
    if numItemsChanged > 0:
        print("Saved", numItemsChanged, "items to", fname)
    input("Press Enter to continue...")

def delete(items, num):
    for item in sortedItems(items):
        if items[item] == num:
            items[item] = 0
            return
def sortedItems(items):
    return sorted(items, key = lambda k: k.lower())
def sort(items):
    ind = 1
    for item in sortedItems(items):
        if items[item] != 0:
            items[item] = ind
            ind += 1
def options(empty, edited):
    str="[A]dd "
    if not empty:
        str+="[D]elete "
    if edited:
        str+="[S]ave "
    return str+"[Q]uit: "
def getFileName():
    all_files = os.listdir(".")
    fileList = []
    for file in all_files:
        if file.endswith(".lst"):
            fileList.append(file)
    list.sort(fileList, key = lambda k: k.lower())
    items = {}
    printFiles(items, fileList)
    fname = input("Choose filename: ")
    if fname.isdigit():
        return items[int(fname)]
    elif not fname.endswith(".lst"):
        return fname+".lst"
    return fname
def printFiles(items, fileList):
    ind = 1
    for file in fileList:
        items[ind] = file
        if 10 <= len(fileList) < 100:
            print(str(ind).ljust(2), end="")
        elif 100 <= len(fileList) < 1000:
            print(str(ind).ljust(3), end="")
        else:
            print(ind, end="")
        print(": ", file, end="")
        print("\n", end="")
        ind += 1
main()