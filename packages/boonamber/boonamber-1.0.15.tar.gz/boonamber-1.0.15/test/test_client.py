import csv
import os
import nose
import time
from nose.tools import assert_equal
from nose.tools import assert_true
from nose.tools import assert_raises
from nose.tools import assert_is_instance
from boonamber import AmberClient, AmberUserError, AmberCloudError

TEST_SENSOR_ID = '0e3acc64e8e069e1'


def env_check():
    global saved_amber_password
    saved_amber_password = os.environ.get('AMBER_PASSWORD')
    assert saved_amber_password != None, "must set AMBER_PASSWORD in environment"


class Test1Init:

    def __init__(self):
        # first test class will do an environment test
        env_check()

    def unset_environment_variables(self):
        os.environ['AMBER_PASSWORD'] = ''
        os.environ['AMBER_LICENSE_FILE'] = ''
        os.environ['AMBER_LICENSE_ID'] = ''
        os.environ['AMBER_USERNAME'] = ''
        os.environ['AMBER_PASSWORD'] = ''
        os.environ['AMBER_SERVER'] = ''

    def test_01_init(self):
        self.unset_environment_variables()

        # set credentials using license file
        amber = AmberClient(license_id="default", license_file="test.Amber.license")

        # set credentials using license file specified via environment variables
        os.environ['AMBER_LICENSE_FILE'] = "test.Amber.license"
        os.environ['AMBER_LICENSE_ID'] = "default"
        amber = AmberClient(license_id=None, license_file=None)

        # set credentials directly using environment variables
        os.environ['AMBER_USERNAME'] = "amber-test-user"
        os.environ['AMBER_PASSWORD'] = "filler-password"
        os.environ['AMBER_SERVER'] = "https:#amber-local.boonlogic.com/dev"
        amber = AmberClient(license_id=None, license_file=None)

        self.unset_environment_variables()

    def test__02_init_negative(self):
        self.unset_environment_variables()
        assert_raises(AmberUserError, AmberClient, "default", "nonexistent-license-file")
        assert_raises(AmberUserError, AmberClient, "nonexistent-license-id", "test.Amber.license")
        assert_raises(AmberUserError, AmberClient, "missing-username", "test.Amber.license")
        assert_raises(AmberUserError, AmberClient, "missing-password", "test.Amber.license")
        assert_raises(AmberUserError, AmberClient, "missing-server", "test.Amber.license")


class Test2Auth:

    def __init__(self):
        os.environ['AMBER_PASSWORD'] = saved_amber_password

    def test__01_authenticate(self):
        os.environ['AMBER_PASSWORD'] = saved_amber_password
        amber = AmberClient(license_file="test.Amber.license")
        result = amber._authenticate()

    def test__02_authenticate_negative(self):
        self.amber = AmberClient(license_id="garbage", license_file="test.Amber.license")
        with assert_raises(AmberCloudError) as context:
            self.amber._authenticate()
        assert_equal(context.exception.code, 401)


class Test5Endpoints:

    def __init__(self):
        os.environ['AMBER_PASSWORD'] = saved_amber_password
        self.amber = AmberClient(license_file="test.Amber.license")

    def setup_created_sensor(self):
        try:
            sensor_id = self.amber.create_sensor('test-sensor')
        except Exception as e:
            raise RuntimeError("setup failed: {}".format(e))
        self.sensor_id = sensor_id

    def teardown_created_sensor(self, sensor_id):
        try:
            self.amber.delete_sensor(sensor_id)
        except Exception as e:
            raise RuntimeError("teardown failed, sensor was not deleted: {}".format(e))

    def test_01_create_sensor(self):
        sensor_id = self.amber.create_sensor('test-sensor')
        self.teardown_created_sensor(sensor_id)

    def test_02_delete_sensor(self):
        self.setup_created_sensor()
        self.amber.delete_sensor(self.sensor_id)

    def test_03_delete_sensor_negative(self):
        with assert_raises(AmberCloudError) as context:
            self.amber.delete_sensor('nonexistent-sensor-id')
        assert_equal(context.exception.code, 404)

    def test_04_update_label(self):
        label = self.amber.update_label(TEST_SENSOR_ID, 'new-label')
        assert_equal(label, 'new-label')

        try:
            self.amber.update_label(TEST_SENSOR_ID, 'test-sensor')
        except Exception as e:
            raise RuntimeError("teardown failed, label was not changed back to 'test-sensor': {}".format(e))

    def test_05_update_label_negative(self):
        with assert_raises(AmberCloudError) as context:
            label = self.amber.update_label('nonexistent-sensor-id', 'test-sensor')
        assert_equal(context.exception.code, 404)

    def test_06_get_sensor(self):
        expected = {
            'label': 'test-sensor',
            'sensorId': TEST_SENSOR_ID,
            'tenantId': 'amber-test-user'
        }
        sensor = self.amber.get_sensor(TEST_SENSOR_ID)
        assert_equal(sensor['label'], 'test-sensor')
        assert_equal(sensor['sensorId'], TEST_SENSOR_ID)
        assert_true('usageInfo' in sensor)

    def test_07_get_sensor_negative(self):
        with assert_raises(AmberCloudError) as context:
            sensor = self.amber.get_sensor('nonexistent-sensor-id')
        assert_equal(context.exception.code, 404)

    def test_08_list_sensors(self):
        sensors = self.amber.list_sensors()
        assert_true(TEST_SENSOR_ID in sensors.keys())

    def test_09_configure_sensor(self):
        expected = {
            'anomalyHistoryWindow': 0,
            'featureCount': 1,
            'streamingWindowSize': 25,
            'samplesToBuffer': 1000,
            'anomalyHistoryWindow': 1000,
            'learningRateNumerator': 10,
            'learningRateDenominator': 10000,
            'learningMaxClusters': 1000,
            'learningMaxSamples': 1000000,
        }
        config = self.amber.configure_sensor(TEST_SENSOR_ID, feature_count=1, streaming_window_size=25,
                                             samples_to_buffer=1000,
                                             anomaly_history_window=1000,
                                             learning_rate_numerator=10,
                                             learning_rate_denominator=10000,
                                             learning_max_clusters=1000,
                                             learning_max_samples=1000000)
        assert_equal(config, expected)

    def test_10_configure_sensor_negative(self):
        with assert_raises(AmberCloudError) as context:
            config = self.amber.configure_sensor('nonexistent-sensor-id')
        assert_equal(context.exception.code, 404)

        # invalid feature_count or streaming_window_size
        assert_raises(AmberUserError, self.amber.configure_sensor, TEST_SENSOR_ID, feature_count=-1)
        assert_raises(AmberUserError, self.amber.configure_sensor, TEST_SENSOR_ID, feature_count=1.5)
        assert_raises(AmberUserError, self.amber.configure_sensor, TEST_SENSOR_ID, streaming_window_size=-1)
        assert_raises(AmberUserError, self.amber.configure_sensor, TEST_SENSOR_ID, streaming_window_size=1.5)

    def test_11_get_config(self):
        expected = {
            'anomalyHistoryWindow': 0,
            'featureCount': 1,
            'streamingWindowSize': 25,
            'samplesToBuffer': 1000,
            'anomalyHistoryWindow': 1000,
            'learningRateNumerator': 10,
            'learningRateDenominator': 10000,
            'learningMaxClusters': 1000,
            'learningMaxSamples': 1000000,
            'percentVariation': 0.05,
            'features': [{'minVal': 0, 'maxVal': 1}]
        }
        config = self.amber.get_config(TEST_SENSOR_ID)
        assert_equal(config, expected)

    def test_12_get_config_negative(self):
        with assert_raises(AmberCloudError) as context:
            config = self.amber.get_config('nonexistent-sensor-id')
        assert_equal(context.exception.code, 404)

    def test_13_stream_sensor(self):
        results = self.amber.stream_sensor(TEST_SENSOR_ID, 1)
        assert_true('state' in results)
        assert_true('message' in results)
        assert_true('progress' in results)
        assert_true('clusterCount' in results)
        assert_true('retryCount' in results)
        assert_true('streamingWindowSize' in results)
        assert_true('SI' in results)
        assert_true('AD' in results)
        assert_true('AH' in results)
        assert_true('AM' in results)
        assert_true('AW' in results)
        print(results['state'])

        # scalar data should return SI of length 1
        assert_true(len(results['SI']) == 1)

        # array data should return SI of same length
        results = self.amber.stream_sensor(TEST_SENSOR_ID, [1, 2, 3, 4, 5])
        assert_true(len(results['SI']) == 5)

    def test_14_stream_sensor_negative(self):
        with assert_raises(AmberCloudError) as context:
            results = self.amber.stream_sensor('nonexistent-sensor-id', [1, 2, 3, 4, 5])
        assert_equal(context.exception.code, 404)

        # invalid data
        assert_raises(AmberUserError, self.amber.stream_sensor, TEST_SENSOR_ID, [])
        assert_raises(AmberUserError, self.amber.stream_sensor, TEST_SENSOR_ID, [1, '2', 3])
        assert_raises(AmberUserError, self.amber.stream_sensor, TEST_SENSOR_ID, [1, [2, 3], 4])

    def test_15_get_root_cause(self):
        config = self.amber.get_config(TEST_SENSOR_ID)
        expected = [[0] * len(config['features']) * config['streamingWindowSize']] * 2
        config = self.amber.get_root_cause(TEST_SENSOR_ID, pattern_list=[[1] * len(config['features']) * config['streamingWindowSize'], [0] * len(config['features']) * config['streamingWindowSize']])
        assert_equal(config, expected)

    def test_16_get_root_cause_negative(self):
        with assert_raises(AmberCloudError) as context:
            config = self.amber.get_root_cause('nonexistent-sensor-id', id_list=[1])
        assert_equal(context.exception.code, 404)

        # give both fail
        with assert_raises(AmberUserError) as context:
            config = self.amber.get_root_cause(TEST_SENSOR_ID, id_list=[1], pattern_list=[[1,2,3],[4,5,6]])

        # give neither fail
        with assert_raises(AmberUserError) as context:
            config = self.amber.get_root_cause(TEST_SENSOR_ID)

        assert_raises(AmberCloudError, self.amber.get_root_cause, TEST_SENSOR_ID, [1])

    def test_17_get_status(self):
        status = self.amber.get_status(TEST_SENSOR_ID)
        assert_true('pca' in status)
        assert_true('numClusters' in status)

    def test_18_get_status_negative(self):
        with assert_raises(AmberCloudError) as context:
            status = self.amber.get_status('nonexistent-sensor-id')
        assert_equal(context.exception.code, 404)

    def test_19_get_pretrain_state(self):
        response = self.amber.get_pretrain_state(TEST_SENSOR_ID)
        assert_true('state' in response)
        assert_equal(response['state'], 'None')

    def test_20_get_pretrain_state_negative(self):
        with assert_raises(AmberCloudError) as context:
            response = self.amber.get_pretrain_state('nonexistent-sensor-id')
        assert_equal(context.exception.code, 404)

    def test_21_pretrain_sensor(self):
        with open('output_current.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            data = []
            for row in csv_reader:
                for d in row:
                    data.append(float(d))

        results = self.amber.pretrain_sensor(TEST_SENSOR_ID, data, block=True)
        assert_equal(results['state'], 'Pretrained')

        results = self.amber.pretrain_sensor(TEST_SENSOR_ID, data, block=False)
        assert_equal(results['state'], 'Pretraining')
        while True:
            time.sleep(5)
            results = self.amber.get_pretrain_state(TEST_SENSOR_ID)
            if results['state'] == 'Pretraining':
                continue
            else:
                break
        assert_equal(results['state'], 'Pretrained')

    def test_22_pretrain_sensor_negative(self):
        with assert_raises(AmberCloudError) as context:
            response = self.amber.pretrain_sensor('nonexistent-sensor-id', [1, 2, 3, 4, 5], block=True)
        assert_equal(context.exception.code, 404)

        # not enough data to fill sample buffer
        with assert_raises(AmberCloudError) as context:
            response = self.amber.pretrain_sensor(TEST_SENSOR_ID, [1, 2, 3, 4, 5], block=True)
        assert_equal(context.exception.code, 400)



class Test3APICall:

    def __init__(self):
        env_check()

    def setUp(self):
        self.amber = AmberClient(license_file="test.Amber.license")
        self.amber.password = os.environ['AMBER_PASSWORD']

        self.server = self.amber.server
        self.headers = {
            'Content-Type': 'application/json',
        }

    def test_api_call(self):
        # first call covers reauth case, second call covers no reauth case
        self.amber._api_call('GET', self.server + '/sensors', self.headers)
        self.amber._api_call('GET', self.server + '/sensors', self.headers)

    def test_api_call_negative(self):
        # call that fails due to a garbage internal token
        self.amber.reauth_time = time.time() + 60
        self.amber.token = 'garbage-token'
        assert_raises(AmberCloudError, self.amber._api_call, 'GET', self.server + '/sensors', self.headers)


class Test4DataHandling:

    def __init__(self):
        env_check()

    def setUp(self):
        self.amber = AmberClient(license_file="test.Amber.license")

    def test_convert_to_csv(self):
        # valid scalar inputs
        assert_equal("1.0", self.amber._convert_to_csv(1))
        assert_equal("1.0", self.amber._convert_to_csv(1.0))

        # valid 1d inputs
        assert_equal("1.0,2.0,3.0", self.amber._convert_to_csv([1, 2, 3]))
        assert_equal("1.0,2.0,3.0", self.amber._convert_to_csv([1, 2, 3.0]))
        assert_equal("1.0,2.0,3.0", self.amber._convert_to_csv([1.0, 2.0, 3.0]))

        # valid 2d inputs
        assert_equal("1.0,2.0,3.0,4.0", self.amber._convert_to_csv([[1, 2], [3, 4]]))
        assert_equal("1.0,2.0,3.0,4.0", self.amber._convert_to_csv([[1, 2, 3, 4]]))
        assert_equal("1.0,2.0,3.0,4.0", self.amber._convert_to_csv([[1], [2], [3], [4]]))
        assert_equal("1.0,2.0,3.0,4.0", self.amber._convert_to_csv([[1, 2], [3, 4.0]]))
        assert_equal("1.0,2.0,3.0,4.0", self.amber._convert_to_csv([[1.0, 2.0], [3.0, 4.0]]))

    def test_convert_to_csv_negative(self):
        # empty data
        assert_raises(ValueError, self.amber._convert_to_csv, [])
        assert_raises(ValueError, self.amber._convert_to_csv, [[]])
        assert_raises(ValueError, self.amber._convert_to_csv, [[], []])

        # non-numeric data
        assert_raises(ValueError, self.amber._convert_to_csv, None)
        assert_raises(ValueError, self.amber._convert_to_csv, 'a')
        assert_raises(ValueError, self.amber._convert_to_csv, 'abc')
        assert_raises(ValueError, self.amber._convert_to_csv, [1, None, 3])
        assert_raises(ValueError, self.amber._convert_to_csv, [1, 'a', 3])
        assert_raises(ValueError, self.amber._convert_to_csv, [1, 'abc', 3])
        assert_raises(ValueError, self.amber._convert_to_csv, [[1, None], [3, 4]])
        assert_raises(ValueError, self.amber._convert_to_csv, [[1, 'a'], [3, 4]])
        assert_raises(ValueError, self.amber._convert_to_csv, [[1, 'abc'], [3, 4]])

        # badly-shaped data
        assert_raises(ValueError, self.amber._convert_to_csv, [1, [2, 3], 4])            # mixed nesting
        assert_raises(ValueError, self.amber._convert_to_csv, [[1, 2], [3, 4, 5]])       # ragged array
        assert_raises(ValueError, self.amber._convert_to_csv, [[[1, 2, 3, 4]]])          # nested too deep
        assert_raises(ValueError, self.amber._convert_to_csv, [[[1], [2], [3], [4]]])


if __name__ == '__main__':
    argv = ['nosetests', '--verbosity=2']
    nose.run(defaultTest=__name__ + ':Test1Init', argv=argv)
    nose.run(defaultTest=__name__ + ':Test2Auth', argv=argv)
    nose.run(defaultTest=__name__ + ':Test3APICall', argv=argv)
    nose.run(defaultTest=__name__ + ':Test4DataHandling', argv=argv)
    nose.run(defaultTest=__name__ + ':Test5Endpoints', argv=argv)
