import matplotlib.pyplot as plt 
import seaborn as sns 
from io import BytesIO
import base64
from .models import Product
from django.contrib.auth.models import User


def get_sales_from_id(value):
        salesman = User.objects.get(id = value)
        return salesman


def get_image():
          #create  a bite buffer for the image to save 
          buffer = BytesIO() # byte object
          # create the plot with the use of 
          # Bytes object as its 'file'
          plt.savefig(buffer,format='png')
          buffer.seek(0)
          # retreive the entire content of the 'file'
          image_png = buffer.getvalue()
          graph = base64.b64encode(image_png)
          graph = graph.decode('utf-8')
          #free the memory
          buffer.close()
          return graph
        

def get_simple_plot(chart_type, *args, **kwargs):
          plt.switch_backend('AGG')
          fig = plt.figure(figsize= (10,4))

          x = kwargs.get('x')
          y = kwargs.get('y')
          data = kwargs.get('data')

          df = kwargs.get('df')

          if chart_type == 'bar plot':
                    title = 'total price by day (bar)'
                    plt.title(title)
                    plt.bar(x,y)
          elif chart_type == 'line plot':
                    title = 'total price by day (line)'
                    plt.title(title)
                    plt.plot(x,y)
          else:
                    title = 'Product count'
                    plt.title(title)
                    sns.countplot(x = data['name'])
          plt.xticks(rotation=45)
          plt.tight_layout()

          grapth = get_image()
          return grapth





