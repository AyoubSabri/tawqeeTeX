from data import init_data
from latex import gen_pdf
from parser import get_args

def main():
    init_data(*get_args())
    gen_pdf()

def main_gui():
    pass

if __name__ == '__main__':
    main()
