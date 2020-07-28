from pylatex import Document, Head, Foot, LineBreak, LargeText, PageStyle, Tabular, VerticalSpace
from pylatex.utils import NoEscape, bold, italic

from .utils import *

def gen_pdf(data):
    '''
    This function generates a pdf prayer time schedule using latexself.
    It takes a Tawqeetex object (data) that must be initialized before the call.
    '''
    geometry_options = {"tmargin": "3cm", "bmargin": "2cm", "rmargin": "2cm", "lmargin": "2cm"}
    doc = Document(geometry_options=geometry_options)

    # Add packages for arabic text
    doc.preamble.append(NoEscape(r'\usepackage[T2A,LAE,T1]{fontenc}'))
    doc.preamble.append(NoEscape(r'\usepackage[arabic, USenglish]{babel}'))

    # Add document header
    header = PageStyle("header") # header_thickness=0, footer_thickness=0
    # # Create left header
    # with header.create(Head("L")):
    #     header.append("")
    # # Create center header
    # with header.create(Head("C")):
    #     header.append("")
    # # Create right header
    # with header.create(Head("R")):
    #     header.append("logo goes here")
    # Create center footer
    with header.create(Foot("C")):      #NOTE: L and R footer are also available
        header.append("Generated with tawqeeTeX")

    # Add Heading
    doc.preamble.append(header)
    doc.change_document_style("header")

    doc.append(NoEscape(r'\begin{center}'))

    #doc.append(VerticalSpace('20pt'))
    doc.append(LargeText(bold(get_title_str(data.lang, data.month, data.year))))
    doc.append(VerticalSpace('20pt'))
    doc.append(LineBreak())
    doc.append(LargeText(italic(data.city)))
    doc.append(VerticalSpace('20pt'))
    doc.append(LineBreak())

    doc.append(NoEscape(r'\rowcolors{2}{green!10}{yellow!10}'))
    doc.append(NoEscape(r'\setlength{\arrayrulewidth}{0.5pt}'))

    # Create table for the prayer time schedule
    with doc.create(Tabular('|lc|cccccc|cr|', pos='c', row_height='1.35', col_space='7.5', width=10)) as table:

        table.add_hline()
        table.add_row(('', get_month_str(data.lang, data.month), 'Isha', 'Maghrib', 'Asr', 'Dhuhr',
                       'Shuruq', 'Fajr', NoEscape(r'\AR{' + data.months['hi'] + '}'),
                        ''), color='lightgray!20')
        table.add_row(('', '', *get_prayers_str(), '', ''), color='lightgray!20')
        table.add_hline()
        c = 0

        for day, weekday in data.date_gr.items():
            # Insert timings
            table.add_row(get_weekday_str(weekday, data.lang), day, data.isha[c], data.maghrib[c],
                          data.asr[c], data.dhuhr[c], data.sunrise[c], data.fajr[c], data.hi_day[c],
                          NoEscape(r'\AR{' + data.hi_weekday[c] + '}'))
            table.add_hline()
            c += 1

    doc.append(NoEscape(r'\end{center}'))
    doc.generate_pdf(data.city + '-' + data.month + '-' + data.year, clean_tex=False, silent=True)
