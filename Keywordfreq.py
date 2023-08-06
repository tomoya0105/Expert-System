import os
import re
from collections import Counter

def read_word_frequency_list(file_path):
    # word frequency listをtxtファイルから読み込む
    word_frequency_list = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word, count = line.strip().split()
            word_frequency_list[word] = int(count)
    return word_frequency_list

def create_keyword_frequency_list(corpus_folder, word_frequency_list):
    keyword_frequency_list = {}

    # Corpusフォルダ内のテキストファイルを全て処理
    for filename in os.listdir(corpus_folder):
        file_path = os.path.join(corpus_folder, filename)
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                # word frequency listの単語がCorpus内で出現した場合のみkeyword frequency listに追加
                for word, count in word_frequency_list.items():
                    keyword_count = text.lower().count(word)
                    if keyword_count > 0:
                        keyword_frequency_list[word] = keyword_count * count

    return keyword_frequency_list

def save_keyword_frequency_list_to_file(keyword_frequency_list, output_file):
    # keyword frequency listをtxtファイルに保存
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in keyword_frequency_list.items():
            file.write(f'{word} {count}\n')

def display_top_n_keyword_frequency(keyword_frequency_list, n=20):
    # 上位n位のkeyword frequency listを表示
    top_n_keywords = Counter(keyword_frequency_list).most_common(n)
    for keyword, frequency in top_n_keywords:
        print(f"{keyword}: {frequency}")

def get_top_n_keyword_count_sum(keyword_frequency_list, n=20):
    # 上位n位のkeywordのcount数の合計を計算
    top_n_keywords = Counter(keyword_frequency_list).most_common(n)
    count_sum = sum(frequency for keyword, frequency in top_n_keywords)
    return count_sum


if __name__ == "__main__":
    # (i)のword frequency listを外部のtxtファイルから読み込む
    word_frequency_list_file1 = "./ShareWordFrequencyList_1.txt"
    word_frequency_list_file2 = "./ShareWordFrequencyList_2.txt"
    word_frequency_list1 = read_word_frequency_list(word_frequency_list_file1)
    word_frequency_list2 = read_word_frequency_list(word_frequency_list_file2)
    #print("Word Frequency List1:")
    #print(word_frequency_list1)
    #print("Word Frequency List2:")
    #print(word_frequency_list2)

    # (ii)のCorpusフォルダからkeyword frequency listを作成する
    corpus_folder = "./Brown_tokenized"
    keyword_frequency_list1 = create_keyword_frequency_list(corpus_folder, word_frequency_list1)
    keyword_frequency_list2 = create_keyword_frequency_list(corpus_folder, word_frequency_list2)

    # 上位20の単語を取り除く
    num_top_words_to_remove = 20
    sorted_keywords1 = sorted(keyword_frequency_list1.items(), key=lambda x: x[1], reverse=True)
    sorted_keywords2 = sorted(keyword_frequency_list2.items(), key=lambda x: x[1], reverse=True)
    final_keyword_frequency_list1 = dict(sorted_keywords1[num_top_words_to_remove:])
    final_keyword_frequency_list2 = dict(sorted_keywords2[num_top_words_to_remove:])

    print("Keyword Frequency List1:")
    display_top_n_keyword_frequency(final_keyword_frequency_list1, n=20)
    #print(keyword_frequency_list1)
    print("Keyword Frequency List2:")
    display_top_n_keyword_frequency(final_keyword_frequency_list2, n=20)
    #print(keyword_frequency_list2)

  #上位20単語のcount数の合計を計算して表示
    top_n_count_sum1 = get_top_n_keyword_count_sum(final_keyword_frequency_list1, n=20)
    top_n_count_sum2 = get_top_n_keyword_count_sum(final_keyword_frequency_list2, n=20)
    print(f"Top 20 keyword count sum: {top_n_count_sum1}")
    print(f"Top 20 keyword count sum: {top_n_count_sum2}")
    if top_n_count_sum1 < top_n_count_sum2:
      print("K1がQを書いた可能性は低いです\n")
    else:
      print("K2がQを書いた可能性は低いです\n")

    # keyword frequency listをtxtファイルに保存
    output_file1 = "share_keyword_frequency_list1.txt"
    output_file2 = "share_keyword_frequency_list2.txt"
    save_keyword_frequency_list_to_file(final_keyword_frequency_list1, output_file1)
    save_keyword_frequency_list_to_file(final_keyword_frequency_list2, output_file2)
    print(f"Keyword frequency list saved to {output_file1}.")
    print(f"Keyword frequency list saved to {output_file2}.")
