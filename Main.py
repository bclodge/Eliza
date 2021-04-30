import random


def preprocess(sentence):
    string_to_process = sentence
    remove_punc = ''.join(i for i in string_to_process if i not in ("?", ".", ",", "!", ":", ";"))
    sentence = remove_punc.lower()

    return sentence


def conjugate(sentence):
    conjugates = {'are': 'am', 'am': 'are', 'were': 'was', 'was': 'were', 'you': 'i', 'i': 'you', 'your': 'my',
                  'my': 'your', 'ive': "you've", 'youve': "I've", 'im': "you're", 'youre': "I'm", 'me': 'you'}

    for i, j in conjugates.items():
        sentence = sentence.replace(i, j)

    return sentence


def keywords(sentence):
    words = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i", "are you",
             "i cant", "i am", "im ", "you ", "i want", "what", "how", "who", "where", "when", "why", "name", "cause",
             "sorry", "dream", "hello", "hi ", "maybe", "no", "your", "always", "think", "alike", "yes", "friend"
                                                                                                         "computer"]

    for word in words:
        if word in sentence:
            index = words.index(word)
            sentence = sentence.replace(word, str(index))
            return sentence

    sentence = str(-1)
    return sentence


def buildreply(sentence):
    get_reply_number = sentence.split()

    reply_number_asString = get_reply_number[0]
    reply_number = int(reply_number_asString)

    seperator = " "
    rest_of_sentence = seperator.join(get_reply_number[1:])

    reply = getreply(reply_number)

    if reply.endswith('*'):
        x = reply.replace('*', rest_of_sentence)
        return x

    return reply


def getreply(reply_number):
    if reply_number == -1:
        neg_one = ["What does that suggest to you?", "I see.", "I'm not sure I understand you fully.",
                   "Come, come, elucidate your thoughts.", "Can you elaborate on that?", "That is quite interesting."]
        random_reply_choice = random.randrange(0, len(neg_one))
        sentence = neg_one[random_reply_choice]
        return sentence
    elif reply_number == 0:
        zero = ["Don't you believe that I can *", "Perhaps you would like me to be able to *",
                "You want me to be able to *"]
        random_reply_choice = random.randrange(0, len(zero))
        sentence = zero[random_reply_choice]
        return sentence
    elif reply_number == 1:
        one = ["Perhaps you don't want to *", "Do you want to be able to *"]
        random_reply_choice = random.randrange(0, len(one))
        sentence = one[random_reply_choice]
        return sentence
    elif reply_number == 2 or reply_number == 3:
        two_and_three = ["What makes you think I am *", "Does it please you to believe I am *",
                         "Perhaps you would like to be *", "Do you sometimes wish you were *"]
        random_reply_choice = random.randrange(0, len(two_and_three))
        sentence = two_and_three[random_reply_choice]
        return sentence
    elif reply_number == 4:
        four = ["Don't you really *", "Why don't you *", "Do you wish to be able to *", "Does that trouble you?"]
        random_reply_choice = random.randrange(0, len(four))
        sentence = four[random_reply_choice]
        return sentence
    elif reply_number == 5:
        five = ["Tell me more about such feelings.", "Do you often feel *", "Do you enjoy feeling *"]
        random_reply_choice = random.randrange(0, len(five))
        sentence = five[random_reply_choice]
        return sentence
    elif reply_number == 6:
        six = ["Do you really believe I don't *", "Perhaps in good time I will *", "Do you want me to *"]
        random_reply_choice = random.randrange(0, len(six))
        sentence = six[random_reply_choice]
        return sentence
    elif reply_number == 7:
        seven = ["Do you think you should be able to *", "Why can't you *"]
        random_reply_choice = random.randrange(0, len(seven))
        sentence = seven[random_reply_choice]
        return sentence
    elif reply_number == 8:
        eight = ["Why are you interested in whether or not I am *", "Would you prefer if I were not *",
                 "Perhaps in your fantasies I am *"]
        random_reply_choice = random.randrange(0, len(eight))
        sentence = eight[random_reply_choice]
        return sentence
    elif reply_number == 9:
        nine = ["How do you know you can't *", "Have you tried?", "Perhaps you can now *"]
        random_reply_choice = random.randrange(0, len(nine))
        sentence = nine[random_reply_choice]
        return sentence
    elif reply_number == 10 or reply_number == 11:
        ten_and_eleven = ["Did you come to me because you are *", "How long have you been *",
                          "Do you believe it is normal to be *", "Do you enjoy being *"]
        random_reply_choice = random.randrange(0, len(ten_and_eleven))
        sentence = ten_and_eleven[random_reply_choice]
        return sentence
    elif reply_number == 12:
        twelve = ["We were discussing you, not me.", "Oh, I *", "You're not really talking about me, are you?"]
        random_reply_choice = random.randrange(0, len(twelve))
        sentence = twelve[random_reply_choice]
        return sentence
    elif reply_number == 13:
        thirteen = ["What would it mean to you if you got *", "Why do you want *", "Suppose you got *",
                    "What if you never got *", "I sometimes also want *"]
        random_reply_choice = random.randrange(0, len(thirteen))
        sentence = thirteen[random_reply_choice]
        return sentence
    elif reply_number == 14 or reply_number == 15 or reply_number == 16 or reply_number == 17 or reply_number == 18 \
            or reply_number == 19:
        fourteen_through_nineteen = ["Why do you ask?", "Does that question interest you?",
                                     "What answer would please you the most?", "What do you think?",
                                     "Are such questions on your mind often?",
                                     "What is it that you really want to know?",
                                     "Have you asked anyone else?", "Have you asked such questions before?",
                                     "What else comes to your mind when you ask that?"]
        random_reply_choice = random.randrange(0, len(fourteen_through_nineteen))
        sentence = fourteen_through_nineteen[random_reply_choice]
        return sentence
    elif reply_number == 20:
        twenty = ["Names don't interest me.", "I don't care about names.  Please go on."]
        random_reply_choice = random.randrange(0, len(twenty))
        sentence = twenty[random_reply_choice]
        return sentence
    elif reply_number == 21:
        twenty_one = ["Is that the real reason?", "Don't any other reasons come to mind?",
                      "Does that reason explain anything else?", "What other reasons might there be?"]
        random_reply_choice = random.randrange(0, len(twenty_one))
        sentence = twenty_one[random_reply_choice]
        return sentence
    elif reply_number == 22:
        twenty_two = ["Please don't apologize!", "Apologies are not necessary."]
        random_reply_choice = random.randrange(0, len(twenty_two))
        sentence = twenty_two[random_reply_choice]
        return sentence
    elif reply_number == 23:
        twenty_three = ["What does that dream suggest to you?", "Do you dream often?",
                        "What persons appear in your dreams?", "Are you disturbed by your dreams?"]
        random_reply_choice = random.randrange(0, len(twenty_three))
        sentence = twenty_three[random_reply_choice]
        return sentence
    elif reply_number == 24 or reply_number == 25:
        twenty_four_and_twenty_five = ["How do you do.  Please state your problem."]
        random_reply_choice = random.randrange(0, len(twenty_four_and_twenty_five))
        sentence = twenty_four_and_twenty_five[random_reply_choice]
        return sentence
    elif reply_number == 26:
        twenty_six = ["You don't seem quite certain.", "Why the uncertain tone?", "Can't you be more positive?",
                      "You aren't sure?", "Don't you know?"]
        random_reply_choice = random.randrange(0, len(twenty_six))
        sentence = twenty_six[random_reply_choice]
        return sentence
    elif reply_number == 27:
        twenty_seven = ["Are you saying no just to be negative?", "You are being a bit negative.", "Why not?",
                        "Are you sure?", "Why no?"]
        random_reply_choice = random.randrange(0, len(twenty_seven))
        sentence = twenty_seven[random_reply_choice]
        return sentence
    elif reply_number == 28:
        twenty_eight = ["Why are you concerned about my *", "What about your own *"]
        random_reply_choice = random.randrange(0, len(twenty_eight))
        sentence = twenty_eight[random_reply_choice]
        return sentence
    elif reply_number == 29:
        twenty_nine = ["Can you think of a specific example?", "When?", "What are you thinking of?", "Really, always?"]
        random_reply_choice = random.randrange(0, len(twenty_nine))
        sentence = twenty_nine[random_reply_choice]
        return sentence
    elif reply_number == 30:
        thirty = ["Do you really think so?", "But you are not sure you *", "Do you doubt *"]
        random_reply_choice = random.randrange(0, len(thirty))
        sentence = thirty[random_reply_choice]
        return sentence
    elif reply_number == 31:
        thirty_one = ["In what way?", "What resemblence do you see?", "What does the similarity suggest to you?",
                      "What other connections do you see?", "Could there really be some connection?", "How?"]
        random_reply_choice = random.randrange(0, len(thirty_one))
        sentence = thirty_one[random_reply_choice]
        return sentence
    elif reply_number == 32:
        thirty_two = ["You seem quite positive.", "Are you sure?", "I see.", "I understand."]
        random_reply_choice = random.randrange(0, len(thirty_two))
        sentence = thirty_two[random_reply_choice]
        return sentence
    elif reply_number == 33:
        thirty_three = ["Why do you bring up the topic of friends?", "Do your friends worry you?",
                        "Do your friends pick on you?", "Are you sure you have any friends?",
                        "Do you impose on your friends?", "Perhaps your love for your friends worries you."]
        random_reply_choice = random.randrange(0, len(thirty_three))
        sentence = thirty_three[random_reply_choice]
        return sentence
    else:
        thirty_four = ["Do computers worry you?", "Are you frightened by machines?", "Why do you mention computers?",
                       "What do you think machines have to do with your problem?",
                       "Don't you think computers can help people?", "What is it about machines that worries you?"]
        random_reply_choice = random.randrange(0, len(thirty_four))
        sentence = thirty_four[random_reply_choice]
        return sentence


def tests():
    test1 = "testing, the. preprocess!"
    print("Test One: Preprocessing func")
    print(preprocess(test1))

    test2 = "i am very sad"
    print(conjugate(test2))

    test3 = "what is your name?"
    print(keywords(test3))

    print(buildreply(keywords(test3)))


# tests()


def eliza():
    print("Hello, I am Eliza.  Tell me your problems.")
    while True:
        sentence = input(">")
        if sentence == "bye" or sentence == "shut up":
            break
        sentence = preprocess(sentence)
        sentence = keywords(sentence)
        sentence = conjugate(sentence)
        sentence = buildreply(sentence)
        print(sentence)


eliza()
