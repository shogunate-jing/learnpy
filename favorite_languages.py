favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}


for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
	language.title() + ".")


friends = ['phil','sarah']
for name in sorted(favorite_languages.keys()):
	print(name.title())

for name in friends:
	print(name.title() + ",I see you favorite language is " +
	favorite_languages[name].title() + "!")

for languages in set(favorite_languages.values()):
	print(languages.title())

