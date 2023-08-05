from jinja2 import Environment, PackageLoader, StrictUndefined

from strictdoc.core.document_tree_iterator import DocumentTreeIterator
from strictdoc.core.traceability_index import TraceabilityIndex
from strictdoc.export.html.renderers.markup_renderer import MarkupRenderer


class RequirementsCoverageHTMLGenerator:
    env = Environment(
        loader=PackageLoader("strictdoc", "export/html/templates"),
        undefined=StrictUndefined,
    )
    env.globals.update(isinstance=isinstance)

    @staticmethod
    def export(
        document_tree, traceability_index: TraceabilityIndex, link_renderer
    ):
        document_tree_iterator = DocumentTreeIterator(document_tree)

        output = ""

        template = RequirementsCoverageHTMLGenerator.env.get_template(
            "requirements_coverage/requirements_coverage.jinja.html"
        )

        markup_renderer = MarkupRenderer.create("RST")
        output += template.render(
            document_tree=document_tree,
            traceability_index=traceability_index,
            documents_iterator=document_tree_iterator.iterator(),
            link_renderer=link_renderer,
            renderer=markup_renderer,
            static_path="_static",
        )

        return output
