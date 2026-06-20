from semantic_kernel import Kernel

from experiments.requirement_plugin import (
    RequirementPlugin
)

kernel = Kernel()

kernel.add_plugin(
    RequirementPlugin(),
    plugin_name="RequirementPlugin"
)

plugin = kernel.plugins["RequirementPlugin"]

function = plugin["extract_requirements"]

print(type(function))
print(function)


print("Semantic Kernel Created Successfully")

print(kernel.plugins)