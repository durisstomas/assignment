import datetime

substring1 = '#1'
substring2 = '$2'
hash_one_words = 0
dolar_two_words = 0
var = -1
hash_one_sentences = 0
dolar_two_sentences = 0

with open('textfile.txt', mode='r') as text_file, open('hash_one.txt', mode='a') as hash_one,\
        open('dolar_two.txt', mode='a') as dolar_two, open('processing.log', mode='a') as log_file:

    log_file.write('\nstart of processing:' + str(datetime.datetime.now()))

    data = text_file.read()
    word = data.split()

    for slova in word:
        if substring1 in slova:
            if var != 0:
                hash_one_sentences = hash_one_sentences + 1
            var = 0
        elif substring2 in slova:
            if var != 1:
                dolar_two_sentences = dolar_two_sentences + 1
            var = 1

        if var == 0:
            hash_one.write(slova.removeprefix('#1') + ' ')
            hash_one_words = hash_one_words + 1
        elif var == 1:
            dolar_two.write(slova.removeprefix('$2') + ' ')
            dolar_two_words = dolar_two_words + 1

    log_file.write(' number of words in hash_one:' + str(hash_one_words) + ' number of words in dolar_two:' + str(dolar_two_words) +
                   ' numer of sentences in hash_one:' + str(hash_one_sentences) + ' number of senteces in dolar_two:' + str(dolar_two_sentences) +
                   ' end of processing:' + str(datetime.datetime.now()))

    text_file.close()
    hash_one.close()
    dolar_two.close()
    log_file.close()