from django.contrib.admin.apps import AdminConfig


class BankAdminConfig(AdminConfig):
    default_site = "bankApp.admin.MyBankProjectAdmin"
