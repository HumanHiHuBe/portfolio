from django.db import models

# Create your models here.
class Projects(models.Model):
    pTitle = models.CharField(max_length=200, null=True, blank=True)
    pImg = models.ImageField()
    pDesc = models.TextField(null=True, blank=True)
    pUrl = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.pTitle

class ContactInfo(models.Model):
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    githubUrl = models.URLField(null=True, blank=True)
    linkedInUrl = models.URLField(null=True, blank=True)
    hackerrankUrl = models.URLField(null=True, blank=True)
    leetcodeUrl = models.URLField(null=True, blank=True)
    youtubeUrl = models.URLField(null=True, blank=True)
    link1 = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)
    name1 = models.CharField(null=True, blank=True, max_length=100)
    name2 = models.CharField(null=True, blank=True, max_length=100)
    phoneImg = models.FileField(null=True, blank=True, upload_to='contacts')
    emailImg = models.FileField(null=True, blank=True, upload_to='contacts')
    githubUrlImg = models.FileField(null=True, blank=True, upload_to='contacts')
    linkedInUrlImg = models.FileField(null=True, blank=True, upload_to='contacts')
    hackerrankUrlImg = models.FileField(null=True, blank=True, upload_to='contacts')
    leetcodeUrlImg = models.FileField(null=True, blank=True, upload_to='contacts')
    youtubeUrlImg = models.FileField(null=True, blank=True, upload_to='contacts')
    link1Img = models.FileField(null=True, blank=True, upload_to='contacts')
    link2Img = models.FileField(null=True, blank=True, upload_to='contacts')
    name1 = models.CharField(null=True, blank=True, max_length=100)
    name2 = models.CharField(null=True, blank=True, max_length=100)
    def __str__(self):
        return self.linkedInUrl

class Resume(models.Model):
    resume = models.FileField()
    def __str__(self):
        return self.resume.url

class MyPhoto(models.Model):
    selfImage = models.ImageField()
    def __str__(self):
        return self.selfImage.url

class Message(models.Model):
    senderName = models.CharField(max_length=200, blank=False)
    senderEmail = models.EmailField(null=True, blank=True)
    theMessage = models.TextField(blank=False)
    def __str__(self):
        return self.senderName + "'s Message"


class About(models.Model):
    about = models.TextField(default="")
    def __str__(self):
        return self.about[:101]

    


