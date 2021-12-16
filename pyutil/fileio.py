
def file_lines(filename: str, lineMapper=lambda line : line):
  return [lineMapper(line) for line in map(str.rstrip, open(filename))]
