def retorna3():
  return 3

def test_retorna31():
  assert retorna3() == 3

#v4 calling a object $python ex_fire.py add 10 10
import fire
class Calculator(object):

  def add(self, x, y):
    return x + y

  def multiply(self, x, y):
    return x * y

if __name__ == '__main__':
  calculator = Calculator()
  fire.Fire(calculator)
