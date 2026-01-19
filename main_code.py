def cookie(x):
    if isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
    if type(x) is not bool and isinstance(x, (int, float)):
        return "Who ate the last cookie? It was Monica!"
    
    return "Who ate the last cookie? It was dog!"

print(cookie(x="Hello"))
print(cookie(x=1.2))
print(cookie(x=22))
print(cookie(x=True))