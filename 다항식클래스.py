class Polynomial :
    def __init__( self ):
        self.polynomial_list = []
        
    def degree(self) :
        return len(self.polynomial_list) - 1
    def display(self, msg="f(x) = "):
        show_poly =""
        sign = "x^"
        plus = "+ "
        for i in range(len(self.polynomial_list)-1, -1, -1):
            degree_num = str(i)
            #sign = ""
            #plus = ""
            if i == 0:
                sign = ""
                degree_num = ""
                plus = ""
            show_poly += str(self.polynomial_list[i]) + ".0 " + sign + degree_num + " " + plus
        print(msg + show_poly)
    def add(self, b):
        p = Polynomial()
        if self.degree() > b.degree():
            for i in range(len(b.polynomial_list)):
                p.polynomial_list.append(self.polynomial_list[i] + b.polynomial_list[i])
            for j in range(len(b.polynomial_list), len(self.polynomial_list)):
                p.polynomial_list.append(self.polynomial_list[j]) 
        else :
            for i in range(len(self.polynomial_list)):
                p.polynomial_list.append(self.polynomial_list[i] + b.polynomial_list[i])
            for j in range(len(self.polynomial_list), len(b.polynomial_list)):
                p.polynomial_list.append(b.polynomial_list[j])
        return p
    
    def eval(self, x):
        sum = 0
        for i in range(1, len(self.polynomial_list)):
            sum += x * self.polynomial_list[i]
            x = x * 2
        return "{:.1f}".format(sum + self.polynomial_list[0])
    def read(self): # split / reverse 메소드 함수 활용
        coef = list(map(int, input("최고차항부터 차수를 순서대로 입력하시오: ").split()))
        coef.reverse()
        for i in range(len(coef)):
            self.polynomial_list.append(coef[i])
        
a = Polynomial()
b = Polynomial()
a.read()
b.read()
c = a.add(b)
a.display("A(x) = ")
b.display("B(x) = ")
c.display("A+B = ")
print(" B(2) = ", b.eval(2))
print(" C(2) = ", c.eval(2))