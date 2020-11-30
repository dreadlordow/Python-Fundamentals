def index_validation(index, sentence):
    if 0 <= index < len(sentence):
        return True
    return False


sentence = input().split()

line = input()

while line != 'Stop':
    args = line.split()
    command = args[0]
    if command == 'Delete':
        index = int(args[1])
        if index_validation(index+1,sentence): #тук може да има грешка
            del sentence[index+1]
    elif command == 'Swap':
        first_word = args[1]
        second_word = args[2]
        if first_word in sentence and second_word in sentence:
            first_index = sentence.index(first_word)
            second_index = sentence.index(second_word)
            sentence[first_index], sentence[second_index] = sentence[second_index], sentence[first_index]

    elif command == 'Put':
        word = args[1]
        index = int(args[2])
        if index - 1 == len(sentence) :
            sentence.append(word)
        elif 0 < index <= len(sentence):
            sentence.insert(index-1, word)


    elif command == 'Replace':
        word_one = args[1]
        word_two = args[2]
        if word_two in sentence:
            for i in range(len(sentence)):
                if sentence[i] == word_two:
                    sentence[i] = word_one


    elif command == 'Sort':
        sentence = list(sorted((sentence),reverse=True))
    line = input()
print(' '.join(sentence))