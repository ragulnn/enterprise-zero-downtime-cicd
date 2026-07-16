from app.backend.models.profile import Profile


def get_profile() -> Profile:
    return Profile(
        name="Ragul M",
        title="Cloud & DevOps Engineer",
        location="Tamil Nadu, India",
        summary="Passionate about Azure, Kubernetes, Terraform, Docker and DevOps automation.",
        skills=[
            "Azure",
            "Docker",
            "Kubernetes",
            "Terraform",
            "Azure DevOps",
            "Linux",
            "Python"
        ]
    )
