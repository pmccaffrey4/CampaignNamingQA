# about me

name = 'Patrick'
age = '27'
hobbies = ['Hanging w/ Friends & Family', 'Watching dope tv shows', 'Singing in the mirror', 'Coding']

if __name__ == '__main__':

    print(f'My Name is {name}')
    print(f'I am {age} years old')

    print('My favorite things to do are...')
    for i, h in enumerate(hobbies):

        print(f'Hobby #{i + 1}  {h}')
