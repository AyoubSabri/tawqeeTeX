from .parser import get_args
from .data import Tawqeetex

def console_start():
    '''Retrieves the inputs from the console and starts the pdf schedule generation'''
    args = get_args()
    data = Tawqeetex(*args)
    data.create_schedule()
    print("The prayer time schedule has been generated successfully")
