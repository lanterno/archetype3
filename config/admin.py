from django.contrib import admin


class ArcheTypeAdmin(admin.AdminSite):
    site_title = "Archetype administration"
    site_header = "ArcheType - Models Of Authority"
    index_title = "Welcome to Archetype administration"

    def get_app_list(self, request, app_label=None):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request, app_label)

        desired_order = {"publications": 1, "manuscripts": 2, "scribes": 3, "handwriting": 4, "users": 5, "admin interface": 6}

        app_list = sorted(app_dict.values(), key=lambda x: desired_order.get(x["name"].lower(), 99))
        return app_list