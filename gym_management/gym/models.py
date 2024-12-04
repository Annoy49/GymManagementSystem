from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    membership_start_date = models.DateField()
    membership_end_date = models.DateField()
    membership_type = models.CharField(max_length=50, choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')])
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Class(models.Model):
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    schedule_time = models.DateTimeField()
    max_members = models.IntegerField()
    
    def __str__(self):
        return self.name
