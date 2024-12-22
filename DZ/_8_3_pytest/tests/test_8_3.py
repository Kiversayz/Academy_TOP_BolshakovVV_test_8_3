import pytest

from DZ._8_3_pytest.dz_8_2_1 import DisciplineTeacher

@pytest.fixture
def teacher():
    # Инициализация объекта класса Teacher с нужными параметрами
    teacher_instance = DisciplineTeacher('Стариков Ванадий', 'БГПУ','70','Программирование', 'Студент')
    yield teacher_instance
    teacher_instance.remove_teachers()

def test_get_name(teacher):
    assert teacher.get_name() == "Стариков Ванадий"

def test_get_education(teacher):
    assert teacher.get_education() == "БГПУ"

def test_get_experience(teacher):
    assert teacher.get_experience() == '70'

def test_set_experience(teacher):
    new_experience = teacher.set_experience('12')
    assert new_experience == '12'

def test_get_teacher_data(teacher):
    assert teacher.get_teacher_data() == "Стариков Ванадий, образование БГПУ, опыт работы 70 лет.\nПредмет Программирование, должность Студент"

def test_add_mark(teacher):
    result = teacher.add_mark("Иванов Иван", 5)
    assert result == "Стариков Ванадий поставил оценку 5 студенту Иванов Иван.\nПредмет Программирование"

def test_remove_mark(teacher):
    result = teacher.remove_mark("Иванов Иван", 5)
    assert result == "Стариков Ванадий удалил оценку 5 студенту Иванов Иван.\nПредмет Программирование"

def test_give_a_consultation(teacher):
    result = teacher.give_a_consultation("10-А")
    assert result == "Стариков Ванадий Провел консультацию в классе 10-А.\nПо предмету Программирование как Студент"

def test_get_discipline(teacher):
    assert teacher.get_discipline() == "Программирование"

def test_get_job_title(teacher):
    assert teacher.get_job_title() == "Студент"

def test_set_job_title(teacher):
    result = teacher.set_job_title('Преподователь')
    assert result == "Преподователь"

def test_append_teachers(teacher):
    assert teacher.append_teachers('Большаков Валерий')[1] == "Большаков Валерий"

def test_get_teachers(teacher):
    assert teacher.get_teachers() == ['Стариков Ванадий']

def test_remove_teachers(teacher):
    result = teacher.remove_teachers()
    assert result == []
