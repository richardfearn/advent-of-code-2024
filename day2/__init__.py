from itertools import pairwise


def part_1_answer(reports):
    return [is_safe(parse_report(report)) for report in reports].count(True)


def is_safe(report):
    return is_ascending(report) or is_ascending(reversed(report))


def is_ascending(report):
    diffs = {(a - b) for (a, b) in pairwise(report)}
    return (min(diffs) >= 1) and (max(diffs) <= 3)


def part_2_answer(reports):
    return [is_safe_with_removal(parse_report(report)) for report in reports].count(True)


def is_safe_with_removal(report):
    return is_safe(report) or any(is_safe(level_removed(report, i)) for i in range(len(report)))


def level_removed(report, i):
    return report[:i] + report[i + 1:]


def parse_report(report):
    return [int(n) for n in report.split()]
