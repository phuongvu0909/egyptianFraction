import math
#nr:tử số, dr: mẫu số
def egyptianFraction(nr, dr):
 
    #Mảng chứa phần tử mẫu số của phân số đơn vị
    ef = []
    while nr != 0:
        #tính mẫu số của phân số đơn vị
        x = math.ceil(dr / nr)
 
        #thêm mẫu số vào mảng
        ef.append(x)
 
        #thay đổi tử số và mẫu số của phân số cần phân tích
        nr = x * nr - dr
        dr = dr * x
 
    #in kết quả
    for i in range(len(ef)):
        if i != len(ef) - 1:
            print(" 1/{0} +".format(ef[i]), end = " ")
        else:
            print(" 1/{0}".format(ef[i]), end = " ")
 
# gọi hàm phân tích
nr = int(input("Nhập tử số:"))
dr = int(input("Nhập mẫu số:"))
print("Phân số " +
          "{0}/{1} trở thành phân số Ai Cập là:".
                format(nr, dr), end="\n")
egyptianFraction(nr, dr)

