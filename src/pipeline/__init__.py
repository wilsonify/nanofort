import os

sink_host = os.getenv("PIPELINE_SINK_HOST", "127.0.0.1")
sink_port = os.getenv("PIPELINE_SINK_PORT", "5558")

vent_host = os.getenv("PIPELINE_VENT_PORT", "127.0.0.1")
vent_port = os.getenv("PIPELINE_VENT_PORT", "5557")

sink_addr = f"tcp://{sink_host}:{sink_port}"
vent_addr = f"tcp://{vent_host}:{vent_port}"
