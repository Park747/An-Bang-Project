import csv
import os
import django

# django project 생성 시 자동으로 생성되는 모듈 외의 파일의 사용할 때 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AnBang.settings")
django.setup()

from mainApp.models import Building

with open('building_data.csv', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Building.objects.get_or_create(
            name = row[0],
            address = row[1],
            latitude = row[2],
            longitude = row[3]
        )