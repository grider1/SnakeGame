import pygame


class Node:

    def __init__(self, size, x, y):
        self.type = "empty"
        self.size = size
        self.x = x
        self.y = y

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def get_size(self):
        return self.size
