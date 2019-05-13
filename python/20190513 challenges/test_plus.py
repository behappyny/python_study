#파이썬의 모듈은 import 해서 사용하는 프로그램을 말함

import unittest

# 테스트 대상 plus 함수

def plus(a, b):
    return a + b

class PlusTest(unittest.TestCase): #테스트 프로그램 작성시 규칙 1 : Unittest 모듈의 TestCase를 상속할 것

#테스트 프로그램
    def test_plus(self): #규칙 2 : 테스트하는 함수는 test_로 시작하는 
        self.assertEqual(10, plus(2, 8))

if __name__ == "__main__" : 
    unittest.main()