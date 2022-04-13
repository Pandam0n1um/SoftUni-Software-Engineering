class Programmer:
    def __init__(self, name, language, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def change_language(self, new_language, skills_needed):
        if self.skills>=skills_needed and not self.language==new_language:
            self.language,new_language=new_language,self.language
            return f"{self.name} switched from {new_language} to {self.language}"
        elif self.skills>=skills_needed:
            return f"{self.name} already knows {self.language}"
        else:
            return f"{self.name} needs {skills_needed-self.skills} more skills"

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
