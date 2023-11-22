from fpdf import FPDF

def draw_pdf(text_data, filename, title, subtitle, copyright, pagination):
    class PDF(FPDF):
        def header(self):
            self.set_font('DejaVuSansBold', 'B', 16)
            self.set_fill_color(4,138,255)
            self.cell(0, 15, title, 0, 1, 'C', 1)
            self.set_font('DejaVuSansBold', 'B', 14)
            self.cell(0, 10, subtitle, 0, 1, 'C', 1)
            self.set_fill_color(255, 255, 255)

        def footer(self):
            self.set_y(-15)
            self.set_font('DejaVuSansItalic', 'I', 8)
            self.set_fill_color(177,0,232)
            self.cell(0, 10, copyright + ' - ' + pagination + ' %s' % self.page_no(), 0, 0, 'C', 1)
            self.set_fill_color(255, 255, 255)

        def text_box(self, text):
            # Set left and right margin for the text box
            left_margin = 10
            right_margin = 10
            self.set_left_margin(left_margin)
            self.set_right_margin(right_margin)

            # Calculate available width for the text box
            text_box_width = self.w - left_margin - right_margin

            # Output the text in a multicell
            self.multi_cell(text_box_width, 10, text)

        def style_line(self, line):
            # Determine font size and style based on the starting characters
            if line.startswith("###"):
                self.set_font('DejaVuSansBold', 'B', 14)
                line = line.lstrip('#')
            elif line.startswith("##"):
                self.set_font('DejaVuSansBold', 'B', 18)
                line = line.lstrip('#')
            elif line.startswith("#"):
                self.set_font('DejaVuSansBold', 'B', 23)
                line = line.lstrip('#')
            else:
                # Default style
                self.set_font('DejaVuSans', size=12)

            return line

    pdf = PDF(orientation='P', unit='mm', format='A4')

    # Add the 'DejaVuSans' font with distinct names for each style
    pdf.add_font('DejaVuSans', '', 'ttf/DejaVuLGCSans.ttf', uni=True)
    pdf.add_font('DejaVuSansBold', 'B', 'ttf/DejaVuLGCSans-Bold.ttf', uni=True)
    pdf.add_font('DejaVuSansItalic', 'I', 'ttf/DejaVuLGCSans-Oblique.ttf', uni=True)
    pdf.add_font('DejaVuSansBoldItalic', 'BI', 'ttf/DejaVuLGCSans-BoldOblique.ttf', uni=True)

    pdf.set_font('DejaVuSans', size=12)
    pdf.add_page()

    for line in text_data:
        # Check if there is enough space for the current line
        line_width = pdf.get_string_width(line)
        remaining_space = pdf.h - pdf.get_y() - pdf.b_margin
        if line_width > pdf.w - pdf.l_margin - pdf.r_margin or remaining_space < pdf.font_size:
            pdf.text_box(line)  # Use text_box to handle multiline text
        else:
            # Style the line and remove leading '#'
            styled_line = pdf.style_line(line)
            
            # Write the line to the PDF
            pdf.cell(0, 10, styled_line, ln=True)

    # Save the PDF to the specified filename
    pdf.output(filename, 'F')

# Open template_math.txt and read the contents
with open("eg_res_math.txt", "r", encoding="utf-8") as file:
    data_template = file.read()

def generate_pdf(title,subtitle,filename, text_data):
    # Define your header, footer, and pagination information
   
    copyright = "Student App - copyright"

    # Call the draw_pdf function
    draw_pdf(text_data.splitlines(), filename, title, subtitle, copyright, "Page")


#for testing puorposes only
# title = "Matematica Blea"
# subtitle = "Cea mai ebanutaia materie pentru pidari"
# generate_pdf(title,subtitle,"test_output.pdf",data_template)