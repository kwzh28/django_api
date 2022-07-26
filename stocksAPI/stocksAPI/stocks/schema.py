import graphene
from graphene_django import DjangoObjectType
from .models import StocksInfo

class InfoType(DjangoObjectType):
    class Meta:
        model = StocksInfo
        fields = (
            'Date',
            'Open',
            'High',
            'Low',
            'Close',
            'Volume',
        )

class Query(graphene.ObjectType):
    stocks = graphene.List(InfoType)
    def resolve_stocks(root, info, **kwargs):
        return StocksInfo.objects.all()
schema = graphene.Schema(query=Query)

#class StockInput(graphene.InputObjectType):
#    Date = graphene.Date()
#    Open = graphene.String()
#    High = graphene.String()
#    Low = graphene.String()
#    Close = graphene.String()
#    Volume = graphene.String()
