from semantic_kernel import Kernel

from experiments.service_plugin_v2 import (
    ServicePlugin
)

kernel = Kernel()

kernel.add_plugin(
    ServicePlugin(),
    plugin_name="ServicePlugin"
)

print("Plugin Registered Successfully")

print(kernel.plugins)