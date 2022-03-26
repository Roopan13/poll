from django.contrib import admin
from .models import Vote
# Register your models here.
@admin.register(Vote)
class VoteModelAdmin(admin.ModelAdmin):
    list_display = ['id','option_one','option_two','option_three','option_one_count','option_two_count','option_three_count']
