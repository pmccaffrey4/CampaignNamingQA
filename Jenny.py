# about me

name = 'Jenny'
age = '24'
hobbies = ["tv shows","dogs & coffee","drawing"]

if __name__ == '__main__':

    print(f'My Name is {name}')
    print(f'I am {age} years old')

    print('My favorite things to do are...')
    for i, h in enumerate(hobbies):

        print(f'Hobby #{i + 1}  {h}')
