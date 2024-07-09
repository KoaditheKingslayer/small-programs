from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class NoteApp(App):
    def build(self):
        # Layout
        layout = BoxLayout(orientation='vertical')

        # Text input for notes
        self.text_input = TextInput(multiline=True)
        layout.add_widget(self.text_input)

        # Save button
        save_button = Button(text="Save", on_press=self.save_note)
        layout.add_widget(save_button)

        # Display saved notes
        self.notes_label = Label(text="")
        layout.add_widget(self.notes_label)

        return layout

    def save_note(self, instance):
        # Get the current text from the text input
        current_note = self.text_input.text

        # Append the note to the existing notes
        existing_notes = self.notes_label.text
        new_notes = f"{existing_notes}\n- {current_note}"

        # Update the label with the new notes
        self.notes_label.text = new_notes

        # Clear the text input for the next note
        self.text_input.text = ""

if __name__ == '__main__':
    NoteApp().run()
