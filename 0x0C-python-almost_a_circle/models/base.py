#!/usr/bin/python3
"""base.py
This module contains a class 'Base'
"""

import json
import os
import csv
import turtle
import random


class Base():
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json representation for a list of objects to a file"""
        filename = cls.__name__ + '.json'
        with open(filename, 'w+') as my_file:
            my_list = []
            if list_objs is not None and len(list_objs) > 0:
                for elem in list_objs:
                    my_list.append(elem.to_dictionary())
            my_file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns list from json string"""
        if (json_string is None or len(json_string) == 0):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance using dictionary as attribute"""
        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from file containing a json string"""
        my_list = []
        file_name = cls.__name__ + '.json'
        if os.path.exists(file_name) is True:
            with open(file_name, 'r') as my_file:
                my_list = cls.from_json_string(my_file.read())
            for i in range(len(my_list)):
                my_list[i] = cls.create(**my_list[i])
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes a list of object that inherit from base to a .csv file"""
        file_name = cls.__name__ + '.csv'
        with open(file_name, "w+") as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                else:
                    return
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                for elem in list_objs:
                    writer.writerow(elem.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load list of object from a csv file"""
        my_list = []
        file_name = cls.__name__ + '.csv'
        if os.path.exists(file_name) is True:
            with open(file_name, "r") as csvfile:
                dictreader = csv.DictReader(csvfile)
                my_list = [dict([key, int(value)] for key, value
                                in dictionary.items()) for dictionary
                           in dictreader]
            for i in range(len(my_list)):
                my_list[i] = cls.create(**my_list[i])
        return my_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws list of rectangle and squares using the turtle module"""
        colorlist = ('red', 'blue', 'purple', 'yellow', 'green', 'pink')
        my_turtle = turtle.Turtle()
        my_turtle.up
        my_turtle.penup()
        my_turtle.goto(-200, -200)
        for elem in list_rectangles:
            my_turtle.penup()
            my_turtle.goto(-200 + elem.x * 2 + 20, -200 + elem.y * 2 + 20)
            my_turtle.color(random.choice(colorlist), random.choice(colorlist))
            my_turtle.begin_fill()
            for i in range(2):
                my_turtle.forward(elem.width)
                my_turtle.left(90)
                my_turtle.forward(elem.height)
                my_turtle.left(90)
            my_turtle.end_fill()
        for elem in list_squares:
            my_turtle.penup()
            my_turtle.goto(-200 + elem.x * 2 + 20, -200 + elem.y * 2 + 20)
            my_turtle.color(random.choice(colorlist), random.choice(colorlist))
            my_turtle.begin_fill()
            for i in range(4):
                my_turtle.forward(elem.size)
                my_turtle.left(90)
            my_turtle.end_fill()
        turtle.exitonclick()
