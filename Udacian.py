from datetime import datetime

class Udacian:
    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status

    def print_udacian(self):
        print(
            '''
            name: {}
            city: {}
            enrollment: {}
            nanodegree: {}
            status: {}
            '''.format(
                self.name,
                self.city,
                self.enrollment,
                self.nanodegree,
                self.status
            )
        )