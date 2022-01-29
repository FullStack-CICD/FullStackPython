from multipledispatch import dispatch
class MethodOverload:
    @dispatch(int)
    def rectaglearea(self,area):
        actarea = area * area
        print(actarea)

    @dispatch(int,int)
    def rectaglearea(self,area,area1):
        actarea = area * area1
        print(actarea)

    def triglearea(self,area):
        actrea = area * area
        print(actrea)

    def circlearea(self,area):
        actrea = area
        print(actrea)


MethodOverload().rectaglearea(10)
MethodOverload().rectaglearea(10,5)
MethodOverload().triglearea(10)
MethodOverload().circlearea(10)