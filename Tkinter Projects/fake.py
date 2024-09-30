# importing the required libraries  
from faker import Faker  
import pandas as pd  
  
# defining the variable for Faker() module  
sample = Faker()  
  
# generating the profiles of 20 people  
mydata = [sample.profile() for n in range(20)]  
my_dframe = pd.DataFrame(mydata)  
  
print(my_dframe)  