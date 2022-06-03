class Equipment:
    ID = 1

    def __init__(self, name):
        self.id = Equipment.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id():
        res = Equipment.ID
        Equipment.ID += 1
        return res

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
