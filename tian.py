# about me

name = 'Tian Shan'
age = '23'
hobbies = ['Watching movies', 'Traveling']

if __name__ == '__main__':

    print(f'My Name is {name}')
    print(f'I am {age} years old')

    print('My favorite things to do are...')
    for i, h in enumerate(hobbies):

        print(f'Hobby #{i + 1}  {h}')
