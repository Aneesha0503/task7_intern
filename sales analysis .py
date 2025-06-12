#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3               
import pandas as pd           
import matplotlib.pyplot as plt  

conn = sqlite3.connect('sales_data.db')  
cursor = conn.cursor()                  


# In[2]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,    -- Unique ID for each sale
    product TEXT,              -- Product name
    quantity INTEGER,          -- Quantity sold
    price REAL                 -- Price per unit
)
''')


# In[3]:


sample_data = [
    ('Laptop', 6, 500.00),
    ('Smartphone', 10, 300.00),
    ('Tablet', 7, 950.00),
    ('Laptop', 5, 700.00),
    ('Smartphone', 6, 500.00),
    ('Tablet', 3, 200.00)
]
cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)
conn.commit()


# In[4]:


query = '''
SELECT product,
       SUM(quantity) AS total_qty,                      
       SUM(quantity * price) AS revenue                 
FROM sales
GROUP BY product                                        
'''


# In[5]:


df = pd.read_sql_query(query, conn)


# In[6]:


print("Sales Summary :\n")  # Display title
print(df)     


# In[7]:


plt.figure(figsize=(8,5))                                
df.plot(kind='bar', x='product', y='revenue',            # Bar chart: x = product, y = revenue
        legend=False, color='skyblue')                   
plt.title('Total Revenue by Product')                    
plt.xlabel('Product')                                    
plt.ylabel('Revenue')                                    
plt.grid(axis='y', linestyle='--', alpha=0.7)            
plt.tight_layout()                                       
plt.savefig("sales_chart.png")                           


# In[8]:


conn.close()


# In[ ]:




