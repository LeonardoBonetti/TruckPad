class Driver:
    def __init__(self, id, name, last_name, date_of_birth, gender_id, cnh_type_id):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender_id = gender_id
        self.cnh_type_id = cnh_type_id

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'gender_id': self.gender_id,
            'cnh_type_id': self.cnh_type_id,
        }