# 0x02. Python - Async Comprehension

| `Python` | `Back-end` |

![meme](./images/meme1.png)

## Resources

**Read or watch:**

- [`PEP 530 – Asynchronous Comprehensions`](https://intranet.alxswe.com/rltoken/hlwtED-iLsdORSgly8DsyQ)
- [`What’s New in Python: Asynchronous Comprehensions / Generators`](https://intranet.alxswe.com/rltoken/0OkbObYzCKtO7ZUAxfKvkw)
- [`Type-hints for generators`](https://intranet.alxswe.com/rltoken/l4Fnno568VbVIn9GvrFVtQ)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements

### General

- A `README.md` file, at the root of the folder of the project, is mandatory
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- All your files must be executable
- The length of your files will be tested using `wc`
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the `pycodestyle` style (version 2.5.x)
- All your functions and coroutines must be type-annotated.
- All your modules should have a documentation (`python3 -c 'print(**import**("my_module").**doc**)'`)
- All your functions should have a documentation (`python3 -c 'print(**import**("my_module").my_function.**doc**)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

### 0. Async Generator

Write a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a `random` number between 0 and 10. Use the random module.

```shell
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```

solution - [0-async_generator.py](0-async_generator.py)
