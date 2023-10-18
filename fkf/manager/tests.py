from django.test import TestCase

# from .models import County, Academy, Player
from .util import DB


class TestDB(TestCase):
    def setUp(self):
        self.county_name = "Test County"
        self.academy_name = "Test Academy"
        self.player_name = "Test Player"

    def test_create_county(self):
        result = DB.create_county(self.county_name, "admin", "password")
        self.assertEqual(
            result, f"County instance {self.county_name} created successfully."
        )

    def test_create_academy(self):
        DB.create_county(self.county_name, "admin", "password")
        result = DB.create_academy(
            self.academy_name, self.county_name, "admin", "password"
        )
        self.assertEqual(
            result, f"Academy instance {self.academy_name} created successfully."
        )

    def test_create_player(self):
        DB.create_county(self.county_name, "admin", "password")
        DB.create_academy(self.academy_name, self.county_name, "admin", "password")
        result = DB.create_player(self.player_name, self.academy_name)
        self.assertEqual(
            result, f"Player instance {self.player_name} created successfully."
        )

    def test_update_instance(self):
        DB.create_county(self.county_name, "admin", "password")
        result = DB.update_instance(
            "County", "name", self.county_name, admin="new_admin"
        )
        self.assertEqual(result, "County instance updated successfully.")

    def test_delete_instance(self):
        DB.create_county(self.county_name, "admin", "password")
        result = DB.delete_instance("County", "name", self.county_name)
        self.assertEqual(
            result,
            f"County instance with name = {self.county_name} deleted successfully.",
        )

    def test_all_instances_with_filter(self):
        DB.create_county(self.county_name, "admin", "password")
        result = DB.all_instances("County", "admin", "admin")
        self.assertEqual(len(result), 1)

    def test_all_instances_without_filter(self):
        DB.create_county(self.county_name, "admin", "password")
        result = DB.all_instances("County")
        self.assertEqual(len(result), 1)


# if __name__ == "__main__":
#     unittest.main()
