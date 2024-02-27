

def read_data(path):
    try:
        with open(path,'r',encoding='utf8')as f:
  #          print("데이터")
  #          print(f.read().split("\n"))
            i = f.read().split("\n")
    except FileNotFoundError:
        print("파일을 읽을 수 없음")
    return i 

def write_data(data,path):
    try:
        with open(path,'w')as f:
            f.write(data)
    except FileNotFoundError:
        print("파일을 읽을 수 없음")

def add_data(data1,data2):
    for i in range(len(data1)):
        data3= {data1[i]:data2[i]}
    return data3
