def get_winners_overview(input_str: str):
    overview = {}
    for line in input_str.splitlines():
        number_info, tickets = line.split(":")
        ticket_number = int(number_info.split()[1])
        my_ticket, winner_numbers = tickets.split(' | ')

        my_ticket = [int(i) for i in my_ticket.split()]
        winner_numbers = [int(i) for i in winner_numbers.split()]

        n_winners = len(set(my_ticket) & set(winner_numbers))
        overview[ticket_number] = n_winners
    return overview


def part_a(input_str: str):
    data = get_winners_overview(input_str)
    points = 0
    for n in data.values():
        points += 2 ** (n-1) if n else 0
    return points


def part_b(input_str: str):
    winner_overview = get_winners_overview(input_str)
    n_tickets = {idx: 1 for idx in winner_overview.keys()}

    for ticket_id, n_ticket_won in winner_overview.items():
        for new_ticket_id in range(ticket_id+1, ticket_id+1+n_ticket_won):
            n_tickets[new_ticket_id] += 1 * n_tickets[ticket_id]
    total_tickets = sum(n_tickets.values())

    return total_tickets
