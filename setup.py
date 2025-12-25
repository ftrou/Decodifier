from setuptools import setup, find_packages

setup(
    name="decodifier",
    version="0.1.0",
    description="Local-first LLM tooling engine for code projects",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn[standard]",
        "pydantic",
        "python-multipart",
        "watchdog",
        "sqlalchemy",
        "chromadb",
        "python-dotenv",
        "sentence-transformers",
        "unidiff",
        "pyyaml",
        "requests",
    ],
    python_requires=">=3.10",
)
