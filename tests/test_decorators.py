from src.decorators import log


def test_log_print(capsys):
    """Проверка работы декоратора при выводе лога в консоль
    и отсутствии ошибок в результате работы декорируемой функции"""
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "Function my_function called with args: (1, 2) and kwargs: {}. Result: 3." in captured.out
    assert "was running for" in captured.out


def test_log_print_error(capsys):
    """Проверка работы декоратора при выводе лога в консоль
    и наличии ошибки в результате работы декорируемой функции"""
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, "e")
    captured = capsys.readouterr()
    assert "Function my_function called with args: (1, 'e') and kwargs: {}. Resulted with an Error: " in captured.out
    assert "was running for" in captured.out


def test_log_file():
    """Проверка работы декоратора при выводе лога в заданный файл
    и отсутствии ошибок в результате работы декорируемой функции"""
    @log(filename="log_file_test.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3

    with open("log_file_test.txt", "r") as f:
        content = f.read()

    assert "Function my_function called with args: (1, 2) and kwargs: {}. Result: 3." in content
    assert "was running for" in content


def test_log_file_error():
    """Проверка работы декоратора при выводе лога в заданный файл
    и наличии ошибки в результате работы декорируемой функции"""
    @log(filename="log_file_test.txt")
    def my_function(x, y):
        return x + y

    my_function(1, "e")

    with open("log_file_test.txt", "r") as f:
        content = f.read()

    assert "Function my_function called with args: (1, 'e') and kwargs: {}. Resulted with an Error: " in content
    assert "was running for" in content
