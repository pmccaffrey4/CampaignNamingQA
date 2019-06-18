# about me

name = 'Andy'
age = '24'
hobbies = ['Playing Basketball', 'Playing Soccer']

if __name__ == '__main__':

    print(f'My Name is {name}')
    print(f'I am {age} years old')

    print('My favorite things to do are...')
    for i, h in enumerate(hobbies):

        print(f'Hobby #{i + 1}  {h}')
