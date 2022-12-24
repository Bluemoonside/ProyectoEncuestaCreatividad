from django.contrib import admin
from .models.Choice import Choice
from .models.Dimension import Dimension
from .models.Indicator import Indicator
from .models.MeasurementCriterion import MeasurementCriterion
from .models.Poll import Poll
from .models.Question import Question
from .models.Respondent import Respondent
from .models.Scale import Scale
from .models.ScaleLabel import ScaleLabel 
from .models.Variable import Variable

admin.site.register(Choice)
admin.site.register(Dimension)
admin.site.register(Indicator)
admin.site.register(MeasurementCriterion)
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Respondent)
admin.site.register(Scale)
admin.site.register(ScaleLabel)
admin.site.register(Variable)