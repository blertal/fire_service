import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from PIL import Image as PILImage
from ai_agent import generate_pil_image_caption, llm_model

KV = '''
<NeonButton@Button>:
    font_size: 44
    background_normal: ''
    background_color: 0, 0.8, 0.6, 1
    color: 1, 1, 1, 1
    size_hint: 0.5, None
    pos_hint: {'center_x': 0.5}
    height: 80
    canvas.before:
        Color:
            rgba: 0, 1, 0.8, 0.3
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [40,]
        Color:
            rgba: 0, 0.8, 0.6, 1
        RoundedRectangle:
            pos: self.pos[0]+2, self.pos[1]+2
            size: self.size[0]-4, self.size[1]-4
            radius: [38,]

<FireDetectionLayout>:
    orientation: 'vertical'
    padding: 20
    spacing: 20

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: 0.3

        FileChooserIconView:
            id: filechooser
            path: root.content_path
            filters: ['*.png', '*.jpg', '*.jpeg']
            icon_size: 96
            font_size: 32
            canvas.before:
                Color:
                    rgba: 0, 0.2, 0.2, 0.2
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [24,]

    NeonButton:
        text: "Analyze Selected Image"
        on_press: root.analyze_image()
        height: 80

    Label:
        id: result_label
        text: root.result_text
        font_size: 42
        color: 0, 1, 0.8, 1
        size_hint_y: None
        height: 40

    Label:
        id: description_label
        text: root.description_text
        font_size: 36
        color: 0.8, 1, 1, 1
        size_hint_y: None
        height: 120
        text_size: self.width, None
        halign: 'center'
        valign: 'top'

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: 180
        spacing: 10

        TextInput:
            id: why_input
            hint_text: "Write here clarifying questions"
            font_size: 32
            multiline: True
            size_hint_y: None
            height: 80

        NeonButton:
            text: "Ask"
            on_press: root.ask_why()
            size_hint: 0.5, None
            pos_hint: {'center_x': 0.5}
            height: 80

    Label:
        id: why_label
        text: root.why_text
        font_size: 32
        color: 1, 0.8, 0.2, 1
        size_hint_y: None
        height: 80
        text_size: self.width, None
        halign: 'center'
        valign: 'top'

    Image:
        id: img_widget
        source: root.img_source
        allow_stretch: True
        keep_ratio: True
        size_hint_y: 0.3
        canvas.before:
            Color:
                rgba: 0, 0.2, 0.2, 0.2
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [24,]
'''

class FireDetectionLayout(BoxLayout):
    content_path = StringProperty(os.path.join(os.path.dirname(__file__), 'content'))
    result_text = StringProperty("Result will appear here.")
    description_text = StringProperty("")
    why_text = StringProperty("")
    img_source = StringProperty("")
    last_img_path = None

    def analyze_image(self):
        selected = self.ids.filechooser.selection
        if not selected:
            self.result_text = "Please select an image."
            self.description_text = ""
            self.why_text = ""
            self.last_img_path = None
            return
        img_path = selected[0]
        self.img_source = img_path
        self.last_img_path = img_path
        pil_img = PILImage.open(img_path)
        try:
            # Yes/No answer
            result = generate_pil_image_caption(
                model=llm_model,
                pil_image=pil_img,
                prompt="Is there a fire emergency in this image? Answer yes or no."
            )
            self.result_text = f"AI Result: {result}"

            # Description (2-4 sentences)
            description = generate_pil_image_caption(
                model=llm_model,
                pil_image=pil_img,
                prompt="Describe in 2 to 4 sentences what you see in this image."
            )
            self.description_text = f"Description: {description}"
            self.why_text = ""
        except Exception as e:
            self.result_text = f"Error generating caption: {e}"
            self.description_text = ""
            self.why_text = ""

    def ask_why(self):
        question = self.ids.why_input.text.strip()
        if not self.last_img_path or not question:
            self.why_text = "Please analyze an image and enter a question."
            return
        pil_img = PILImage.open(self.last_img_path)
        try:
            answer = generate_pil_image_caption(
                model=llm_model,
                pil_image=pil_img,
                prompt=question
            )
            self.why_text = f"AI says: {answer}"
        except Exception as e:
            self.why_text = f"Error: {e}"

class FireDetectionApp(App):
    def build(self):
        Builder.load_string(KV)
        return FireDetectionLayout()

if __name__ == '__main__':
    FireDetectionApp().run()