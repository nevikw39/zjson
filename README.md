# zjson
## 快速產生可供 ZeroJudge 系統匯入題目格式之檔案

這是為了快速把吳邦一教授的 **AP325** 教材中的題目快速製作成可匯入格式的工具。因此，測資檔案格式為 `{directory_$i}.{in|out}, for i in {1..5}`，假定皆為五筆測資。

### Input

總共需要至多八個輸入：
1. 目錄名稱
2. 題目標題
3. 範例程式碼名稱，如果沒有請直接 *Enter⏎↩︎* 空行會跳過忽略
4. 題目內容。因為可能有很多行，所以會讀取直到空行
5. 輸入說明。因為可能有很多行，所以會讀取直到空行
6. 輸出說明。因為可能有很多行，所以會讀取直到空行
7. 範例輸入。因為可能有很多行，所以會讀取直到空行
8. 範例輸出。因為可能有很多行，所以會讀取直到空行

### Example

#### 直接輸入

以下以 `sum` 為例。

```bash
python3 gen.py
```

輸入內容：

```
sum     // 目錄名稱
The Sum // 題目標題
        // 空行表無範例程式碼
Given $a$ & $b$, then $a + b = $?? // 題目內容開始
                                   // 題目內容結束
Two integrals respectively representing $a$ & $b$ in separated lines. // 輸入說明開始
                                                                      // 輸入說明結束
Result of $a + b$. // 輸出說明開始
                   // 輸出說明結束
1 // 範例輸入開始
1
  // 範例輸入結束
2 // 範例輸出開始
  // 範例輸出結束
```

```bash
cat [sum.zjson](sum.zjson)
```

#### 重新定向

直接輸入顯然很不方便，有時我們需要對內容進行排版，畢竟ＰＤＦ赴至好容易跑掉，當然別忘惹加上 LaTeX。這時，我們可以依照輸入順序存到文字檔裡，再重新定向到 *stdin*。以下以 `P_4_7` 為例。

```bash
vim [P_4_7.txt](P_4_7.txt)
python3 gen.py < P_4_7.txt
cat [P_4_7.zjson](P_4_7.zjson)
```
