import re
import matplotlib.pyplot as mpl
import collections
from matplotlib.backends.backend_pdf import PdfPages

#############################################

def sentiment_analysis(text_for_analysis):
    main_sentiment = 0
    for token in text_for_analysis:
        if token in wordlist_positive:
            main_sentiment += 1
        elif token in wordlist_negative:
            main_sentiment -= 1
    return (main_sentiment)

def negative_counter(text_for_analysis):
    negative_count = 0
    for word in text_for_analysis:
        if word in wordlist_negative:
            negative_count +=1
    return negative_count

def positive_counter(text_for_analysis):
    positive_count = 0
    for word in text_for_analysis:
        if word in wordlist_positive:
            positive_count +=1
    return positive_count

def neutral_counter (text_for_analysis):
    neutral_count = 0
    for word in text_for_analysis:
        if word not in wordlist_positive and word not in wordlist_negative:
            neutral_count +=1
    return neutral_count

def overall_sentiment():
    if (sentiment_analysis(text_for_analysis)) == 0:
        print ("""The sentiment is NEUTRAL (0)""")
        decision = input ("""Would you like to see the details and charts? Y/N
        """)
        if decision == "Y":
            one_Y_decision()

            decision = input("""Would you like to save the data to a file? Y/N
            """)
            if decision == 'Y':
                save_data()


    elif (sentiment_analysis(text_for_analysis)) > 0:
        print ("""The sentiment is POSITIVE (""" + str((sentiment_analysis(text_for_analysis))) + ')')
        decision = input ("""Would you like to see the details and charts? Y/N
        """)
        if decision == "Y":
            one_Y_decision()
            decision = input("""Would you like to save the data to a file? Y/N
                        """)
            if decision == 'Y':
                save_data()

    elif (sentiment_analysis(text_for_analysis)) < 0:
        print("""The sentiment is NEGATIVE (""" + str((sentiment_analysis(text_for_analysis))) + ')')
        decision = input ("""Would you like to see the details and charts? Y/N
        """)
        if decision == "Y":
            one_Y_decision()
            decision = input("""Would you like to save the data to a file? Y/N
                        """)
            if decision == 'Y':
                save_data()

def most_common_words(text_for_analysis):
    counter = collections.Counter(text_for_analysis)
    return counter.most_common()


def one_Y_decision():
    print("""% of Positive Words: """ + str(poz_per) + """%""")
    print("""% of Negative Words: """ + str(neg_per) + """%""")
    print("""% of Neutral Words: """ + str(neu_per) + """%""")
    sentiment_chart(text_for_analysis, False)
    print("""Most common negative words are: """)
    print(most_common_words(text_negative))
    most_common_chart_negative(text_negative, False)
    print("""Most common positive words are: """)
    print (most_common_words(text_positive))
    most_common_chart_positive(text_positive, False)
    print("""Most common neutral words are: """)
    print (most_common_words(text_neutral))
    most_common_chart_neutral(text_neutral, False)


def sentiment_chart(text_for_analysis, save, name = False):

    neg_per = negative_counter(text_for_analysis)/(negative_counter(text_for_analysis) + positive_counter(text_for_analysis) + neutral_counter(text_for_analysis)) * 100
    poz_per = positive_counter(text_for_analysis)/(negative_counter(text_for_analysis) + positive_counter(text_for_analysis) + neutral_counter(text_for_analysis)) * 100
    neu_per = neutral_counter(text_for_analysis)/(negative_counter(text_for_analysis) + positive_counter(text_for_analysis) + neutral_counter(text_for_analysis)) * 100
    x_axis_pr = ['Negative','Positive','Neutral']
    y_axis_pr = [neg_per, poz_per, neu_per]
    mpl.pie(y_axis_pr, labels = x_axis_pr, autopct = '%.1f%%')
    mpl.title('% of sentiment')
    mpl.grid(True)
    mpl.minorticks_on()
    mpl.ylabel('% of Words')
    if save == False:
        mpl.show()
    elif save == True:
        mpl.savefig((str(re.sub('.txt','', name))+ '_percentage.pdf'))
    mpl.clf()



def most_common_chart_negative(text_for_analysis, save, name = False):
    y_axis_ne =[]
    x_axis_ne = []
    if len(most_common_words(text_for_analysis))<10:
        for i in range (len(most_common_words(text_for_analysis))):
            y_axis_ne.append(most_common_words(text_for_analysis)[i][1])
            x_axis_ne.append(most_common_words(text_for_analysis)[i][0])
    if len(most_common_words(text_for_analysis))>=10:
        for i in range (10):
            y_axis_ne.append(most_common_words(text_for_analysis)[i][1])
            x_axis_ne.append(most_common_words(text_for_analysis)[i][0])
    mpl.bar(x_axis_ne, y_axis_ne)
    mpl.xticks(x_axis_ne, x_axis_ne, rotation='vertical')
    mpl.title('Most common negative words')
    mpl.grid(True)
    mpl.minorticks_on()
    mpl.ylabel('Number of words')
    if save == False:
        mpl.show()
    elif save == True:
        mpl.savefig((str(re.sub('.txt', '', name)) + '_negative.pdf'))
    mpl.clf()


def most_common_chart_positive(text_for_analysis, save, name = False):
    y_axis_po =[]
    x_axis_po = []
    if len(most_common_words(text_for_analysis))<10:
        for i in range (len(most_common_words(text_for_analysis))):
            y_axis_po.append(most_common_words(text_for_analysis)[i][1])
            x_axis_po.append(most_common_words(text_for_analysis)[i][0])
    if len(most_common_words(text_for_analysis))>=10:
        for i in range (10):
            y_axis_po.append(most_common_words(text_for_analysis)[i][1])
            x_axis_po.append(most_common_words(text_for_analysis)[i][0])
    mpl.bar(x_axis_po, y_axis_po)
    mpl.xticks(x_axis_po, x_axis_po, rotation='vertical')
    mpl.title('Most common positive words')
    mpl.grid(True)
    mpl.minorticks_on()
    mpl.ylabel('Number of words')
    if save == False:
        mpl.show()
    elif save == True:
        mpl.savefig((str(re.sub('.txt', '', name)) + '_positive.pdf'))
    mpl.clf()

def most_common_chart_neutral(text_for_analysis, save, name = False):
    y_axis_nu =[]
    x_axis_nu = []
    if len(most_common_words(text_for_analysis))<10:
        for i in range (len(most_common_words(text_for_analysis))):
            y_axis_nu.append(most_common_words(text_for_analysis)[i][1])
            x_axis_nu.append(most_common_words(text_for_analysis)[i][0])
    if len(most_common_words(text_for_analysis))>=10:
        for i in range (10):
            y_axis_nu.append(most_common_words(text_for_analysis)[i][1])
            x_axis_nu.append(most_common_words(text_for_analysis)[i][0])
    mpl.bar(x_axis_nu, y_axis_nu)
    mpl.xticks(x_axis_nu, x_axis_nu, rotation='vertical')
    mpl.title('Most common neutral words')
    mpl.grid(True)
    mpl.minorticks_on()
    mpl.ylabel('Number of words')
    if save == False:
        mpl.show()
    elif save == True:
        mpl.savefig((str(re.sub('.txt', '', name)) + '_neutral.pdf'))
    mpl.clf()

def save_data():
    filename = str(input("Enter the name or the path of the file: "))
    file = open (filename, 'w')
    file.write("""% of Positive Words: """ + str(poz_per) + """%\n""" )
    file.write("""% of Negative Words: """ + str(neg_per) + """%\n""")
    file.write("""% of Neutral Words: """ + str(neu_per) + """%\n""")

    if number == 3 or number == 4:
        file.write("""The keyword is: """ + str(keyword) + """\n""")
        file.write("""Sentences with the keyword are: """ + """\n""")
        for sentence in keyword_sentences:
            file.write(sentence)
        file.write("""\n""")
        file.write("""\n""")

    file.write("""Most common negative words are: \n""")
    for element in range (len(most_common_words(text_negative))):
        for x in most_common_words(text_negative)[element]:
            file.write(str(x))
            file.write(' ')
    file.write('\n')
    file.write('\n')
    file.write("""Most common positive words are: \n""")
    for element in range (len(most_common_words(text_positive))):
        for x in most_common_words(text_positive)[element]:
            file.write(str(x))
            file.write(' ')
    file.write('\n')
    file.write('\n')
    file.write("""Most common neutral words are: \n""")
    for element in range (len(most_common_words(text_neutral))):
        for x in most_common_words(text_neutral)[element]:
            file.write(str(x))
            file.write(' ')
    file.close()


#    most_common_chart_positive(text_for_analysis, True, filename)
#    most_common_chart_negative(text_for_analysis, True, filename)
#    most_common_chart_neutral(text_for_analysis, True, filename)
#    sentiment_chart(text_for_analysis, True, filename)

def text_sort(text_for_analysis):
    text_negative = []
    for i in text_for_analysis:
        if i in wordlist_negative:
            text_negative.append(i)
    text_positive = []
    for i in text_for_analysis:
        if i in wordlist_positive:
            text_positive.append(i)
    text_neutral = []
    for i in text_for_analysis:
        if i not in text_positive and i not in text_negative:
            text_neutral.append(i)
    return text_negative, text_positive, text_neutral


def percentages ():
    neg_per = negative_counter(text_for_analysis) / (negative_counter(text_for_analysis) + positive_counter(text_for_analysis) + neutral_counter(text_for_analysis)) * 100
    poz_per = positive_counter(text_for_analysis) / (negative_counter(text_for_analysis) + positive_counter(text_for_analysis) + neutral_counter(text_for_analysis)) * 100
    neu_per = neutral_counter(text_for_analysis) / (negative_counter(text_for_analysis) + positive_counter(text_for_analysis) + neutral_counter(text_for_analysis)) * 100
    return  neg_per, poz_per, neu_per

def open_file(path):
    text = open((path), 'r')
    text_list = str(text.read()).lower()
    text.close()
    text_for_analysis = re.sub(r'[^\w\s\']', '', text_list)  # deleting punctuation
    text_for_analysis = re.split('[^\w]', text_for_analysis)
    while '' in text_for_analysis:
        text_for_analysis.remove('')
    return  text_for_analysis
#####################################################

# to load negative words
wordlist_negative = set()
wordlist_negative_file = open(r'C:\Users\Ja\PycharmProjects\Sentiment_Analisys\negative_words.txt','r')
for line in wordlist_negative_file:
    wordlist_negative.add(line.strip())
wordlist_negative_file.close()

# to load positive words
wordlist_positive = set()
wordlist_positive_file = open(r'C:\Users\Ja\PycharmProjects\Sentiment_Analisys\positive_words.txt','r')
for line in wordlist_positive_file:
    wordlist_positive.add(line.strip())
wordlist_positive_file.close()

#to load stopwords
stopwords = set()
stopwords_file = open(r'C:\Users\Ja\PycharmProjects\Sentiment_Analisys\stopwords.txt','r')
for line in stopwords_file:
    stopwords.add(line.strip())
stopwords_file.close()

################################################

print ("""Welcome to Simple Sentiment Analysis Tool
*** MENU ***
1. Sentiment Analysis (with stopwords)
2. Sentiment Analysis (without stopwords)
3. Keywords Analysis (with stopwords)
4. Keywords Analysis (without stopwords)
""")

number = int(input("Select a number: "))
if number == 1:
    path = input ("Enter the path to the file: "
                  "")
    text_for_analysis = open_file(path)
    neg_per, poz_per, neu_per = percentages()
    text_negative, text_positive, text_neutral = text_sort(text_for_analysis)
    overall_sentiment()

elif number == 2:
    path = input("Enter the path to the file: "
                 "")
    text_for_analysis = open_file(path)
    for element in text_for_analysis:
        if element in stopwords:
            text_for_analysis.remove(element)
    neg_per, poz_per, neu_per = percentages()
    text_negative, text_positive, text_neutral = text_sort(text_for_analysis)
    overall_sentiment()

elif number == 3:
    keyword = input("Enter the keywords you are looking for: "
                    "")
    path = input("Enter the path to the file: "
                 "")
    text = open((path), 'r')
    sentence_text = str(text.read())
    text.close()

    sentence_text = re.sub(r'[\n]', '', sentence_text)
    sentence_text = re.split('[.!?]', sentence_text)
    keyword_sentences = []
    for sentence in sentence_text:
        sentence_text_temp = re.split(' ', sentence)
        if keyword in sentence_text_temp:
            keyword_sentences.append(sentence)
    print("""Sentences with the keyword are:
    """)
    for sentence in keyword_sentences:
        print (sentence)
    text_for_analysis = []
    for element in keyword_sentences:
        element = re.sub(r'[^\w\s]', '', element)  # deleting punctuation
        split_element = re.split('\s|\'', element)
        for word in split_element:
            text_for_analysis.append((word).lower())
    while '' in text_for_analysis:
        text_for_analysis.remove('')
    neg_per, poz_per, neu_per = percentages()
    text_negative, text_positive, text_neutral = text_sort(text_for_analysis)

    decison = input("""Would you like to see the details and charts? Y/N
    """)
    if decison == "Y":
        overall_sentiment()

elif number == 4:
    keyword = input("""Enter the keywords you are looking for:
    """)
    path = input("""Enter the path to the file:
    """)
    text = open((path), 'r')
    sentence_text = str(text.read())
    text.close()
    sentence_text = re.sub(r'[\n]', '', sentence_text)
    sentence_text = re.split('[.!?]', sentence_text)
    keyword_sentences = []
    for sentence in sentence_text:
        sentence_text_temp = re.split(' ', sentence)
        if keyword in sentence_text_temp:
            keyword_sentences.append(sentence)
    print("""Sentences with the keyword are:
    """)
    for sentence in keyword_sentences:
        print (sentence)
    text_for_analysis = []
    for element in keyword_sentences:
        element = re.sub(r'[^\w\s]', '', element)  # deleting punctuation
        split_element = re.split('\s|\'', element)
        for word in split_element:
            if word.lower() not in stopwords:
                text_for_analysis.append(word.lower())
    neg_per, poz_per, neu_per = percentages()
    text_negative, text_positive, text_neutral = text_sort(text_for_analysis)
    decison = input("""Would you like to see the details and charts? Y/N
    """)
    if decison == "Y":
        overall_sentiment()

