# pylint: disable=too-few-public-methods

from enum import Enum, auto


def part_1_answer(lines):
    disk_map = parse(lines)

    free_space = move_forward_to_next_non_empty_free_space_or_end(disk_map.head)
    last_file = move_back_to_next_non_empty_file_or_start(disk_map.tail)

    while (free_space.value.type != RegionType.END) and (last_file.value.type != RegionType.START):

        # Fill the free space
        num_blocks_to_move = min(free_space.value.length, last_file.value.length)
        new_region = File(num_blocks_to_move, last_file.value.file_id)
        disk_map.insert_before(free_space, new_region)
        last_file.value.length -= num_blocks_to_move
        free_space.value.length -= num_blocks_to_move

        # Move to next non-empty file if necessary
        last_file = move_back_to_next_non_empty_file_or_start(last_file)
        disk_map.discard_after(last_file)

        # Remove free space, if it's now empty
        if free_space.value.length == 0:
            free_space_to_remove = free_space
            free_space = move_forward_to_next_non_empty_free_space_or_end(free_space)
            disk_map.remove(free_space_to_remove)

    return checksum(disk_map)


def move_forward_to_next_non_empty_free_space_or_end(node):
    while not (((node.value.type == RegionType.FREE_SPACE) and (node.value.length > 0))
               or (node.value.type == RegionType.END)):
        node = node.next
    return node


def move_back_to_next_non_empty_file_or_start(node):
    while not (((node.value.type == RegionType.FILE) and (node.value.length > 0))
               or (node.value.type == RegionType.START)):
        node = node.prev
    return node


def checksum(disk_map):
    total = 0
    start_pos = 0
    pos = disk_map.head
    while pos.value.type != RegionType.END:
        region = pos.value
        if region.type == RegionType.FILE:
            total += sum(pos * region.file_id for pos in range(start_pos, start_pos + region.length))
        start_pos += region.length
        pos = pos.next
    return total


def part_2_answer(lines):
    disk_map = parse(lines)

    file_nodes = {}
    node = disk_map.head
    while node.value.type != RegionType.END:
        if node.value.type == RegionType.FILE:
            file_nodes[node.value.file_id] = node
        node = node.next

    max_file_num = max(file_nodes.keys())

    # "move each file exactly once in order of decreasing file ID number
    # starting with the file with the highest file ID number"
    for file_num in range(max_file_num, 0, -1):
        file_to_move_node = file_nodes[file_num]
        # noinspection PyTypeChecker
        file_to_move: File = file_to_move_node.value

        # Find span of free space to the left of the file, large enough to fit the file
        free_space = disk_map.head
        while not (((free_space.value.type == RegionType.FILE) and
                    (free_space.value.file_id == file_to_move.file_id))
                   or ((free_space.value.type == RegionType.FREE_SPACE) and
                       (free_space.value.length >= file_to_move_node.value.length))):
            free_space = free_space.next

        if free_space.value.type == RegionType.FREE_SPACE:
            # Found a span of free space large enough
            disk_map.insert_before(free_space, file_to_move_node.value)
            free_space.value.length -= file_to_move_node.value.length
            file_to_move_node.value = FreeSpace(file_to_move_node.value.length)
            freed_space = file_to_move_node
            del file_to_move_node

            # Remove span of free space, if it's now empty
            if free_space.value.length == 0:
                disk_map.remove(free_space)

            # Merge freed space with free space before it
            if freed_space.prev.value.type == RegionType.FREE_SPACE:
                freed_space.value.length += freed_space.prev.value.length
                disk_map.remove(freed_space.prev)

            # Merge freed space with free space after it
            if freed_space.next.value.type == RegionType.FREE_SPACE:
                freed_space.value.length += freed_space.next.value.length
                disk_map.remove(freed_space.next)

            # Remove trailing free space
            if disk_map.tail.prev.value.type == RegionType.FREE_SPACE:
                disk_map.remove(disk_map.tail.prev)

    return checksum(disk_map)


def parse(lines):
    file = True
    file_id = 0
    disk_map = LinkedList()
    for i in lines[0]:
        length = int(i)
        if file:
            disk_map.append(File(length, file_id))
            file_id += 1
        elif length > 0:
            disk_map.append(FreeSpace(length))
        file = not file
    return disk_map


class Node:
    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev = prev_node
        self.next = next_node


class RegionType(Enum):
    START = auto()
    FILE = auto()
    FREE_SPACE = auto()
    END = auto()


class Region:
    def __init__(self, region_type, length):
        self.type = region_type
        self.length = length


class File(Region):
    def __init__(self, length, file_id):
        super().__init__(RegionType.FILE, length)
        self.length = length
        self.file_id = file_id

    def __repr__(self):
        return f"File[id={self.file_id}, length={self.length}]"


class FreeSpace(Region):
    def __init__(self, length):
        super().__init__(RegionType.FREE_SPACE, length)

    def __repr__(self):
        return f"FreeSpace[length={self.length}]"


class LinkedList:
    def __init__(self):
        self.head = Node(Region(RegionType.START, 0), None, None)
        self.tail = Node(Region(RegionType.END, 0), None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, value):
        new_node = Node(value, self.tail.prev, self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    @staticmethod
    def insert_before(node, value):
        new_node = Node(value, node.prev, node)
        node.prev.next = new_node
        node.prev = new_node

    @staticmethod
    def remove(node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def discard_after(self, node):
        node.next = self.tail
        self.tail.prev = node
