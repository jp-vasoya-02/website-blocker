import flet as ft
from app import block_websites
import os
import sys


def main(page: ft.Page):
    page.title = "Start and End Time Picker with Website Input"

    # Text fields to display selected start and end times
    start_time_text = ft.Text("Start time: Not selected")
    end_time_text = ft.Text("End time: Not selected")

    # List to store websites
    websites = []

    def start_time_changed(e):
        start_time_text.value = f"Start time: {start_time_picker.value.strftime('%H:%M')}"
        page.update()

    def end_time_changed(e):
        end_time_text.value = f"End time: {end_time_picker.value.strftime('%H:%M')}"
        page.update()

    # Create start time picker
    start_time_picker = ft.TimePicker(
        confirm_text="Confirm",
        error_invalid_text="Time out of range",
        help_text="Pick your start time",
        on_change=start_time_changed,
    )

    # Create end time picker
    end_time_picker = ft.TimePicker(
        confirm_text="Confirm",
        error_invalid_text="Time out of range",
        help_text="Pick your end time",
        on_change=end_time_changed,
    )

    # Add time pickers to the page overlay
    page.overlay.extend([start_time_picker, end_time_picker])

    # Buttons to open time pickers
    start_time_button = ft.ElevatedButton(
        "Pick start time",
        icon=ft.icons.ACCESS_TIME,
        on_click=lambda _: start_time_picker.pick_time(),
    )
    
    end_time_button = ft.ElevatedButton(
        "Pick end time",
        icon=ft.icons.ACCESS_TIME,
        on_click=lambda _: end_time_picker.pick_time(),
    )

    # Arrange buttons side by side
    button_row = ft.Row(
        controls=[start_time_button, end_time_button],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    # Arrange text fields side by side
    text_row = ft.Row(
        controls=[start_time_text, end_time_text],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    # Input field for website list
    website_input = ft.TextField(
        label="Enter website URL",
        hint_text="e.g., https://example.com",
        width=400
    )

    website_list = ft.Column()

    def add_website(e):
        websites.append(website_input.value)
        website_list.controls.append(ft.Text(website_input.value))
        website_input.value = ""
        page.update()

    add_website_button = ft.ElevatedButton(
        text="Add Website",
        on_click=add_website
    )

    # Layout for website input and list
    website_input_row = ft.Row(
        controls=[website_input, add_website_button],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    def submit_data(e):
        start_time = start_time_picker.value.strftime('%H') if start_time_picker.value else "Not selected"
        end_time = end_time_picker.value.strftime('%H') if end_time_picker.value else "Not selected"
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print("Websites:", websites)
        block_websites(int(start_time),int(end_time),websites)
    submit_button = ft.ElevatedButton(
        text="Submit",
        on_click=submit_data
    )

    # Add all components to the page
    page.add(button_row, text_row, website_input_row, website_list, submit_button)

ft.app(target=main)
