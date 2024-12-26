from collections import defaultdict

import utils


def part_1_answer(lines):
    rules, updates = parse(lines)
    must_be_before, must_be_after = process_rules(rules)

    return sum(middle_page_number(update)
               for update in updates
               if is_correct_order(update, must_be_before, must_be_after))


def is_correct_order(update, must_be_before, must_be_after):
    for i, n in enumerate(update):
        before = set(update[:i])
        after = set(update[i + 1:])
        if not_subset(before, must_be_before[n]) or not_subset(after, must_be_after[n]):
            return False
    return True


def part_2_answer(lines):
    rules, updates = parse(lines)
    must_be_before, must_be_after = process_rules(rules)

    return sum(middle_page_number(make_correct(update, must_be_before))
               for update in updates
               if not is_correct_order(update, must_be_before, must_be_after))


def make_correct(update, must_be_before):
    update = set(update)
    must_be_before = {a: b.intersection(update) for a, b in must_be_before.items() if a in update}

    new_order = []
    while len(update) > 0:
        next_page = next(page for page in update if len(must_be_before[page]) == 0)
        update.remove(next_page)
        new_order.append(next_page)

        must_be_before.pop(next_page)
        for pages in must_be_before.values():
            pages.remove(next_page)

    return new_order


def middle_page_number(update):
    return update[len(update) // 2]


def not_subset(a, b):
    return not a <= b


def parse(lines):
    rules, updates = utils.group_lines(lines)  # pylint: disable=unbalanced-tuple-unpacking
    rules = [parse_rule(rule) for rule in rules]
    updates = [parse_update(update) for update in updates]
    return rules, updates


def parse_rule(rule):
    return (int(n) for n in rule.split("|"))


def parse_update(update):
    return [int(n) for n in update.split(",")]


def process_rules(rules):
    must_be_before = defaultdict(set)
    must_be_after = defaultdict(set)
    for a, b in rules:
        must_be_before[b].add(a)
        must_be_after[a].add(b)
    return must_be_before, must_be_after
