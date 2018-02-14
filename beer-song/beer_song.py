def recite(start, take=1):
    def bottles(i):
        return '{} {}'.format('no more' if i == 0 else i, 'bottle' if i == 1 else 'bottles')

    result = []
    for i in range(start, start-take, -1):
        result.append('{} of beer on the wall, {} of beer.'.format(
            bottles(i).capitalize(),
            bottles(i)
        ))
        result.append('{}, {} of beer on the wall.'.format(
            'Go to the store and buy some more' if i == 0 else 'Take {} down and pass it around'.format(
                'it' if i == 1 else 'one'
            ),
            bottles((i - 1) % 100)
        ))
        result.append('')

    return result[:-1]

