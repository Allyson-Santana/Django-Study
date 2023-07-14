from django.db import transaction
from django.http import HttpResponse
from .models import Publishers, Category, Video, People
from django.db import transaction
from django.db.models.aggregates import (
    Avg,
    Sum,
    Count,
    Max,
    Min,
)

@transaction.atomic
def acid_atomic(request):

    p1 = People.objects.get(id=1)
    p1.count = 2
    p1.save()

    p2 = People.objects.get(id=1)
    p2.count = 2
    p2.save()

    return HttpResponse("A.C.I.D")


def register_people(request):
    with transaction.atomic():
        People(name="Luiz", count=1).save()

        People(name="Cardoso", count=1).save()

    return HttpResponse("register_obejects to ACID")



###################### aggregates  ######################

def aggregate(request):

    # AQUI VC PODE USAR O .all(), .filter(), etc...
    # Usa-se o 'aggregate" somente quando a operação for em uma unica Tabela \n
    # Caso contrário usa-se annotate

    aggregate_query_all = Video.objects.all().aggregate(
        avg_count=Avg('duration'),
        sum_count=Sum('duration'),
        max_count=Max('duration'),
        min_count=Min('duration'),
    )
    print("aggregate_query_all => ", aggregate_query_all)

    ############################

    aggregate_query_filter = Video.objects.filter(category__id=1).aggregate(
        avg_count=Avg('duration'),
        sum_count=Sum('duration'),
        max_count=Max('duration'),
        min_count=Min('duration'),
    )
    print("aggregate_query_filter => ", aggregate_query_filter)


    return HttpResponse("Study the aggregates")



def annotate(request):

    publishers = Publishers.objects.all().annotate(
        duration_total=Sum('video__duration')
    )

    for p in publishers:
        print(p.name, p.duration_total)

    #################################

    # .values realizar agrupamento de coluna

    grupBy_video = Video.objects.all().values('type').annotate(avg=Avg('duration'))

    print(grupBy_video)

    return HttpResponse("Study the annotate")
