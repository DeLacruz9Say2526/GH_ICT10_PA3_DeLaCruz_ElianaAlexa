# comment here
from pyscript import display, document


def countries_capital(e):
    document.getElementById('output').innerHTML = ' '
    user_input = document.getElementById('input1').value.capitalize().strip()

    countries = {
    'madagascar' : 'antananarivo',
    'mongolia' : 'ulaanbataar',
    'egypt' : 'cairo',
    'philippines' : 'manila',
    'usa' : 'dc washington',
    'denmark' : 'copenhangen',
    'chile' : 'santiago'
    }

    countries_checker = user_input in countries

    display_message = (f'Sorry, {user_input} isnt in the selection.', f'{user_input} is in this selection')

    display(display_message[countries_checker], target='output', append=False)


    # display(display_message[country_checker], target='output', append=False )

