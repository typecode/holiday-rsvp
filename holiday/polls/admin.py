from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields':  ['question']}),
    ('Date information', {'fields': ['pub_date']}),
  ]
  inlines = [ChoiceInline]
  list_display = ('question', 'pub_date')
  list_filter = ['pub_date']
  search_fields = ['question']
  date_hiearchy = ['pub_date']

admin.site.register(Poll, PollAdmin)
