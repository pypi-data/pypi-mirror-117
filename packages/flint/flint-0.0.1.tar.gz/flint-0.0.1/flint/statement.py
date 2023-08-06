"""flint Statement class

:copyright: Copyright 2021 Marshall Ward, see AUTHORS for details.
:license: Apache License, Version 2.0, see LICENSE for details.
"""


class Statement(list):
    def __init__(self, *args, **kwds):
        # XXX: 'tag' is a dumb name, "type" or "class" is better but namespace
        #   issues ofc...
        self.tag = kwds.pop('tag') if 'tag' in kwds else None
        self.line_number = None

        super(Statement, self).__init__(*args, **kwds)

    # XXX: Dumb name... override __str__?
    def gen_stmt(self):
        """Recreate the statement by gathering tokens and null tokens."""
        header = ''.join(self[0].head)
        footer = ''.join(self[-1].tail)
        tag = self.tag if self.tag else '~'

        stmt = '{}│ '.format(tag)
        stmt += header.rsplit('\n')[-1] if header else ''
        stmt += ''.join([str(tok) + ''.join(tok.tail) for tok in self[:-1]])
        stmt += str(self[-1])
        stmt += ''.join(footer.rsplit('\n', 1)[:-1]) if footer else ''

        return stmt.replace('\n', '\n │ ')

    def reformat(self):
        """This is just a placeholder at the moment, but the idea is that this
        will 'reformat' the text according to a style guide."""
        return ' '.join([str(tok) for tok in self])
