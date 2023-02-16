####Exercises on Fnction and how it works
#Exercise 8-1.Message:function called display_message() that prints one sen￾tence
def display_message():
    '''Display simple message'''
    print('Message on how functions works in Python ')
display_message()

#Exercise 8-2.Favorite Book:Example of function called favorite_book() with its title
def favorite_book(title):
    '''My favourite book'''
    print(f'My favorite book is {title}')
favorite_book('Alice')

#Exercise 8-3. T-Shirt:function called make_shirt() that accepts a size and the 

def Make_shirt(size,message):

    print(f'{size} shirt, {message}')

Make_shirt('Medium','you are the best')
Make_shirt(size='Medium',message='you are the best')

#Exercise 8-4. Large Shirts: Modify the T_shirt() function so that shirts are large by default
def make_shirt_2(size='large',message='I love Python'):
    '''Summarising shirt details'''
    print(f'{size} shirt, {message}')

make_shirt_2('large')
make_shirt_2('medium')
make_shirt_2('small','Potential programmer')

#Exercise 8-5. Cities: function that describe_city() that accepts the name of a city its country.
def describe_city(city,country='Nigeria'):
    '''Describe a city'''
    print(f'{city} is an important city in {country}')
describe_city('Kano')
describe_city('Kebbi')
describe_city('Jeddah','Saudi Arabia')

#Exercise 8-6. City Names: Write a function called city_country() that takes in 
# the name of a city and its country.
def city_country(city,country):
    '''Returns the formatted name of a city and its country'''
    full = f'{city}, {country}'
    return full.title()

KN = city_country('Kano','Nigeria')
print(KN)
UK = city_country('London','United Kingdom')
print(UK)
GA = city_country('Accra','Ghana')
print(GA)

#Exercise 8-7. Album: function called album() that builds a dictionary 
# describing a music album with artist name and album title.
def make_album(artist_name,album_title):
    '''Returns a dictionary of music album details'''
    music_album = {'artist':artist_name,'album_title':album_title}
    return music_album
a = make_album('West life','My love')
b = make_album('Celinedion','I\'m alive')
c = make_album('Nazifi Asnanic','Bankwana')
print(a,b,c,)
    
def make_album_2(artist_name,album_title,song_num=None):
    '''Returns a dictionary of music album details'''
    music_album = {'artist':artist_name,'album_title':album_title}
    if song_num:
        music_album['Number of songs'] = song_num
    return music_album

d = make_album_2('Sadi Sidi','Ke nakeso',2)
print(d)
e = make_album_2('Naziru','Sarki Sunusi')  
print(e)
#Exercise 8-8. User Albums: Write a while loop that allows users to enter
# an album’s artist and title and call make_album() with the user’s input and print the dictionary 
while True:
    print('Please Enter the album\'s details')
    print('Enter "q" to quit')
    album_artist = input('Enter the name of the artist: ')
    if album_artist == 'q':
        break
    album_title = input('Enter the title of the album: ')
    if album_title == 'q':
        break

    album = make_album(album_artist,album_title)
    print(f'\nHere is the album: {album}')

#Exercise 8-9. Messages: Make a list containing a series of short text messages.
# and Pass the list to a function called show_messages()
messages = ['My journey to become programmer','Data Scientist','Machine Learning','Deep Learning']
def show_messages(list):
    '''Prints the messages contained in a list of messages passed to it'''
    for item in list:
        print(item)
show_messages(messages)

#Exercise 8-10. Sending Messages:Write a function called send_messages() 
# that prints each text message and moves each message to a new list
def send_messages(message_list,sent_messages):
    '''Moves each message in the message_list to sent_messages list after printing'''
    while message_list:
        sent_message = message_list.pop()
        print(f'Sending message: {sent_message}')
        sent_messages.append(sent_message)

messages = ['My journey to become programmer','Data Scientist','Machine Learning','Deep Learning']
sent = []
send_messages(messages,sent)
print(f'initial: {messages},final: {sent}')

#Exercise 8-11.Archived Messages: Call the function send_messages(), 
# print both of your lists to show that the original list retained
messages = ['My journey to become programmer','Data Scientist','Machine Learning','Deep Learning']
sent = []
send_messages(messages[:],sent)

#Exercise 8-12. Sandwiches: Write a function that accepts a list of items a people that wants sandwich. 
def make_sandwich(*items):
    '''Print a summary of the contents of ordered sandwich'''
    print(f'Sandwich will be made containing the following: ')
    for item in items:
        print(f'-{item}')
make_sandwich('pizza','burger','shawarma')

#Exercise 8-13. User Profile: User_profile.py from page 149. Build a profile of 
# yourself by calling build_profile(), using your first and last names
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
build_profile('Umar','Sani',age=30,language='Hausa',country='Nigeria')

#Exercise 8-14.Cars: Write a function that stores information about a car in a dictionary. 
def make_car(Manufacturer,Model_name,**Car_info):
    '''Gives information about a car'''
    Car_info['Manufacturer'] = Manufacturer
    Car_info['Model_Name'] = Model_name 
    return Car_info
make_car('Toyota','Le',Year=2010,Colour='Blue')