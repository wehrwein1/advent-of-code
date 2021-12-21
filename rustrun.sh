#!/bin/bash

# rustrun.sh: wrap compile/run into single command for use as VSCode keyboard shortcut binding (cmd-enter)
# adapted from http://blog.joncairns.com/2015/10/a-single-command-to-compile-and-run-rust-programs/
# update: extended with 'build' and 'test' options to use in pipelines

scriptName=$(basename $0)

function print_usage() {
  echo "Usage: ./$scriptName ACTION (OPTIONS)"
  echo
  echo "Actions:"
  echo " run      Compile and run a source file, e.g. './$scriptName run path/to/file.rs'"
  echo " build    Run 'cargo build' in all folders containing Cargo.toml"
  echo " test     Run 'cargo test' in all folders containing Cargo.toml"
}

function compile_and_run_source_file() {
  name=$(basename $1 .rs)
  if [[ "$name" == '.rs' ]]; then
    print_usage
    exit 0
  fi
  rustc $@ && ./$name && rm $name
}

function build_all() {
  for f in $(find . -type f -name "Cargo.toml" -exec dirname "{}" \; |sort -u); do
    pushd $f > /dev/null;
    cargo build --verbose || exit $?
    popd > /dev/null;
  done
}

function test_all() {
  for f in $(find . -type f -name "Cargo.toml" -exec dirname "{}" \; |sort -u); do
    pushd $f > /dev/null;
    cargo test --verbose || exit $?
    popd > /dev/null;
  done
}

action="$1"
case "$action" in
  ("run")   compile_and_run_source_file "$2";;
  ("build") build_all ;;
  ("test")  test_all ;;
  (*) print_usage ;;
esac
