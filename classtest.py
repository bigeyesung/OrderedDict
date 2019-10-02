from collections import OrderedDict

def Main():

   
    scores1 = OrderedDict({'Mary': 7, 'Jane': 9,  'Tom': 13})
    scores2 = OrderedDict({'Mary': 7, 'Jane': 35, 'Tom': 13})
    scores3 = OrderedDict({'Mary': 7, 'Jane': 22, 'Tom': 13})
    print(type(scores1))
    score = OrderedDict()
    score["1"] = scores1
    score["3"] = scores2
    score["2"] = scores3
    print(score)
    od = OrderedDict(sorted(score.items(), key=lambda item: item[1]['Jane']))
    #od = OrderedDict(sorted(d.items(), key=lambda(k,v):(v,k)))
    #phonebook_sorted = OrderedDict(sorted(score.items()))
    d = OrderedDict([(7484,
              [{'book_id': 7484,
                'book_quantity': 43,
                'condition': 'New Book',
                'id': 7484,
                'isbn_13': '9788131727591',
                'seller_book_id': 7484,
                'selling_price': 629.0,
                'title': 'Network Management:  Principles and Practice,  2/e'}]),
             (7485,
              [{'book_id': 7484,
                'book_quantity': 43,
                'condition': 'New Book',
                'id': 7484,
                'isbn_13': '9788131727591',
                'seller_book_id': 7484,
                'selling_price': 29.0,
                'title': 'Network Management:  Principles and Practice,  2/e'}])])
    for key,value in d.items():
        print(key)
        print(value)
    print(d)
    od = OrderedDict(sorted(d.items(), key=lambda item: item[1][0]['selling_price']))
    print(od)
    print(type(od))
    od = sorted(score, key=lambda x: (score[x]['Jane']))
    #score = sorted(score, key=lambda x: (score[x]['Jane']))
    print(score)

if __name__ == "__main__":
    Main()