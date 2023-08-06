import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from collections import defaultdict
import os

K1 = []
K2 = []
Q = []
size = 20

class POS_Analysis :
    def __init__(self, text) :
        self.pos = pos_tag(word_tokenize(text)) # 1. tag the part-of-speech (POS) of each word
        
    # allow the user to select any word or string and display the word or string in context
    def select_word(self, word) :
        index = [i for i, x in enumerate(self.pos) if x[0] == word]
        lst = []

        for i in index :
            if i < 1 :
                lst.append(self.pos[i][0] + ' ' + self.pos[i+1][0])
            elif i > len(self.pos)-2 :
                lst.append(self.pos[i-1][0] + ' ' + self.pos[i][0])
            else :
                lst.append(self.pos[i-1][0] + ' ' + self.pos[i][0] + ' ' + self.pos[i+1][0])
            
        return lst
        
    # allow the user to search for POS patterns following the target word, e.g. absolutely + JJ
    def target_word(self, word) :
        index = [i for i, x in enumerate(self.pos) if x[0] == word]
        lst = []
        
        for i in index :
            lst.append(self.pos[i][0] + ' ' + self.pos[i+1][1])
            
        return lst
        
    # count the number of identical POS patterns in each dataset
    def count_pos(self) :
        #print('4. count the number of identical POS patterns in each dataset')
        d = defaultdict(int)
        
        for i in range(len(self.pos)-1) :
            d[self.pos[i][0] + ' ' + self.pos[i+1][1]] += 1
            
        return d
        
    def data_print(self) :
        print(self.pos)

# allow the user to select any word or string and display the word or string in context
def select_word() :
    word = input('検索する単語')
    d = defaultdict(int)
    
    for i in range(len(K1)) :
        lst = K1[i].select_word(word)
    
        for j in lst :
            d[j] += 1
            
    for i in range(len(K2)) :
        lst = K2[i].select_word(word)
    
        for j in lst :
            d[j] += 1
            
    for i in range(len(Q)) :
        lst = Q[i].select_word(word)
    
        for j in lst :
            d[j] += 1
            
    for i, j in d.items() :
        print(i)
        
# allow the user to search for POS patterns following the target word, e.g. absolutely + JJ
def target_word() :
    word = input('検索する単語')
    d = defaultdict(int)
    
    for i in range(len(K1)) :
        lst = K1[i].target_word(word)
    
        for j in lst :
            d[j] += 1
            
    for i in range(len(K2)) :
        lst = K2[i].target_word(word)
    
        for j in lst :
            d[j] += 1
            
    for i in range(len(Q)) :
        lst = Q[i].target_word(word)
    
        for j in lst :
            d[j] += 1
            
    for i, j in d.items() :
        print(i)
        
# Compare the top 20 patterns
def comp(A, B) :
    num = 0
    
    for i in range(size) :
        for j in range(size) :
            if A[i][0] == B[j][0] :
                num += 1
    
    return num

# count the number of identical POS patterns in each dataset
def analysis() :
    K1_data = defaultdict(int)
    K2_data = defaultdict(int)
    Q_data = defaultdict(int)
    K1_list = []
    K2_list = []
    Q_list = []
    
    for i in range(len(K1)) :
        d = K1[i].count_pos()
        for p, n in d.items() :
            K1_data[p] += n
            
    for i,j in K1_data.items() :
        K1_list.append([i, j])
        
    K1_list.sort(reverse=True, key=lambda x:x[1])
        
    for i in range(len(K2)) :
        d = K2[i].count_pos()
        for p, n in d.items() :
            K2_data[p] += n
            
    for i,j in K2_data.items() :
        K2_list.append([i, j])
        
    K2_list.sort(reverse=True, key=lambda x:x[1])
        
    for i in range(len(Q)) :
        d = Q[i].count_pos()
        for p, n in d.items() :
            Q_data[p] += n
            
    for i,j in Q_data.items() :
        Q_list.append([i, j])
        
    Q_list.sort(reverse=True, key=lambda x:x[1])
    
    while True :
        K1_cnt = comp(Q_list, K1_list)
        K2_cnt = comp(Q_list, K2_list)
        
        if K1_cnt > K2_cnt :
            print("K2 is the least similar dataset.")
            break
        elif K1_cnt < K2_cnt :
            print("K1 is the least similar dataset.")
            break
        else :
            size += 20

def main() :
    #text = 'The first suggestion to learn something using ChatGPT is to make quizzes.'
    # folderのパス
    K1_folder_path = "K1 dataset"
    K2_folder_path = "K2 dataset"
    Q_folder_path = "Q dataset"
    
    # folderのfileを取得
    K1_files = os.listdir(K1_folder_path)
    K2_files = os.listdir(K2_folder_path)
    Q_files = os.listdir(Q_folder_path)
    
    # dataset K1
    for file in K1_files :
        if file.endswith(".txt") :
            file_path = os.path.join(K1_folder_path, file)
            f = open(file_path, 'r')
            text = f.read()
            K1.append(POS_Analysis(text))
            
    # dataset K2
    for file in K2_files :
        if file.endswith(".txt") :
            file_path = os.path.join(K2_folder_path, file)
            f = open(file_path, 'r')
            text = f.read()
            K2.append(POS_Analysis(text))
            
    # dataset Q
    for file in Q_files :
        if file.endswith(".txt") :
            file_path = os.path.join(Q_folder_path, file)
            f = open(file_path, 'r')
            text = f.read()
            Q.append(POS_Analysis(text))
    
    while True :
        print('--------------------------------------------------------------------------------------------')
        print('0 : Finish and count the number of identical POS patterns in each dataset')
        print('1 : Allow the user to select any word or string and display the word or string in context')
        print('2 : Allow the user to search for POS patterns following the target word, e.g. absolutely + JJ')
        order = int(input())
        
        if order == 0 :
            break
        elif order == 1 :
            # allow the user to select any word or string and display the word or string in context
            print('Allow the user to select any word or string and display the word or string in context')
            select_word()
        elif order == 2 :
            # allow the user to search for POS patterns following the target word, e.g. absolutely + JJ
            print('Allow the user to search for POS patterns following the target word, e.g. absolutely + JJ')
            target_word()
        else :
            print(str(order) + " is nothing. Reinput from 0 to 2.")
            
    # count the number of identical POS patterns in each dataset
    analysis()

if __name__ == "__main__" :
    main()
