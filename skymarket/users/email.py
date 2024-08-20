from templated_mail.mail import BaseEmailMessage


class DomainOverride:
    frontend_domain = '127.0.0.1:3000'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['domain'] = self.frontend_domain
        return context


class PasswordResetEmail(DomainOverride, BaseEmailMessage):
    template_name = "email/password_reset.html"
