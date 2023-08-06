<div align="center">

  # AsyncThread
  A threading implementation for asynchronous functions.

  [![](https://img.shields.io/github/contributors/Geographs/AsyncThread)](https://github.com/Geographs/OneSnipe/graphs/contributors)
  [![](https://img.shields.io/github/forks/Geographs/AsyncThread)](https://github.com/Geographs/OneSnipe/network/members)
  [![](https://img.shields.io/github/stars/Geographs/AsyncThread)](https://github.com/Geographs/OneSnipe/stargazers)
  [![](https://img.shields.io/github/issues/Geographs/AsyncThread)](https://github.com/Geographs/OneSnipe/issues)
  [![](https://img.shields.io/github/license/Geographs/AsyncThread)](https://github.com/Geographs/OneSnipe/blob/main/LICENSE)

  [![](https://www.codefactor.io/repository/github/geographs/asyncthread/badge)](https://www.codefactor.io/repository/github/geographs/onesnipe)
  [![](https://img.shields.io/lgtm/grade/python/g/Geographs/asyncthread)](https://lgtm.com/projects/g/Geographs/OneSnipe)

  # Usage
  <div align="left">

  ```python
from asyncthread import Thread


async def hello_world() -> None:
    print("Hello, World!")


thread = Thread(func=hello_world())
thread.start()
thread.join()
  ```

  ```python
from asyncthread import Thread


async def hello_world() -> None:
    print("Hello, World!")


thread = Thread(func=[hello_world() for _ in range(1000)], workers=10)
thread.start()
thread.join()
  ```

  </div>

</div>