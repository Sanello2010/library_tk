from tkinter import *
from os import listdir


def write_files(dict_lib, dict_ind, dict_insp):
    with open('library/lib.txt', 'w') as lib:  # I am making the new file for entire library.
        for r in dict_lib:
            lib.write((str(r) + ',' + str(dict_lib[r]) + '\n').replace('{', ' ').replace('}', '').replace("'",
                                                                                                          ''))  # I write entire library. The books names was encoded.
    with open('library/encode.txt', 'w') as encoding_b:  # Here I am making the file to decoding search results.
        for m in dict_ind:
            encoding_b.write(str(m) + ' ' + str(dict_ind[m]) + '\n')
    with open('library/inspect.txt', 'w') as insp:  # Here I am making the file to decoding search results.
        for m1 in dict_insp:
            insp.write(str(m1) + ' ' + str(dict_insp[m1]) + '\n')


def read_lib():
    dict_all = {}
    with open('library/lib.txt',
              'r') as lib1:  # Here I am reading the file with the saved information of the entire library.
        var1 = []
        var2 = set()
        for p in lib1:
            var1 = p.replace(',', '').replace("'", '').rstrip().split(' ', maxsplit=1)
            var2 = set(var1[1].split())
            dict_all[var1[0]] = var2
    return dict_all


def read_enc():
    dict_i = {}
    set_b = set()
    code = []
    with open('library/encode.txt',
              'r') as encoding_b:  # Here I am reading the file with decoding information to the new dictionary.
        for a in encoding_b:
            code = a[:-1].split()
            dict_i[int(code[0])] = code[1]
            set_b.add(code[1])
    return dict_i, set_b


def read_insp():
    dict_insp = {}
    with open('library/inspect.txt',
              'r') as insp:  # Here I am reading the file with decoding information to the new dictionary.
        for a in insp:
            code = a[:-1].split()
            dict_insp[code[0]] = int(code[1])
    return dict_insp

    ######################################################################


lib_files = listdir('library')
books = listdir('books')  # 'HW_dict/books/'
dict_index = {}
dict_index_inspect = {}
dict11 = {}
content = set()

if 'lib.txt' and 'encode.txt' and 'inspect.txt' not in lib_files:

    for book in enumerate(books):
        dict_index[book[0]] = book[1]  # There is dictionary for decoding.
        dict_index_inspect[book[1]] = book[0]  # There is dictionary for inspecting the library.
        with open('books/' + book[1], encoding='1251') as book1:  # 'HW_dict/books/'
            try:
                content = set(book1.read().lower().replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('-',
                                                                                                                 ' ').replace(
                    '?', ' ').replace('"', ' ').replace(':', ' ').replace(';', ' ').replace(')', ' ').replace('(',
                                                                                                              ' ').split())
            except:
                print('Error')
            else:
                for word in content:
                    if word in dict11:
                        dict11[word].add(book[0])
                    else:
                        dict11[word] = {book[0]}
    write_files(dict11, dict_index, dict_index_inspect)

    ###################################################################### There is check books in library


def fun4(event):
    books_check = listdir('books')
    dict_index1 = {}
    set_books = set()
    dict_all_books = {}
    # try:
    dict_all_books = read_lib()
    dict_index1, set_books = read_enc()
    dict_index_inspect = read_insp()
    # except:
    #    print('Error in reading files')

    checkset = {b for b in books_check}

    set_off = set()
    set_add = set()
    code_off = []
    content = set()
    dict_add = {}
    del_items = []

    if not set_books ^ checkset:
        print('You have the current library')
        text2.delete(0.0, END)
        text2.insert(1.1, 'You have the current library')
    else:
        if len(set_books) > len(checkset):  # There is the script for removing missing books
            if len(set_books) - len(checkset) == 1:
                print('Any book was deleted')
                text2.delete(0.0, END)
                text2.insert(1.1, 'Any book was deleted')
            else:
                print('Any books were deleted')
                text2.delete(0.0, END)
                text2.insert(1.1, 'Any books were deleted')
            set_off = set_books - checkset

            try:
                for r in set_off:
                    code_off.append(dict_index_inspect[r])
                    del dict_index_inspect[r]
            except:
                print('Error insp')

            for r1 in code_off:
                del dict_index1[r1]
            for r2 in dict_all_books:
                for r3 in code_off:
                    if str(r3) in dict_all_books[r2]:
                        dict_all_books[r2].remove(str(r3))
                if not len(dict_all_books[r2]):
                    del_items.append(r2)
            if del_items:
                for r4 in del_items:
                    del dict_all_books[r4]

            write_files(dict_all_books, dict_index1, dict_index_inspect)  # Here I am makimg the  corrected files.

        else:
            set_add = checkset - set_books
            if len(checkset) - len(set_books) == 1:
                print('Any book was added')
                text2.delete(0.0, END)
                text2.insert(1.1, 'Any book was added')
            else:
                print('Any books were added')
                text2.delete(0.0, END)
                text2.insert(1.1, 'Any books were added')
            number = 0
            for t1 in set_add:
                while number in dict_index1:
                    number += 1
                    if number > 1000:
                        brake
                dict_index_inspect[t1] = number
                dict_index1[number] = t1
                dict_add[number] = t1
                for book11 in dict_add:
                    with open('books/' + dict_add[book11], encoding='1251') as book1:  # 'HW_dict/books/'
                        try:
                            content = set(
                                book1.read().lower().replace(',', ' ').replace('.', ' ').replace('-', ' ').replace('!',
                                                                                                                   ' ').replace(
                                    '?', ' ').replace('"', ' ').replace(':', ' ').replace(';', ' ').replace(')',
                                                                                                            ' ').replace(
                                    '(', ' ').split())
                        except:
                            print('Error')
                        else:
                            for word in content:
                                if word in dict_all_books:
                                    dict_all_books[word].add(book11)
                                else:
                                    dict_all_books[word] = {book11}

            write_files(dict_all_books, dict_index1, dict_index_inspect)  # Here I am makimg the  corrected files.


############################################################## searching for recomendations

def fun3(event):
    set_books1 = set()
    result1 = ''
    keyword = list_words_e.get()
    list_w = keyword.replace(',', '').replace('.', '').split()
    print(list_w)

    dict_all_books1 = {}
    dict_index2 = {}

    dict_all_books1 = read_lib()
    dict_index2, _ = read_enc()
    # print(dict_index2)
    try:
        set_books1 = frozenset(dict_all_books1[list_w[0]])

        for i in list_w[1:]:
            set_books1 &= frozenset(dict_all_books1[i])
    except:
        print('Key error')
    set_books = {int(z) for z in set_books1}

    list_decode = [dict_index2[t] for t in set_books]

    text1.delete(0.0, END)
    for recom in list_decode:
        result1 += recom + "\n"
        # print(recom)
    # print(result1)
    text1.insert(1.1, result1)

    with open('library/result.txt', 'w') as result:
        result.write(str(list_w).lstrip("[").rstrip("]").replace("'", '') + '|' + str(list_decode).lstrip("[").rstrip(
            "]").replace("'", '').replace("/", '').replace('"', ''))
    text2.delete(0.0, END)
    text2.insert(1.1, 'Searching results')


##############################################################   load last search

def fun5(event):
    old_search = ''
    last_search = ''
    with open('library/result.txt', 'r') as result1:
        old_search = result1.read().split('|')
    text1.delete(0.0, END)
    last_search = old_search[0] + '\n' + old_search[1]
    text1.insert(1.1, last_search)
    text2.delete(0.0, END)
    text2.insert(1.1, 'Previous results uploaded')


##############################################################   tkinter
root = Tk()
root.title('Library')

# search_1 = Label(text='Enter ', width=30)

key_words = Label(text='Enter keyword or keywords', width=20)
key_words.grid(row=0, column=0)

button1 = Button(text='Search', width=20, height=2)
button1.grid(row=0, column=3, rowspan=1)

button2 = Button(text='Check', width=20, height=2)
button2.grid(row=1, column=3, rowspan=2)

button3 = Button(text='Load last search', width=20, height=2)
button3.grid(row=3, column=3, rowspan=1)

list_words_e = Entry(width=40)
list_words_e.grid(row=0, column=1)

res = Label(width=20)
res.grid(row=2, column=0, columnspan=2)

text1 = Text(width=50, height=10)
text1.grid(row=3, column=0, columnspan=3)

text2 = Text(width=50, height=1)
text2.grid(row=4, column=0, columnspan=3)

button1.bind('<Button-1>', fun3)
button2.bind('<Button-1>', fun4)
button3.bind('<Button-1>', fun5)

root.mainloop()