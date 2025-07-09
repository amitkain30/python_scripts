def merge_the_tools(string:str, k:int):
    # your code goes here
    num_substrings = int(len(string)/k)
    
    for i in range(num_substrings):
        substring = string[i:i+k]
        print(substring)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
