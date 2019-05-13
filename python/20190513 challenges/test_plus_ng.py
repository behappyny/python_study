import unittest

# 테스트 대상 plus 함수
def plus(a,b) : 
    return a + b 

class Plustest(unittest.TestCase) : 

    #테스트 프로그램
    def test_plus(self):
        self.assertEqual(10,plus(2,8))
        self.assertEqual(20,plus(2,8))

if __name__ == "__main__" :
    unittest.main()




#TestCase 클래스의 함수 // assert(검사)

#1. assertEqual(a,b) : a 와 b가 같은가
#2. asserNotEqual(a,b) : a와 b가 다른가
#3. assertTrue(x) : x가 True인가
#4. assertIs(a,b) : a와 b의 객체인가
#5. assertIn(a,b) : b 안에 a가 있는가 