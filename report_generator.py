from constants import *
from analytics_grabber import grab_analytics
import uuid # Custom ID for every report, don't overwrite old ones.

def write_report() -> None:
    use_uuid = uuid.uuid4()
    report_path = f"./report_{use_uuid}.txt"

    with open(report_path, 'a') as file:
        file.write('')