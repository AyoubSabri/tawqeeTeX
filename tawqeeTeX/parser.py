import argparse

prog_name = 'tawqeeTeX'
version = '1.0'

def get_args():

    # create the parser
    parser = argparse.ArgumentParser(prog=prog_name, description='tawqeeTeX is a LaTeX prayer time generator',
                                     epilog="Developed by Ayoub Sabri - ayoub.sabri@etu.upmc.fr")

    # positional arguments
    parser.add_argument('city')
    parser.add_argument('country')
    parser.add_argument('month')
    parser.add_argument('year')

    # optional arguments
    parser.add_argument('-m', '--method',
        choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
        default='1', help="""
        set the calculation method (default: 1)
        1  - Muslim World League \n
        2  - Islamic Society of North America \n
        3  - Egyptian General Authority of Survey \n
        4  - Umm Al-Qura University, Makkah \n
        5  - University of Islamic Sciences, Karachi \n
        6  - Institute of Geophysics, University of Tehran \n
        7  - Shia Ithna-Ashari, Leva Institute, Qum \n
        8  - Gulf Region \n
        9  - Kuwait \n
        10 - Qatar \n
        11 - Majlis Ugama Islam Singapura, Singapore \n
        12 - Union Organization Islamique de France \n
        13 - Diyanet İşleri Başkanlığı, Turkey \n
        14 - Spiritual Administration of Muslims of Russia \n\n

        Please refer to https://aladhan.com/calculation-methods to know more""")

    parser.add_argument('-a', '--adjustment', default='0',
                        help='define the offset for the hijri calendar (default: %(default)s)')

    parser.add_argument('-l','--language', default='en',
                        choices=['en', 'fr', 'it'],
                        help='set the language (default: %(default)s)')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version,
                        help='print the current version of the software')

    #TODO: update

    args = vars(parser.parse_args())
    return  args['city'], args['country'], args['month'], args['year'], \
            args['method'], args['language'], args['adjustment']
