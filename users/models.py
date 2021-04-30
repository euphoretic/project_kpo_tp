from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @classmethod
    def parse_name(cls, name: str) -> dict:
        if name is None:
            return {}

        parts = name.split('', 2)

        if len(parts) == 1:
            return {'first_name': parts[0]}

        if len(parts) == 2:
            return {'first_name': parts[0], 'last_name': parts[1:]}

        return {'first_name': parts[0], 'last_name': ' '.join(parts[1:])}

    def __str__(self):
        name = self.first_name + ' ' + self.last_name

        if len(name) < 3:
            return self.username

        return name.strip()

    def setattr_and_save(self, key, value):
        """set attribute of the model and save
        there override selected_city, first_name, last_name, favourites_list  """
        setattr(self, key, value)
        self.save()


