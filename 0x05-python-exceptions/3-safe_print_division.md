# 3. Integers division with debug

Write a function that divides 2 integers and prints the result.

- Prototype: `def safe_print_division(a, b):`
- You can assume that `a` and `b` are integers
- The result of the division should print on the `finally:` section preceded by `Inside result:`
- Returns the value of the division, otherwise: `None`
- You have to use `try: / except: / finally:`
- You have to use `"{}".format()` to print the result
- You are not allowed to import any module

```bash
guillaume@ubuntu:~/0x05$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

guillaume@ubuntu:~/0x05$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
guillaume@ubuntu:~/0x05$
```
