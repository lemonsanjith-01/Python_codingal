temparature = int(input('What is the temparature:'))
if temparature < 20:
  outfit = 'jacket'
  print('Wear a Jacket')
else:
  outfit = 't-shirt'
  print('Wear a t-shirt')
is_raining = bool(input('Is it raining? (True or False): '))
if is_raining:
  print('Bring an umbrella with you')
else:
  print('Go freehand')
windspeed = int(input('What is the windspeed in km/h:'))
if windspeed > 30:
  needs_windbreaker = 'yes'
  print('It is windy today.')
  print('Wear a windbreaker over your', outfit)
else:
  need_windbreaker = 'no'
  print('it is calm today.')
  print('No need for a wind breaker over your', outfit)
is_puddles = input('Are there puddle on the ground? (Yes/No)')
if is_puddles == 'yes':
  shoes = 'boots'
  print('The ground is wet')
  print('wear', shoes)
else:
  shoes = 'sneakers'
  print('The ground is not wet')
  print('wear', shoes)
