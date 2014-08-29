from docutils import nodes
from sphinx.locale import _
from docutils.parsers.rst import Directive
from sphinx.util.compat import make_admonition

class BoardDirective(Directive):

    has_content = True

    def run(self):
        ad = make_admonition(board, self.name, [_('Board')], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        return ad

class board(nodes.Admonition, nodes.Element):
    pass

def visit_board_node(self, node):
    self.visit_admonition(node)

def depart_board_node(self, node):
    self.depart_admonition(node)

def setup(app):
    app.add_node(board,
                 html=(visit_board_node, depart_board_node),
                 latex=(visit_board_node, depart_board_node),
                 text=(visit_board_node, depart_board_node))

    app.add_directive('board', BoardDirective)
