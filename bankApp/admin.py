from django.contrib import admin


class MyBankProjectAdmin(admin.AdminSite):
    site_id = "My Django Project Admin Site"
    site_header = "Welcome to the my Bank Application Admin Interface"
    index_title = "My Django Project Index"
