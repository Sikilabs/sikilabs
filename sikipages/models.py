from django.db import models
from mezzanine.pages.models import Page


class SikiPage(Page):
    catch_words = models.CharField(max_length=256)
    text = models.TextField()
    action_btn_text = models.CharField(max_length=256)
    action_btn_lnk = models.URLField()