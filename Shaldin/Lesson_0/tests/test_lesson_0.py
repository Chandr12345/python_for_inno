from Shaldin.Lesson_0.lesson_0 import return_value


def test_lesson_0():
    hello = return_value()
    assert hello == 'Hello', 'Function return_value returned not Hello'
