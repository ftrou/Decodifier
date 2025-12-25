DECODIFIER_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "decodifier_list_projects",
            "description": "List all DeCodifier projects available on this backend.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "decodifier_create_project",
            "description": "Register a new project by name and path.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Human-friendly name."},
                    "path": {"type": "string", "description": "Absolute path to the project root."},
                    "ignore": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional ignore patterns.",
                    },
                    "id": {"type": "string", "description": "Optional fixed project id."},
                },
                "required": ["name", "path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "decodifier_get_project_tree",
            "description": "Get the file tree for a project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_id": {"type": "string", "description": "Project id."},
                    "max_depth": {
                        "type": "integer",
                        "description": "Maximum depth to return.",
                        "default": 5,
                    },
                },
                "required": ["project_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "decodifier_read_file",
            "description": "Read a text file in a project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_id": {"type": "string", "description": "Project id."},
                    "path": {
                        "type": "string",
                        "description": "Project-relative path to the file (e.g. 'engine/app/main.py').",
                    },
                },
                "required": ["project_id", "path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "decodifier_save_file",
            "description": "Write or overwrite a text file in a project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_id": {"type": "string", "description": "Project id."},
                    "path": {
                        "type": "string",
                        "description": "Project-relative file path to write (e.g. 'scratch/hello.txt').",
                    },
                    "content": {"type": "string", "description": "Full file content to save."},
                },
                "required": ["project_id", "path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "decodifier_upload_file",
            "description": "Upload a binary file to a project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_id": {"type": "string", "description": "Project id."},
                    "path": {"type": "string", "description": "Project-relative file path to write."},
                    "content": {
                        "type": "string",
                        "description": "Raw content (UTF-8) for the uploaded file.",
                    },
                    "filename": {
                        "type": "string",
                        "description": "Optional filename for the upload payload.",
                        "default": "upload.bin",
                    },
                },
                "required": ["project_id", "path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "decodifier_apply_patch",
            "description": "Apply a unified diff patch to a file in a project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_id": {"type": "string", "description": "Project id."},
                    "path": {"type": "string", "description": "Project-relative file path."},
                    "patch": {"type": "string", "description": "Unified diff patch text."},
                },
                "required": ["project_id", "path", "patch"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "decodifier_list_packs",
            "description": "List available tool packs.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "decodifier_enable_packs_for_project",
            "description": "Enable a list of packs for a project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_id": {"type": "string", "description": "Project id."},
                    "packs": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Pack ids to enable.",
                    },
                },
                "required": ["project_id", "packs"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "decodifier_get_pack_specs_for_project",
            "description": "Get tool specs for packs enabled on a project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_id": {"type": "string", "description": "Project id."},
                },
                "required": ["project_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "decodifier_get_project_events",
            "description": "Fetch recent audit events for a project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_id": {"type": "string", "description": "Project id."},
                    "limit": {
                        "type": "integer",
                        "description": "Optional maximum number of events to return.",
                        "default": 20,
                    },
                },
                "required": ["project_id"],
            },
        },
    },
]
