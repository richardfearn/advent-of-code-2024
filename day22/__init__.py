from collections import deque, defaultdict


def part_1_answer(lines):
    initial_secret_numbers = [int(line) for line in lines]
    return sum(evolve_n_times(n, 2000) for n in initial_secret_numbers)


def evolve_n_times(number, count):
    for _ in range(count):
        number = evolve(number)
    return number


def evolve(number):
    number = prune(mix(number, (number * 64)))
    number = prune(mix(number, (number // 32)))
    number = prune(mix(number, (number * 2048)))
    return number


def mix(a, b):
    return a ^ b


def prune(n):
    return n % 16777216


def part_2_answer(lines):
    initial_secret_numbers = [int(line) for line in lines]

    sequence_buyer_prices = defaultdict(dict)

    for buyer, initial_secret_number in enumerate(initial_secret_numbers):

        number = initial_secret_number
        old_price = number % 10

        price_changes = deque()

        for step in range(1, 2001):

            number = evolve(number)
            price = number % 10

            price_change = price - old_price

            price_changes.append(price_change)
            if step > 4:
                price_changes.popleft()

            if step >= 4:
                sequence = tuple(price_changes)
                if buyer not in sequence_buyer_prices[sequence]:
                    sequence_buyer_prices[sequence][buyer] = price

            old_price = price

    total_prices_per_sequence = {sequence: sum(prices.values()) for sequence, prices in sequence_buyer_prices.items()}
    return max(total_prices_per_sequence.values())
