from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import black
import json
import argparse
import textwrap

def create_resume(json_file, output_file):
    # JSON data + validation
    with open(json_file) as f:
        data = json.load(f)
    
    if "name" not in data:
        raise ValueError("Resume must contain a 'name' field")
    
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter
    
    # Layout configuration
    left_margin = 0.75 * inch
    right_margin = width - 0.75 * inch
    y_position = height - 0.75 * inch
    line_height = 14
    def check_space(lines_needed=1):
        nonlocal y_position
        required_space = lines_needed * line_height
        if (y_position - required_space) < (0.75 * inch):  # space check
            c.showPage()
            y_position = height - 0.75 * inch
        return y_position

    # ---------- Header Section ----------
    check_space(4)
    c.setFont("Helvetica-Bold", 24)
    name = data["name"]
    name_width = c.stringWidth(name, "Helvetica-Bold", 24)
    c.drawString((width - name_width)/2, y_position, name)
    y_position -= line_height * 1.5  # Increased spacing

    # Title (optional)
    if data.get("title"):
        check_space(2)
        c.setFont("Helvetica-Bold", 16)  # Larger font size
        title = data["title"]
        title_width = c.stringWidth(title, "Helvetica-Bold", 16)
        c.drawString((width - title_width)/2, y_position, title)
        y_position -= line_height * 1.5

    # Social Links (optional)
    social_links = [
        ("GitHub", data.get("github")),
        ("LeetCode", data.get("leetcode")),
        ("LinkedIn", data.get("linkedin"))
    ]
    social_links = [ (t, u) for t, u in social_links if u ]
    
    if social_links:
        check_space(2)
        c.setFont("Helvetica", 11)  # Slightly larger font
        total_width = sum(c.stringWidth(t, "Helvetica", 11) for t, _ in social_links)
        total_width += 20 * (len(social_links)-1)
        x_start = (width - total_width)/2
        
        for i, (text, url) in enumerate(social_links):
            text_width = c.stringWidth(text, "Helvetica", 11)
            c.drawString(x_start, y_position, text)
            c.linkURL(url, (x_start, y_position, x_start + text_width, y_position + line_height))
            x_start += text_width
            if i < len(social_links) - 1:
                dot = " • "
                dot_width = c.stringWidth(dot, "Helvetica", 11)
                c.drawString(x_start, y_position, dot)
                x_start += dot_width

        
        y_position -= line_height * 1.5

    # (optional)
    contact_items = [
        data.get("address"),
        data.get("phone"),
        data.get("email")
    ]
    contact_items = [ci for ci in contact_items if ci]
    
    if contact_items:
        check_space(3)
        c.setFont("Helvetica", 11)
        contact_str = " • ".join(contact_items)
        
        if c.stringWidth(contact_str, "Helvetica", 11) > (width - 1.5*inch):
            lines = textwrap.wrap(contact_str, width=60)
        else:
            lines = [contact_str]
        
        for line in lines:
            line_width = c.stringWidth(line, "Helvetica", 11)
            c.drawString((width - line_width)/2, y_position, line)
            y_position -= line_height
        
        y_position -= line_height * 0.75  # spacing

    # ---------- Section Rendering ----------
    def draw_section(title):
        nonlocal y_position
        check_space(3)
        c.setFont("Helvetica-Bold", 16)  # large section titles
        c.drawString(left_margin, y_position, title.upper())
        c.line(left_margin, y_position-4, right_margin, y_position-4)  # thick line
        y_position -= line_height * 1.5  # space after section header

    # ---------- Professional Summary ----------
    if data.get("professional_summary"):
        draw_section("Professional Summary")
        c.setFont("Helvetica", 11)
        summary = data["professional_summary"]
        for line in textwrap.wrap(summary, width=80):
            check_space()
            c.drawString(left_margin, y_position, line)
            y_position -= line_height
        y_position -= line_height * 0.75

# ---------- Skills ----------
    if data.get("skills"):
        draw_section("Skills")
        c.setFont("Helvetica", 11)
        skills_text = ", ".join(data["skills"])  # replaced • with ,
        if c.stringWidth(skills_text, "Helvetica", 11) > (width - 1.5*inch):
            lines = textwrap.wrap(skills_text, width=80)
        else:
            lines = [skills_text]
        
        for line in lines:
            check_space()
            c.drawString(left_margin, y_position, line)
            y_position -= line_height
        
        y_position -= line_height * 0.75


    # ---------- Work Experience ----------
    work_exp_entries = data.get("work_experience", [])
    if work_exp_entries:
        draw_section("Work Experience")
        
        for exp in work_exp_entries:
            if not all(key in exp for key in ["company", "position"]):
                continue
            
            check_space(4)
            # Company & Date
            c.setFont("Helvetica-Bold", 13)
            company = exp["company"]
            date = exp.get("date", "")
            date_width = c.stringWidth(date, "Helvetica-Bold", 13)
            c.drawString(left_margin, y_position, company)
            c.drawString(right_margin - date_width, y_position, date)
            y_position -= line_height * 1.2
            
            # Position & Location
            c.setFont("Helvetica", 11)
            position = exp["position"]
            location = exp.get("location", "")
            loc_width = c.stringWidth(location, "Helvetica", 11)
            c.drawString(left_margin, y_position, position)
            c.drawString(right_margin - loc_width, y_position, location)
            y_position -= line_height * 1.2
            
            for bullet in exp.get("bullets", []):
                check_space(2)
                wrapped = textwrap.wrap(bullet, width=80)
                c.drawString(left_margin + 0.2*inch, y_position, "• " + wrapped[0])
                y_position -= line_height
                for line in wrapped[1:]:
                    check_space()
                    c.drawString(left_margin + 0.4*inch, y_position, line)
                    y_position -= line_height
            
            y_position -= line_height * 0.75

    # ---------- Education ----------
    if data.get("education"):
        edu = data["education"]
        if all(key in edu for key in ["institution", "degree", "duration"]):
            draw_section("Education")
            
            check_space(4)
            c.setFont("Helvetica-Bold", 13)
            c.drawString(left_margin, y_position, edu["institution"])
            duration = edu["duration"]
            date_width = c.stringWidth(duration, "Helvetica-Bold", 13)
            c.drawString(right_margin - date_width, y_position, duration)
            y_position -= line_height * 1.2
            
            c.setFont("Helvetica-Oblique", 11)
            c.drawString(left_margin, y_position, edu["degree"])
            location = edu.get("location", "")
            loc_width = c.stringWidth(location, "Helvetica-Oblique", 11)
            c.drawString(right_margin - loc_width, y_position, location)
            y_position -= line_height * 1.2
            
            if edu.get("gpa"):
                c.setFont("Helvetica", 11)
                c.drawString(left_margin, y_position, f"GPA: {edu['gpa']}")
                y_position -= line_height
            
            y_position -= line_height * 0.75

    # ---------- Projects ----------
    projects = data.get("projects", [])
    if projects:
        draw_section("Projects")
        projects_section_drawn = True
        
        for proj in projects:
            if "name" not in proj:
                continue
            
            check_space(4)
            c.setFont("Helvetica-Bold", 13)
            name = proj["name"]
            c.drawString(left_margin, y_position, name)
            if proj.get("link"):
                text_width = c.stringWidth(name, "Helvetica-Bold", 13)
                c.linkURL(proj["link"], (left_margin, y_position, 
                                    left_margin + text_width, y_position + line_height))
            
            y_position -= line_height * 1.2
            
            # Bullet points
            c.setFont("Helvetica", 11)
            for bullet in proj.get("bullets", []):
                check_space(2)
                wrapped = textwrap.wrap(bullet, width=80)
                c.drawString(left_margin + 0.2*inch, y_position, "• " + wrapped[0])
                y_position -= line_height
                for line in wrapped[1:]:
                    check_space()
                    c.drawString(left_margin + 0.4*inch, y_position, line)
                    y_position -= line_height
            
            y_position -= line_height * 0.75

    # ---------- Achievements ----------
    if data.get("achievements"):
        draw_section("Achievements")
        c.setFont("Helvetica", 11)
        
        for achievement in data["achievements"]:
            check_space(2)
            wrapped = textwrap.wrap(achievement, width=80)
            c.drawString(left_margin + 0.2*inch, y_position, "• " + wrapped[0])
            y_position -= line_height
            for line in wrapped[1:]:
                check_space()
                c.drawString(left_margin + 0.4*inch, y_position, line)
                y_position -= line_height
        
        y_position -= line_height * 0.75

    # ---------- Certifications ----------
    if data.get("certifications"):
        draw_section("Certifications")
        c.setFont("Helvetica", 11)
        
        for cert in data["certifications"]:
            check_space()
            if isinstance(cert, dict):
                text = cert.get("name", "")
                url = cert.get("link")
            else:
                text = str(cert)
                url = None
            
            if text:
                c.drawString(left_margin, y_position, text)
                if url:
                    text_width = c.stringWidth(text, "Helvetica", 11)
                    c.linkURL(url, (left_margin, y_position, 
                                left_margin + text_width, y_position + line_height))
                y_position -= line_height
        
        y_position -= line_height * 0.75

    # ---------- Languages ----------
    if data.get("languages"):
        draw_section("Languages")
        c.setFont("Helvetica", 11)
        
        lang_items = []
        for lang in data["languages"]:
            if "name" not in lang:
                continue
            proficiency = lang.get("proficiency", "")
            lang_items.append(f"{lang['name']}{f' ({proficiency})' if proficiency else ''}")
        
        if lang_items:
            lang_str = " • ".join(lang_items)
            if c.stringWidth(lang_str, "Helvetica", 11) > (width - 1.5*inch):
                lines = textwrap.wrap(lang_str, width=80)
            else:
                lines = [lang_str]
            
            for line in lines:
                check_space()
                c.drawString(left_margin, y_position, line)
                y_position -= line_height
            
            y_position -= line_height * 0.75

    c.save()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate PDF resume from JSON")
    parser.add_argument("json_file", help="Path to JSON resume file")
    parser.add_argument("output_file", help="Output PDF path", default="resume.pdf", nargs="?")
    args = parser.parse_args()
    
    create_resume(args.json_file, args.output_file)
    print(f"Resume generated: {args.output_file}")
