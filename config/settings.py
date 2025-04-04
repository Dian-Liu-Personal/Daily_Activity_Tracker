"""
Application settings for the Activity Tracker app.
"""

# Application metadata
APP_TITLE = "Dian的日历"
APP_ICON = ""  # Favicon/emoji for the app
APP_LAYOUT = "wide"  # 'wide' or 'centered'

# Data storage settings
DATA_DIR = "data"
DAILY_DATA_FILE = "daily_data.json"
WEEKLY_DATA_FILE = "weekly_data.json"

# UI settings
THEME_COLOR = "#4CAF50"  # Primary theme color
SECONDARY_COLOR = "#FFC107"  # Secondary theme color

# Activity types
DAILY_ACTIVITIES = [
    # Study activities (工作安排)
    {"id": "jung", "name": "开会", "category": "学习安排", "type": "boolean"},
    {"id": "english", "name": "写代码", "category": "学习安排", "type": "boolean"},
    {"id": "metaphysics", "name": "学习", "category": "学习安排", "type": "boolean"},
    {"id": "bowel_movement", "name": "社交", "category": "学习安排", "type": "boolean"},
    
    # Life activities (生活)
    {"id": "biking", "name": "骑车", "category": "生活", "type": "boolean"},
    {"id": "cooking", "name": "做饭", "category": "生活", "type": "boolean"},
    {"id": "family", "name": "家人", "category": "生活", "type": "boolean"},
    {"id": "dog_walking", "name": "遛狗", "category": "生活", "type": "boolean"},
    {"id": "casual_reading", "name": "看书", "category": "生活", "type": "boolean"},
    {"id": "exercise", "name": "健身", "category": "生活", "type": "complex", "has_time": True},
    
    # Entertainment activities (娱乐)
    {"id": "drawing", "name": "打球", "category": "娱乐", "type": "boolean"},
    {"id": "watching_shows", "name": "看剧", "category": "娱乐", "type": "boolean"},
    {"id": "friends", "name": "朋友", "category": "娱乐", "type": "boolean"},
    {"id": "doi", "name": "DOI", "category": "娱乐", "type": "boolean"},
    
    # Special activities with additional inputs
    #{"id": "doi", "name": "DOI", "category": "特殊", "type": "boolean"},
]

# Mood range
MOOD_RANGE = [
    {"value": 1, "label": "很差"},
    {"value": 2, "label": "差"},
    {"value": 3, "label": "一般"},
    {"value": 4, "label": "好"},
    {"value": 5, "label": "很好"}
]

WEEKLY_ACTIVITIES = [
    {"id": "housework", "name": "做家务", "type": "boolean"},
    {"id": "eating_out", "name": "外出就餐", "type": "boolean"},
    {"id": "eating_out", "name": "打比赛", "type": "boolean"}
]

# Date display formats
DATE_FORMAT = "%A, %B %d, %Y"
SHORT_DATE_FORMAT = "%a %m/%d"
MONTH_YEAR_FORMAT = "%B %Y"
