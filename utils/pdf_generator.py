from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(filename, title, content):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(title, styles["Title"])
    )

    story.append(
        Paragraph("<br/><br/>", styles["BodyText"])
    )

    content = content.replace("\n", "<br/>")

    story.append(
        Paragraph(content, styles["BodyText"])
    )

    doc.build(story)