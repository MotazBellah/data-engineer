from database_setup import get_data

def run():
    return get_data('''select date, target from rate where date = '2019-06-06'
                    and source = 'USD' union  select date, target from rate
                    where date = '2019-06-07' and source = 'EUR' ;''')

if __name__ == '__main__':
    print(run())
