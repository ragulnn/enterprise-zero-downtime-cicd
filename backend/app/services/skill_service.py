from app.models.skill import Skill


def get_skills():

    return [

        Skill(
            category="Cloud",
            name="Microsoft Azure",
            level="Intermediate"
        ),

        Skill(
            category="Containers",
            name="Docker",
            level="Intermediate"
        ),

        Skill(
            category="Containers",
            name="Kubernetes",
            level="Intermediate"
        ),

        Skill(
            category="Infrastructure",
            name="Terraform",
            level="Intermediate"
        ),

        Skill(
            category="CI/CD",
            name="Azure DevOps",
            level="Intermediate"
        ),

        Skill(
            category="Operating System",
            name="Linux",
            level="Intermediate"
        ),

        Skill(
            category="Programming",
            name="Python",
            level="Intermediate"
        )
    ]

