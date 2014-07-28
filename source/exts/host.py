from docutils import nodes
from sphinx.locale import _
from docutils.parsers.rst import Directive
from sphinx.util.compat import make_admonition

class HostDirective(Directive):

    has_content = True

    def run(self):
        ad = make_admonition(host, self.name, [_('Host')], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        return ad

class host(nodes.Admonition, nodes.Element):
    pass

def visit_host_node(self, node):
    self.visit_admonition(node)

def depart_host_node(self, node):
    self.depart_admonition(node)

def setup(app):
    app.add_node(host,
                 html=(visit_host_node, depart_host_node),
                 latex=(visit_host_node, depart_host_node),
                 text=(visit_host_node, depart_host_node))

    app.add_directive('host', HostDirective)
