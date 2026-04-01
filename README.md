# advent-of-code
Advent of code puzzles, see https://adventofcode.com

[![go](https://github.com/wehrwein1/advent-of-code/actions/workflows/go.yml/badge.svg)](https://github.com/wehrwein1/advent-of-code/actions/workflows/go.yml)
[![python](https://github.com/wehrwein1/advent-of-code/actions/workflows/python.yml/badge.svg)](https://github.com/wehrwein1/advent-of-code/actions/workflows/python.yml)
[![rust](https://github.com/wehrwein1/advent-of-code/actions/workflows/rust.yml/badge.svg)](https://github.com/wehrwein1/advent-of-code/actions/workflows/rust.yml)

### First time dev set up
```bash
# software packages
brew install pyenv
brew install python

# virtual env
python3 -m venv .venv
source .venv/bin/activate # (VSCode does this for you in terminal, also could alias as "activate")
pip install -r requirements.txt
deactivate
```