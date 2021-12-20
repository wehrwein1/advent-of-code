#!/bin/bash

# rustrun.sh: wrap compile/run into single command for use as VSCode keyboard shortcut binding (cmd-enter)
# adapted from http://blog.joncairns.com/2015/10/a-single-command-to-compile-and-run-rust-programs/
name=$(basename $1 .rs)
if [[ "$name" == '.rs' ]]; then
  echo "Usage: ./$(basename $0) FILE"
  exit 0
fi
rustc $@ && ./$name && rm $name
