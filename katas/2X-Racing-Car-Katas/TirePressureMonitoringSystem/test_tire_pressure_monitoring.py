from tire_pressure_monitoring import Alarm, Sensor
from unittest.mock import patch
import unittest


class AlarmTest(unittest.TestCase):
    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        assert not alarm.is_alarm_on

    @patch.object(Sensor, 'pop_next_pressure_psi_value')
    def test_if_alarm_is_on(self, patched_pop_next_pressure_psi_value):
        patched_pop_next_pressure_psi_value.return_value = 100
        alarm = Alarm()
        alarm.check()
        assert alarm.is_alarm_on

    def test_if_alarm_is_off(self):
        alarm = Alarm()
        with patch.object(Sensor, 'pop_next_pressure_psi_value', return_value=20) as fetch_pressure:
            alarm.check()
            assert not alarm.is_alarm_on
        fetch_pressure.assert_called_once()

