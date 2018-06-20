from django.core.management import BaseCommand
from django.utils import timezone

from nullblank.models import NullBlank


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 指定しないと発生するエラーは以下の通り
        #   sqlite3.IntegrityError:
        #   NOT NULL constraint failed: nullblank_nullblank.intBlank
        #   NOT NULL constraint failed: nullblank_nullblank.dateBlank
        #   NOT NULL constraint failed: nullblank_nullblank.boolBlank
        # 2回目以降、何も指定しないと発生するエラーは以下の通り
        #   UNIQUE constraint failed: nullblank_nullblank.charBlankUnique
        NullBlank(
            intBlank=0,
            dateBlank=timezone.now(),
            boolBlank=True,
            # 初回だけなら指定しなくてもOKだが、二回目以降は指定が必要
            charBlankUnique=timezone.now().strftime('%Y/%m/%d %H:%M:%S')
        ).save()
