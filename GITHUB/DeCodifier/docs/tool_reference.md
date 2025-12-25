# Tool Reference

These tools match `decodifier/tool_registry.py`.

- decodifier_list_projects: no args
- decodifier_create_project: name, path, ignore?, id?
- decodifier_get_project_tree: project_id, max_depth?
- decodifier_read_file: project_id, path
- decodifier_save_file: project_id, path, content
- decodifier_upload_file: project_id, path, content, filename?
- decodifier_apply_patch: project_id, path, patch
- decodifier_list_packs: no args
- decodifier_enable_packs_for_project: project_id, packs
- decodifier_get_pack_specs_for_project: project_id
- decodifier_get_project_events: project_id, limit?
