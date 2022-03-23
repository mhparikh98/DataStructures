from typing import List
from math import pow

# https://www.javatpoint.com/tower-of-hanoi-puzzle-using-python


class TowerOfHanoi:

    def __init__(self) -> None:
        self.total_disks = 0

    def __recursively_move_disks(self, total_disks: int, source: str, auxillary: str, destination: str) -> None:
        if total_disks == 1:
            print("Move disk {} from {} to {}".format(total_disks, source, destination))
        else:
            self.__recursively_move_disks(total_disks-1, source, destination, auxillary)
            print("Move disk {} from {} to {}".format(total_disks, source, destination))
            self.__recursively_move_disks(total_disks-1, auxillary, source, destination)

    def __move_disk(self, source: List, destination: List, source_pole: str, destination_pole: str) -> None:
        if len(source) > 0 and len(destination) > 0:
            if source[0] > destination[0]:
                disk_no = destination.pop(0)
                source.append(disk_no)
                print("Move disk {} from {} to {}".format(disk_no, destination_pole, source_pole))
            else:
                disk_no = source.pop(0)
                destination.append(disk_no)
                print("Move disk {} from {} to {}".format(disk_no, source_pole, destination_pole))
        elif len(source) > 0:
            disk_no = source.pop(0)
            destination.append(disk_no)
            print("Move disk {} from {} to {}".format(disk_no, source_pole, destination_pole))
        elif len(destination) > 0:
            disk_no = destination.pop(0)
            source.append(disk_no)
            print("Move disk {} from {} to {}".format(disk_no, destination_pole, source_pole))

    def __iteratively_move_disks(self, total_disks: int, source: str, auxillary: str, destination: str) -> None:
        total_moves = int(pow(2, total_disks) - 1)
        source_list = list(range(1, total_disks +1))
        auxillary_list, destination_list = [], []

        if total_disks % 2 == 0:
            auxillary, destination = destination, auxillary

        
        for move in range(1, total_moves+1):
            if move % 3 == 1:
                self.__move_disk(source_list, destination_list, source, destination)
            elif move % 3 == 2:
                self.__move_disk(source_list, auxillary_list, source, auxillary)
            else:
                self.__move_disk(auxillary_list, destination_list, auxillary, destination)

    def __call__(self) -> None:
        self.total_disks = int(input("Enter total number of disks\n"))
        approach = int(input("Enter the appoach for TOH\n 1. Recursively\n 2. Iteratively\n\n"))
        print("\n")
        import time
        if approach % 2 == 0:
            self.__iteratively_move_disks(self.total_disks, "A", "B", "C")
        else:
            self.__recursively_move_disks(self.total_disks, "A", "B", "C")
        

obj = TowerOfHanoi()
obj()