def tabular(header, data, spacing):
    col = len(header)
    row = len(data)
    data_count = row*col
    arr = [0 for _ in range(data_count)]
    for i in range(row):
        for j in range(col):
            arr[i*j] = data[i][j]
    print(arr)
    
    header_len = len(max(header))
    print(header_len)
    #data_len = len(max(arr))
    #print(data_len)
    
    
    
my_header = ["distrikter", "populasjon"]
my_data = [["test1", "10"], ["test2", "2"], ["test3", "3"],]

tabular(my_header, my_data, 2)

print(my_data)