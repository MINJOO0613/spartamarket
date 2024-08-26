from django import template
from datetime import timedelta, timezone

register = template.Library()

@register.filter
def custom_timesince(value, now=None):
    if not value:
        return ""
    if now is None:
        now = timezone.now()
    delta = now - value
    
    if delta < timedelta(minutes=1):
        return "방금 전"
    elif delta < timedelta(hours=1):
        minutes = int(delta.total_seconds() / 60)
        return f"{minutes}분 전"
    elif delta < timedelta(days=1):
        hours = int(delta.total_seconds() / 3600)
        return f"{hours}시간 전"
    else:
        days = delta.days
        if days == 1:
            return "어제"
        elif days < 7:
            return f"{days}일 전"
        elif days < 30:
            weeks = days // 7
            return f"{weeks}주 전"
        else:
            months = days // 30
            return f"{months}개월 전"