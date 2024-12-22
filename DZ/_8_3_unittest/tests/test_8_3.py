import unittest

from DZ._8_3_unittest.dz_8_2_1 import Teacher,DisciplineTeacher

class TestTeacher(unittest.TestCase):
    
    def test_Teacher(self):
        teacher = Teacher('Большаков Валерий', 'БГПУ','5')
        self.assertEqual(teacher.get_name(),'Большаков Валерий')
        self.assertEqual(teacher.get_education(),'БГПУ')
        self.assertEqual(teacher.get_experience(),'5')
        self.assertEqual(teacher.set_experience('6')[0],'6')
        self.assertEqual(teacher.get_teachers()[0],'Большаков Валерий')
        self.assertEqual(teacher.remove_teachers(),[])
    
    def test_teacher_list(self):
        teacher = Teacher('Большаков Валерий', 'БГПУ','5')
        self.assertEqual(teacher.get_teachers()[0],'Большаков Валерий')
        self.assertEqual(teacher.append_teachers('Большаков Валерий2')[1],'Большаков Валерий2')
        self.assertEqual(teacher.remove_teachers(),[])
    
    def test_teacher_methols(self):
        teacher = Teacher('Большаков Валерий', 'БГПУ','5')
        self.assertEqual(teacher.get_teacher_data(),'Большаков Валерий, образование БГПУ, опыт работы 5 лет.')
        self.assertEqual(teacher.add_mark('студент','5'),'Большаков Валерий поставил оценку 5 студенту студент.')
        self.assertEqual(teacher.remove_mark('студент','5'),'Большаков Валерий удалил оценку 5 студенту студент.')
        self.assertEqual(teacher.give_a_consultation('Биологии'),'Большаков Валерий Провел консультацию в классе Биологии.')
        self.assertEqual(teacher.remove_teachers(),[])

class TestDisciplineTeacher(unittest.TestCase):
    
    def test_DisciplineTeacher(self):
        teacher = DisciplineTeacher('Стариков Ванадий', 'БГПУ','70','Программирование', 'Студент')
        self.assertEqual(teacher.get_name(),'Стариков Ванадий')
        self.assertEqual(teacher.get_education(),'БГПУ')
        self.assertEqual(teacher.get_experience(),'70')
        self.assertEqual(teacher.set_experience('12'),'12')
        self.assertEqual(teacher.get_teachers()[0],'Стариков Ванадий')
        self.assertEqual(teacher.set_job_title('Инопланетянин'),'Инопланетянин')
        self.assertEqual(teacher.remove_teachers(),[])
    
    def test_teacher_list(self):
        teacher = DisciplineTeacher('Стариков Ванадий', 'БГПУ','70','Программирование', 'Студент')
        self.assertEqual(teacher.get_teachers()[0],'Стариков Ванадий')
        self.assertEqual(teacher.append_teachers('Большаков Валерий')[1],'Большаков Валерий')
        self.assertEqual(teacher.remove_teachers(),[])
    
    def test_teacher_methols(self):
        teacher = DisciplineTeacher('Стариков Ванадий', 'БГПУ','70','Программирование', 'Студент')
        self.assertEqual(teacher.get_teacher_data(),"Стариков Ванадий, образование БГПУ, опыт работы 70 лет.\nПредмет Программирование, должность Студент")
        self.assertEqual(teacher.add_mark('студент','5'),'Стариков Ванадий поставил оценку 5 студенту студент.\nПредмет Программирование')
        self.assertEqual(teacher.remove_mark('студент','5'),'Стариков Ванадий удалил оценку 5 студенту студент.\nПредмет Программирование')
        self.assertEqual(teacher.give_a_consultation('Биологии'),'Стариков Ванадий Провел консультацию в классе Биологии.\nПо предмету Программирование как Студент')
        self.assertEqual(teacher.remove_teachers(),[])
