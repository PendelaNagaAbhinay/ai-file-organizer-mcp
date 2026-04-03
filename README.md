# Run AI on your local files - safely and privately.

This MCP server lets Claude Desktop:
- organize your folders
- find files instantly
- automate file management

# AI File Organizer + Finder (Initial Version)

This refers to the baseline version of the MCP server before the major refactoring for safety, scalability, and enhanced organization.

## Features implemented at start:
- **Workspace Safety**: Basic `safe_path` function that resolves paths.
- **Find by Name**: Tool `find_by_name(pattern, directory=".")` that returns a newline-separated string of matches.
- **Find by Content**: Tool `find_by_content(text, directory=".")` that reads all files (including binary) to find text matches.
- **File CRUD Operations**:
    - `read_file(path)`: Simple text read.
    - `write_file(path, content)`: Simple text write.
    - `append_file(path, content)`: Simple text append.
    - `delete_file(path)`: Simple file deletion.
- **Directory Listing**: `list_directory(path)` tool returning a raw list of filenames.

## Known Limitations (V1):
- Files were moved/categorized by flattening the structure (losing folders).
- No limit on results; large directories could cause crashes or token overflows.
- No exclusion of heavy directories like `node_modules` or `.git`.
- Binary files were scanned for text, causing potential errors or slow performance.
- Clean filenames tool was destructive and ran automatically on all files.

