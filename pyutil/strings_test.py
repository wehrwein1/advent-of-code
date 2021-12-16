from pyutil.strings import partition

def test_partition():
  assert partition(["line1", "line2", "line3"]) == [["line1","line2","line3"]]
  assert partition(["line1", "line2", "", "line3", "line4"]) == [["line1","line2"],["line3","line4"]]
