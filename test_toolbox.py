import my_toolbox as mtb


def my_test():      
    print("my tool")
    mtb.clear_screen(30)
    data = mtb.get_data_list()
    print(data)
    xbar = mtb.mean(data)
    print(f"{xbar:0.2f}")
    med = mtb.median(data)
    print(f"{med:0.2f}")
    mtb.writecsv(data)
    mtb.plot(data)
      
def main():
    my_test()
    
if __name__ == '__main__' :
    main()
    
