from django.db import models

# # should I add choices to this model instead of typing each property of the model?
class Strategy(models.Model):
    picture_clues = models.BooleanField(default=False)
    stretch_it = models.BooleanField(default=False)
    chunking = models.BooleanField(default=False)
    get_mouth_ready = models.BooleanField(default=False)
    go_back_and_reread = models.BooleanField(default=False)
    does_it_make_sense = models.BooleanField(default=False)
    does_it_sound_right = models.BooleanField(default=False)
    self_corrects = models.BooleanField(default=False)

    class Meta:
        db_table = "Strategy"