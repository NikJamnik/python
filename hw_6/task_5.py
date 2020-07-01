class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        super().draw()
        print("Pen style")


class Pencil(Stationery):

    def draw(self):
        super().draw()
        print("Pencil style")


class Handle(Stationery):

    def draw(self):
        super().draw()
        print("Handle style")


pen = Pen("pen")
pen.draw()

pencil = Pencil("pencil")
pencil.draw()

handle = Handle("handle")
handle.draw()
