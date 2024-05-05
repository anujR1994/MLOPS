import pandas as pd
import numpy as np
Unstructured = 'Student A scored 12 marks in Maths , 2 in Science, 3 in English...\
In Maths stu B scored 2 marks'
semi_structured = {'Student A':[12,2,3,4,5],'Student B':[2,3,6]}
structured_data = pd.DataFrame({'StudentA':[1,2,3,4,5],'StudentB':[2,3,6,np.nan,np.nan]})
print('End of code')