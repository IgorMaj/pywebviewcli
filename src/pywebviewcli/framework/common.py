def parse_app_init_file(file_path: str):
    """Returns imports and the rest as strings, used by the template"""
    with open(file_path, "r") as file:
        lines = file.readlines()

    import_lines = []
    main_code_lines = []

    # Iterate through the lines of the file
    for line in lines:
        if line.startswith("import"):
            import_lines.append(line)
        else:
            # we indent, since it will end up inside the add event listener callback, for format reasons
            main_code_lines.append(f"\t{line}")

    # Join the lines into multiline strings, note: lines already contain newline separator
    imports = "".join(import_lines)
    main_code = "".join(main_code_lines)

    return imports, main_code
