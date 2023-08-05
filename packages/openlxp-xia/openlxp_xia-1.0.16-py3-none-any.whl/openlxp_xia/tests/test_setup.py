from uuid import UUID

from django.test import TestCase


class TestSetUp(TestCase):
    """Class with setup and teardown for tests in XIS"""

    def setUp(self):
        """Function to set up necessary data for testing"""

        # globally accessible data sets
        self.source_metadata = {
            "Test": "0",
            "Test_id": "2146",
            "Test_url": "https://example.test.com/",
            "End_date": "9999-12-31T00:00:00-05:00",
            "test_name": "test name",
            "Start_date": "2017-03-28T00:00:00-04:00",
            "KEY": "TestData 123",
            "SOURCESYSTEM": "AGENT",
            "test_description": "test description",
            "supplemental_data": "sample1"
        }
        self.key_value = "TestData 123_AGENT"
        self.key_value_hash = "d2a7f8cc5d5484a4dde099c6a21a903a"
        self.hash_value = "f454114ba41034e14df2a8f3c14a047d"

        self.target_metadata = {
            "Course": {
                "CourseCode": "TestData 123",
                "CourseTitle": "Acquisition Law",
                "CourseAudience": "test_data",
                "DepartmentName": "",
                "CourseObjective": "test_data",
                "CourseShortDescription": "test description",
                "CourseProviderName": "AGENT",
                "CourseSpecialNotes": "test_data",
                "CoursePrerequisites": "None",
                "EstimatedCompletionTime": "4.5 days",
                "CourseSectionDeliveryMode": "Resident",
                "CourseAdditionalInformation": "None"
            },
            "CourseInstance": {
                "CourseURL": "https://agent.tes.com/ui/lms-learning-details"
            },
            "General_Information": {
                "EndDate": "end_date",
                "StartDate": "start_date"
            }
        }

        self.target_key_value = "TestData 123_AGENT"
        self.target_key_value_hash = "d2a7f8cc5d5484a4dde099c6a21a903a"
        self.target_hash_value = "eaf3e57b7f21b4d813f1258fb4ebf89d"

        self.xia_data = {
            'metadata_record_uuid': UUID(
                '09edea0e-6c83-40a6-951e-2acee3e99502'),
            'target_metadata': {
                "Course": {
                    "CourseCode": "TestData 123",
                    "CourseTitle": "Acquisition Law",
                    "CourseAudience": "test_data",
                    "DepartmentName": "",
                    "CourseObjective": "test_data",
                    "CourseDescription": "test_data",
                    "CourseProviderName": "AGENT",
                    "CourseSpecialNotes": "test_data",
                    "CoursePrerequisites": "None",
                    "EstimatedCompletionTime": "4.5 days",
                    "CourseSectionDeliveryMode": "Resident",
                    "CourseAdditionalInformation": "None"
                },
                "CourseInstance": {
                    "CourseURL":
                        "https://agent.tes.com/ui/lms-learning-details"
                },
                "General_Information": {
                    "EndDate": "end_date",
                    "StartDate": "start_date"
                }
            },
            'target_metadata_hash': 'df0b51d7b45ca29682e930d236963584',
            'target_metadata_key': 'TestData 123_AGENT',
            'target_metadata_key_hash': 'd2a7f8cc5d5484a4dde099c6a21a903a'
        }
        self.xis_expected_data = {
            'unique_record_identifier': UUID(
                '09edea0e-6c83-40a6-951e-2acee3e99502'),
            'metadata': {
                "Course": {
                    "CourseCode": "TestData 123",
                    "CourseTitle": "Acquisition Law",
                    "CourseAudience": "test_data",
                    "DepartmentName": "",
                    "CourseObjective": "test_data",
                    "CourseDescription": "test_data",
                    "CourseProviderName": "AGENT",
                    "CourseSpecialNotes": "test_data",
                    "CoursePrerequisites": "None",
                    "EstimatedCompletionTime": "4.5 days",
                    "CourseSectionDeliveryMode": "Resident",
                    "CourseAdditionalInformation": "None"
                },
                "CourseInstance": {
                    "CourseURL":
                        "https://agent.tes.com/ui/lms-learning-details"
                },
                "General_Information": {
                    "EndDate": "end_date",
                    "StartDate": "start_date"
                }
            },
            'metadata_hash': 'df0b51d7b45ca29682e930d236963584',
            'metadata_key': 'TestData 123_AGENT',
            'metadata_key_hash': 'd2a7f8cc5d5484a4dde099c6a21a903a',
            'provider_name': 'AGENT'
        }

        self.xis_supplemental_expected_data = {
            'unique_record_identifier': UUID(
                '09edea0e-6c83-40a6-951e-2acee3e99502'),
            'metadata': {
                "Field1": "ABC",
                "Field2": "123",
                "Field3": "ABC-123"
            },
            'metadata_hash': 'df0b51d7b45ca29682e930d236963584',
            'metadata_key': 'TestData 123_AGENT',
            'metadata_key_hash':
                '6acf7689ea81a1f792e7668a23b1acf5',
            'provider_name': 'AGENT'
        }

        self.xia_supplemental_data = {
            'metadata_record_uuid': UUID(
                '09edea0e-6c83-40a6-951e-2acee3e99502'),
            'supplemental_metadata': {
                "Field1": "ABC",
                "Field2": "123",
                "Field3": "ABC-123"
            },
            'supplemental_metadata_hash': 'df0b51d7b45ca29682e930d236963584',
            'supplemental_metadata_key': 'TestData 123_AGENT',
            'supplemental_metadata_key_hash':
                '6acf7689ea81a1f792e7668a23b1acf5'
        }

        self.xis_supplemental_expected_data = {
            'unique_record_identifier': UUID(
                '09edea0e-6c83-40a6-951e-2acee3e99502'),
            'metadata': {
                "Field1": "ABC",
                "Field2": "123",
                "Field3": "ABC-123"
            },
            'metadata_hash': 'df0b51d7b45ca29682e930d236963584',
            'metadata_key': 'TestData 123_AGENT',
            'metadata_key_hash':
                '6acf7689ea81a1f792e7668a23b1acf5',
            'provider_name': 'AGENT'
        }

        self.metadata_invalid = {
            "Test": "0",
            "Test_id": "2146",
            "Test_url": "https://example.test.com/",
            "End_date": "9999-12-31T00:00:00-05:00",
            "test_name": "",
            "Start_date": "",
            "KEY": "TestData 1234",
            "SOURCESYSTEM": "AGENT",
            "test_description": "test description",
        }
        self.key_value_invalid = "TestData 1234_AGENT"
        self.key_value_hash_invalid = "eaf3e57b7f21b4d813f1258fb4ebf89d"
        self.hash_value_invalid = "d9eccc6651c0b95db975aca43fa9b481"

        self.target_metadata_invalid = {
            "Course": {
                "CourseCode": "TestData 1234",
                "CourseTitle": "Acquisition Law",
                "CourseAudience": "test_data",
                "DepartmentName": "",
                "CourseObjective": "test_data",
                "CourseDescription": "",
                "CourseProviderName": "AGENT",
                "CourseSpecialNotes": "test_data",
                "CoursePrerequisites": "None",
                "EstimatedCompletionTime": "4.5 days",
                "CourseSectionDeliveryMode": "Resident",
                "CourseAdditionalInformation": "None"
            },
            "CourseInstance": {
                "CourseURL": "https://agent.tes.com/ui/lms-learning-details"
            },
            "General_Information": {
                "EndDate": "end_date",
                "StartDate": "start_date"
            }
        }

        self.target_key_value_invalid = "TestData 1234_AGENT"
        self.target_key_value_hash_invalid = "d9eccc6651c0b95db975aca43fa9b481"
        self.target_hash_value_invalid = "eaf3e57b7f21b4d813f1258fb4ebf89d"

        self.source_target_mapping = {
            "Course": {
                "CourseProviderName": "SOURCESYSTEM",
                "DepartmentName": "",
                "CourseCode": "KEY",
                "CourseTitle": "test_name",
                "CourseDescription": "test_description",
                "CourseAudience": "test_attendies",
                "CourseSectionDeliveryMode": "test_mode",
                "CourseObjective": "test_objective",
                "CoursePrerequisites": "test_prerequisite",
                "EstimatedCompletionTime": "test_length",
                "CourseSpecialNotes": "test_notes",
                "CourseAdditionalInformation": "test_postscript"
            },
            "CourseInstance": {
                "CourseURL": "test_url"
            },
            "General_Information": {
                "StartDate": "start_date",
                "EndDate": "end_date"
            }
        }

        self.schema_data_dict = {
            'SOURCESYSTEM': 'Required',
            'test_id': 'Optional',
            'KEY': 'Required',
            'test_name': 'Required',
            'test_description': 'Required',
            'test_objective': 'Optional',
            'test_attendies': 'Optional',
            'test_images': 'Optional',
            'test1_id': 'Optional',
            'test_url': 'Optional',
            'Start_date': 'Required',
            'End_date': 'Required',
            'Test_current': 'Recommended'
        }

        self.target_data_dict = {
            'Course': {
                'CourseProviderName': 'Required',
                'DepartmentName': 'Optional',
                'CourseCode': 'Required',
                'CourseTitle': 'Required',
                'CourseDescription': 'Required',
                'CourseShortDescription': 'Required',
                'CourseFullDescription': 'Optional',
                'CourseAudience': 'Optional',
                'CourseSectionDeliveryMode': 'Optional',
                'CourseObjective': 'Optional',
                'CoursePrerequisites': 'Optional',
                'EstimatedCompletionTime': 'Optional',
                'CourseSpecialNotes': 'Optional',
                'CourseAdditionalInformation': 'Optional',
                'CourseURL': 'Optional',
                'CourseLevel': 'Optional',
                'CourseSubjectMatter': 'Required'
            },
            'CourseInstance': {
                'CourseCode': 'Required',
                'CourseTitle': 'Required',
                'Thumbnail': 'Recommended',
                'CourseShortDescription': 'Optional',
                'CourseFullDescription': 'Optional',
                'CourseURL': 'Optional',
                'StartDate': 'Required',
                'EndDate': 'Required',
                'EnrollmentStartDate': 'Optional',
                'EnrollmentEndDate': 'Optional',
                'DeliveryMode': 'Required',
                'InLanguage': 'Optional',
                'Instructor': 'Required',
                'Duration': 'Optional',
                'CourseLearningOutcome': 'Optional',
                'CourseLevel': 'Optional',
                'InstructorBio': 'Optional'
            },
            'General_Information': {
                'StartDate': 'Required',
                'EndDate': 'Required'
            },
            'Technical_Information': {
                'Thumbnail': 'Recommended'
            }
        }

        self.test_target_required_column_names = {
            'Course.CourseCode',
            'Course.CourseProviderName',
            'Course.CourseShortDescription'}
        self.recommended_column_name = {'Technical_Information.Thumbnail',
                                        'CourseInstance.Thumbnail'}

        self.xis_api_endpoint_url = 'http://openlxp-xis:8020/api/metadata/'

        self.supplemental_api_endpoint = 'http://openlxp-xis:8020' \
                                         '/api/supplemental-data/'

        self.test_required_column_names = ['SOURCESYSTEM',
                                           'KEY',
                                           'Start_date', 'End_date']

        self.test_metadata_column_list = [["Test", "Test_id", "Test_url"]]

        self.source_metadata_with_supplemental = {
            "Test": "0",
            "Test_id": "2146",
            "Test_url": "https://example.test.com/",
            "supplemental_data1": "sample1",
            "supplemental_data2": "sample2",
            # check removal of null values from
            "supplemental_data3": "",
        }

        self.supplemental_data = {
            "supplemental_data1": "sample1",
            "supplemental_data2": "sample2"
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
