def merge_the_tools(string:str, k:int):
    # your code goes here
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        
        seen_chars = set()
        uniq_char_list = []

        for char in substring:
            if char not in seen_chars:
                uniq_char_list.append(char)
                seen_chars.add(char)

        print("".join(uniq_char_list))
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
