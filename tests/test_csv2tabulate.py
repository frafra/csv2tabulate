import io

from csv2tabulate.converter import convert


def test_convert():
    file_obj = io.StringIO("label1,label2,label3\na,b,c")
    rows = convert(file_obj, tablefmt="github").split("\n")
    assert len(rows) == 3
    assert set(rows[1]) ^ set("|-") == set()
