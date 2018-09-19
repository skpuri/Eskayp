from django.db import models

class Category(models.Model):
    Name = models.CharField(max_length=140)
    HasSubcategory = models.BooleanField(default=False)
    def __str__(self):
        return self.Name

class Subcategory(models.Model):
    Name = models.CharField(max_length=140)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    def __str__(self):
        return self.Name

class SearchResult(models.Model):
    id = models.AutoField(primary_key=True, db_index=True) #referenced in more than one place - index it
    Name = models.CharField(max_length=140)
	#TODO: make this ManyToManyField(Subcategory)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT) #Foreign Key -> Category table
    ConsolidatedRating = models.SmallIntegerField(blank=True) #Maybe not necessary - prevents recalculation every time
    Description = models.TextField(blank=True) #date invented, person/organization, check wiki info
    Tutorials = models.TextField(blank=True)
    IsBest = models.BooleanField(default=False)
    #NumberOfRatings = models.IntegerField() #write function to autoincrement this number when appropriate UserRating row is inserted
	#UpdatedDate = models.DateTimeField(blank=True)
    def __str__(self):
        return self.Name

class UserRatings(models.Model):
    UserID = models.AutoField(primary_key=True, db_index=True) #this table will be large - index it
    searchresult = models.ForeignKey(SearchResult, on_delete=models.PROTECT)
    IPAddress = models.GenericIPAddressField(unique=True) #this is probably redundent with UserID - i can user IPAddress as PK?
    Rating = models.SmallIntegerField()
	#CreatedDate = models.DateTimeField(default=datetime.now, blank=True)