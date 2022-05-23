# Jinja test to generate PDFs from HTML files.
# install wkhtmltopdf on the terminal: sudo apt install -y wkhtmltopdf


from jinja2 import Environment, FileSystemLoader, select_autoescape
import pdfkit


def html2pdf(html_path, pdf_path):
    '''Convert html to pdf using pdfkit'''
    options = {
        'page-size': 'Letter',
        'margin-top': '0.35in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None
    }
    with open(html_path) as f:
        pdfkit.from_file(f, pdf_path, options=options)


env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

# template = env.get_template("one.html")
# print(template.render(thing ="Hello there"))

template = env.get_template("one.html")
context = {
    "thing": "Hello There",
    "data": [
        {"name": "wibble", "count": 45},
        {"name": "sqokl", "count": 45}
    ]
}

print(template.render(**context))

html_path = "/home/vincenzo/PycharmProjects/test_jinja/templates/one.html"
pdf_path = "/home/vincenzo/PycharmProjects/test_jinja/pdf/one.pdf"

html2pdf(html_path, pdf_path)
