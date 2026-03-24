from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

class FileUpload(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'File Upload'
        verbose_name_plural = 'File Uploads'

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

class Article(models.Model):
    subject = models.ForeignKey(Subject, related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Competition(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Competition'
        verbose_name_plural = 'Competitions'

class Activity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    competition = models.ForeignKey(Competition, related_name='activities', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

class ActivityParticipant(models.Model):
    activity = models.ForeignKey(Activity, related_name='participants', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, related_name='activities', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Activity Participant'
        verbose_name_plural = 'Activity Participants'