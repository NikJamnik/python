from abc import ABC, abstractmethod


class MyNegativeValueError(Exception):
    """My class for negative values exceptions"""

    def __init__(self, text):
        self.text = text


class MyTechniqueTypeException(Exception):
    """My class for wrong type of technique"""

    def __init__(self, text):
        self.text = text


class TechnicalStore:
    """Class of the store with technique"""
    _current_technique = {}

    def __str__(self):
        string = ""
        for department, department_store in self._current_technique.items():
            string += f"{department}\n"
            for technique, count in department_store.items():
                string += f"\t{technique}: {count}\n"
        return string

    # method for adding technique to the store
    def accept_technique(self, department, technique, count):
        if department in self._current_technique:
            if technique in self._current_technique[department]:
                self._current_technique[department][technique] += count
            else:
                self._current_technique[department][technique] = count
        else:
            self._current_technique[department] = {}
            self._current_technique[department][technique] = count


class Technique(ABC):
    """Base class for technique"""
    _type = ""
    _model = ""

    def __init__(self, model):
        self._model = model

    def __str__(self):
        return f"{self._type} {self._model}"

    # I need to define methods __eq__ and __hash__ for the dictionary in the store class to understand different stuff
    @abstractmethod
    def __eq__(self, other):
        return self._type == other._type and self._model == other._model

    # I need to define methods __eq__ and __hash__ for the dictionary in the store class to understand different stuff
    @abstractmethod
    def __hash__(self):
        return (hash(self._type) * hash(self._model) - hash(self._model) + hash(self._type)) % 17

    # some method of base class
    def turn_on(self):
        print(f"{self._type} {self._model} is on!")

    # some method of base class
    def turn_off(self):
        print(f"{self._type} {self._model} is off!")

    # some method of base class, which his children have to define
    @abstractmethod
    def working(self, **kwargs):
        pass


class Printer(Technique):
    """Class for Printer"""
    _is_in_color = False
    _type = "Printer"

    def __init__(self, model, is_in_color):
        super().__init__(model)
        self._is_in_color = is_in_color

    def __str__(self):
        return super().__str__() + ' ' + f"{'with color' if self._is_in_color else 'without color'}"

    def __eq__(self, other):
        return self._type == other._type and self._model == other._model and self._is_in_color == other._is_in_color

    def __hash__(self):
        return (hash(self._type) * hash(self._model) + hash(self._is_in_color) -
                hash(self._model) + hash(self._is_in_color) * hash(self._type)) % 37

    def working(self, pages):
        self.turn_on()
        print(f"Printing {pages} pages!")
        self.turn_off()


class Scanner(Technique):
    """Class for Scanner"""
    _work_area_size = 0
    _type = "Scanner"

    def __init__(self, model, work_area_size):
        super().__init__(model)
        self._work_area_size = work_area_size

    def __str__(self):
        return super().__str__() + ' ' + f"work area size {self._work_area_size}"

    def __eq__(self, other):
        return self._type == other._type and self._model == other._model and self._work_area_size == other._work_area_size

    def __hash__(self):
        return (hash(self._type) * hash(self._model) + hash(self._work_area_size) -
                hash(self._model) + hash(self._work_area_size) * hash(self._type)) % 47

    def working(self, lists):
        self.turn_on()
        print(f"Scanning {lists} lists!")
        self.turn_off()


class Xerox(Technique):
    """Class for Xerox"""
    _is_image_available = False
    _type = "Xerox"

    def __init__(self, model, is_image_available):
        super().__init__(model)
        self._is_image_available = is_image_available

    def __str__(self):
        return super().__str__() + ' ' + f"{'image on' if self._is_image_available else 'image off'}"

    def __eq__(self, other):
        return self._type == other._type and self._model == other._model and self._is_image_available == other._is_image_available

    def __hash__(self):
        return (hash(self._type) * hash(self._model) + hash(self._is_image_available) -
                hash(self._model) + hash(self._is_image_available) * hash(self._type)) % 91

    def working(self, info):
        self.turn_on()
        print(f"Sending {info}!")
        self.turn_off()


store = TechnicalStore()
technique_types = ['Printer', 'Scanner', 'Xerox']

print(f"Technique type must be from {technique_types}")
while True:
    try:
        technique_type, technique_model = input("Input '- -' to terminate or type and model separated by ' ': ").split()
        if technique_type == '-' and technique_model == '-':
            break
        if not (technique_type in technique_types):
            raise MyTechniqueTypeException("Wrong technique type!")
    except ValueError:
        print("There must be 2 values!")
        continue
    except MyTechniqueTypeException:
        print(f"Technique type must be from {technique_types}!")
        continue

    try:
        technique_count = int(input("Input technique count: "))
        if technique_count < 1:
            raise MyNegativeValueError("Count must be positive number >= 1!")
    except ValueError:
        print("Count must be an integer number!")
        continue
    except MyNegativeValueError as e:
        print(e)
        continue

    department = input("Input department of the store: ")

    if technique_type == 'Printer':
        is_in_color = input("Input '+' if printer is in color or '-' in other case: ")
        if is_in_color == '+':
            new_technique = Printer(technique_model, True)
        elif is_in_color == '-':
            new_technique = Printer(technique_model, False)
        else:
            print("Wrong symbol!")
            continue
        store.accept_technique(department, new_technique, technique_count)
    elif technique_type == 'Scanner':
        try:
            work_area = float(input("Input scanner's work area: "))
            if work_area <= 0.0:
                raise MyNegativeValueError("Work area must be positive number >= 1!")
        except ValueError:
            print("Count must be a positive float number!")
            continue
        except MyNegativeValueError as e:
            print(e)
            continue
        new_technique = Scanner(technique_model, work_area)
        store.accept_technique(department, new_technique, technique_count)
    else:
        is_image_available = input("Input '+' if xerox works with images or '-' in other case: ")
        if is_image_available == '+':
            new_technique = Xerox(technique_model, True)
        elif is_image_available == '-':
            new_technique = Xerox(technique_model, False)
        else:
            print("Wrong symbol!")
            continue
        store.accept_technique(department, new_technique, technique_count)
print(store)
