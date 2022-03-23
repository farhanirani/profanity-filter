import csv

# reading the csv file
file = open("words.csv", "r")
csvreader = csv.reader(file)
header = next(csvreader)

profane_words = []
entire_dict = []

# creating a dictionary and a lookup from the csv
for row in csvreader:
    profane_words.append(row[0])
    entire_dict.append(row)

file.close()


def backend(text):

    # checking the sentence
    text = text.lower().split()
    print("Sentence : ", text)

    # array to store profane locations in dictionary
    profane_single_location = [0 for _ in range(len(text))]
    profane_phrase_location = [0 for _ in range(len(text))]
    profane_true_or_false_single = [0 for _ in range(len(text))]
    profane_true_or_false_phrase = [0 for _ in range(len(text))]
    profane_true_or_false_all_words = [0 for _ in range(len(text))]

    # checking single words
    for i in range(len(text)):
        if text[i] in profane_words:
            profane_true_or_false_single[i] = 1
            profane_true_or_false_all_words[i] = 1
            profane_single_location[i] = profane_words.index(text[i])
            text[i] = '*' * len(text[i])

    # checking phrases (double and triple words)
    for i in range(0, len(text) - 1):
        phrase = ' '.join(text[i:i + 2])
        if phrase in profane_words:
            profane_true_or_false_phrase[i] = 1
            profane_true_or_false_all_words[i] = 1
            profane_true_or_false_all_words[i + 1] = 1
            profane_phrase_location[i] = profane_words.index(phrase)

    for i in range(0, len(text) - 2):
        phrase = ' '.join(text[i:i + 3])
        if phrase in profane_words:
            profane_true_or_false_phrase[i] = 1
            profane_true_or_false_all_words[i] = 1
            profane_true_or_false_all_words[i + 1] = 1
            profane_true_or_false_all_words[i + 2] = 1
            profane_phrase_location[i] = profane_words.index(phrase)

    severity_total = 0
    severity_count = 0

    print()

    for i in range(len(profane_single_location)):
        if profane_true_or_false_single[i]:
            print(entire_dict[profane_single_location[i]])
            severity_count += 1
            severity_total += float(
                entire_dict[profane_single_location[i]][-2])

    for i in range(len(profane_phrase_location)):
        if profane_true_or_false_phrase[i]:
            print(entire_dict[profane_phrase_location[i]])
            severity_count += 1
            severity_total += float(
                entire_dict[profane_phrase_location[i]][-2])

    # checking severity
    count_ones = 0
    for i in profane_true_or_false_all_words:
        count_ones += i
    percent_words_bad = 100 * count_ones / len(profane_true_or_false_all_words)

    severity_average = 0
    if severity_count:
        severity_average = severity_total / severity_count
    severity_percentage = 100 * severity_average / 3

    # more weightage to the severity from dict than words
    total_severity = 85 * severity_percentage / 100 + 15 * percent_words_bad / 100

    return round(total_severity, 2), profane_true_or_false_all_words, ' '.join(text)
