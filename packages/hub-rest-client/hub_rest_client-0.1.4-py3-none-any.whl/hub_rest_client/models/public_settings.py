from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicSettings")


try:
    from ..models import settings
except ImportError:
    import sys

    settings = sys.modules[__package__ + "settings"]


@attr.s(auto_attribs=True)
class PublicSettings(settings.Settings):
    """ """

    locale: "Union[Unset, locale_m.Locale]" = UNSET
    hub_motto_hidden: "Union[Unset, bool]" = UNSET
    company_logo: "Union[Unset, str]" = UNSET
    login_message: "Union[Unset, str]" = UNSET
    login_field_placeholder: "Union[Unset, str]" = UNSET
    system_message: "Union[Unset, str]" = UNSET
    end_user_agreement: "Union[Unset, end_user_agreement_m.EndUserAgreement]" = UNSET
    installation_type: "Union[Unset, str]" = UNSET
    email_verification_required: "Union[Unset, bool]" = UNSET
    host_service_name: "Union[Unset, str]" = UNSET
    host_service_application_name: "Union[Unset, str]" = UNSET

    def to_dict(self) -> Dict[str, Any]:
        locale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.to_dict()

        hub_motto_hidden = self.hub_motto_hidden
        company_logo = self.company_logo
        login_message = self.login_message
        login_field_placeholder = self.login_field_placeholder
        system_message = self.system_message
        end_user_agreement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.end_user_agreement, Unset):
            end_user_agreement = self.end_user_agreement.to_dict()

        installation_type = self.installation_type
        email_verification_required = self.email_verification_required
        host_service_name = self.host_service_name
        host_service_application_name = self.host_service_application_name

        field_dict: Dict[str, Any] = {}
        _Settings_dict = super().to_dict()
        field_dict.update(_Settings_dict)
        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if hub_motto_hidden is not UNSET:
            field_dict["hubMottoHidden"] = hub_motto_hidden
        if company_logo is not UNSET:
            field_dict["companyLogo"] = company_logo
        if login_message is not UNSET:
            field_dict["loginMessage"] = login_message
        if login_field_placeholder is not UNSET:
            field_dict["loginFieldPlaceholder"] = login_field_placeholder
        if system_message is not UNSET:
            field_dict["systemMessage"] = system_message
        if end_user_agreement is not UNSET:
            field_dict["endUserAgreement"] = end_user_agreement
        if installation_type is not UNSET:
            field_dict["installationType"] = installation_type
        if email_verification_required is not UNSET:
            field_dict["emailVerificationRequired"] = email_verification_required
        if host_service_name is not UNSET:
            field_dict["hostServiceName"] = host_service_name
        if host_service_application_name is not UNSET:
            field_dict["hostServiceApplicationName"] = host_service_application_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        try:
            from ..models import end_user_agreement as end_user_agreement_m
            from ..models import locale as locale_m
        except ImportError:
            import sys

            end_user_agreement_m = sys.modules[__package__ + "end_user_agreement"]
            locale_m = sys.modules[__package__ + "locale"]

        d = src_dict.copy()

        _locale = d.pop("locale", UNSET)
        locale: Union[Unset, locale_m.Locale]
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = locale_m.Locale.from_dict(_locale)

        hub_motto_hidden = d.pop("hubMottoHidden", UNSET)

        company_logo = d.pop("companyLogo", UNSET)

        login_message = d.pop("loginMessage", UNSET)

        login_field_placeholder = d.pop("loginFieldPlaceholder", UNSET)

        system_message = d.pop("systemMessage", UNSET)

        _end_user_agreement = d.pop("endUserAgreement", UNSET)
        end_user_agreement: Union[Unset, end_user_agreement_m.EndUserAgreement]
        if isinstance(_end_user_agreement, Unset):
            end_user_agreement = UNSET
        else:
            end_user_agreement = end_user_agreement_m.EndUserAgreement.from_dict(_end_user_agreement)

        installation_type = d.pop("installationType", UNSET)

        email_verification_required = d.pop("emailVerificationRequired", UNSET)

        host_service_name = d.pop("hostServiceName", UNSET)

        host_service_application_name = d.pop("hostServiceApplicationName", UNSET)

        public_settings = cls(
            locale=locale,
            hub_motto_hidden=hub_motto_hidden,
            company_logo=company_logo,
            login_message=login_message,
            login_field_placeholder=login_field_placeholder,
            system_message=system_message,
            end_user_agreement=end_user_agreement,
            installation_type=installation_type,
            email_verification_required=email_verification_required,
            host_service_name=host_service_name,
            host_service_application_name=host_service_application_name,
        )

        return public_settings
