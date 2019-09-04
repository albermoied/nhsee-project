from django.db import models


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=255, null=False)
    avg_score = models.DecimalField(max_digits=10, null=False, decimal_places=6)
    rank = models.DecimalField(max_digits=10, null=False, decimal_places=6)
    z_score = models.DecimalField(max_digits=10, null=False, decimal_places=6)
    scaled_score = models.DecimalField(max_digits=10, null=False, decimal_places=6)
    scaled_rank = models.DecimalField(max_digits=10, null=False, decimal_places=6)
    scaled_z = models.DecimalField(max_digits=10, null=False, decimal_places=6)
    isef_score = models.DecimalField(max_digits=10, null=False, decimal_places=6)
    isef_rank = models.DecimalField(max_digits=10, null=False, decimal_places=6)
    no_show = models.BooleanField(null=False)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.title,
        self.description, self.category, self.no_show)
