# https://adventofcode.com/2020/day/19
from typing import List, Dict, Tuple
import re
from pyutil.fileio import file_lines
from pyutil.testing import assert_equals
from pyutil.strings import partition

def parened(text):                    return '({})'.format(text if type(text) == str else ' '.join(text))

def load_message_rules(lines : List[str], is_part1=True) -> Tuple[Dict, List[str]]:
  rules_part, messages = partition(lines)
  message_rules = dict( (int(tokens[0]), tokens[1]) for tokens in [rule.split(': ') for rule in rules_part])
  if not is_part1:
    message_rules[8]  = "42 | 42 8"
    message_rules[11] = "42 31 | 42 11 31"
  return message_rules, messages

def build_rule_regex(rule_spec : str, message_rules : Dict[int,str]) -> str:
  if '"' in rule_spec: return rule_spec.replace('"', '') # literal rule, 'a' or 'b'
  if "|" in rule_spec:
    groups = list(map(str.strip, rule_spec.split(" | ")))
    regexes = [parened(build_rule_regex(group, message_rules)) for group in groups]
    return parened("|".join(map(parened, regexes)))
  rule_refs = list(map(int, rule_spec.split(' ')))
  return ''.join(map(lambda rule_ref : build_rule_regex(message_rules[rule_ref], message_rules), rule_refs))
assert_equals(build_rule_regex('"a"', {}), 'a')
assert_equals(build_rule_regex('"b"', {}), 'b')
assert_equals(build_rule_regex('4', { 4: '"a"'}), 'a')
assert_equals(build_rule_regex('4 4', { 4: '"a"'}), 'aa')
assert_equals(build_rule_regex('4 | 5', { 4: '"a"', 5 : '"b"'}), '(((a))|((b)))')
assert_equals(build_rule_regex('4 4 | 5 5', { 4: '"a"', 5 : '"b"'}), '(((aa))|((bb)))')
assert_equals(build_rule_regex('2 3 | 3 2', { 2: '4 4 | 5 5', 3: ' 4 5 | 5 4', 4: '"a"', 5 : '"b"'}), '((((((aa))|((bb)))(((ab))|((ba)))))|(((((ab))|((ba)))(((aa))|((bb))))))')

def find_valid_messages(message_rules : Dict[int,str], messages : List[str], starting_rule=0) -> List[str]:
  regex_pattern = build_rule_regex(message_rules[starting_rule], message_rules)
  valid_messages = list(filter(lambda msg : re.match(regex_pattern + "$", msg), messages))
  return valid_messages
assert_equals(find_valid_messages(*load_message_rules(file_lines('2020/input/19_TEST.txt'))), ['ababbb', 'abbbab'])
assert_equals(find_valid_messages(*load_message_rules(file_lines('2020/input/19_TEST2.txt'))), ['bbabbbbaabaabba', 'ababaaaaaabaaab','ababaaaaabbbaba'])
# assert_equals(find_valid_messages(*load_message_rules(load_file('2020/input/19_TEST2.txt'), is_part1=False)), ['bbabbbbaabaabba', 'babbbbaabbbbbabbbbbbaabaaabaaa', 'aaabbbbbbaaaabaababaabababbabaaabbababababaaa', 'bbbbbbbaaaabbbbaaabbabaaa', 'bbbababbbbaaaaaaaabbababaaababaabab', 'ababaaaaaabaaab', 'ababaaaaabbbaba', 'baabbaaaabbaaaababbaababb', 'abbbbabbbbaaaababbbbbbaaaababb', 'aaaaabbaabaaaaababaa', 'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa', 'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'])

print(f"part 1: count of valid messages: {len(find_valid_messages(*load_message_rules(file_lines('2020/input/19_INPUT.txt'))))}")
# print(f"part 2: count of valid messages: {len(find_valid_messages(*load_message_rules(load_file('2020/input/19_INPUT.txt'), is_part1=False)))}")