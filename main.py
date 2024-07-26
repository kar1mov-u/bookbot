def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    dic={}
    text_low = text.lower()
    #Poppulating dictionary
    for ch in text_low:
        if ch == ' ' or not ch.isalpha():
            continue
        elif ch not in dic:
            dic[ch]=1
        else:
            dic[ch]+=1
    #Sorting dictionary in order of apperacnce
    s_dic = dict(sorted(dic.items(), key=lambda item : item[1], reverse=True))
    return s_dic

def main():
    path = "books/frankenstein.txt"
    # Opening file and reading it
    with open(path) as f:
        content = f.read()
    
    num_words = count_words(content)
    num_chars = count_chars(content)
    print(f' --- Begin report of {path} ---')
    print(f'{num_words} words found in the document\n')
    for char in num_chars:
        print(f"The '{char}' character was found {num_chars[char]} times")
    print('--- End report ---')

main()