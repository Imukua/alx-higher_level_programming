#!/usr/bin/python3
"""Defines a Base class"""
import json
import turtle
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json convert of a list of dictionaries
           Args:
                :: List-dictionaries(list): list of dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dicts from a json string
           Args:
                :: json_string(json): json to be converted
        """

        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects into a file
           args:
                :: list_objs(list): list of class instances
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                listdicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(listdicts))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set
           Args:
                :: dictionary(dict): key value pair of arguments
           Returns: instance with all attributtes set
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file and return a list of instances."""

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                json_string = jsonfile.read()
                list_dicts = Base.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances to CSV format and save to file.
           Args:
                :: list_objs: list of instances"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow(obj.to_csv_row())
    import turtle

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle graphics module."""
        window = turtle.Screen()
        window.bgcolor("white")
        pen = turtle.Turtle()
        pen.speed(2)

        def draw_shape(shape, color):
            pen.color(color)
            pen.begin_fill()
            for _ in range(4):
                pen.forward(shape.width)
                pen.right(90)
            pen.end_fill()

        for rectangle in list_rectangles:
            draw_shape(rectangle, "red")

        for square in list_squares:
            draw_shape(square, "blue")

        turtle.done()