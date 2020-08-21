import json
import sys
import os


def inputArticle(prompt: str = '', endl: str = '\n') -> str:
    '''讀入數個段落，直到遇到空行

    Args:
        prompt: 第一次呼叫 input() 的 prompt 參數，預設為 ''
        endl: 每個段落間的分隔，預設為 '\n'

    Returns:
        段落字串
    '''
    y = str()
    try:
        s = input(prompt + ":\n>>> ")
        while s:
            y += s + endl
            s = input("... ")
    except EOFError:
        pass
    return y


# 打開範本檔
with open("sample.zjson") as f:
    j = json.load(f)

# 取得目錄名稱，如果有指定命令列參數則直接使用，否則等待輸入
folder = input("folder>>> ") if len(sys.argv) == 1 else sys.argv[1]

# 輸入題目標題
j["title"] = input("title\t>>> ")

# 輸入範例程式碼名稱，如果為空則忽略
code = input('code\t>>> ')
if code and os.path.exists(f"./{folder}/{folder}{code}"):
    with open(f"./{folder}/{folder}{code}") as f:
        j["samplecode"] = f.read()

# 分別輸入內容、輸入說明、輸出說明、範例輸入、範例輸出，其中皆以空行分隔
j["content"] = "<p>" + inputArticle("content", "</p><p>")[:-3]
j["theinput"] = "<p>" + inputArticle("the_in", "</p><p>")[:-3]
j["theoutput"] = "<p>" + inputArticle("the_out", "</p><p>")[:-3]
j["sampleinput"] = inputArticle("sample_in")
j["sampleoutput"] = inputArticle("sample_out")

# 讀取測資
for i in range(1, 5 + 1):
    try:
        with open(f"{folder}/{folder}_{i}.in") as f:
            j["testinfiles"].append(f.read())
        with open(f"{folder}/{folder}_{i}.out") as f:
            j["testoutfiles"].append(f.read())
    except FileNotFoundError:
        break

# 寫進檔案，大功告成
with open(f"{folder}.zjson", 'w', encoding="utf-8") as f:
    json.dump(j, f, ensure_ascii=False)
