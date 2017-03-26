my_list = list(range(10))
##print(my_list)
##print(type(my_list))
##print(type(my_list[0]))
##
##
##my_list = [str(l) for l in my_list]
##print(type(my_list))
##print(type(my_list[0]))

##my_list = [True, "2", 3.0, 4]
##for l in my_list:
##    print(type(l))


##import array
##my_array = array.array('i', my_list)
##print(my_array)

import numpy as np
##print(np.array([1,4,2,5,3]))
my_array = np.array([1,2,3,4], dtype = 'float32')
print(type(my_array))

