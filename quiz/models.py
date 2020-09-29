from django.db import models


class Question(models.Model):
    qn_id = models.AutoField(primary_key=True)
    statement = models.TextField(blank=False)
    opt1 = models.TextField(blank=False)
    opt2 = models.TextField(blank=False)
    opt3 = models.TextField(blank=False)
    opt4 = models.TextField(blank=False)
    answer = models.TextField(
        default="opt1",
        blank=False,
        choices=[
            ("opt1", "Option 1"),
            ("opt2", "Option 2"),
            ("opt3", "Option 3"),
            ("opt4", "Option 4")
        ]
    )
    page = models.CharField(default="comp_t", blank=False, max_length=10, choices=[('q-comp_t', "Computational Thinking"),
                                                                                   ('q-data_r', "Data Representation"),
                                                                                   ('q-algo', 'algorithms'),
                                                                                   ('q-code', 'Code')])

