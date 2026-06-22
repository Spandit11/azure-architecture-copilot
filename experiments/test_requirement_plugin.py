from semantic_kernel import Kernel

from experiments.requirement_plugin_v2 import (
    RequirementPlugin
)

kernel = Kernel()

kernel.add_plugin(
    RequirementPlugin(),
    plugin_name="RequirementPlugin"
)

print("Plugin Registered Successfully")

print(kernel.plugins)

plugin = kernel.plugins["RequirementPlugin"]

function = plugin["extract_requirements"]

print(type(function))

print(dir(function))