Implementation procedure
1. WordFrequency.py
2. KeywordFreq.py
3. KeywordPOS.py

Dataset
K1 dataset.txt
K2 dataset.txt
Q dataset.txt

Link
EL159_2311175007: Datasets Q, K1 and K2 (u-aizu.ac.jp)


Source code description
WordFrequency.py
First, load each file onto the program. (まず、各ファイルをプログラム上に読み込む。)


Next, create tuples of K1, K2, and Q, each of which is a set of words and the number of times the word appears, separated by spaces in the text sentence.           (次に、テキスト文を空白で区切って、単語とその単語の出現回数をセットにしたタプルをK1、K2、Qのそれぞれ作る。)


Using each tuple, create a WordFrequencyList for each.            (各タプルを用いて、それぞれに対応するWordFrequencyListを作る。)


From the WordFrequencyList, create two ShareWordFrequencyLists (swfl), which are lists of common words only.             (WordFrequencyListから、共通単語のみを集めたリストであるShareWordFrequencyList（swfl）を２つ作る。)


Make a list (swfl20) of the top 20 words from the aforementioned ShareWordFrequencyList and output it to the standard output.                  (前述のShareWordFrequencyListの上位２０位までの単語を集めたリスト（swfl20）を作って標準出力する。)


Use the two swfl20 to identify and exclude those with low similarity to Q.                              (２つのswfl20を使って、Qとの類似度の低いものを特定し除外する。)


Output the contents of each ShareWordFrequencyList (reSWFL) to a text file. (ShareWordFrequencyList_1.txt) (ShareWordFrequencyList_2.txt).   (ShareWordFrequencyList（reSWFL）の内容をそれぞれテキストファイルに出力する。（ShareWordFrequencyList_1.txt）（ShareWordFrequencyList_2.txt）)


KeywordFreq.py
First, load the two ShareWordFrequencyList.txt files created by WordFrequency.py.
(まず、WordFrequency.pyで作った二つのShareWordFrequencyList.txtファイルを読み込む。)

Then create a Share_keyword_frequency_list from the ShareWordfrequencyList with reference to the Copus, Brown_tokenized.
(次に、CopusであるBrown_tokenizedを参照して、ShareWordfrequencyListからShare_keyword_frequency_listを作成する。)

Words such as 'a' and 'the' cannot be used as KEYWORDS, so remove the top 20 WORDS.
(aやtheなどの単語はkeywordとしては使えないので、上位20wordを取り除く。)

Display the top 20 WORDS on screen.
(上位20wordを画面に表示する。)

Determine whether K1 or K2 should be excluded by finding and comparing the total number of counts in the top 20 WORD.
（上位20wordのcount数の合計を求めて比較することで、K1とK2のどちらを除外するべきかを判断する。）

Finally, save the Share_keyword_frequency_list as a txt file.
（最後に、Share_keyword_frequency_listをtxtファイルとして保存する。）

KeywordPOS.py
Assign "POS" to each word.
（各単語に”POS”を割り当てる）
	
If "allow the user to select any word or string and display the word or string in context", display the typed word together with the words before and after.
（「ユーザーが任意の単語または文字列を選択し、その単語または文字列をコンテキスト内で表示できるようにする」場合は、入力した単語を前後の単語と合わせて表示します）

If "allow the user to search for POS patterns following the target word, e.g. absolutely + JJ", display "input word + next word's POS".
（「ユーザーがターゲット単語に続くPOS patternを検索できるようにする（例：absolute + JJ）」の場合、「入力された単語 + 次の単語のPOS」を表示します。）

Count POS patterns for each data and sort in descending order based on the number.
（データごとにPOS patternをカウントし、その数に基づいて降順にソートします。）

Compare the top 20 patterns and view the least likely dataset.
（上位 20 のパターンを比較し、最も可能性の低いデータセットを表示します。）
