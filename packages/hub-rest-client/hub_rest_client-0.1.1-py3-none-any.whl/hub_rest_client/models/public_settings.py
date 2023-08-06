from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.end_user_agreement import EndUserAgreement
    from ..models.locale import Locale
else:
    Locale = "Locale"
    EndUserAgreement = "EndUserAgreement"

from ..models.settings import Settings

T = TypeVar("T", bound="PublicSettings")


@attr.s(auto_attribs=True)
class PublicSettings(Settings):
    """ """

    locale: Union[Unset, Locale] = UNSET
    hub_motto_hidden: Union[Unset, bool] = UNSET
    company_logo: Union[Unset, str] = UNSET
    login_message: Union[Unset, str] = UNSET
    login_field_placeholder: Union[Unset, str] = UNSET
    system_message: Union[Unset, str] = UNSET
    end_user_agreement: Union[Unset, EndUserAgreement] = UNSET
    installation_type: Union[Unset, str] = UNSET
    email_verification_required: Union[Unset, bool] = UNSET
    host_service_name: Union[Unset, str] = UNSET
    host_service_application_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        _Settings_dict = super(Settings).to_dict()
        field_dict.update(_Settings_dict)
        field_dict.update(self.additional_properties)
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
        d = src_dict.copy()

        _Settings_kwargs = super(Settings).from_dict(src_dict=d).to_dict()

        _locale = d.pop("locale", UNSET)
        locale: Union[Unset, Locale]
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = Locale.from_dict(_locale)

        hub_motto_hidden = d.pop("hubMottoHidden", UNSET)

        company_logo = d.pop("companyLogo", UNSET)

        login_message = d.pop("loginMessage", UNSET)

        login_field_placeholder = d.pop("loginFieldPlaceholder", UNSET)

        system_message = d.pop("systemMessage", UNSET)

        _end_user_agreement = d.pop("endUserAgreement", UNSET)
        end_user_agreement: Union[Unset, EndUserAgreement]
        if isinstance(_end_user_agreement, Unset):
            end_user_agreement = UNSET
        else:
            end_user_agreement = EndUserAgreement.from_dict(_end_user_agreement)

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
            **_Settings_kwargs,
        )

        public_settings.additional_properties = d
        return public_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
