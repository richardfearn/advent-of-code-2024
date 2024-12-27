# pylint: disable=too-few-public-methods

from enum import Enum, auto


def part_1_answer(lines):
    disk_map = parse(lines)

    while len([r for r in disk_map if r.type == RegionType.FREE_SPACE]) > 0:

        # Still have at least one region of free space to fill. Find the first one
        first_free_space_index, first_free_space = next(
            (i, r) for i, r in enumerate(disk_map)
            if r.type == RegionType.FREE_SPACE)

        # Will fill the free space with blocks from the last file
        last_file_index = len(disk_map) - 1
        last_file = disk_map[last_file_index]

        num_blocks_to_move = min(first_free_space.length, last_file.length)

        # Move blocks from last file
        new_region = File(num_blocks_to_move, last_file.file_id)
        disk_map.insert(first_free_space_index, new_region)
        first_free_space_index += 1
        last_file_index += 1
        first_free_space.length -= num_blocks_to_move
        last_file.length -= num_blocks_to_move

        # Remove free space region, if it's now empty
        if first_free_space.length == 0:
            disk_map.pop(first_free_space_index)
            last_file_index -= 1

        # Remove last file, if it's now empty
        if last_file.length == 0:
            disk_map.pop(last_file_index)

            # Also remove any free space that could now be at the end
            if disk_map[len(disk_map) - 1].type == RegionType.FREE_SPACE:
                disk_map.pop(len(disk_map) - 1)

    return checksum(disk_map)


def checksum(disk_map):
    total = 0
    start_pos = 0
    for region in disk_map:
        if region.type == RegionType.FILE:
            total += sum(pos * region.file_id for pos in range(start_pos, start_pos + region.length))
        start_pos += region.length
    return total


def part_2_answer(lines):
    disk_map = parse(lines)

    max_file_num = max(r.file_id for r in disk_map if r.type == RegionType.FILE)

    for file_to_move in range(max_file_num, 0, -1):
        file_index, file = next(
            (i, r) for i, r in enumerate(disk_map)
            if r.type == RegionType.FILE and r.file_id == file_to_move)

        move_file_if_possible(disk_map, file_index, file)

    return checksum(disk_map)


def move_file_if_possible(disk_map, file_index, file):
    for i in range(0, file_index):
        if disk_map[i].type == RegionType.FREE_SPACE:
            free_space_index, free_space = i, disk_map[i]

            if free_space.length >= file.length:
                # Free space is large enough to contain the file

                # Move the file
                disk_map.insert(i, file)
                free_space_index += 1
                file_index += 1
                free_space.length -= file.length
                disk_map[file_index] = FreeSpace(file.length)

                # Remove free space region, if it's now empty
                if free_space.length == 0:
                    disk_map.pop(free_space_index)
                    file_index -= 1

                # Also remove any free space that could now be at the end
                while disk_map[len(disk_map) - 1].type == RegionType.FREE_SPACE:
                    disk_map.pop(len(disk_map) - 1)

                # Merge adjacent free space regions
                for j in range(len(disk_map) - 1, 0, -1):
                    if (disk_map[j - 1].type == RegionType.FREE_SPACE) and (disk_map[j].type == RegionType.FREE_SPACE):
                        disk_map[j - 1].length += disk_map[j].length
                        disk_map.pop(j)

                return


def parse(lines):
    file = True
    file_id = 0
    disk_map = []
    for i in lines[0]:
        length = int(i)
        if file:
            disk_map.append(File(length, file_id))
            file_id += 1
        elif length > 0:
            disk_map.append(FreeSpace(length))
        file = not file
    return disk_map


class RegionType(Enum):
    FILE = auto()
    FREE_SPACE = auto()


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
