from semantic_kernel.functions import (
    kernel_function
)


class RequirementPlugin:

    @kernel_function(
        description="Extract requirements"
    )
    def extract_requirements(
        self,
        user_requirement: str
    ) -> str:

        return (
            f"Requirements extracted from: "
            f"{user_requirement}"
        )