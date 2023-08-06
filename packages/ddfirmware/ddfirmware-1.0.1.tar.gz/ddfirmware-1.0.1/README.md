# ddfirmware

## What is ddfirmware?

ddfirmware is a simple script for terminal use.  It queries dd-wrt.com for router firmware based on user input and writes it to the present working directory. 

## System Requirements

* python3
* python requests package (```pip install requests```)

<img src='ddfirmware_screenshot.png'>


## Installation

```pip install ddfirmware```

## Usage

To use ddfirmware:

### Basic / Current Day

```ddfirmware [router]```

Example: ddfirmware r7000; uses fuzzy regex match

    * Lists all routers that match [router] and prompts user to choose
    * Prints contents of present working directory
    * Prompts user to confirm they wish to download available binary
