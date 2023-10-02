from django.db import models


class Category(models.Model):
    '''
        Model for advert category

        Attributes:
            name (str): Name of category
    '''

    name = models.CharField(max_length=255)

    def __str__(self):
        '''Render a string representation of a Category instance'''
        return self.name
    

class City(models.Model):
    '''
        Model for advert city

        Attributes:
            name (str): Name of city
    '''

    name = models.CharField(max_length=255) 

    def __str__(self):
        '''Render a string representation of a City instance'''
        return self.name
    

class Advert(models.Model):
    '''
        Model for Advert

        Attributes:
            created (datetime): The date and time the advert was created.
            title (str): The title of the advert (limited to 255 characters).
            description (str): The description of the advert.
            city (City): The city associated with the advert (foreign key).
            category (Category): The category associated with the advert (foreign key).
            views (int): A count of the views of the advert (defaults to 0).
    '''
    
    created = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=255)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        '''Render a string representation of a Advert instance'''
        return self.title
