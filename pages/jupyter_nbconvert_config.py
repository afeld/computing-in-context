"""Settings for the slides that myst-slides builds with nbconvert, equivalent to `make slides`."""

from pathlib import Path

c = get_config()  # noqa: F821

c.SlidesExporter.reveal_scroll = True
c.TemplateExporter.extra_template_basedirs = [str(Path(__file__).parent.parent / "_templates")]
c.TemplateExporter.template_name = "reveal-with-css"
