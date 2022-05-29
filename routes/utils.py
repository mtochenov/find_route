from trains.models import Train


def dfs_paths(graph, start, goal):
    """ Функция поиска всех возможных маршрутов из одного города в другой. Вариант посещения
    одного и того же города более одного раза, не рассматривается."""
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.departure_city_id, set())
        graph[q.departure_city_id].add(q.destination_city_id)
    return graph


def get_routes(request, form) -> dict:
    context = {"form": form}
    qs = Train.objects.all().select_related("departure_city", "destination_city")
    graph = get_graph(qs)
    data = form.cleaned_data
    departure_city = data["departure_city"]
    destination_city = data["destination_city"]
    cities = data["cities"]
    route_time = data["route_time"]
    all_routes = list(dfs_paths(graph, departure_city.id, destination_city.id))
    if not len(all_routes):
        raise ValueError("Такого маршрута нет, попробуйте еще")
    if cities:
        """Если есть города, через которые нужно проехать"""
        _cities = [city.id for city in cities]
        correct_routes = []
        for route in all_routes:
            if all(city in route for city in _cities):
                correct_routes.append(route)
        if not correct_routes:
            raise ValueError("Нельзя проложить маршрут через эти города")
    else:
        correct_routes = all_routes
    routes = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.departure_city_id, q.destination_city_id), [])
        all_trains[(q.departure_city_id, q.destination_city_id)].append(q)
    for route in correct_routes:
        tmp = {}
        tmp["trains"] = []
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_trains[(route[i], route[i+1])]
            q = qs[0]
            total_time += q.travel_time
            tmp["trains"].append(q)
        tmp["total_time"] = total_time
        if total_time <= route_time:
            """Если общее время в пути <= заданного, то добавляем маршрут в общий список"""
            routes.append(tmp)
    if not routes:
        """Если список пуст то нет таких маршрутов, которые удовлетворяли бы заданным условиям"""
        raise ValueError("Время по такому маршруту будет больше заданного")
    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r["total_time"] for r in routes))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route["total_time"]:
                    sorted_routes.append(route)
    context["routes"] = sorted_routes
    context["cities"] = {"departure_city": departure_city, "destination_city": destination_city}

    return context
