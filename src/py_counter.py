import libcst.matchers as m
import libcst as cst

def PyCount():
    # parses through the given test file
    search = cst.parse_module(open("test.py").read())

    def count_class_definitions():
        definitions = m.findall(search, m.ClassDef())
        print(len(definitions))