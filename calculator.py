class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0

        if a == 0 or b == 0:  
            return 0
    
        # ใช้ XOR หากพบว่าตัวใดตัวหนึ่งติดลบจะต้องได้คำตอบที่ติดลบ
        ShouldItBeNegative = (a < 0) ^ (b < 0) 

        a = -a if a < 0 else a
        b = -b if b < 0 else b

        for i in range(b):
            result = self.add(result, a)

        return -result if ShouldItBeNegative else result

    def divide(self, a, b):
        result = 0

        if b == 0:  
            return None

        # ใช้ XOR หากพบว่าตัวใดตัวหนึ่งติดลบจะต้องได้คำตอบที่ติดลบ
        ShouldItBeNegative = (a < 0) ^ (b < 0)

        a = -a if a < 0 else a
        b = -b if b < 0 else b

        while a >= b:
            a = self.subtract(a, b)
            result += 1

        return -result if ShouldItBeNegative else result

    def modulo(self, a, b):
        """
            แบ่งเป็น 4 กรณี
                1. - mod - 
                2. + mod +
                3. + mod - 
                4. - mod + 
            จากที่ทำการทดลองพบว่ากรณี (- mod +) = -(+ mod -)
        """
        og_b = b

        if (a<0 and b<0) :   # กรณีแรก: ทั้งคู่มีค่าติดลบ
            result = a - self.multiply(self.divide(a,b),b)
            return result
        
        # กรณี (+ mod -)
        if b < 0 and a > 0:  # กลับให้เป็นกรณี (- mod +) 
            a = -a
            b = -b
        
        # ที่เหลือทั้งสามกรณีใช้วิธีเดียวกัน
        if b == 0: # ดักกรณี b เป็น 0
            return None
        
        b = -b if b < 0 else b

        # คำนวณผลเศษ
        dividedResult = self.divide(a, b)
        remainder = a - self.multiply(dividedResult, b)
        
        # หากเศษติดลบให้บวกด้วยค่า b
        if remainder < 0:
            remainder += b
        
        # กรณี 3. (+ mod -) จะได้คำตอบติดลบเสมอ
        if og_b < 0:
            return -remainder
        
        return remainder

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))          # Output: 3
    print("Example: subtraction: ", calc.subtract(4, 2))  # Output: 2
    print("Example: multiplication: ", calc.multiply(-2, 3))  # Output: -6
    print("Example: division: ", calc.divide(-10, 2))     # Output: -5
    print("Example: modulo: ", calc.modulo(-10, 3))       # Output: -1
