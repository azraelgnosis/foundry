import sqlite3

class Row(sqlite3.Row):
    def __init__(self, cursor, values):
        self.cursor = cursor
        self.values = values
        self.columns = [col[0] for col in cursor.description]
        self.val = " ".join([val for col, val in zip(self.columns, self.values) if 'val' in col]) # combines values with 'val' in column name.

        for col, val in zip(self.columns, self.values):
            setattr(self, col, val)

    def get(self, attr:str):
        try:
            return getattr(self, attr)
        except AttributeError:
            return None

    def items(self):
        return zip(self.columns, self.values)

    def __getitem__(self, obj:str):
        return None or getattr(self, obj)

    def __repr__(self): return f"{self.val}"

class Model:
    __slots__ = ['id', 'val']
    fks = {}

    def __init__(self):
        self.id = None
        self.val = None

    def init(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @staticmethod
    def _coerce_type(val, separator=","):
        """
        Coerces `val` as a float or int if applicable,
        else returns original value.

        :param val: Value to coerce.
        """

        if isinstance(val, str):
            if len(coll := val.split(separator)) > 1:
                val = [Model._coerce_type(elem.strip()) for elem in coll]

            try:
                if "." in str(val):
                    val = float(val)
                else:
                    val = int(val)
            except TypeError: pass
            except ValueError: pass

        return val

    @classmethod
    def from_row(cls, row):
        new_obj = cls()

        for col in row.columns:
            setattr(new_obj, col, row.get(col))

        return NotImplemented

    def to_list(self) -> list:
        return [getattr(self, val) for val in self.__slots__]

    @classmethod
    def from_dict(cls, dct):
        new_obj = cls()

        for slot in cls.__slots__:
            val = cls._coerce_type(dct.get(slot))
            setattr(new_obj, slot, val)

        new_obj.init()

        return new_obj

    def to_dict(self):
        return {key: getattr(self, key) for key in self.__slots__}

    def __repr__(self):
        name = type(self).__name__.lower()
        return f"{name}: {id} {val}".format(name=name, id=self[name+"_id"], val=self[name+"_val"])

    def __getitem__(self, key):
        try:
            return getattr(self, key)
        except TypeError:
            raise KeyError


class User(Model):
    __slots__ = ['password']

    def __init__(self):
        self.id = None
        self.password = None