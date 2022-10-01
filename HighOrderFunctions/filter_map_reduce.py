from functools import reduce

def run():
    my_list = [1,2,3,4,5,6]
    
    odd = list(filter(lambda i: i%2 !=0,my_list))
    
    squares = list(map(lambda i: i**2,my_list))
    
    second_list = [2,2,2,2,2]
    all_multiplied = reduce(lambda a,b:a*b,second_list)
    print(all_multiplied)
    
if __name__ == '__main__':
    run()