# ask user whether the person has accounts
facebook = input('Facebook account? (y/n): ') == 'y'
twitter = input('Twitter account? (y/n): ') == 'y'
instagram = input('Instagram account? (y/n): ') == 'y'

print(f"facebook = {facebook}")
print(f"twitter = {twitter}")
print(f"instagram = {instagram}")
if sum((facebook, twitter, instagram)) >= 2:
    print('You are a good influencer!')
else:
    print('You are NOT a good influencer.')
