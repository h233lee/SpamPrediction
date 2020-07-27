import pandas as pd
import numpy as np
import re
import sys


spam = pd.read_csv('SMSSpamCollection', sep = '\t', header = None, names = ['Label', 'SMS'])
spam["SMS"] = spam['SMS'].apply(lambda x: re.sub('\W',' ',x.lower()))

spam['SMS'] = spam['SMS'].str.split()
vocabulary = []

for i in spam['SMS']:
    for word in i:
        vocabulary.append(word)

vocabulary = list(set(vocabulary))

word_counts_per_sms = {unique_word: [0] * len(spam['SMS']) for unique_word in vocabulary}

for index, sms in enumerate(spam['SMS']):
    for word in sms:
        word_counts_per_sms[word][index] += 1

df = pd.DataFrame(word_counts_per_sms)

spam_clean = pd.concat([spam, df], axis=1)

p_spam = spam_clean['Label'].value_counts(normalize=True)[0]
p_ham = spam_clean['Label'].value_counts(normalize=True)[1]
n_spam = spam_clean[spam_clean['Label'] == 'spam'].iloc[:, 2:].sum().sum()
n_ham = spam_clean[spam_clean['Label'] == 'ham'].iloc[:, 2:].sum().sum()
n_vocabulary = len(vocabulary)

def calc_params(a=1):
    # Initiate parameters
    parameters_spam = {unique_word:0 for unique_word in vocabulary}
    parameters_ham = {unique_word:0 for unique_word in vocabulary}

    #split to spam and ham
    spam = spam_clean[spam_clean['Label'] == 'spam']
    ham = spam_clean[spam_clean['Label'] == 'ham']

    for v in vocabulary:
        wi_given_spam = spam[v].sum()
        parameters_spam[v] = (wi_given_spam+a)/(n_spam + a*n_vocabulary)

        wi_given_ham = ham[v].sum()
        parameters_ham[v] = (wi_given_ham+a)/(n_ham + a*n_vocabulary)

    return(parameters_spam, parameters_ham)


parameters_spam, parameters_ham = calc_params()

def classify(message):

    message = re.sub('\W', ' ', message)
    message = message.lower()
    message = message.split()

    p_spam_given_message = p_spam
    p_ham_given_message = p_ham

    for word in message:
        if word in parameters_spam:
            p_spam_given_message *= parameters_spam[word]
        else:
            next

        if word in parameters_ham:
            p_ham_given_message *= parameters_ham[word]
        else:
            next

    if p_ham_given_message > p_spam_given_message:
        return 'Not Spam'
    elif p_spam_given_message > p_ham_given_message:
        return 'SPAM!'
    else:
        return 'needs human classification'

print(classify(sys.argv[1]))
