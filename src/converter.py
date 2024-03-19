def persian_number_to_integer(user_input):
    persian_numbers = {
        'یک': 1, 'دو': 2, 'سه': 3, 'چهار': 4, 'پنج': 5,
        'شش': 6, 'هفت': 7, 'هشت': 8, 'نه': 9, 'ده': 10,
        'یازده': 11, 'دوازده': 12, 'سیزده': 13, 'چهارده': 14, 'پانزده': 15,
        'شانزده': 16, 'هفده': 17, 'هجده': 18, 'نوزده': 19, 'بیست': 20,
        'سی': 30, 'چهل': 40, 'پنجاه': 50, 'شصت': 60, 'هفتاد': 70,
        'هشتاد': 80, 'نود': 90, 'صد': 100, 'هزار': 1000, 'میلیون': 1000000,
        'میلیارد': 1000000000
    }

    words = user_input.split()
    number = 0
    accumulator = 0

    for word in words:
        if word in persian_numbers:
            accumulator += persian_numbers[word]
        elif word == 'نیم':
            accumulator += 0.5
        elif word == 'و':
            number += accumulator
            accumulator = 0

    number += accumulator

    return number