from django.apps import AppConfig

class TrainingplannerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trainingplanner'  # <- Nazwa musi pasować do `INSTALLED_APPS`
