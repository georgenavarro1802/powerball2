from __future__ import unicode_literals

from django.db import models


class Player(models.Model):
    """ A virtual person playing lottery numbers """
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    n1 = models.IntegerField(default=1)
    n2 = models.IntegerField(default=1)
    n3 = models.IntegerField(default=1)
    n4 = models.IntegerField(default=1)
    n5 = models.IntegerField(default=1)
    powb = models.IntegerField(default=1)

    def __str__(self):
        return "{0} {1}".format(self.firstname, self.lastname)

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"
        ordering = ('firstname', 'lastname')

    def representation(self):
        return "\n{0} {1} {2} {3} {4} {5} {6} PowerBall: {7}".format(self.firstname,
                                                                     self.lastname,
                                                                     self.n1, self.n2, self.n3, self.n4, self.n5,
                                                                     self.powb)
