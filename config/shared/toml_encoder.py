import toml


class TomlArraySeparatorEncoderWithNewline(toml.TomlArraySeparatorEncoder):
    """Special version indenting the first element of and array.

    In https://github.com/zopefoundation/meta/issues/118 we suggest to switch
    to Python 3.11 and its built-in toml support. We'll see if this path is
    still needed then.
    """

    def __init__(self, _dict=dict, preserve=False, separator=",",
                 indent_first_line=False):
        super(TomlArraySeparatorEncoderWithNewline, self).__init__(
            _dict=_dict, preserve=preserve, separator=separator)
        self.indent_first_line = indent_first_line

    def dump_list(self, v):
        t = []
        retval = "["
        if self.indent_first_line:
            retval += self.separator.strip(',')
        for u in v:
            t.append(self.dump_value(u))
        while t != []:
            s = []
            for u in t:
                if isinstance(u, list):
                    for r in u:
                        s.append(r)
                else:
                    retval += " " + u + self.separator
            t = s
        retval += " ]"
        return retval
