import nbformat


def read_notebook(notebook_path):
    return nbformat.read(notebook_path, as_version=4)


def is_markdown(cell):
    return cell.cell_type == "markdown"


def is_h1(cell):
    return is_markdown(cell) and cell.source.startswith("# ")


def is_magic(source):
    return source.startswith("%%")


def is_system_command(source: str):
    return source.startswith("!")


def is_code_cell(cell):
    return cell.cell_type == "code"


def is_python(cell):
    source = cell.source
    return is_code_cell(cell) and not (is_magic(source) or is_system_command(source))
