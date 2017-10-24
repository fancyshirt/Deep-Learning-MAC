import csv
import numpy as numpy

def read_csv_file(file_name, row_from, cln_from, feature):
    return_table = {}
    #with open(file_name, newline='') as csvfile:
    with open(file_name, newline='') as csvfile:
        #content = csv.reader(csvfile, delimiter=' ', quotechar='|')
        content = csv.reader(csvfile)

        #for row in content:
        #    print(', '.join(row))

        read_list = list(content)
        read_array = numpy.array(read_list)

        #print(read_array)

        return_table = read_array[cln_from:, row_from:]
        table_keys = read_array[cln_from:, row_from - 1]
        #print(type(return_table))

    return return_table, table_keys
#-

def rearrange_table(resource, types, month, days, hours):

    rearrange_table = numpy.array([0 for x in range(days * hours)])

    for index in range(month):
        # print(str(index) +  " month")

        for i_type in range(types):
            # print("  the " + str(i_type) + "-th type")

            temp_table = []

            for day in range(days):
                # print("    the " + str(day) + "-th day")

                for value in resource[index * month + i_type * types]:
                    temp_table.append(value)

                # print("--")
                # print(temp_table)
            rearrange_table = numpy.vstack((rearrange_table, temp_table))

    return rearrange_table[1:, :]
#-

train_data, train_keys = read_csv_file('train.csv', 3, 1, 18)
test_data, test_keys = read_csv_file('test_X.csv', 2, 0, 18)

## train_data with 18-types for 12-month, 20-days, 24-hours
## train_data[(month * num_month) + (N * num_type)] will be the
##         month-th data with N-th type data stream.
train_data = rearrange_table(train_data, 18, 12, 20, 24)
print("Train data[0]:\nFor 0-th type of data, 20(days)*24(hours) = " + str(len(train_data[0])))
print(train_data[0])
print("Train data: (" + str(len(train_data)) + ") 18(type)*12(month)\n")
print(train_data)

## test_data with 18-types for 12-month, 10-days(20 data/10 days), 9-hours
## test_data[(month * num_month) + (N * num_type)] will be the
##         month-th data with N-th type data stream.
# print("test data[0]:\nFor 0-th type of data, *9(hours) = " + str(len(test_data[0])))
# print(test_data[0])
# print("test data: (" + str(len(test_data)) + ") 18(type)*12(month)*20(testing data)\n")
# print(test_data)

#-
