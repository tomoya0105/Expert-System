# -*- coding: utf-8 -*-
# データ読み込み-----------------------------------------
with open('K1 dataset.txt') as f1:
    data1 = f1.read()  

with open('K2 dataset.txt') as f2:
    data2 = f2.read()  

with open('Q dataset.txt') as f3:
    data3 = f3.read()  


# 単語カウント-------------------------------------------
import collections

counter = collections.Counter(data1.split())
d1 = counter.most_common()

counter = collections.Counter(data2.split())
d2 = counter.most_common()

counter = collections.Counter(data3.split())
d3 = counter.most_common()


# 標準出力----------------------------------------------
# for count, word in d1[:20]:
#     print(count, word)

# print("----------------------")

# for count, word in d2[:20]:
#     print(count, word)
    
# print("----------------------")

# for count, word in d3[:20]:
#     print(count, word)

# WordFrequencyリスト作成---------------------------------
wfl = [[], [], []]

for word, count in d1:
    wfl[0].append(word)

for word, count in d2:
    wfl[1].append(word)

for word, count in d3:
    wfl[2].append(word)
    
    
# 単語比較-------------------------------------------------
swfl = [[], []]
for i in range(2):
    for word in wfl[i]:
        if word in wfl[2] and word not in swfl[i]:
            swfl[i].append(word)

# 上位20位に絞って出力---------------------------------------
swfl20 = [[], []]
for i in range(2):
    for word in swfl[i][:20]:
        swfl20[i].append(word)

for i in range(2):
    print(swfl20[i])
    print("-------------------------------------------------------------------------------------------------")
    
# 最も類似度の低いデータセットを特定----------------------------
sum1 = 0
sum2 = 0

for word1 in swfl20[0]:
    for word2, count2 in d1:
        if word1 is word2:
            sum1 += count2
            
for word1 in swfl20[1]:
    for word2, count2 in d2:
        if word1 is word2:
            sum2 += count2
        
if sum1 < sum2:
    print("落選候補、選ばれたのは K1 でした。\n")
else:
    print("落選候補、選ばれたのは K2 でした。\n")
    
# おまけ-----------------------------------------------
# for i in range(2):
#     print(swfl[i])
#     print("-------------------------------------------------------------------------------------------------")
    
    
    
#ここからreSWFL作成(要望してきたやつ)-------------------------------------
reSWFL1 = d1
reSWFL2 = d2

# swfl[0]の要素にない要素をreSWFL1から削除する
reSWFL1 = [(word, count) for word, count in reSWFL1 if word in swfl[0]]

# swfl[1]の要素にない要素をreSWFL2から削除する
reSWFL2 = [(word, count) for word, count in reSWFL2 if word in swfl[1]]

        
print(reSWFL1) 
print("-------------------------------------------------------------------------------------------------")
print(reSWFL2) 

# txtファイル作成-------------------------------------------------------
with open('ShareWordFrequencyList_1.txt', 'w') as f1:
    for item in reSWFL1:
        line = ' '.join(str(x) for x in item).replace(',', '').replace('(', '').replace(')', '') + '\n'
        f1.write(line)
        
with open('ShareWordFrequencyList_2.txt', 'w') as f2:
    for item in reSWFL2:
        line = ' '.join(str(x) for x in item).replace(',', '').replace('(', '').replace(')', '') + '\n'
        f2.write(line)

f1.close()
f2.close()