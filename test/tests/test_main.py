import os
import time
import pytest
from resources.testdata.test_data import TestData as td
from ..pages.home_page import HomePage
from ..utils import parquet_utils
from ..utils.compare_utils import DataCompareDBUtils
from resources.testdata.schemas import (synergynettopology, softwareversion, devicestatus, metrics,
                                        eameshtopology, readingdefinitions, systemsettings, electrictopology,
                                        eventdefinition, firmware, activealarm, blinkinterval, readingdefinitions,
                                        device, reading, readingdefinitions_interval, readingdefinition_pqm,
                                        readingdefnition_intrumentation, sessionstatistics, metricdefinition, event,
                                        job)
from resources.testdata import sel_bronze_queries_01 as sbqu
from ..utils.cluster_utils import Cluster
from resources.testdata import sel_silver_queries_02 as ssqu
from resources.testdata import sel_quarantine_queries_03 as sequ
from resources.testdata import sel_bronze_transf_queries_04 as btqu
from resources.testdata import trunc_bronze_queries_05 as tbqu
from resources.testdata import trunc_silver_queries_06 as tsqu
from resources.testdata import trunc_quarantine_queries_07 as tqqu


@pytest.fixture(scope="class")
def driver(browser):
    driver_instance = HomePage(browser)
    return driver_instance


@pytest.fixture(scope="class")
def db_connect(databricks_connection):
    # db_instance = DatabricksDBUtils()
    return databricks_connection


class TestLoginPage:
    # @pytest.mark.smoke
    # @pytest.mark.test_marker

    def test_successful_login(self, driver):
        driver.go_to_login_page()
        driver.enter_username(td.VALID_USERNAME)
        driver.click_next_button()
        driver.enter_password(td.VALID_PASSWORD)
        time.sleep(3)
        # driver.click_signin_button()
        time.sleep(20)
        assert driver.is_login_successful() == td.TITLE
        print("login is successful")

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_activate_license(self, driver):
        # self.test_successful_login(driver)
        assert driver.activate_license(td.DURATION, td.REASON)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_truncate_tables(self, db_connect, query):
        val = db_connect.truncate_table(query)
        if val:
            print("Data successfully truncated")
        else:
            print(val)

    # @pytest.mark.smoke
    # @pytest.mark.test_marker
    def test_create_upload_files_in_container(self, driver, schema, data, parquet_file):
        success_file = "success.parquet"
        directory_path = "resources\\testdata\\parquet_files\\"
        parquet_utils.create_parquet_file(data, schema, parquet_file)
        lis = [os.path.join(os.getcwd(), directory_path, parquet_file),
               os.path.join(os.getcwd(), directory_path, success_file)]
        driver.upload_files_in_container(list_of_files=lis)
        # assert

    # @pytest.mark.smoke
    # @pytest.mark.test_marker
    def test_files_successfully_processed(self, driver):
        driver.process_file()

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_compare_parquet_with_bronze_table(self, db_connect, query=None, parquet_file_name=None):
        # print(db_connect.fetch_data(query))
        directory_path = "resources\\testdata\\parquet_files\\"
        parquet_file_path = os.path.join(os.getcwd(), directory_path, parquet_file_name)
        df1 = db_connect.fetch_data_as_dataframe(query)
        df2 = parquet_utils.remove_duplicates_and_fetch_df(parquet_file_path)
        # Compare the dataframes
        comparison_result = DataCompareDBUtils.compare_query_results(df1, df2)
        if comparison_result == 'The query results are identical.':
            print("Dataframes are equal.")
        else:
            print("Dataframes are different.")
            print(comparison_result)

    def test_compare_bronze_silver_tables_result(self, db_connect, query1, query2):
        # Convert query results to DataFrames
        result_df1 = db_connect.fetch_data_as_dataframe(query1)
        result_df2 = db_connect.fetch_data_as_dataframe(query2)
        comparison_result = DataCompareDBUtils.compare_query_results(result_df1, result_df2)
        print(comparison_result)


class TestCases(TestLoginPage):
    #@pytest.mark.smoke
    @pytest.mark.test_marker
    def test_base(self, driver):
        self.test_successful_login(driver)
        self.test_activate_license(driver)

    # @pytest.mark.smoke
    #@pytest.mark.test_marker
    def test_synergynettopology_bronze(self, driver, db_connect):
        sch = synergynettopology.schema
        data = synergynettopology.data
        pq_file = "SynergyNetTopology_2_20230925_120000_001.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.synergynettopology)
        self.test_truncate_tables(db_connect, query=tsqu.synergynettopology)
        self.test_truncate_tables(db_connect, query=tqqu.synergynettopology)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.synergynettopology,
                                                    parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_eameshtopology_bronze(self, driver, db_connect):
        sch = eameshtopology.schema
        data = eameshtopology.data
        pq_file = "EAMeshTopology_2_20231020_120000_001.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.eameshtopology)
        self.test_truncate_tables(db_connect, query=tsqu.eameshtopology)
        self.test_truncate_tables(db_connect, query=tqqu.eameshtopology)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.eameshtopology, parquet_file_name=pq_file)

    @pytest.mark.test_marker
    #@pytest.mark.smoke
    def test_systemsettings_bronze(self, driver, db_connect):
        sch = systemsettings.schema
        data = systemsettings.data
        pq_file = "SystemSettings_2_20231017_120000_001.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.systemsettings)
        self.test_truncate_tables(db_connect, query=tsqu.systemsettings)
        self.test_truncate_tables(db_connect, query=tqqu.systemsettings)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.systemsettings, parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_electritopology_bronze(self, driver, db_connect):
        sch = electrictopology.schema
        data = electrictopology.data
        pq_file = "ElectricityDistributionTopology_2_20231010_120000.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.electrictopology)
        self.test_truncate_tables(db_connect, query=tsqu.electrictopology)
        self.test_truncate_tables(db_connect, query=tqqu.electrictopology)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.electrictopology,
                                                    parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_softwareversion_bronze(self, driver, db_connect):
        sch = softwareversion.schema
        data = softwareversion.data
        pq_file = "SoftwareVersion_20231019_120000_001.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.softwareversion)
        self.test_truncate_tables(db_connect, query=tsqu.softwareversion)
        self.test_truncate_tables(db_connect, query=tqqu.softwareversion)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.softwareversion, parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_readingdefinition_bronze(self, driver, db_connect):
        sch = readingdefinitions.schema
        data = readingdefinitions.data
        pq_file = "ReadingsDefinitions_2_20231012_120000.parquet"  # readingdefinition
        self.test_truncate_tables(db_connect, query=tbqu.readingdefinition)
        self.test_truncate_tables(db_connect, query=tsqu.readingdefinition)
        self.test_truncate_tables(db_connect, query=tqqu.readingdefinition)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.readingdefinition, parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_reading_bronze(self, driver, db_connect):
        sch = reading.schema
        data = reading.data
        pq_file = "Readings_2_20231012_120000.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.reading)
        self.test_truncate_tables(db_connect, query=tsqu.reading)
        self.test_truncate_tables(db_connect, query=tqqu.reading)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.reading, parquet_file_name=pq_file)

    # @pytest.mark.smoke
    # @pytest.mark.test_marker
    def test_devicestatus_bronze(self, driver, db_connect):
        sch = devicestatus.schema
        data = devicestatus.data
        pq_file = "DeviceStatus_2_20231025_120000_001.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.devicestatus)
        self.test_truncate_tables(db_connect, query=tsqu.devicestatus)
        self.test_truncate_tables(db_connect, query=tqqu.devicestatus)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.devicestatus,
                                                    parquet_file_name=pq_file)

    # @pytest.mark.smoke
    # @pytest.mark.test_marker
    def test_firmware_bronze(self, driver, db_connect):
        sch = firmware.schema
        data = firmware.data
        pq_file = "Firmware_2_20231026_120000_001.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.firmware)
        self.test_truncate_tables(db_connect, query=tsqu.firmware)
        self.test_truncate_tables(db_connect, query=tqqu.firmware)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.firmware,
                                                    parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_sessionstatistics_bronze(self, driver, db_connect):
        sch = sessionstatistics.schema
        data = sessionstatistics.data
        pq_file = "SessionStatistics_2_20231026_120000.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.sessionstatistics)
        self.test_truncate_tables(db_connect, query=tsqu.sessionstatistics)
        self.test_truncate_tables(db_connect, query=tqqu.sessionstatistics)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.sessionstatistics,
                                                    parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_eventdefinitions_bronze(self, driver, db_connect):
        sch = eventdefinition.schema
        data = eventdefinition.data
        pq_file = "EventDefinitions_2_20231026_120000.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.eventdefinition)
        self.test_truncate_tables(db_connect, query=tsqu.eventdefinition)
        self.test_truncate_tables(db_connect, query=tqqu.eventdefinition)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.eventdefinition,
                                                    parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_metricdefinitions_bronze(self, driver, db_connect):
        sch = metricdefinition.schema
        data = metricdefinition.data
        pq_file = "MetricDefinitions_2_20231026_120000.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.metricdefinition)
        self.test_truncate_tables(db_connect, query=tsqu.metricdefinition)
        self.test_truncate_tables(db_connect, query=tqqu.metricdefinition)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.metricdefinition,
                                                    parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_metric_bronze(self, driver, db_connect):
        sch = metrics.schema
        data = metrics.data
        pq_file = "Metrics_2_20231030_120000.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.metric)
        self.test_truncate_tables(db_connect, query=tsqu.metric)
        self.test_truncate_tables(db_connect, query=tqqu.metric)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.metric,
                                                    parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_event_bronze(self, driver, db_connect):
        sch = event.schema
        data = event.data
        pq_file = "Events_2_20231031_120000_0001.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.event)
        self.test_truncate_tables(db_connect, query=tsqu.event)
        self.test_truncate_tables(db_connect, query=tqqu.event)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.event,
                                                    parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_activealarm_bronze(self, driver, db_connect):
        sch = activealarm.schema
        data = activealarm.data
        pq_file = "ActiveAlarms_2_20231031_120000_0001.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.activealarm)
        # self.test_truncate_tables(db_connect, query=tsqu.activealarm)
        # self.test_truncate_tables(db_connect, query=tqqu.activealarm)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.activealarm,
                                                    parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_jobs_bronze(self, driver, db_connect):
        sch = job.schema
        data = job.data
        pq_file = "Jobs_2_20231031_120000_0001.parquet"
        self.test_truncate_tables(db_connect, query=tbqu.job)
        # self.test_truncate_tables(db_connect, query=tsqu.activealarm)
        # self.test_truncate_tables(db_connect, query=tqqu.activealarm)
        self.test_create_upload_files_in_container(driver, sch, data, pq_file)
        self.test_files_successfully_processed(driver)
        self.test_compare_parquet_with_bronze_table(db_connect, query=sbqu.job,
                                                    parquet_file_name=pq_file)

    # @pytest.mark.test_marker
    @pytest.mark.smoke
    def test_run_silver_job(self, db_connect):
        db_connect.run_silver_job()

    # @pytest.mark.test_marker
    # @pytest.mark.smoke
    def test_silver_synergynettopology_table(self, db_connect):
        silver = ssqu.synergynettopology
        bronze = btqu.synergynettopology_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_silver_eameshtopology_table(self, db_connect):
        silver = ssqu.eameshtopology
        bronze = btqu.eameshtopology_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    @pytest.mark.smoke
    def test_silver_systemsettings_table(self, db_connect):
        silver = ssqu.systemsettings
        bronze = btqu.systemsettings_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_silver_software_version_new_table(self, db_connect):
        silver = ssqu.softwareversion
        bronze = btqu.softwareversion_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_electrictopology_table(self, db_connect):
        silver = ssqu.electrictopology
        bronze = btqu.electrictopology_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_silver_devicestatus_table(self, db_connect):
        silver = ssqu.devicestatus
        bronze = btqu.devicestatus_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_silver_readingdefinition_table(self, db_connect):
        silver = ssqu.readingdefinition
        bronze = btqu.readingdefinition_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_silver_reading_table(self, db_connect):
        silver = ssqu.reading
        bronze = btqu.reading_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_silver_firmware_table(self, db_connect):
        silver = ssqu.firmware
        bronze = btqu.firmware_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_silver_sessionstatistics_table(self, db_connect):
        silver = ssqu.sessionstatistics
        bronze = btqu.sessionstatistics_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_silver_eventdefinition_table(self, db_connect):
        silver = ssqu.eventdefinition
        bronze = btqu.eventdefinition_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_silver_metricdefinition_table(self, db_connect):
        silver = ssqu.metricdefinition
        bronze = btqu.metricdefinition_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_silver_metric_table(self, db_connect):
        silver = ssqu.metric
        bronze = btqu.metric_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_silver_event_table(self, db_connect):
        silver = ssqu.event
        bronze = btqu.event_p
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=silver)

    # @pytest.mark.smoke
    def test_quarantine_synergynettopology(self, db_connect):
        bronze = btqu.synergynettopology_f
        quarantine = sequ.synergynettopology
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_eameshtopology(self, db_connect):
        bronze = btqu.eameshtopology_f
        quarantine = sequ.eameshtopology
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    @pytest.mark.smoke
    def test_quarantine_systemsettings(self, db_connect):
        bronze = btqu.systemsettings_f
        quarantine = sequ.systemsettings
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_softwareversion(self, db_connect):
        bronze = btqu.softwareversion_f
        quarantine = sequ.softwareversion
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_electrictopology(self, db_connect):
        bronze = btqu.electrictopology_f
        quarantine = sequ.electrictopology
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_readingdefinition(self, db_connect):
        bronze = btqu.readingdefinition_f
        quarantine = sequ.readingdefinition
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_reading(self, db_connect):
        bronze = btqu.reading_f
        quarantine = sequ.reading
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_devicestatus(self, db_connect):
        bronze = btqu.devicestatus_f
        quarantine = sequ.devicestatus
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_firmware(self, db_connect):
        bronze = btqu.firmware_f
        quarantine = sequ.firmware
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_sessionstatistics(self, db_connect):
        bronze = btqu.sessionstatistics_p
        quarantine = sequ.sessionstatistics
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_eventdefinition(self, db_connect):
        bronze = btqu.eventdefinition_f
        quarantine = sequ.eventdefinition
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_metricdefinition(self, db_connect):
        bronze = btqu.metricdefinition_f
        quarantine = sequ.metricdefinition
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_metric(self, db_connect):
        bronze = btqu.metric_f
        quarantine = sequ.metric
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

    # @pytest.mark.smoke
    def test_quarantine_event(self, db_connect):
        bronze = btqu.event_f
        quarantine = sequ.event
        self.test_compare_bronze_silver_tables_result(db_connect, query1=bronze, query2=quarantine)

