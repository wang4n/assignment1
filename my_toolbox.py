import datetime
import matplotlib.pyplot as plt

def clear_screen(x):
    print("\n" * x)
    print('screen cleared')
      
def mean(data_list):
    sum = 0.0
    for num in data_list.values():
        sum = sum + num[0]
    return sum / len(data_list)

def median(data_list):
    sort_data_list = sorted(data_list.items(), key=lambda x: x[1])
    size = len(sort_data_list)
    midPos = size // 2  #integer division
 
    if size % 2 == 0:   # evern elements
        median = (sort_data_list[midPos][1][0] + sort_data_list[midPos-1][1][0])/2
    else:
        median = sort_data_list[midPos][1][0]
    return median

def up_down(data_list):
    if len(data_list) == 1:
        return 0
    else:
        return round((list(data_list.values())[-1])[0] - (list(data_list.values())[-2])[0], 2)

def gain_loss(data_list):
    if len(data_list) == 1:
        return 0
    else:
        return round(((list(data_list.values())[-1])[0] - (list(data_list.values())[-2])[0])/(list(data_list.values())[-2])[0]*100, 2)


def get_data_list():
    fname = input("Enter filename(include .filetype) for input: ")
    dict = {}
    if fname.endswith('.csv'):
        with open(fname, 'r') as file:
            dict2 = {}
            for line in file.read().splitlines()[1:]:
                date, *_, close = line.split(',')
                key = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%y%m%d')
                dict2[key] = close
            sorted_dict = sorted(dict2.items(), key=lambda x: x[0])
            with open('temp', 'w') as f2:
                f2.write("Date,Close\n")
                for item in sorted_dict:
                    f2.write(item[0] + ',' + item[1] + '\n')
        fname = "temp"
                    
    with open(fname, 'r') as f:
        for line in f.read().splitlines()[1:1000]:
            date, *_, close = line.split(',')
            key = datetime.datetime.strptime(date, '%y%m%d').strftime('%Y/%m/%d')
            dict[key] = [float(close), float(close), float(close), 0, 0]
            means = round(mean(dict), 2)
            medians = round(median(dict), 2)
            up_downs = up_down(dict)
            gain_losses = gain_loss(dict)
            dict[key] = [float(close), means, medians, up_downs, gain_losses]
    return dict

def writecsv(data_list):
    fname = input("Enter filename(include .csv) for output csv: ")
    with open(fname, 'w') as f:
        f.write("Date,Close,Mean,Median,Up/Down,Gain%/Loss%\n")
        for item in data_list.items():
            converted_list = [str("%.2f" % element) for element in item[1]]
            vals = ",".join(converted_list)
            f.write(item[0] + ',' + vals + '%' + '\n')
       
def plot(data):
    keys = list(data.keys())
    values = list(data.values())
    (keys,values) = zip(*data.items())
    p = plt.plot(keys,values)
    plt.legend(p, ('Close', 'Mean', 'Median', 'Up/Close', 'Gain%/Loss%'))
    plt.title('Stock data')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.show()
    

def main():
    print('This is my_tools module called')
    data = get_data_list()
    print(data)
    writecsv(data)

if __name__ == '__main__' :
    main()
    