from copy import deepcopy

from django.apps import apps as django_apps
from django.test import TestCase
from edc_constants.constants import (
    ABSENT,
    DECREASED,
    NO,
    NORMAL,
    NOT_EXAMINED,
    OTHER,
    PRESENT,
    PRESENT_WITH_REINFORCEMENT,
    REDUCED,
    YES,
)
from edc_form_validators import FormValidatorTestCaseMixin
from edc_list_data import site_list_data

from edc_mnsi import list_data
from edc_mnsi.calculator import (
    MnsiCalculator,
    MnsiPatientHistoryCalculatorError,
    MnsiPhysicalAssessmentCalculatorError,
)
from edc_mnsi.model_mixins import abnormal_foot_appearance_observations_model
from edc_mnsi.models import AbnormalFootAppearanceObservations

from ..forms import MnsiForm, MnsiFormValidator
from ..models import Mnsi


class TestCaseMixin(TestCase):

    foot_choices = ["right", "left"]

    @classmethod
    def setUpTestData(cls):
        site_list_data.initialize()
        site_list_data.register(list_data, app_name="edc_mnsi")
        site_list_data.load_data()

    @staticmethod
    def get_mnsi_obj(abnormal_obs_left_foot=None, abnormal_obs_right_foot=None, **responses):
        """Returns an Mnsi model instance with the m2ms added"""
        mnsi = Mnsi(**responses)
        mnsi.save()
        for obj in abnormal_obs_left_foot:
            mnsi.abnormal_obs_left_foot.add(obj)
        for obj in abnormal_obs_right_foot:
            mnsi.abnormal_obs_right_foot.add(obj)
        return mnsi

    @staticmethod
    def get_empty_set():
        return django_apps.get_model(
            abnormal_foot_appearance_observations_model
        ).objects.filter(name=None)

    @staticmethod
    def get_nonempty_set():
        return django_apps.get_model(
            abnormal_foot_appearance_observations_model
        ).objects.filter(name="infection")

    def get_best_case_answers(self):
        data = {
            "mnsi_performed": YES,
            "mnsi_not_performed_reason": None,
            # Part 1: Patient History
            "numb_legs_feet": NO,
            "burning_pain_legs_feet": NO,
            "feet_sensitive_touch": NO,
            "muscle_cramps_legs_feet": NO,  # no effect on score, regardless of value
            "prickling_feelings_legs_feet": NO,
            "covers_touch_skin_painful": NO,
            "differentiate_hot_cold_water": YES,
            "open_sore_foot_history": NO,
            "diabetic_neuropathy": NO,
            "feel_weak": NO,  # no effect on score, regardless of value
            "symptoms_worse_night": NO,
            "legs_hurt_when_walk": NO,
            "sense_feet_when_walk": YES,
            "skin_cracks_open_feet": NO,
            "amputation": NO,
        }
        for foot_choice in self.foot_choices:
            data.update(
                {
                    f"examined_{foot_choice}_foot": YES,
                    f"normal_appearance_{foot_choice}_foot": YES,
                    f"abnormal_obs_{foot_choice}_foot": self.get_empty_set(),
                    f"ulceration_{foot_choice}_foot": ABSENT,
                    f"ankle_reflexes_{foot_choice}_foot": PRESENT,
                    f"vibration_perception_{foot_choice}_toe": PRESENT,
                    f"monofilament_{foot_choice}_foot": NORMAL,
                }
            )
        return data

    @staticmethod
    def get_worst_case_patient_history_data():
        return {
            # Part 1: Patient History
            "numb_legs_feet": YES,
            "burning_pain_legs_feet": YES,
            "feet_sensitive_touch": YES,
            "prickling_feelings_legs_feet": YES,
            "covers_touch_skin_painful": YES,
            "differentiate_hot_cold_water": NO,
            "open_sore_foot_history": YES,
            "diabetic_neuropathy": YES,
            "symptoms_worse_night": YES,
            "legs_hurt_when_walk": YES,
            "sense_feet_when_walk": NO,
            "skin_cracks_open_feet": YES,
            "amputation": YES,
        }

    def get_worst_case_physical_assessment_data(self):
        data = {}
        for foot_choice in ["left", "right"]:
            data.update(
                {
                    f"examined_{foot_choice}_foot": YES,
                    f"normal_appearance_{foot_choice}_foot": NO,
                    f"abnormal_obs_{foot_choice}_foot": self.get_nonempty_set(),
                    f"ulceration_{foot_choice}_foot": PRESENT,
                    f"ankle_reflexes_{foot_choice}_foot": ABSENT,
                    f"vibration_perception_{foot_choice}_toe": ABSENT,
                    f"monofilament_{foot_choice}_foot": ABSENT,
                }
            )
        return data


class TestMnsiCalculators(TestCaseMixin, TestCase):
    def test_calculator_instantiated_with_dict(self):
        responses = self.get_best_case_answers()
        mnsi_calculator = MnsiCalculator(**responses)
        self.assertEqual(mnsi_calculator.patient_history_score(), 0)
        self.assertEqual(mnsi_calculator.physical_assessment_score(), 0)

    def test_calculator_instantiated_with_model(self):
        responses = self.get_best_case_answers()
        model = self.get_mnsi_obj(**responses)
        mnsi_calculator = MnsiCalculator(model)
        self.assertEqual(mnsi_calculator.patient_history_score(), 0)
        self.assertEqual(mnsi_calculator.physical_assessment_score(), 0)

    def test_calculator_instantiated_with_dict2(self):
        responses = self.get_best_case_answers()
        responses.update(self.get_worst_case_patient_history_data())
        responses.update(self.get_worst_case_physical_assessment_data())
        mnsi_calculator = MnsiCalculator(**responses)
        self.assertEqual(mnsi_calculator.patient_history_score(), 13)
        self.assertEqual(mnsi_calculator.physical_assessment_score(), 10)

    def test_calculator_instantiated_with_model2(self):
        responses = self.get_best_case_answers()
        responses.update(self.get_worst_case_patient_history_data())
        responses.update(self.get_worst_case_physical_assessment_data())
        model = self.get_mnsi_obj(**responses)
        mnsi_calculator = MnsiCalculator(model)
        self.assertEqual(mnsi_calculator.patient_history_score(), 13)
        self.assertEqual(mnsi_calculator.physical_assessment_score(), 10)

    def test_missing_required_field_raises_mnsi_patient_history_calculator_error(
        self,
    ):
        responses = self.get_best_case_answers()
        responses.pop("amputation")
        mnsi_calculator = MnsiCalculator(**responses)
        with self.assertRaises(MnsiPatientHistoryCalculatorError):
            mnsi_calculator.patient_history_score()

    def test_missing_non_required_fields_does_not_raise_mnsi_patient_history_calculator_error(
        self,
    ):
        responses = self.get_best_case_answers()
        responses.pop("muscle_cramps_legs_feet")
        responses.pop("feel_weak")
        mnsi_calculator = MnsiCalculator(**responses)
        try:
            mnsi_calculator.patient_history_score()
        except MnsiPatientHistoryCalculatorError as exc:
            self.fail(
                f"mnsi_calculator.patient_history_score() raised "
                f"MnsiPatientHistoryCalculatorError unexpectedly.\nDetails: {exc}"
            )

    def test_missing_required_field_raises_mnsi_physical_assessment_calculator_error(
        self,
    ):
        responses = self.get_best_case_answers()
        responses.pop("ulceration_left_foot")
        mnsi_calculator = MnsiCalculator(**responses)
        with self.assertRaises(MnsiPhysicalAssessmentCalculatorError):
            mnsi_calculator.physical_assessment_score()

    def test_best_case_patient_history_returns_min_score_of_zero(self):
        mnsi_calculator = MnsiCalculator(**self.get_best_case_answers())
        self.assertEqual(mnsi_calculator.patient_history_score(), 0)

    def test_worst_case_patient_history_returns_max_score_of_thirteen(self):
        responses = self.get_best_case_answers()
        responses.update(self.get_worst_case_patient_history_data())
        mnsi_calculator = MnsiCalculator(**responses)
        self.assertEqual(mnsi_calculator.patient_history_score(), 13)

    def test_q4_and_q10_do_not_affect_patient_history_score(self):
        # Best case score should be 0
        responses = self.get_best_case_answers()
        mnsi_calculator = MnsiCalculator(**responses)
        self.assertEqual(mnsi_calculator.patient_history_score(), 0)

        # Best case score should remain 0 after modifying q4 and 10
        responses.update({"muscle_cramps_legs_feet": YES, "feel_weak": YES})
        mnsi_calculator = MnsiCalculator(**responses)
        self.assertEqual(mnsi_calculator.patient_history_score(), 0)

        # Worst case score should be 13
        responses.update(self.get_worst_case_patient_history_data())
        mnsi_calculator = MnsiCalculator(**responses)
        self.assertEqual(mnsi_calculator.patient_history_score(), 13)

        # Best case score should remain 13 after modifying q4 and 10
        responses.update({"muscle_cramps_legs_feet": NO, "feel_weak": NO})
        mnsi_calculator = MnsiCalculator(**responses)
        self.assertEqual(mnsi_calculator.patient_history_score(), 13)

    def test_best_case_physical_assessment_returns_min_score_of_zero(self):
        mnsi_calculator = MnsiCalculator(**self.get_best_case_answers())
        self.assertEqual(mnsi_calculator.physical_assessment_score(), 0)

    def test_worst_case_physical_assessment_returns_max_score_of_ten(self):
        responses = self.get_best_case_answers()
        responses.update(self.get_worst_case_physical_assessment_data())
        mnsi_calculator = MnsiCalculator(**responses)
        self.assertEqual(mnsi_calculator.physical_assessment_score(), 10)

    def test_patient_history_scores_where_YES_awards_one_point(self):
        one_point_if_yes_response_questions = [
            "numb_legs_feet",  # Q1
            "burning_pain_legs_feet",  # Q2
            "feet_sensitive_touch",  # Q3
            "prickling_feelings_legs_feet",  # Q5
            "covers_touch_skin_painful",  # Q6
            "open_sore_foot_history",  # Q8
            "diabetic_neuropathy",  # Q9
            "symptoms_worse_night",  # Q11
            "legs_hurt_when_walk",  # Q12
            "skin_cracks_open_feet",  # Q14
            "amputation",  # Q15
        ]

        for question in one_point_if_yes_response_questions:
            with self.subTest(
                f"Testing '{question}' with 'YES' response is worth 1 point",
                question=question,
            ):
                responses = self.get_best_case_answers()
                responses[question] = YES
                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.patient_history_score(), 1)

    def test_patient_history_scores_where_NO_awards_one_point(self):
        one_point_if_no_response_questions = [
            "differentiate_hot_cold_water",  # Q7
            "sense_feet_when_walk",  # Q13
        ]

        for question in one_point_if_no_response_questions:
            with self.subTest(
                f"Testing '{question}' with 'NO' response is worth 1 point",
                question=question,
            ):
                responses = self.get_best_case_answers()
                responses[question] = NO
                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.patient_history_score(), 1)

    def test_physical_assessment_abnormal_foot_appearance_awards_one_point(self):
        normal_foot_appearance_questions = [
            "normal_appearance_right_foot",
            "normal_appearance_left_foot",
        ]

        for question in normal_foot_appearance_questions:
            with self.subTest(
                f"Testing '{question}' with 'NO' response is worth 1 point",
                question=question,
            ):
                responses = self.get_best_case_answers()
                responses[question] = NO
                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.physical_assessment_score(), 1.0)

    def test_physical_assessment_foot_ulceration_present_awards_one_point(self):
        ulceration_questions = [
            "ulceration_right_foot",
            "ulceration_left_foot",
        ]

        for question in ulceration_questions:
            with self.subTest(
                f"Testing '{question}' with 'PRESENT' response is worth 1 point",
                question=question,
            ):
                responses = self.get_best_case_answers()
                responses[question] = PRESENT
                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.physical_assessment_score(), 1.0)

    def test_physical_assessment_ankle_reflexes_present_reinforcement_awards_half_point(
        self,
    ):
        ankle_reflex_questions = [
            "ankle_reflexes_right_foot",
            "ankle_reflexes_left_foot",
        ]

        for question in ankle_reflex_questions:
            with self.subTest(
                f"Testing '{question}' with 'PRESENT_REINFORCEMENT' response "
                "is worth 0.5 point",
                question=question,
            ):
                responses = self.get_best_case_answers()
                responses[question] = PRESENT_WITH_REINFORCEMENT
                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.physical_assessment_score(), 0.5)

    def test_physical_assessment_ankle_reflexes_absent_awards_one_point(
        self,
    ):
        ankle_reflex_questions = [
            "ankle_reflexes_right_foot",
            "ankle_reflexes_left_foot",
        ]

        for question in ankle_reflex_questions:
            with self.subTest(
                f"Testing '{question}' with 'ABSENT' response is worth 1 point",
                question=question,
            ):
                responses = self.get_best_case_answers()
                responses[question] = ABSENT
                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.physical_assessment_score(), 1)

    def test_physical_assessment_vibration_perception_decreased_awards_half_point(
        self,
    ):
        vibration_perception_questions = [
            "vibration_perception_right_toe",
            "vibration_perception_left_toe",
        ]

        for question in vibration_perception_questions:
            with self.subTest(
                f"Testing '{question}' with 'DECREASED' response is worth 0.5 point",
                question=question,
            ):
                responses = self.get_best_case_answers()
                responses[question] = DECREASED
                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.physical_assessment_score(), 0.5)

    def test_physical_assessment_vibration_perception_absent_awards_one_point(
        self,
    ):
        vibration_perception_questions = [
            "vibration_perception_right_toe",
            "vibration_perception_left_toe",
        ]

        for question in vibration_perception_questions:
            with self.subTest(
                f"Testing '{question}' with 'ABSENT' response is worth 1 point",
                question=question,
            ):
                responses = self.get_best_case_answers()
                responses[question] = ABSENT
                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.physical_assessment_score(), 1)

    def test_physical_assessment_monofilament_reduced_awards_half_point(
        self,
    ):
        monofilament_questions = [
            "monofilament_right_foot",
            "monofilament_left_foot",
        ]

        for question in monofilament_questions:
            with self.subTest(
                f"Testing '{question}' with 'REDUCED' response is worth 0.5 point",
                question=question,
            ):
                responses = self.get_best_case_answers()
                responses[question] = REDUCED
                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.physical_assessment_score(), 0.5)

    def test_physical_assessment_monofilament_absent_awards_one_point(
        self,
    ):
        monofilament_questions = [
            "monofilament_right_foot",
            "monofilament_left_foot",
        ]

        for question in monofilament_questions:
            with self.subTest(
                f"Testing '{question}' with 'ABSENT' response is worth 0.5 point",
                question=question,
            ):
                responses = self.get_best_case_answers()
                responses[question] = ABSENT
                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.physical_assessment_score(), 1)

    def test_physical_assessment_one_foot_not_examined(
        self,
    ):
        for foot_choice in self.foot_choices:
            with self.subTest(excluded_foot=foot_choice):
                # Set worse case responses
                responses = self.get_best_case_answers()
                responses.update(self.get_worst_case_physical_assessment_data())

                # Set excluded foot, remove further answers
                responses[f"examined_{foot_choice}_foot"] = NO
                responses.pop(f"normal_appearance_{foot_choice}_foot")
                responses.pop(f"ulceration_{foot_choice}_foot")
                responses.pop(f"ankle_reflexes_{foot_choice}_foot")
                responses.pop(f"vibration_perception_{foot_choice}_toe")
                responses.pop(f"monofilament_{foot_choice}_foot")

                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.physical_assessment_score(), 5)

    def test_physical_assessment_no_feet_examined_awards_zero_points(
        self,
    ):
        responses = self.get_best_case_answers()

        for foot_choice in self.foot_choices:
            # Set excluded foot, remove further answers
            responses[f"examined_{foot_choice}_foot"] = NO
            responses.pop(f"normal_appearance_{foot_choice}_foot")
            responses.pop(f"ulceration_{foot_choice}_foot")
            responses.pop(f"ankle_reflexes_{foot_choice}_foot")
            responses.pop(f"vibration_perception_{foot_choice}_toe")
            responses.pop(f"monofilament_{foot_choice}_foot")

        mnsi_calculator = MnsiCalculator(**responses)
        self.assertEqual(mnsi_calculator.physical_assessment_score(), 0)

    def test_physical_assessment_other_responses_ignored_if_foot_not_examined(
        self,
    ):
        for foot_choice in self.foot_choices:
            with self.subTest(foot_choice=foot_choice):
                # Set worse case responses
                responses = self.get_best_case_answers()
                responses.update(self.get_worst_case_physical_assessment_data())

                # Set excluded foot, don't remove further answers
                responses[f"examined_{foot_choice}_foot"] = NO
                mnsi_calculator = MnsiCalculator(**responses)
                self.assertEqual(mnsi_calculator.physical_assessment_score(), 5)

        # Test for both feet excluded
        for foot_choice in self.foot_choices:
            responses[f"examined_{foot_choice}_foot"] = NO
        mnsi_calculator = MnsiCalculator(**responses)
        self.assertEqual(mnsi_calculator.physical_assessment_score(), 0)


class TestMnsiFormValidator(FormValidatorTestCaseMixin, TestCaseMixin, TestCase):

    form_validator_default_form_cls = MnsiFormValidator

    def test_valid_form_ok(self):
        cleaned_data = deepcopy(self.get_best_case_answers())
        form = MnsiForm(data=cleaned_data)
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_physical_assessment_questions_applicable_if_foot_examined(self):
        for foot_choice in self.foot_choices:
            for question_field in [
                f"ulceration_{foot_choice}_foot",
                f"ankle_reflexes_{foot_choice}_foot",
                f"vibration_perception_{foot_choice}_toe",
                f"monofilament_{foot_choice}_foot",
            ]:
                # Setup test case
                cleaned_data = self.get_best_case_answers()
                cleaned_data.update({f"examined_{foot_choice}_foot": YES})
                cleaned_data.update({question_field: NOT_EXAMINED})

                # Test
                with self.subTest(foot_choice=foot_choice, question_field=question_field):
                    form_validator = self.validate_form_validator(cleaned_data)
                    self.assertIn(question_field, form_validator._errors)
                    self.assertIn(
                        "Invalid. Foot was examined",
                        str(form_validator._errors.get(question_field)),
                    )
                    self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

    def test_physical_assessment_questions_not_applicable_if_foot_not_examined(self):
        for foot_choice in self.foot_choices:
            for question_field in [
                f"normal_appearance_{foot_choice}_foot",
                f"ulceration_{foot_choice}_foot",
                f"ankle_reflexes_{foot_choice}_foot",
                f"vibration_perception_{foot_choice}_toe",
                f"monofilament_{foot_choice}_foot",
            ]:
                # Setup test case
                cleaned_data = self.get_best_case_answers()
                cleaned_data.update({f"examined_{foot_choice}_foot": NO})
                cleaned_data.update(
                    {
                        f"normal_appearance_{foot_choice}_foot": NOT_EXAMINED,
                        f"abnormal_obs_{foot_choice}_foot": self.get_empty_set(),
                        f"ulceration_{foot_choice}_foot": NOT_EXAMINED,
                        f"ankle_reflexes_{foot_choice}_foot": NOT_EXAMINED,
                        f"vibration_perception_{foot_choice}_toe": NOT_EXAMINED,
                        f"monofilament_{foot_choice}_foot": NOT_EXAMINED,
                    }
                )
                # set one field as answered, e.g. != NOT_EXAMINED
                cleaned_data.update(
                    {
                        question_field: self.get_best_case_answers()[question_field],
                    }
                )

                # Test
                with self.subTest(foot_choice=foot_choice, question_field=question_field):
                    form_validator = self.validate_form_validator(cleaned_data)
                    self.assertIn(question_field, form_validator._errors)
                    self.assertIn(
                        "Invalid. Foot was not examined",
                        str(form_validator._errors.get(question_field)),
                    )
                    self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

    def test_abnormal_observations_required_if_foot_appearance_not_normal(self):
        cleaned_data = deepcopy(self.get_best_case_answers())

        for foot in ["right_foot", "left_foot"]:
            field = f"normal_appearance_{foot}"
            m2m_field = f"abnormal_obs_{foot}"

            with self.subTest(
                f"Testing '{m2m_field}' is required if {field}='No'",
                field=field,
                m2m_field=m2m_field,
            ):
                cleaned_data.update({field: NO})
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertIn(m2m_field, form_validator._errors)
                self.assertIn(
                    "This field is required",
                    str(form_validator._errors.get(m2m_field)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

                # Set back to YES, and move on to next test
                cleaned_data.update({field: YES})

    def test_abnormal_observations_accepted_if_foot_appearance_not_normal(self):
        cleaned_data = deepcopy(self.get_best_case_answers())
        m2m_field_selection = AbnormalFootAppearanceObservations.objects.filter(
            name="infection"
        )

        for foot in ["right_foot", "left_foot"]:
            field = f"normal_appearance_{foot}"
            m2m_field = f"abnormal_obs_{foot}"

            with self.subTest(
                f"Testing '{m2m_field}' accepted if {field}='No'",
                field=field,
                m2m_field=m2m_field,
            ):
                cleaned_data.update({field: NO, m2m_field: m2m_field_selection})
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertEqual(form_validator._errors, {})

    def test_abnormal_observations_not_applicable_if_foot_appearance_is_normal(self):
        cleaned_data = deepcopy(self.get_best_case_answers())
        m2m_field_selection = AbnormalFootAppearanceObservations.objects.filter(
            name="infection"
        )

        for foot in ["right_foot", "left_foot"]:
            field = f"normal_appearance_{foot}"
            m2m_field = f"abnormal_obs_{foot}"

            with self.subTest(
                f"Testing '{m2m_field}' accepted if {field}='No'",
                field=field,
                m2m_field=m2m_field,
            ):
                cleaned_data.update({field: YES, m2m_field: m2m_field_selection})
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertIn(m2m_field, form_validator._errors)
                self.assertIn(
                    "This field is not required",
                    str(form_validator._errors.get(m2m_field)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

                # Set to No (i.e. make m2m applicable) and move onto next test
                cleaned_data.update({field: NO})

    def test_other_field_required_if_other_specified(self):
        cleaned_data = deepcopy(self.get_best_case_answers())
        other_observation = AbnormalFootAppearanceObservations.objects.filter(name=OTHER)

        for foot in ["right_foot", "left_foot"]:
            field = f"normal_appearance_{foot}"
            m2m_field = f"abnormal_obs_{foot}"
            m2m_field_other = f"{m2m_field}_other"

            with self.subTest(
                f"Testing '{m2m_field_other}' required if {m2m_field}={other_observation}",
                field=field,
                m2m_field=m2m_field,
                m2m_field_other=m2m_field_other,
            ):
                # Select 'other', then test it's required
                cleaned_data.update({field: NO, m2m_field: other_observation})
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertIn(m2m_field_other, form_validator._errors)
                self.assertIn(
                    "This field is required",
                    str(form_validator._errors.get(m2m_field_other)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

                # Complete 'other' field, and move onto next test
                cleaned_data.update({m2m_field_other: "Some other value"})

    def test_other_field_not_required_if_other_not_specified(self):
        cleaned_data = self.get_best_case_answers()
        non_other_observation = AbnormalFootAppearanceObservations.objects.filter(
            name="infection"
        )

        for foot in ["right_foot", "left_foot"]:
            field = f"normal_appearance_{foot}"
            m2m_field = f"abnormal_obs_{foot}"
            m2m_field_other = f"{m2m_field}_other"

            with self.subTest(
                f"Testing '{m2m_field_other}' completed when not required",
                field=field,
                m2m_field=m2m_field,
                m2m_field_other=m2m_field_other,
            ):
                # Try with normal foot appearance
                cleaned_data.update({field: YES, m2m_field_other: "Some other value"})
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertIn(m2m_field_other, form_validator._errors)
                self.assertIn(
                    "This field is not required",
                    str(form_validator._errors.get(m2m_field_other)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

                # Try with abnormal foot appearance, and non-'other' observation
                cleaned_data.update(
                    {
                        field: NO,
                        m2m_field: non_other_observation,
                        m2m_field_other: "Some other value",
                    }
                )
                form_validator = self.validate_form_validator(cleaned_data)
                self.assertIn(m2m_field_other, form_validator._errors)
                self.assertIn(
                    "This field is not required",
                    str(form_validator._errors.get(m2m_field_other)),
                )
                self.assertEqual(len(form_validator._errors), 1, form_validator._errors)

                # Remove 'other' field value, make valid and move onto next test
                del cleaned_data[m2m_field]
                del cleaned_data[m2m_field_other]
                cleaned_data.update({field: YES})
