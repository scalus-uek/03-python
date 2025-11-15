interested = input('Are you interested in computer science? (y/n): ') == 'y'
plays_games = input('Do you like playing computer games? (y/n): ') == 'y'
has_instagram = input('Do you have an Instagram account? (y/n): ') == 'y'

print('\nSURVEY RESULTS')
print('Interested in computer science: ' + ('Yes' if interested else 'No'))
print('Playing computer games: ' + ('Yes' if plays_games else 'No'))
print('Has an Instagram account: ' + ('Yes' if has_instagram else 'No'))
