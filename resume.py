from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black
import json
import argparse
import textwrap

def create_resume(json_file, output_file):
    # loading the JSON data
    with open(json_file) as f:
        data = json.load(f)

    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter
    
    # margins and spacing
    left_margin = 0.75 * inch
    right_margin = width - 0.75 * inch
    y_position = height - 0.75 * inch
    line_height = 12
    
    # ---------- Header ----------
    # 1. Name (centered, large, bold)
    c.setFont("Helvetica-Bold", 24)
    name_width = c.stringWidth(data["name"], "Helvetica-Bold", 24)
    c.drawString((width - name_width)/2, y_position, data["name"])
    y_position -= line_height * 1.5

    # 2. Role (centered, smaller, bold)
    if "title" in data:
        c.setFont("Helvetica-Bold", 14)
        role_width = c.stringWidth(data["title"], "Helvetica-Bold", 14)
        c.drawString((width - role_width)/2, y_position, data["title"])
        y_position -= line_height * 1.5

    # 3. Social links (centered, clickable)
    social_links = []
    if "github" in data:
        social_links.append(("GitHub", data["github"]))
    if "leetcode" in data:
        social_links.append(("LeetCode", data["leetcode"])) 
    if "linkedin" in data:
        social_links.append(("LinkedIn", data["linkedin"]))

    if social_links:
        c.setFont("Helvetica", 10)
        c.setFillColor(HexColor("#0000FF"))  # Blue for links
        
        # Calculated total width of all social links with spacing
        total_width = sum(c.stringWidth(text, "Helvetica", 10) for text, _ in social_links)
        total_width += 20 * (len(social_links)-1)  # space between links
        
        x_start = (width - total_width)/2
        
        for text, url in social_links:
            text_width = c.stringWidth(text, "Helvetica", 10)
            # Drawing clickable link
            c.drawString(x_start, y_position, text)
            c.linkURL(url, (x_start, y_position, x_start + text_width, y_position + line_height))
            x_start += text_width + 20  # Added spacing between links
        
        c.setFillColor(black)  # Reset color
        y_position -= line_height * 1.5

    # 4. Contact info (address • phone • email in one line)
    contact_items = []
    if "address" in data:
        contact_items.append(data["address"])
    if "phone" in data:
        contact_items.append(data["phone"])
    if "email" in data:
        contact_items.append(data["email"])

    if contact_items:
        c.setFont("Helvetica", 10)
        contact_str = " • ".join(contact_items)
        
        # Wrap if too long
        if c.stringWidth(contact_str, "Helvetica", 10) > (width - 1.5*inch):
            contact_lines = textwrap.wrap(contact_str, width=60)
            for line in contact_lines:
                line_width = c.stringWidth(line, "Helvetica", 10)
                c.drawString((width - line_width)/2, y_position, line)
                y_position -= line_height
        else:
            line_width = c.stringWidth(contact_str, "Helvetica", 10)
            c.drawString((width - line_width)/2, y_position, contact_str)
            y_position -= line_height
        
        y_position -= line_height * 0.5

    # ---------- Sections ----------
    def draw_section(title):
        nonlocal y_position
        if y_position < 1.5 * inch:  # for page break
            c.showPage()
            y_position = height - 0.75 * inch
        
        c.setFont("Helvetica-Bold", 14)
        c.drawString(left_margin, y_position, title.upper())
        c.line(left_margin, y_position-2, right_margin, y_position-2)
        y_position -= line_height * 1.5

    # ---------- Professional Summary ----------
    if 'professional_summary' in data:
        draw_section("Professional Summary")
        c.setFont("Helvetica", 10)
        summary = data['professional_summary']
        wrapped = textwrap.wrap(summary, width=80)
        for line in wrapped:
            if y_position < 1.5 * inch:
                c.showPage()
                y_position = height - 0.75 * inch
            c.drawString(left_margin, y_position, line)
            y_position -= line_height
        y_position -= line_height * 0.5

    # ---------- Skills ----------
    if 'skills' in data:
        draw_section("Skills")
        c.setFont("Helvetica", 10)
        skills_text = " • ".join(data["skills"])
        if c.stringWidth(skills_text, "Helvetica", 10) > (width - 1.5*inch):
            skills_lines = textwrap.wrap(skills_text, width=80)
            for line in skills_lines:
                c.drawString(left_margin, y_position, line)
                y_position -= line_height
        else:
            c.drawString(left_margin, y_position, skills_text)
            y_position -= line_height
        y_position -= line_height * 0.5

    # ---------- Work Experience ----------
    if 'work_experience' in data:
        draw_section("Work Experience")
        for exp in data["work_experience"]:
            # Company and date
            c.setFont("Helvetica-Bold", 12)
            c.drawString(left_margin, y_position, exp["company"])
            date_width = c.stringWidth(exp["date"], "Helvetica-Bold", 12)
            c.drawString(right_margin - date_width, y_position, exp["date"])
            y_position -= line_height
            
            # Position and location
            c.setFont("Helvetica-Oblique", 10)
            c.drawString(left_margin, y_position, exp["position"])
            loc_width = c.stringWidth(exp["location"], "Helvetica-Oblique", 10)
            c.drawString(right_margin - loc_width, y_position, exp["location"])
            y_position -= line_height * 1.5
            
            # Bullet points
            c.setFont("Helvetica", 10)
            for bullet in exp["bullets"]:
                if y_position < 1.5 * inch:
                    c.showPage()
                    y_position = height - 0.75 * inch
                wrapped = textwrap.wrap(bullet, width=80)
                c.drawString(left_margin + 0.2*inch, y_position, "• " + wrapped[0])
                y_position -= line_height
                for line in wrapped[1:]:
                    c.drawString(left_margin + 0.4*inch, y_position, line)
                    y_position -= line_height
            y_position -= line_height * 0.5

    # ---------- Education ----------
    if 'education' in data:
        draw_section("Education")
        c.setFont("Helvetica-Bold", 12)
        c.drawString(left_margin, y_position, data["education"]["institution"])
        date_width = c.stringWidth(data["education"]["duration"], "Helvetica-Bold", 12)
        c.drawString(right_margin - date_width, y_position, data["education"]["duration"])
        y_position -= line_height
        
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(left_margin, y_position, data["education"]["degree"])
        loc_width = c.stringWidth(data["education"]["location"], "Helvetica-Oblique", 10)
        c.drawString(right_margin - loc_width, y_position, data["education"]["location"])
        y_position -= line_height
        
        c.setFont("Helvetica", 10)
        c.drawString(left_margin, y_position, f"GPA: {data['education']['gpa']}")
        y_position -= line_height * 1.5

    # ---------- Projects ----------
    if 'projects' in data:
        draw_section("Projects")
        for proj in data["projects"]:
            # Project name with optional link
            c.setFont("Helvetica-Bold", 12)
            if 'link' in proj and proj['link']:
                c.setFillColor(HexColor("#0000FF"))
                c.drawString(left_margin, y_position, proj["name"])
                text_width = c.stringWidth(proj["name"], "Helvetica-Bold", 12)
                c.linkURL(proj['link'], (left_margin, y_position, 
                                   left_margin + text_width, y_position + line_height))
            else:
                c.setFillColor(black)
                c.drawString(left_margin, y_position, proj["name"])
            c.setFillColor(black)
            y_position -= line_height * 1.5
            
            # Bullet points
            c.setFont("Helvetica", 10)
            for bullet in proj["bullets"]:
                if y_position < 1.5 * inch:
                    c.showPage()
                    y_position = height - 0.75 * inch
                wrapped = textwrap.wrap(bullet, width=80)
                c.drawString(left_margin + 0.2*inch, y_position, "• " + wrapped[0])
                y_position -= line_height
                for line in wrapped[1:]:
                    c.drawString(left_margin + 0.4*inch, y_position, line)
                    y_position -= line_height
            y_position -= line_height * 0.5

    # ---------- Certifications ----------
    if 'certifications' in data:
        draw_section("Certifications")
        c.setFont("Helvetica", 10)
        c.setFillColor(HexColor("#0000FF"))  # links
        for cert in data["certifications"]:
            if y_position < 1.5 * inch:
                c.showPage()
                y_position = height - 0.75 * inch
            if isinstance(cert, dict):
                text = cert['name']
                if 'link' in cert:
                    text_width = c.stringWidth(text, "Helvetica", 10)
                    c.linkURL(cert['link'], (left_margin, y_position, 
                                       left_margin + text_width, y_position + line_height))
            else:
                text = cert
            c.drawString(left_margin, y_position, text)
            y_position -= line_height
        y_position -= line_height * 0.5

    # ---------- Languages ----------
    if 'languages' in data:
        draw_section("Languages")
        c.setFont("Helvetica", 10)
        lang_str = " • ".join([
            f"{lang['name']} ({lang['proficiency']})" if 'proficiency' in lang else lang['name'] 
            for lang in data["languages"]
        ])
        if c.stringWidth(lang_str, "Helvetica", 10) > (width - 1.5*inch):
            lang_lines = textwrap.wrap(lang_str, width=80)
            for line in lang_lines:
                c.drawString(left_margin, y_position, line)
                y_position -= line_height
        else:
            c.drawString(left_margin, y_position, lang_str)
            y_position -= line_height
        y_position -= line_height * 0.5

    c.save()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate PDF resume from JSON")
    parser.add_argument("json_file", help="Path to JSON resume file")
    parser.add_argument("output_file", help="Output PDF file path", default="resume.pdf", nargs="?")
    args = parser.parse_args()
    
    create_resume(args.json_file, args.output_file)
    print(f"Resume generated successfully: {args.output_file}")
