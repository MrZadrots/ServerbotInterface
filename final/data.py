class DATA():
    part = -1
    def set_part(self, p):
        self.part = p

    def get_part(self):
        return self.part

class ROUTE():
    route = []
    def add_route(self, p):
        self.route.append(p)

    def remove_route(self):
        self.route.remove(len(self.route) - 1)
