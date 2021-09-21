import liwc
parse, category_names = liwc.load_token_parser("./LIWC2007_Portugues_win.dic")
resp = list(parse("ansioso"))
print(resp)
