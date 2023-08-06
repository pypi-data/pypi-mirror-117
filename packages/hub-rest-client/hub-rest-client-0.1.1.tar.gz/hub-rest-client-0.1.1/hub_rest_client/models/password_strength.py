from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PasswordStrength")


@attr.s(auto_attribs=True)
class PasswordStrength:
    """ """

    reference_score: Union[Unset, int] = UNSET
    score: Union[Unset, int] = UNSET
    max_score: Union[Unset, int] = UNSET
    reference_entropy: Union[Unset, int] = UNSET
    entropy: Union[Unset, int] = UNSET
    max_entropy: Union[Unset, int] = UNSET
    feedback_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_score = self.reference_score
        score = self.score
        max_score = self.max_score
        reference_entropy = self.reference_entropy
        entropy = self.entropy
        max_entropy = self.max_entropy
        feedback_message = self.feedback_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_score is not UNSET:
            field_dict["referenceScore"] = reference_score
        if score is not UNSET:
            field_dict["score"] = score
        if max_score is not UNSET:
            field_dict["maxScore"] = max_score
        if reference_entropy is not UNSET:
            field_dict["referenceEntropy"] = reference_entropy
        if entropy is not UNSET:
            field_dict["entropy"] = entropy
        if max_entropy is not UNSET:
            field_dict["maxEntropy"] = max_entropy
        if feedback_message is not UNSET:
            field_dict["feedbackMessage"] = feedback_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        reference_score = d.pop("referenceScore", UNSET)

        score = d.pop("score", UNSET)

        max_score = d.pop("maxScore", UNSET)

        reference_entropy = d.pop("referenceEntropy", UNSET)

        entropy = d.pop("entropy", UNSET)

        max_entropy = d.pop("maxEntropy", UNSET)

        feedback_message = d.pop("feedbackMessage", UNSET)

        password_strength = cls(
            reference_score=reference_score,
            score=score,
            max_score=max_score,
            reference_entropy=reference_entropy,
            entropy=entropy,
            max_entropy=max_entropy,
            feedback_message=feedback_message,
        )

        password_strength.additional_properties = d
        return password_strength

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
