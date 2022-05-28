class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def change_name(self):
        pass

    def change_age(self):
        pass

    



    


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
