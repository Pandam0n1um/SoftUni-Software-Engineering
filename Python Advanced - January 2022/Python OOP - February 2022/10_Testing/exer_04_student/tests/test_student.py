from unittest import TestCase, main

from project.student import Student


class StudentsTest(TestCase):

    def setUp(self) -> None:
        new_student_courses = {
            'LightsaberFight': ['En guard!', ['Saber throw'], ],
            'ForceUse': ['Force Push', 'Force Pull', ]
        }
        self.new_student = Student('Luke', new_student_courses)

    def test_init_with_courses(self):
        expected_courses = {
            'LightsaberFight': ['En guard!', ['Saber throw'], ],
            'ForceUse': ['Force Push', 'Force Pull', ]
        }
        self.assertEqual('Luke', self.new_student.name)
        self.assertEqual(expected_courses, self.new_student.courses)

    # rather pointless
    def test_init_without_courses(self):
        student_without_courses = Student('Kylo')
        self.assertEqual('Kylo', student_without_courses.name)
        self.assertEqual({}, student_without_courses.courses)

    def test_enroll_existing_course_update_notes(self):
        result = self.new_student.enroll('ForceUse', ['Jedi Mind Tricks'])
        expected_list_notes = ['Force Push', 'Force Pull', 'Jedi Mind Tricks']
        self.assertEqual(expected_list_notes, self.new_student.courses['ForceUse'])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_new_course_with_notes_y_string(self):
        course = 'Mathematics for Jedi'
        notes = ['Calculus 1', 'Calculus 2']
        result = self.new_student.enroll(course, notes, 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in self.new_student.courses)
        self.assertEqual(notes, self.new_student.courses[course])

    def test_enroll_new_course_with_notes_empty_string(self):
        course = 'Mathematics for Jedi'
        notes = ['Calculus 1', 'Calculus 2']
        result = self.new_student.enroll(course, notes, '')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in self.new_student.courses)
        self.assertEqual(notes, self.new_student.courses[course])

    def test_enroll_new_course_without_notes(self):
        course = 'Mathematics for Jedi'
        notes = ['Calculus 1', 'Calculus 2']
        result = self.new_student.enroll(course, notes, 'N')
        self.assertEqual("Course has been added.", result)
        self.assertTrue(course in self.new_student.courses)
        self.assertEqual([], self.new_student.courses[course])

    def test_add_notes_to_existing_course_raises(self):
        course = 'ForceUse'
        notes = 'Jedi Mind Tricks'
        result = self.new_student.add_notes(course, notes)
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['Force Push', 'Force Pull', 'Jedi Mind Tricks'], self.new_student.courses[course])

    def test_add_notes_to_existing_course(self):
        course = 'Mathematics for Jedi'
        notes = ['Calculus 1', 'Calculus 2']
        with self.assertRaises(Exception) as ex:
            self.new_student.add_notes(course, notes)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        course = 'ForceUse'
        result = self.new_student.leave_course(course)
        self.assertEqual("Course has been removed", result)
        self.assertTrue(course not in self.new_student.courses)

    def test_leave_not_existing_course(self):
        course='Many consider to be unnatural'
        with self.assertRaises(Exception) as ex:
            self.new_student.leave_course(course)
        self.assertEqual('Cannot remove course. Course not found.',str(ex.exception))

if __name__ == '__main__':
    main()
