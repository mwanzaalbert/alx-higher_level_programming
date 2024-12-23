
def append_after(file, search_txt, insert_txt):
    with open(file, 'r+', encoding='utf-8') as infile:
        lines = infile.readlines()
#         print(lines)
#         print("".join(lines))
#
        infile.seek(0)
    
        print()
        for index, line in enumerate(lines):
            if search_txt in line:
                    lines.insert(index + 1, insert_txt)
#                     print(line)
#                     print(insert_txt)
#             else:
#                 print(line)
        infile.writelines(lines)


append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")