import flet as ft


def upload_configuration_file(e):
    def pick_files_result(e: ft.FilePickerResultEvent):
        print(e.files[0])

    pick_file_dialog = ft.FilePicker(on_result=pick_files_result)
