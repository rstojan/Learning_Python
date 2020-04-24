music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

print(music)

user_input = input("1. Add artist\n"
                    "2. Add album\n"
                    "3. Add song\n"
                    "4. Print the library\n"
                    "Exit to quit\n"
                    "Enter action: "
)

while True:
    if user_input == 1:
        new_artist = input('New artists name: ')
        music[new_artist]
    elif user_input == 2:
        new_album == input('New album name: ')
        music[artist][new_album]
    elif user_input == 3:
        new_song == input('New song name: ')
        music[artist][album][new_song]
    elif user_input == 4:
        print(music)
        break
