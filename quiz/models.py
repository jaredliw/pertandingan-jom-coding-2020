from django.db import models

class Question(models.Model):
    statement = models.TextField(blank=False)
    op1 = models.TextField(blank=False)
    op2 = models.TextField(blank=False)
    op3 = models.TextField(blank=False)
    op4 = models.TextField(blank=False)
    answer = models.TextField(
        blank=False,
        choices=[
            (op1, "Option 1"),
            (op2, "Option 2"),
            (op3, "Option 3"),
            (op4, "Option 4")
        ]
    )
