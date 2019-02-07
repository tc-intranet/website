from django.db import models

# Create your models here.


class Mentee(models.Model):
    """Model representing a Mentee."""
    first_name = models.CharField(max_length=100, help_text='Anders')
    last_name = models.CharField(max_length=100, help_text='Friis')
    klassetrin = models.CharField(max_length=4, help_text='År hvor deres klasse startede i syvende')

    mentorgruppe = models.ForeignKey('MentorGroup', on_delete=models.SET_NULL, null=True)
    class Meta:
        ordering = ['klassetrin', 'first_name', 'last_name']
    

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.klassetrin}'



class Mentor(models.Model):
    """Model representing a Mentor"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class Meta:
        ordering = ['first_name', 'last_name']
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('mentor-detail', args=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'



class Mentorgroup(models.Model):
    """Model represening a mentor group."""
    name = models.CharField("Group name", max_length=100)
    #last_name = models.CharField(max_length=30)
    mentor = models.ForeignKey('Mentor', on_delete=models.SET_NULL, null=True)
    """class Meta:
        ordering = ['name']"""
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}: {self.mentor}'





