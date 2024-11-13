from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.tableofcontents import TableOfContents
toc = TableOfContents()
toc.levelStyles = [ParagraphStyle(name = 'Heading1',fontSize = 16,leading = 16),ParagraphStyle(name = 'Heading2',fontSize = 12,leading = 14),]
