# cd Stimulation

## Overview

The `cd_stimulate.py` project simulates the Unix "cd" (change directory) command using pure string manipulation. It allows navigation through a simulated file system based on given current and new directory paths, supporting both relative and absolute path navigation.

## Features

- Supports absolute (`/`) and relative paths.
- Handles special cases like current directory (`.`) and parent directory (`..`).
- Ignores multiple consecutive slashes, treating them as a single slash.
- Validates directory names, ensuring they are alphanumeric or special cases (`.` and `..`).

## Requirements

- Python 3.x

## Usage

To use the program, run the `cd_stimulate.py` script with two arguments: the current directory and the new directory.

### Example1

```sh
python cd_stimulate.py /abc/def ghi
```

### Output1

```sh
/abc/def/ghi
```

### Example2

```sh
python cd_stimulate.py /abc/def ../..
```

### Output2

```sh
/
```

### Example3

```sh
python cd_stimulate.py /abc/def ..klm
```

### Output3

```sh
..klm: No such file or directory
```

## How to Run Tests

Run the tests using the Python Interpreter using the following command:

```sh
python test_cd_stimulate.py
```

## Test Cases passed

![Project Logo](passpic.png)


## License
This project is open-source and available under the MIT License. Feel free to modify and distribute it.
