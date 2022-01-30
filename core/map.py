class Map(object):
    _nodes = []  # set
    _edges = {}

    def __init__(self, edges):
        self._edges = edges
        self._nodes = edges.keys()

    def next(self, location, destination):
        if location not in self._nodes:
            return None
        if destination not in self._nodes:
            return None

        visited = [location]

        nodes = self._edges[location]
        options = []
        options.extend(nodes)

        if destination in nodes:
            return destination

        routes = []
        route = []

        while len(options) > 0:
            node = options.pop(len(options) - 1)
            route.append(node)

            if node == destination:
                routes.append(route)
                route = []
            else:
                visited.append(node)

            connections = self._edges[node]
            for connection in connections:
                if connection not in visited:
                    options.append(connection)
                    continue
                route.remove(node)
                visited.remove(node)

        shortest = None
        for route in routes:
            if shortest is None:
                shortest = route

            if len(shortest) > len(route):
                shortest = route

        if shortest is not None:
            return shortest[0]

        return None
