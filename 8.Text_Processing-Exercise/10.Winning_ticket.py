def unique_fn(symbols, half):
    unique = ''
    counter = 0
    for string in symbols:
        sym_count = 0
        for sym in half:
            if string == sym:
                sym_count += 1
        if sym_count > counter:
            counter = sym_count
            unique = string
    unique = unique * counter
    return unique


tickets = input().split(', ')
symbols = '@#$^'
for ticket in tickets:
    won = False
    ticket = ticket.strip()
    if len(ticket) == 20:
        half = int(len(ticket)/2)
        first_half = ticket[0:half]
        second_half = ticket[half:]
        first_half_ticket = ''
        second_half_ticket = ''

        for symbol in first_half:
            if symbol in symbols:
                first_half_ticket += symbol
            else:
                if len(first_half_ticket) < 6:
                    first_half_ticket = ''

        for symbol in second_half:
            if symbol in symbols:
                second_half_ticket += symbol
            else:
                if len(second_half_ticket) < 6:
                    second_half_ticket = ''

        len_one = len(first_half_ticket)
        len_two = len(second_half_ticket)
        left_unique = unique_fn(symbols, first_half_ticket)
        right_unique = unique_fn(symbols, second_half_ticket)

        if len(left_unique) >= 6 and len(right_unique) >= 6 and set(left_unique) == set(right_unique):
            won = True
        if won:
            if len(left_unique) == 10 and len(right_unique) == 10:

                print(f'ticket "{ticket}" - {len(left_unique)}{left_unique[0]} Jackpot!')

            elif 6 <= len(left_unique)  and 6 <= len(right_unique) :

                if len(left_unique) < len(right_unique):
                    to_print = left_unique
                elif len(left_unique) > len(right_unique):
                    to_print = right_unique
                else:
                    to_print = left_unique
                print(f'ticket "{ticket}" - {len(to_print)}{to_print[0]}')



        if not won:
            print(f'ticket "{ticket}" - no match')
    else:
        print(f'invalid ticket')
