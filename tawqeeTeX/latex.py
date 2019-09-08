#TODO: add logo plus information
#TODO: adapt style and font
#TODO: center table
#TODO: add comments
#TODO: import only what is needed

from data import *
from pylatex import *
from pylatex.utils import *

def gen_pdf():

    c = 0

    geometry_options = {"tmargin": "3cm", "bmargin": "2 cm", "rmargin": "2cm", "lmargin": "2cm"}
    doc = Document(geometry_options=geometry_options)

    doc.preamble.append(NoEscape(r'\usepackage[T2A,LAE,T1]{fontenc}'))
    doc.preamble.append(NoEscape(r'\usepackage[arabic, USenglish]{babel}'))

    # Add document header
    header = PageStyle("header")
    # Create left header
    with header.create(Head("L")):
        header.append("Associazione Culturale Islamica \"Annour\"")
        header.append(LineBreak())
        header.append("Via Canale n° 582/4,")
        header.append(LineBreak())
        header.append("48014 Castel Bolognese (RA)")
    # Create center header
    with header.create(Head("C")):
        header.append("")
    # Create right header
    with header.create(Head("R")):
        header.append("logo goes here")
    # Create center footer
    with header.create(Foot("C")):      #NOTE: L and R footer are also available
        header.append("Generated with tawqeeTeX - tawqeeTeX@gmail.com")

    doc.preamble.append(header)
    doc.change_document_style("header")

    # Add Heading
    with doc.create(MiniPage(align='c')):
        doc.append(VerticalSpace('30pt'))
        doc.append(LargeText(bold(get_title_str())))
        doc.append(VerticalSpace('20pt'))
        doc.append(LineBreak())

        with doc.create(Tabu('|lc|cccccc|cr|', pos='c', row_height='1.35', col_space='7.5', width=10)) as table:

            table.add_hline()
            table.add_row(('', get_month_str(), 'Isha', 'Maghrib', 'Asr', 'Dhuhr', 'Shuruq', 'Fajr', NoEscape(r'\AR{' + months['hi'] + '}'), ''), color='lightgray')
            table.add_hline()

            for day, weekday in date_gr.items():
                table.add_row(get_weekday_str(weekday), day, isha[c], maghrib[c], asr[c], dhuhr[c], sunrise[c], fajr[c], hi_day[c], NoEscape(r'\AR{' + hi_weekday[c] + '}'))
                table.add_hline()
                c += 1

    doc.generate_pdf('full', clean_tex=False)
