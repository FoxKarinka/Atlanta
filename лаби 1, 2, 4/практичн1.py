class Route:
    def __init__(self, start, finish, segments):
        self.start = start
        self.finish = finish
        self.segments = segments

    def __str__(self):
        return f"Маршрут {self.start} - {self.finish}: довжина {self.total_distance()} км, привалів {self.rest_stops()}"

    def total_distance(self):
        return sum(self.segments)

    def rest_stops(self):
        return len(self.segments) - 1

    def longest_segment(self):
        return max(self.segments)

    def __lt__(self, other):
        return self.total_distance() < other.total_distance()

    def __le__(self, other):
        return self.total_distance() <= other.total_distance()

    def __eq__(self, other):
        return self.total_distance() == other.total_distance()

def load_routes(filename):
    routes = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.strip():
                continue
            parts = line.strip().split(', ')
            if len(parts) < 3:
                print(f"Помилка: неповний рядок {line.strip()}")
                continue
            start = parts[0]
            finish = parts[1]
            segments = []
            try:
                segments = list(map(int, parts[2:]))
            except ValueError as e:
                print(f"Помилка перетворення числових значень у рядку {line.strip()}: {e}")
                continue
            routes.append(Route(start, finish, segments))
    return routes

def display_routes(routes):
    for route in routes:
        print(route)

def max_rest_stops(routes):
    max_stops = max(route.rest_stops() for route in routes)
    return [route for route in routes if route.rest_stops() == max_stops]

def longest_single_segment(routes):
    longest = max(route.longest_segment() for route in routes)
    return [route for route in routes if route.longest_segment() == longest]

def filter_routes_by_point(routes, point):
    return [route for route in routes if route.start == point or route.finish == point]

filename = 'routes.txt'
routes = load_routes(filename)

sorted_routes = sorted(routes)

print("Відсортовані маршрути за довжиною:")
display_routes(sorted_routes)

routes_with_max_stops = max_rest_stops(routes)
print("\nМаршрути з максимальною кількістю привалів:")
display_routes(routes_with_max_stops)

routes_with_longest_segment = longest_single_segment(routes)
print("\nМаршрути з найдовшим переходом:")
display_routes(routes_with_longest_segment)

point = 'Точках'
routes_by_point = filter_routes_by_point(routes, point)
print(f"\nМаршрути з початком або кінцем у різних {point}:")
display_routes(routes_by_point)
