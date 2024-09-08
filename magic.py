def check_spell(s):
    
    # 定義的括號組
    pairs = ["()", "{}", "[]"]
    
    # 確定原始長度
    initial_length = len(s)
    
    # 字串是否包含已定義的括號組, 若有將其替換為空
    for pair in pairs:
        s = s.replace(pair, "")
    
    # 如果字串為空, 表示所有都括號配對成功, 代表配對成功
    if s == "":
        return "施法成功"

    # 如果字串不為空, 表示仍有無法配對的括號，代表配對失敗
    if len(s) == initial_length:
        return "施法失敗"

    return check_spell(s)

# 輸入測試值
examples = ["()", "{{}}", "{()}", "{([])}", "[)", "({[])}", "{{}", "({)}"]

# 迴圈遍例所有測試值, 並將結果對應輸出
for example in examples:
    result = check_spell(example)
    print("{}: {}".format(example, result))

