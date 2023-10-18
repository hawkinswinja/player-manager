from .models import County, Academy, Player


class DB:
    """Functionalities for manipulating db objects"""

    classes_dict = {
        "County": County,
        "Academy": Academy,
        "Player": Player,
    }

    @staticmethod
    def create_county(name, admin, password):
        """Add a new County instance to the db"""
        county_instance = County.objects.create(
            name=name, admin=admin, password=password
        )
        county_instance.save()
        return f"County instance {name} created successfully."

    @staticmethod
    def create_academy(name, county_name, admin, password):
        """Add a new Academy instance to the db"""
        county_instance = County.objects.get(name=county_name)
        academy_instance = Academy.objects.create(
            name=name, county=county_instance, admin=admin, password=password
        )
        academy_instance.save()
        return f"Academy instance {name} created successfully."

    @staticmethod
    def create_player(name, academy_name):
        """Add a new Player instance to the db"""
        academy_instance = Academy.objects.get(name=academy_name)
        player_instance = Player.objects.create(name=name, academy=academy_instance)
        player_instance.save()
        return f"Player instance {name} created successfully."

    @staticmethod
    def update_instance(class_str, filter_key, filter_val, **kwargs):
        """Update an existing db instance"""
        target_class = DB.classes_dict.get(class_str)
        if target_class:
            try:
                instance = target_class.objects.get(**{filter_key: filter_val})
                for key, value in kwargs.items():
                    setattr(instance, key, value)
                instance.save()
                return f"{class_str} instance updated successfully."
            except target_class.DoesNotExist:
                return f"{class_str} instance with provided attributes not found."
        else:
            return "Class not found."

    @staticmethod
    def delete_instance(class_str, filter_key, filter_val):
        """Delete an existing instance from the db"""
        target_class = DB.classes_dict.get(class_str)
        if target_class:
            try:
                instance = target_class.objects.get(**{filter_key: filter_val})
                instance.delete()
                return f"{class_str} instance with {filter_key} = {filter_val} deleted successfully."
            except target_class.DoesNotExist:
                return (
                    f"{class_str} instance with {filter_key} = {filter_val} not found."
                )
        else:
            return "Class not found."

    @staticmethod
    def all_instances(class_str, filter_key=None, filter_val=None):
        """Retrieve all instances from the db"""
        target_class = DB.classes_dict.get(class_str)
        if target_class:
            if filter_key and filter_val:
                instances = target_class.objects.filter(**{filter_key: filter_val})
            else:
                instances = target_class.objects.all()
            return list(instances)
        else:
            return None
