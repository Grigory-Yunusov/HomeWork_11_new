# Визначити до якої пори року відноситься місяць
month = 11

match month:
    case 3 | 4 | 5:
        season = 'весна'
    case 6 | 7 | 8:
        season = 'літо'
    case 9 | 10 | 11:
        season = 'осінь'
    case 12 | 1 | 2:
        season = 'зима'
print(season)